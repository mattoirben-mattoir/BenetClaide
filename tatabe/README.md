# Vidéo « Apporte ton assiette et tes couverts » — tataBé, marché gourmand

- `tatabe-apporte-ton-assiette.mp4` : vidéo finale, 30 s, 1080×1920 (Reels / TikTok / Stories), sans voix off : musique tropicale + bruitages synchronisés.
- `assets/affiche.jpg` : affiche d'origine ; `extract.py` en tire le logo détouré, le cartouche « Marché gourmand », les photos (texte de l'affiche effacé autour de la femme) et la bande des logos partenaires.
- `anim.html` : animation (canvas), 9 plans suivant le storyboard : accroche, marché, engagement, jetable, consigne, avant de partir, geste, règle, rendez-vous.
- Charte : bleu lagon `#0a3f78` / `#1675b8` / `#8fd3ee`, orange `#f99d0a`, blanc ; police Montserrat.

Re-rendu depuis la racine du dépôt : `SFX_STYLE=tropical video/build.sh tatabe 30 tatabe-apporte-ton-assiette.mp4`
(`SFX_MUSIC=0` pour la version sans musique).
