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

## Version « rafale » (au plus près de la référence)

- `tatabe-rafale-viens-avec-ton-kit.mp4` : 20,5 s, 1080×1920, 12 i/s façon stop-motion sur fond papier orange.
- Entrée : photo instantanée (affiche illustrée) sous film protecteur qui se décolle, titre tapé lettre à lettre, stickers posés un à un.
- Rafale : une carte = une idée, posée d'un coup toutes les 0,6 à 1,3 s (CETTE ANNÉE → ZÉRO → DÉCHET → PRÉPARE TON KIT → 1. ASSIETTE → 2. COUVERTS → 3. GOBELET → 4. TON SAC), pause « & voilà ton kit » (tout dans le sac), puis 0 SACHET PLASTIQUE → AUCUN → JETABLE → SUR PLACE, carte finale tenue 4,6 s.
- `rafale.html` ; re-rendu depuis `tatabe/` : `SFX_OUT=sfx-rafale.json PAGE=rafale.html node ../video/render.js x x && SFX_STYLE=tropical SFX_BPM=124 python3 ../video/sfx.py sfx-rafale.json 20.5 audio-rafale.wav && PAGE=rafale.html DUR=20.5 node ../video/render.js audio-rafale.wav tatabe-rafale-viens-avec-ton-kit.mp4`

### Musique de la version « rafale »

- « Leo N'Gomma » de Baco (`assets/musique-baco-leo-ngomma.wav`, capté depuis l'enregistrement d'écran fourni), extrait de 5,5 s à 26 s. Les cartes tombent sur les demi-temps (74 BPM, `hb(n)` dans `rafale.html`) et la carte finale arrive sur le passage le plus fort.
- Mix : `SFX_MUSIC=0 python3 ../video/sfx.py sfx-rafale.json 20.5 sfx-rafale-effets.wav` puis
  `ffmpeg -ss 5.5 -t 20.5 -i assets/musique-baco-leo-ngomma.wav -i sfx-rafale-effets.wav -filter_complex "[0:a]afade=t=in:d=0.25,afade=t=out:st=19.6:d=0.9[m];[1:a]volume=0.45[s];[m][s]amix=inputs=2:normalize=0:duration=first[a]" -map "[a]" audio-rafale.wav`.
