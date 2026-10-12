# Cut out the five axles of the Facebook visual (white background removed,
# labels and red ground marks dropped: only the largest object is kept).
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
src = Image.open('assets/visuel-reference.png').convert('RGB')
BOXES = {
    'axle-correct':   (330, 266, 750, 410),
    'axle-contre':    (130, 472, 460, 596),
    'axle-carrossage':(630, 476, 940, 596),
    'axle-pincement': (130, 644, 460, 768),
    'axle-ouverture': (625, 652, 940, 768),
}
for name, box in BOXES.items():
    a = np.array(src.crop(box)).astype(int)
    white = a.min(2) > 225
    lab, n = ndimage.label(white)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    fg = ~np.isin(lab, list(border))
    red = (a[..., 0] - np.maximum(a[..., 1], a[..., 2]) > 40)
    red = ndimage.binary_dilation(red, iterations=2)  # include the anti-aliased edges
    fg &= ~red
    fl, fn = ndimage.label(fg)
    sizes = ndimage.sum(fg, fl, range(1, fn + 1))
    fg = fl == (np.argmax(sizes) + 1)
    al = Image.fromarray(fg.astype(np.uint8) * 255).filter(ImageFilter.GaussianBlur(0.7))
    rgba = Image.fromarray(a.astype(np.uint8)).convert('RGBA'); rgba.putalpha(al)
    rgba = rgba.crop(rgba.getbbox()); rgba.save(f'assets/{name}.png'); print(name, rgba.size)
