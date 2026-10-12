// Renders anim.html frame by frame and pipes PNGs into ffmpeg.
// Usage: node render.js <audio.wav> <out.mp4> [stillsDir]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
(async () => {
  const [audio, out, stills] = process.argv.slice(2);
  const FPS = 30, DUR = 12;
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined, args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.join(__dirname, 'anim.html'));
  await page.waitForFunction(() => window.ready === true);
  if (stills) {
    fs.mkdirSync(stills, { recursive: true });
    for (const t of [0.5, 1.8, 3.6, 5.9, 8.4, 9.25, 11.5]) {
      await page.evaluate(t => render(t), t);
      await page.locator('canvas').screenshot({ path: `${stills}/t${t}.png` });
    }
    await browser.close(); return;
  }
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-', '-i', audio,
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
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
