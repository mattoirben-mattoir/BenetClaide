# Cuts the tataBé poster (assets/affiche.jpg, 1638x2048) into the pieces the video needs:
# white logo (alpha from whiteness), orange "Marché gourmand" pill, photo crops, partner band.
import numpy as np
from PIL import Image
from scipy import ndimage

A = 'assets/'
im = Image.open(A + 'affiche.jpg').convert('RGB')
a = np.asarray(im).astype(float)


def save_rgba(rgb, alpha, name):
    out = np.dstack([rgb, np.clip(alpha, 0, 1) * 255]).astype(np.uint8)
    Image.fromarray(out, 'RGBA').save(A + name)


# Logo "tataBé": white letters over the sky. Alpha from the darkest channel (sky has a low red).
x0, y0, x1, y1 = 515, 120, 1625, 470
reg = a[y0:y1, x0:x1]
mn = reg.min(2)
alpha = np.clip((mn - 150) / 80, 0, 1)
# keep only the big connected letters (drops stray bright leaves)
core = (mn > 215) & (reg.max(2) - mn < 30)   # pure white only: drops sunlit leaves
lab, n = ndimage.label(core)
sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
keep = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s > 3000])
keep = ndimage.binary_dilation(keep, iterations=4)
alpha *= keep
alpha[215:, :68] = 0   # sunlit leaf touching the first t
save_rgba(np.full(reg.shape, 255.0), alpha, 'logo.png')

# "MARCHÉ GOURMAND" pill: orange pixels (red >> blue), holes (white letters) filled.
x0, y0, x1, y1 = 1050, 420, 1530, 555
reg = a[y0:y1, x0:x1]
orange = (reg[..., 0] - reg[..., 2]) > 90
lab, n = ndimage.label(orange)
big = lab == (1 + np.argmax(ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))))
pill = ndimage.binary_fill_holes(big)
pill = ndimage.binary_erosion(pill, iterations=1)
alpha = ndimage.gaussian_filter(pill.astype(float), .8)
save_rgba(reg, alpha, 'marche-gourmand.png')

# Woman crop: the poster's logo, emblem and date text sit right next to her turban.
# Mask them (logo matte + white/orange type in the sky) and inpaint the sky back.
import cv2
logo_a = np.asarray(Image.open(A + 'logo.png'))[..., 3] > 20
mask = np.zeros(a.shape[:2], bool)
mask[120:470, 515:1625] |= logo_a
sky = a[60:680, 600:1000]
smn, smx = sky.min(2), sky.max(2)
mask[60:680, 600:1000] |= (smn > 185) & (smx - smn < 60)                  # white type
mask[60:680, 600:1000] |= (sky[..., 0] - sky[..., 2]) > 80                  # orange emblem sun
edge = a[270:420, 545:600]                                                # 't' stroke against the turban
mask[270:420, 545:600] |= (edge.min(2) > 175) & (edge.max(2) - edge.min(2) < 70)
mask = ndimage.binary_dilation(mask, iterations=5)
clean = cv2.inpaint(np.asarray(im)[..., ::-1].copy(), mask.astype(np.uint8) * 255, 12, cv2.INPAINT_TELEA)[..., ::-1]
Image.fromarray(clean).crop((60, 230, 900, 1640)).save(A + 'femme-plateau.jpg', quality=95)

# Photo crops (kept at source resolution; the animation scales them)
im.crop((140, 1060, 1000, 1640)).save(A + 'plateau.jpg', quality=95)       # food close-up
im.crop((560, 640, 1638, 1240)).save(A + 'plage.jpg', quality=95)          # beach, no poster text
im.crop((0, 1600, 1638, 2048)).save(A + 'partenaires.jpg', quality=95)     # wavy band + partner logos
print('ok')

# Partner band with its wavy top, poster photo removed: near-white ground connected to the bottom edge,
# logos inside it filled, plus the green Nari Parane leaves that stick out above the wave.
band = a[1600:2048]
mn, mx = band.min(2), band.max(2)
ground = (mn > 205) & (mx - mn < 28)
lab, n = ndimage.label(ground)
bottom = set(lab[-1][lab[-1] > 0])
m = np.isin(lab, list(bottom))
m = ndimage.binary_closing(m, iterations=3)
m = ndimage.binary_fill_holes(m)
green = (band[..., 1] > band[..., 0] + 25) & (band[..., 1] > band[..., 2])
lab, n = ndimage.label(ndimage.binary_closing(green | m, iterations=2))
m = lab == lab[-30, 800]
m = ndimage.binary_fill_holes(m)
m = ndimage.binary_opening(m, iterations=2)
save_rgba(band, ndimage.gaussian_filter(m.astype(float), .8), 'partenaires.png')
