// Renders anim.html frame by frame and pipes PNGs into ffmpeg.
// Usage: node render.js <audio.wav> <out.mp4> [stillsDir]
// Env: PAGE (animation html, default ./anim.html), DUR (seconds, default 12), STILLS (comma-separated times),
//      SFX_OUT (write the page's sound-effect events, window.SFX, to this JSON file and exit)
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
(async () => {
  const [audio, out, stills] = process.argv.slice(2);
  const FPS = 30, DUR = +(process.env.DUR || 12);
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined, args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(process.env.PAGE || path.join(__dirname, 'anim.html')));
  await page.waitForFunction(() => window.ready === true);
  if (process.env.SFX_OUT) {
    fs.writeFileSync(process.env.SFX_OUT, JSON.stringify(await page.evaluate(() => window.SFX || [])));
    await browser.close(); return;
  }
  if (stills) {
    fs.mkdirSync(stills, { recursive: true });
    for (const t of (process.env.STILLS || '0.5,1.8,3.6,5.9,8.4,9.25,11.5').split(',').map(Number)) {
      await page.evaluate(t => render(t), t);
      await page.locator('canvas').screenshot({ path: `${stills}/t${t}.png` });
    }
    await browser.close(); return;
  }
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-', '-i', audio,
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-ar', '44100', '-c:a', 'aac', '-b:a', '192k',
    '-t', String(DUR), '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = 0; f < FPS * DUR; f++) {
    const buf = await page.evaluate(t => { render(t); return document.getElementById('c').toDataURL('image/png'); }, f / FPS);
    const png = Buffer.from(buf.split(',')[1], 'base64');
    if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
})();
