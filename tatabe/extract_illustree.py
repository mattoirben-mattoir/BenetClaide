# Illustrated poster (assets/affiche-illustree.png, 1122x1402) -> clean, text-free pieces for cartes.html:
#  - femme-illustree.jpg : the woman with her tray, poster logo/emblem/date and the "STANDS..." words inpainted away
#  - plage-illustree.jpg : the lagoon / beach band, used as a living blue background instead of a flat colour
import numpy as np, cv2
from PIL import Image, ImageEnhance
from scipy import ndimage

A = 'assets/'
im = Image.open(A + 'affiche-illustree.png').convert('RGB')
a = np.asarray(im).astype(float)
mn, mx = a.min(2), a.max(2)
whiteish = (mn > 205) & (mx - mn < 45)
orange = (a[..., 0] - a[..., 2] > 90) & (a[..., 0] > 180)
mask = np.zeros(mn.shape, bool)
# logo letters, emblem, date and town name in the sky right of the turban
mask[60:445, 395:1122] |= whiteish[60:445, 395:1122]
mask[60:150, 480:620] |= orange[60:150, 480:620]
mask[170:340, 360:400] |= whiteish[170:340, 360:400]           # first 't' overlapping the turban edge
# pill "MARCHÉ GOURMAND" (orange) and its white type
mask[300:375, 755:1060] = True
# "STANDS GOURMANDS ... DE LOISIRS" (white letters with a dark outline) where they touch the tray
text = np.zeros_like(mask); text[850:1160, 495:660] = whiteish[850:1160, 495:660]
mask = ndimage.binary_dilation(mask, iterations=4) | ndimage.binary_dilation(text, iterations=8)
clean = cv2.inpaint(np.asarray(im)[..., ::-1].copy(), mask.astype(np.uint8) * 255, 9, cv2.INPAINT_NS)[..., ::-1]
clean = Image.fromarray(clean)
clean = ImageEnhance.Color(clean).enhance(1.12)
clean.save(A + 'affiche-illustree-propre.jpg', quality=94)
clean.crop((0, 140, 620, 1170)).save(A + 'femme-illustree.jpg', quality=95)
# lagoon band: sea, beach and hills (no poster text), saturated a little more
ImageEnhance.Color(clean.crop((560, 430, 1122, 800))).enhance(1.15).save(A + 'plage-illustree.jpg', quality=95)
# full-screen background for the card stack: sky, palms, lagoon and beach (text removed above)
clean.crop((420, 120, 1122, 860)).save(A + 'fond-plage.jpg', quality=94)
print('ok')
