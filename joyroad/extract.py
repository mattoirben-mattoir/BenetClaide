# Cut out the elements of the Facebook visual and remove the white background
# (only the white connected to the crop border, so white lettering/chrome stays).
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
src = Image.open('assets/visuel-reference.png').convert('RGB')
BOXES = {
    'joyroad':   (170, 195, 790, 290),
    'tire-normal':    (55, 315, 242, 612),
    'tire-renforce':  (244, 295, 438, 612),
    'tire-at':   (432, 296, 690, 662),
    'tire-mt':   (690, 228, 1012, 662),
    'car-city':  (100, 672, 250, 752),
    'car-suv':   (340, 682, 490, 770),
    'car-pickup':(665, 690, 852, 786),
    'fulda':     (48, 815, 222, 860),
    'goodyear':  (238, 815, 408, 860),
    'michelin':  (432, 800, 602, 862),
}
for name, box in BOXES.items():
    a = np.array(src.crop(box)).astype(int)
    white = (a.min(2) > 228)
    lab, n = ndimage.label(white)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    bg = np.isin(lab, list(border))
    fg = ~bg
    if name == 'tire-mt':
        fg[:54, :72] = False; fg[:44, :100] = False  # end of the Joyroad logo
    sat = a.max(2) - a.min(2) > 70
    if name == 'tire-mt':
        fg[:80] &= ~sat[:80]  # yellow leftovers
    if name == 'car-pickup':
        fg[-16:] &= ~sat[-16:]  # red/blue swoosh of the shop logo under the wheels
    if name.startswith(('tire', 'car')):
        # keep only the main object (drops fragments of neighbouring elements)
        fl, fn = ndimage.label(fg)
        sizes = ndimage.sum(fg, fl, range(1, fn + 1))
        fg = fl == (np.argmax(sizes) + 1)
        fg = ndimage.binary_fill_holes(fg) if name.startswith('car') else fg
    if name == 'joyroad':
        # top of the mud-terrain tire touches the "D": drop its non-yellow pixels
        reg = np.zeros_like(fg); reg[76:, 592:] = True
        yellow = (a[..., 0] > 170) & (a[..., 1] > 140) & (a[..., 2] < 110)
        fg &= ~(reg & ~yellow)
    alpha = fg.astype(np.uint8) * 255
    al = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.8))
    rgba = Image.fromarray(a.astype(np.uint8)).convert('RGBA'); rgba.putalpha(al)
    bb = rgba.getbbox(); rgba = rgba.crop(bb)
    rgba.save(f'assets/{name}.png'); print(name, rgba.size)
