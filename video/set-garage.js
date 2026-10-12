// The garage set, drawn from the photo of Centre Auto Alonzo (Combani): light grey two-storey building,
// blue fascia band with the white « CENTRE AUTO ALONZO » panel, the workshop bay (car lift, strip lights),
// the white tent (tonnelle) on the left, yellow/black kerb, concrete forecourt. No network logos (Top Garage / Groupauto).
// Uses the page's globals (g, W, H, BLUE, RED, WH, text, rrect). Drawn wider than the frame so the camera can roam.
function cartoonBg(t) {
  const X0 = -700, XW = W + 1400;
  // upper floor: light grey render
  g.fillStyle = '#dde2e8'; g.fillRect(X0, -700, XW, 1600);
  g.fillStyle = 'rgba(120,135,155,.06)'; for (let yy = 190; yy < 760; yy += 46) g.fillRect(X0, yy, XW, 2);
  // roof edge (brand blue + red line, as in the series frame)
  g.fillStyle = BLUE; g.fillRect(X0, -700, XW, 850); g.fillStyle = RED; g.fillRect(X0, 156, XW, 12);
  // upper-floor windows (dark glass, light frames) and an AC unit, kept low-contrast behind the titles
  for (const wx of [-430, 120, 720, 1270]) {
    g.fillStyle = '#c4ccd6'; rrect(wx - 12, 398, 244, 176, 10); g.fill();
    g.fillStyle = '#56637a'; g.fillRect(wx, 410, 220, 152);
    g.fillStyle = 'rgba(255,255,255,.12)'; g.beginPath(); g.moveTo(wx + 20, 562); g.lineTo(wx + 120, 410); g.lineTo(wx + 170, 410); g.lineTo(wx + 70, 562); g.fill();
    g.fillStyle = '#c4ccd6'; g.fillRect(wx + 106, 410, 8, 152);
  }
  g.fillStyle = '#f3f5f7'; rrect(420, 430, 190, 112, 8); g.fill(); g.strokeStyle = '#b8c1cc'; g.lineWidth = 3; g.stroke();
  g.strokeStyle = '#9aa5b4'; g.lineWidth = 4; g.beginPath(); g.arc(475, 486, 34, 0, Math.PI * 2); g.stroke();
  for (let i = 0; i < 3; i++) { g.save(); g.translate(475, 486); g.rotate(t * 9 + i * 2.1); g.fillStyle = '#b8c1cc'; g.beginPath(); g.ellipse(14, 0, 16, 7, 0, 0, Math.PI * 2); g.fill(); g.restore(); }
  for (let yy = 455; yy < 525; yy += 12) { g.fillStyle = '#c9d0d9'; g.fillRect(530, yy, 60, 5); }
  // fascia band + the white name panel
  g.fillStyle = '#0a4a96'; g.fillRect(X0, 760, XW, 140);
  g.fillStyle = '#2c69b8'; g.fillRect(X0, 760, XW, 6); g.fillStyle = 'rgba(0,0,0,.18)'; g.fillRect(X0, 900, XW, 10);
  text('ENTRETIEN & RÉPARATION', 40, 814, { f: 'Montserrat', w: 800, s: 30, col: WH, align: 'left' });
  text('TOUTES MARQUES', 40, 852, { f: 'Montserrat', w: 800, s: 30, col: WH, align: 'left' });
  g.fillStyle = '#f4f6f9'; rrect(530, 776, 410, 108, 28); g.fill();
  text('CENTRE AUTO', 735, 811, { f: 'Montserrat', w: 900, s: 42, col: BLUE });
  text('ALONZO', 735, 856, { f: 'Montserrat', w: 900, s: 42, col: BLUE });
  // ground floor wall
  g.fillStyle = '#cfd5dc'; g.fillRect(X0, 910, XW, 500);
  // workshop bay: dark interior, strip lights, car lift, red tool cabinet
  g.fillStyle = '#9aa5b4'; g.fillRect(420, 930, 600, 480);
  const bay = g.createLinearGradient(0, 948, 0, 1410); bay.addColorStop(0, '#3b4555'); bay.addColorStop(1, '#232a35');
  g.fillStyle = bay; g.fillRect(438, 948, 564, 462);
  g.save(); g.shadowColor = '#eaf2ff'; g.shadowBlur = 24; g.fillStyle = '#f5f8ff'; for (const lx of [500, 760]) { rrect(lx, 985, 180, 12, 6); g.fill(); } g.restore();
  g.fillStyle = '#2e3644'; g.fillRect(438, 1030, 564, 4);
  g.fillStyle = '#c2272d'; rrect(870, 1220, 110, 150, 8); g.fill(); g.fillStyle = '#e04a4f'; for (let yy = 1235; yy < 1360; yy += 34) g.fillRect(882, yy, 86, 4);
  g.fillStyle = '#5a6578'; g.fillRect(470, 1100, 22, 310); g.fillRect(950, 1100, 22, 310);
  g.fillStyle = '#3d4b63'; g.fillRect(492, 1370, 458, 18);
  // the white tent (tonnelle) on the left
  g.fillStyle = 'rgba(0,0,0,.08)'; g.fillRect(-150, 1030, 520, 380);
  g.fillStyle = '#e9e4d6'; for (const px of [-90, 330]) g.fillRect(px - 6, 1000, 12, 410);
  g.fillStyle = '#f7f3e8'; g.beginPath(); g.moveTo(-170, 1000); g.lineTo(110, 925); g.lineTo(400, 1000); g.closePath(); g.fill();
  g.strokeStyle = '#d6cfbd'; g.lineWidth = 4; g.stroke();
  g.fillStyle = '#f7f3e8'; g.beginPath(); g.moveTo(-170, 1000);
  for (let x = -170; x < 400; x += 57) g.quadraticCurveTo(x + 28.5, 1052, x + 57, 1000);
  g.closePath(); g.fill(); g.stroke();
  // yellow / black kerb, then the concrete forecourt
  g.fillStyle = '#1b1d22'; g.fillRect(X0, 1400, XW, 26);
  g.fillStyle = '#f2c230'; for (let x = X0; x < X0 + XW; x += 64) { g.beginPath(); g.moveTo(x, 1426); g.lineTo(x + 26, 1400); g.lineTo(x + 52, 1400); g.lineTo(x + 26, 1426); g.fill(); }
  g.fillStyle = '#a9afb7'; g.fillRect(X0, 1426, XW, 1300);
  g.strokeStyle = 'rgba(80,90,105,.25)'; g.lineWidth = 3; for (let x = -640; x < W + 700; x += 360) { g.beginPath(); g.moveTo(x, 1426); g.lineTo(x - 180, 1920); g.stroke(); }
  g.beginPath(); g.moveTo(X0, 1700); g.lineTo(X0 + XW, 1700); g.stroke();
  g.fillStyle = 'rgba(70,80,95,.08)'; g.beginPath(); g.ellipse(860, 1780, 160, 30, 0, 0, Math.PI * 2); g.fill();
}
