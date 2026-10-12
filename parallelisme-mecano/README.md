# « Garde tes roues droites » — version mécano (V3)

- `centre-auto-alonzo-parallelisme-mecano.mp4` : 19,6 s, 1080×1920, sans voix off, musique + bruitages, en boucle.
- `centre-auto-alonzo-parallelisme-mecano-sans-musique.mp4` : même vidéo, bruitages seuls (pic -3 dBFS) pour poser sa musique ; piste seule `audio-bruitages.wav`.

Déroulé : accroche (l'essieu se met à pencher, le mécano sursaute) → le mécano **joue l'analogie** en marchant
droit puis jambes arquées → l'essieu passe par carrossage, contre-carrossage, pincement, ouverture, puis le mécano
règle à la clé (« géométrie correcte ») → 3 bénéfices avec les analogies du texte client → fin avec coordonnées.

Re-rendu : `video/build.sh parallelisme-mecano 19.6 centre-auto-alonzo-parallelisme-mecano.mp4` depuis la racine ;
version sans musique : `SFX_MUSIC=0` pour `sfx.py`, `LOUDNORM=0` pour `render.js`.
