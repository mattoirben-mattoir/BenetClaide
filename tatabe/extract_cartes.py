# Assets for the card-stack version (cartes.html), from the official logo block (assets/logo-officiel-source.png,
# navy on white): white ground removed by flood fill from the borders, plus a white recolour for blue backgrounds,
# and procedural paper textures (lagoon-blue crumpled poster, cream card grain).
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

A = 'assets/'
src = Image.open(A + 'logo-officiel-source.png').convert('RGBA')
a = np.asarray(src).astype(float)
rgb, al = a[..., :3], a[..., 3] / 255
mn = rgb.min(2)
white = (mn > 235) | (al < .1)
lab, n = ndimage.label(white)
border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
ground = np.isin(lab, list(border))
# soft edge: inside ground ring use whiteness as alpha
soft = np.clip((255 - mn) / 70, 0, 1)
alpha = np.where(ground, 0, 1.0)
edge = ndimage.binary_dilation(ground, iterations=2) & ~ground
alpha = np.where(edge, np.maximum(soft, 0), alpha)
alpha = np.where(ndimage.binary_dilation(~ground, iterations=1) & ground, soft * .9, alpha) * al


def save(rgbx, alphax, box, name):
    x0, y0, x1, y1 = box
    out = np.dstack([rgbx[y0:y1, x0:x1], np.clip(alphax[y0:y1, x0:x1], 0, 1) * 255]).astype(np.uint8)
    Image.fromarray(out, 'RGBA').save(A + name)


# un-premultiply the edge (pixels were blended with white)
navy = np.array([0x0b, 0x1a, 0x4f], float)
save(rgb, alpha, (240, 180, 1640, 910), 'logo-bloc.png')              # full block: logo, date, Mtsangamouji, pill
# white version of the wordmark + emblem (navy -> white, orange kept), pill excluded
orange = (rgb[..., 0] - rgb[..., 2]) > 60
dark = ~orange
wrgb = np.where(dark[..., None], 255.0, rgb)
a2 = alpha.copy(); a2[630:, 1030:] = 0                                 # drop the pill under the B
save(wrgb, a2, (240, 180, 1640, 665), 'logo-blanc.png')
save(rgb, a2, (240, 180, 1640, 665), 'logo-navy.png')

# ---------------------------------------------------------------- textures
rng = np.random.default_rng(3)
W, H = 1080, 1920


def noise(scale, w=W, h=H):
    small = rng.standard_normal((h // scale + 2, w // scale + 2))
    return np.asarray(Image.fromarray(((small - small.min()) / np.ptp(small) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)).astype(float) / 255 - .5


def crumple(w=W, h=H, k=60):
    # folds: sum of random straight creases with a soft light/dark side
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    out = np.zeros((h, w))
    for _ in range(k):
        ang = rng.uniform(0, np.pi); c, s = np.cos(ang), np.sin(ang)
        d = (xx - rng.uniform(0, w)) * c + (yy - rng.uniform(0, h)) * s
        out += np.tanh(d / rng.uniform(4, 30)) * rng.uniform(.002, .012) * np.exp(-np.abs(d) / rng.uniform(80, 400))
    return out


base = np.array([0x16, 0x8a, 0xcf], float)                             # bleu lagon lumineux
shade = crumple() * 2.2 + noise(240) * .08 + noise(40) * .04 + noise(3) * .06
bg = np.clip(base[None, None] * (1 + shade[..., None]), 0, 255)
Image.fromarray(bg.astype(np.uint8)).save(A + 'fond-papier.jpg', quality=92)

# solar orange paper (rafale.html background, like the yellow wall of the reference)
base = np.array([0xf9, 0xa5, 0x1a], float)
shade = crumple() * 1.6 + noise(240) * .06 + noise(40) * .03 + noise(3) * .05
Image.fromarray(np.clip(base[None, None] * (1 + shade[..., None]), 0, 255).astype(np.uint8)).save(A + 'fond-orange.jpg', quality=92)

# royal blue of the woman's dress on the illustrated poster (rafale.html background)
base = np.array([0x06, 0x48, 0xf2], float)
shade = crumple() * 1.6 + noise(240) * .07 + noise(40) * .03 + noise(3) * .05
Image.fromarray(np.clip(base[None, None] * (1 + shade[..., None]), 0, 255).astype(np.uint8)).save(A + 'fond-bleu.jpg', quality=92)

# card grain (multiply layer, near white): applied over every card
g = 1 + noise(3, 1000, 1000) * .06 + noise(30, 1000, 1000) * .05 + crumple(1000, 1000, 25) * 3
Image.fromarray(np.clip(g * 245, 0, 255).astype(np.uint8)).convert('RGB').save(A + 'grain-carte.jpg', quality=90)
print('ok')
