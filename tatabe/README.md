# Vidéo « Apporte ton assiette, tes couverts et ton gobelet » — tataBé, marché gourmand

- `tatabe-apporte-ton-assiette.mp4` : vidéo finale, 30 s, 1080×1920 (Reels / TikTok / Stories), sans voix off : musique tropicale + bruitages synchronisés.
- `assets/affiche.jpg` : affiche d'origine ; `extract.py` en tire le logo détouré, le cartouche « Marché gourmand », les photos (texte de l'affiche effacé autour de la femme) et la bande des logos partenaires.
- `anim.html` : animation (canvas), 9 plans suivant le storyboard : accroche, marché, engagement, jetable, consigne, avant de partir, geste, règle, rendez-vous.
- Charte : bleu lagon `#0a3f78` / `#1675b8` / `#8fd3ee`, orange `#f99d0a`, blanc ; police Montserrat.

Re-rendu depuis la racine du dépôt : `SFX_STYLE=tropical video/build.sh tatabe 30 tatabe-apporte-ton-assiette.mp4`
(`SFX_MUSIC=0` pour la version sans musique).

## Version « pile de cartes » (stop-motion)

- `tatabe-cartes-viens-avec-ton-kit.mp4` : 25 s, 1080×1920, animation à 12 i/s façon stop-motion (pile de cartes, étiquettes déchirées, stickers, traits au feutre), musique tropicale à 120 bpm + bruitages papier.
- `cartes.html` : l'animation (plan 1 et fond : affiche illustrée, sans texte, via `extract_illustree.py`) ; `extract_cartes.py` : logo officiel détouré (version bleu marine et version blanche) et textures papier.
- Polices : Anton (titres), Permanent Marker et Caveat (manuscrit), Montserrat.

Re-rendu depuis `tatabe/` :
`SFX_OUT=sfx-cartes.json PAGE=cartes.html node ../video/render.js x x && SFX_STYLE=tropical SFX_BPM=120 python3 ../video/sfx.py sfx-cartes.json 25 audio-cartes.wav && PAGE=cartes.html DUR=25 node ../video/render.js audio-cartes.wav tatabe-cartes-viens-avec-ton-kit.mp4`
(avec `NODE_PATH=/opt/node22/lib/node_modules`).
