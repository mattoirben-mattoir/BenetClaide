# V3 « mécano présentateur » — 3 conseils pneus

- `centre-auto-alonzo-3-conseils-mecano.mp4` : 17,4 s (durées reprises du montage client), 1080×1920, sans voix off, en boucle (la dernière image rejoint la première).
- Une petite histoire avec un **pneu héros** présent du début à la fin : il se dégonfle (accroche), le mécano le regonfle au
  manomètre (pression), l'inspecte à la loupe (usure / vibrations), le redresse à la clé (équilibrage / parallélisme).
- Le **mécano agit** : bras animés en cinématique inverse, outils en main, expressions (choc, inquiet, sourire), saut de joie.
- Fonds alternés blanc / bleu révélés en cercle depuis le pneu, titres en typographie animée + mot-clé surligné,
  bulles qui apportent une info en plus du titre, confettis aux moments de réussite, contour « sticker », grain.

- `centre-auto-alonzo-3-conseils-mecano-sans-musique.mp4` : même vidéo, **bruitages seuls** (pic -3 dBFS), pour poser sa propre musique ; piste seule : `audio-bruitages.wav`.

Re-rendu : `video/build.sh mecano 17.4 centre-auto-alonzo-3-conseils-mecano.mp4` depuis la racine du dépôt.
Version sans musique : `SFX_MUSIC=0` pour `sfx.py`, `LOUDNORM=0` pour `render.js`.
