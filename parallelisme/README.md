# Vidéo « Garde tes roues droites » — Centre Auto Alonzo

- `centre-auto-alonzo-parallelisme.mp4` : vidéo finale, 19 s, 1080×1920, voix off FR + musique.
- `assets/axle-*.png` : essieux découpés du visuel Facebook (`extract.py`).
- Polices, logo du centre et script de rendu partagés avec `../video/`.
- `gen_tts.py` (voix), `mix.py` (musique + mixage → `audio.wav`).

Re-rendu : `PAGE=anim.html DUR=19 NODE_PATH=/opt/node22/lib/node_modules node ../video/render.js audio.wav sortie.mp4`
