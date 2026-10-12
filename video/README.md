# Vidéo « 3 conseils pneus » — Centre Auto Alonzo

- `centre-auto-alonzo-3-conseils-pneus.mp4` : vidéo finale, 15 s, 1080×1920 (format Reels / TikTok / Stories), sans voix off : musique + bruitages synchronisés.
- `assets/` : logo détouré, photo d'atelier (issue du visuel Facebook), polices Barlow Condensed et Montserrat.
- Charte : bleu `#084990`, rouge `#E20816`, fond blanc.
- `sfx.py` : musique + bibliothèque de bruitages synthétisés ; chaque animation déclare ses événements (`window.SFX`), le son tombe sur l'image exacte.
- `build.sh` : chaîne complète, son normalisé à -14 LUFS.
- `anim.html` : animation (canvas), `render.js` : rendu image par image vers ffmpeg.

Re-rendu (événements sonores → bruitage → images) : `video/build.sh video 15 centre-auto-alonzo-3-conseils-pneus.mp4` depuis la racine du dépôt.
