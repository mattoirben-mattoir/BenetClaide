# Vidéo « 3 conseils pneus » — Centre Auto Alonzo

- `centre-auto-alonzo-3-conseils-pneus.mp4` : vidéo finale, 12 s, 1080×1920 (format Reels / TikTok / Stories), voix off FR + musique.
- `assets/` : logo détouré, photo d'atelier (issue du visuel Facebook), polices Barlow Condensed et Montserrat.
- Charte : bleu `#084990`, rouge `#E20816`, fond blanc.
- `anim.html` : animation (canvas), `render.js` : rendu image par image vers ffmpeg.
- `gen_tts.py` : voix off (Kokoro TTS, voix `ff_siwis`), `mix.py` : musique, bruitages et mixage → `audio.wav`.

Re-rendu : `NODE_PATH=/opt/node22/lib/node_modules node render.js audio.wav sortie.mp4`
