import math, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, DUR = 1080, 1920, 30, 11.0
BG = np.array([255, 246, 234])
src = Image.open("src.png").convert("RGB")
a = np.asarray(src).astype(int)
diff = np.abs(a - BG).sum(2)
alpha_full = np.clip((diff - 6) / 40.0, 0, 1)

# name, box (x0,y0,x1,y1); first box claiming a pixel owns it
BOXES = [
    ("cal",      (205, 935, 295, 1020)),
    ("pin",      (795, 930, 905, 1020)),
    ("date",     (100, 1050, 390, 1095)),
    ("du",       (465, 556, 590, 628)),
    ("leaves",   (860, 0, 1080, 268)),
    ("atelier",  (290, 268, 680, 322)),
    ("les",      (440, 330, 595, 442)),
    ("gourm",    (145, 443, 955, 556)),
    ("cup",      (15, 556, 260, 990)),
    ("barista",  (280, 640, 785, 752)),
    ("ribbon",   (235, 752, 808, 836)),
    ("choco",    (775, 560, 1080, 975)),
    ("div1",     (385, 920, 402, 1110)),
    ("clock",    (460, 930, 560, 1025)),
    ("time",     (430, 1040, 610, 1115)),
    ("div2",     (645, 920, 662, 1110)),
    ("lieu",     (700, 1020, 950, 1100)),
    ("prog",     (120, 1195, 875, 1288)),
    ("blockL",   (98, 1288, 500, 1422)),
    ("divP",     (520, 1295, 540, 1405)),
    ("blockR",   (550, 1288, 950, 1422)),
    ("price",    (95, 1425, 970, 1522)),
    ("logo1",    (135, 1598, 440, 1728)),
    ("logo2",    (520, 1598, 665, 1728)),
    ("logo3",    (800, 1598, 915, 1728)),
]
owned = np.zeros((H, W), bool)
layers = {}
for name, (x0, y0, x1, y1) in BOXES:
    al = alpha_full[y0:y1, x0:x1].copy()
    al[owned[y0:y1, x0:x1]] = 0
    owned[y0:y1, x0:x1] = True
    if name == "date":
        al[:] = 0  # replaced by corrected text below
    rgba = np.dstack([a[y0:y1, x0:x1], (al * 255).astype(int)]).astype(np.uint8)
    layers[name] = (Image.fromarray(rgba, "RGBA"), x0, y0)

# leftover check: content not owned by any box
left = (alpha_full > 0.5) & ~owned
print("unowned content px:", int(left.sum()))

# corrected date: "Samedi" / "17 octobre 2026" (matches the two-line time column)
font = ImageFont.truetype("mont.ttf", 30)
font.set_variation_by_name("Bold")
ink = (60, 31, 21)
probe = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
tw = probe.textlength("De 10h30 à", font=font)
size = round(30 * 155 / tw)
font = ImageFont.truetype("mont.ttf", size)
font.set_variation_by_name("Bold")
dimg = Image.new("RGBA", (330, 80), (0, 0, 0, 0))
dd = ImageDraw.Draw(dimg)
for i, line in enumerate(["Samedi", "17 octobre 2026"]):
    lw = dd.textlength(line, font=font)
    dd.text(((330 - lw) / 2, 4 + i * 39), line, font=font, fill=ink + (255,))
# date column centre ≈ 228 ; align baseline rows with the time column (1049 / 1088)
layers["date"] = (dimg, 228 - 165, 1049 - 4 - round(size * 0.22))

# layout fixes: lift programme block a bit and logos out of the Instagram reply-bar zone
SHIFT = {"prog": -30, "blockL": -30, "divP": -30, "blockR": -30, "price": -30,
         "logo1": -75, "logo2": -75, "logo3": -75}

def clamp(x): return max(0.0, min(1.0, x))
def out_cubic(t): return 1 - (1 - t) ** 3
def out_back(t, s=1.7):
    t -= 1
    return t * t * ((s + 1) * t + s) + 1

# name: (start, duration, effect)
ANIM = {
    "leaves":  (0.0, 1.0, "fade_rot"),
    "atelier": (0.4, 0.9, "spread"),
    "les":     (0.9, 0.7, "wipe"),
    "gourm":   (1.1, 0.8, "rise"),
    "du":      (1.7, 0.6, "wipe"),
    "barista": (2.0, 0.8, "pop"),
    "ribbon":  (2.7, 0.7, "wipe"),
    "cup":     (2.9, 0.9, "from_left"),
    "choco":   (3.1, 0.9, "from_right"),
    "cal":     (3.9, 0.5, "pop"),
    "date":    (4.0, 0.6, "rise"),
    "div1":    (4.2, 0.5, "grow"),
    "clock":   (4.3, 0.5, "pop"),
    "time":    (4.4, 0.6, "rise"),
    "div2":    (4.6, 0.5, "grow"),
    "pin":     (4.7, 0.6, "drop"),
    "lieu":    (4.8, 0.6, "rise"),
    "prog":    (5.5, 0.7, "wipe_center"),
    "blockL":  (6.0, 0.6, "rise"),
    "divP":    (6.2, 0.5, "grow"),
    "blockR":  (6.3, 0.6, "rise"),
    "price":   (6.9, 0.6, "pop_soft"),
    "logo1":   (7.4, 0.5, "fade"),
    "logo2":   (7.55, 0.5, "fade"),
    "logo3":   (7.7, 0.5, "fade"),
}

def with_alpha(img, k):
    if k >= 1: return img
    r, g, b, al = img.split()
    al = al.point(lambda v: int(v * k))
    return Image.merge("RGBA", (r, g, b, al))

def scaled(img, s):
    w, h = img.size
    nw, nh = max(1, round(w * s)), max(1, round(h * s))
    return img.resize((nw, nh), Image.LANCZOS), (w - nw) / 2, (h - nh) / 2

def wipe(img, p, center=False):
    w, h = img.size
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    soft = 40
    if center:
        half = p * (w / 2 + soft)
        d.rectangle([w / 2 - half, 0, w / 2 + half, h], fill=255)
    else:
        d.rectangle([0, 0, p * (w + soft), h], fill=255)
    out = img.copy()
    out.putalpha(Image.fromarray((np.asarray(img.split()[3]) * (np.asarray(m) / 255)).astype(np.uint8)))
    return out

def render(t):
    frame = Image.new("RGBA", (W, H), tuple(BG) + (255,))
    for name, _ in BOXES:
        img, x, y = layers[name]
        y += SHIFT.get(name, 0)
        st, du, fx = ANIM[name]
        p = clamp((t - st) / du)
        if p <= 0: continue
        e = out_cubic(p)
        dx = dy = 0.0
        im = img
        if fx == "fade":
            im = with_alpha(img, e)
        elif fx == "rise":
            dy = (1 - e) * 35; im = with_alpha(img, e)
        elif fx == "from_left":
            dx = -(1 - e) * 320; im = with_alpha(img, clamp(p * 2))
        elif fx == "from_right":
            dx = (1 - e) * 320; im = with_alpha(img, clamp(p * 2))
        elif fx in ("pop", "pop_soft"):
            s = out_back(p, 2.2 if fx == "pop" else 1.2)
            s = 0.55 + 0.45 * s if fx == "pop" else 0.85 + 0.15 * s
            im, ox, oy = scaled(img, s); dx += ox; dy += oy
            im = with_alpha(im, clamp(p * 3))
        elif fx == "wipe":
            im = wipe(img, e)
        elif fx == "wipe_center":
            im = wipe(img, e, center=True)
        elif fx == "grow":
            w, h = img.size
            nh = max(1, round(h * e))
            im = img.resize((w, nh)); dy = (h - nh) / 2
        elif fx == "drop":
            dy = -(1 - out_back(p, 2.5)) * 60; im = with_alpha(img, clamp(p * 3))
        elif fx == "spread":
            # letters slide in with tightening spacing: scale x from 1.25 -> 1
            w, h = img.size
            sx = 1 + 0.25 * (1 - e)
            im = img.resize((round(w * sx), h), Image.LANCZOS); dx = (w - im.size[0]) / 2
            im = with_alpha(im, e)
        elif fx == "fade_rot":
            im = with_alpha(img, e)

        # continuous ambient motion once in place
        if name == "leaves":
            ang = 2.2 * math.sin(t * 1.6)
            im = im.rotate(ang, resample=Image.BICUBIC, center=(im.size[0], 0))
        if name in ("cup", "choco") and p >= 1:
            ph = 0 if name == "cup" else 1.7
            dy += 7 * math.sin((t - st - du) * 2.2 + ph) * clamp((t - st - du) / 0.5)
        if name == "price" and t > 8.2:
            k = (t - 8.2) % 1.6
            if k < 0.6:
                s = 1 + 0.025 * math.sin(k / 0.6 * math.pi)
                im, ox, oy = scaled(im, s); dx += ox; dy += oy
        frame.alpha_composite(im, (round(x + dx), round(y + dy)))

    # light sweep across BARISTA once it's in
    if 3.0 <= t <= 4.0:
        img, x, y = layers["barista"]
        k = (t - 3.0) / 1.0
        w, h = img.size
        band = np.zeros((h, w))
        cx = -120 + k * (w + 240)
        xs = np.arange(w)[None, :] + np.arange(h)[:, None] * 0.35
        band = np.clip(1 - np.abs(xs - cx) / 45, 0, 1) * 0.55
        al = np.asarray(img.split()[3]) / 255 * band
        hl = np.dstack([np.full((h, w, 3), 255), al * 255]).astype(np.uint8)
        frame.alpha_composite(Image.fromarray(hl, "RGBA"), (x, y))
    return frame.convert("RGB")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for t in map(float, sys.argv[1:]):
            render(t).save(f"prev_{t:05.2f}.png")
        sys.exit()
    n = int(DUR * FPS)
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264",
                           "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
                           "-movflags", "+faststart", "atelier_barista_story.mp4"], stdin=subprocess.PIPE)
    for i in range(n):
        ff.stdin.write(render(i / FPS).tobytes())
    ff.stdin.close(); ff.wait()
    print("done")
