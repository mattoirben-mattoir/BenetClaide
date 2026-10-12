# Vidéo « Pneus Joyroad » — Centre Auto Alonzo

- `centre-auto-alonzo-pneus-joyroad.mp4` : vidéo finale, 18 s, 1080×1920, voix off FR + musique.
- `assets/` : éléments découpés du visuel Facebook (`extract.py`) — pneus, véhicules, logos Joyroad / Fulda / Goodyear / Michelin.
- Polices, logo du centre et script de rendu partagés avec `../video/`.
- `gen_tts.py` (voix, noms de marques en graphie phonétique), `mix.py` (musique + mixage → `audio.wav`).

Re-rendu : `PAGE=anim.html DUR=18 NODE_PATH=/opt/node22/lib/node_modules node ../video/render.js audio.wav sortie.mp4`
