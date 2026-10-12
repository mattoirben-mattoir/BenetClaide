# Vidéo « Des pneus pour toutes les tailles » — Centre Auto Alonzo

- `centre-auto-alonzo-pneus-toutes-tailles.mp4` : vidéo finale, 16 s, 1080×1920, voix off FR + musique.
- `assets/route.jpg` : photo de la route issue du visuel Facebook (étiquettes d'origine recouvertes, logo masqué par la découpe courbe).
- Polices, logo du centre et script de rendu partagés avec `../video/`.
- `gen_tts.py` (voix), `mix.py` (musique + mixage → `audio.wav`).

Re-rendu : `PAGE=anim.html DUR=16 NODE_PATH=/opt/node22/lib/node_modules node ../video/render.js audio.wav sortie.mp4`
