# Prototype « mécano présentateur » — 3 conseils pneus

- `centre-auto-alonzo-3-conseils-mecano.mp4` : 17,6 s, 1080×1920, sans voix off.
- Un personnage mécano animé (charte Centre Auto Alonzo : casquette et t-shirt marine, logo) présente les conseils :
  bulles de texte, gestes (salut, pointe l'icône, pouce levé), expressions (sourire, inquiet devant l'usure),
  « babillage » sonore sans mots pendant que la bulle s'écrit (`blip` dans `../video/sfx.py`).
- Le personnage reste à l'écran pendant les transitions : un seul présentateur du début à la fin.

Re-rendu : `video/build.sh mecano 17.6 centre-auto-alonzo-3-conseils-mecano.mp4` depuis la racine du dépôt.

Inspirations motion design appliquées :
- accroche-question en typographie animée, mot par mot (« VOS PNEUS S'USENT TROP VITE ? »), puis la promesse ;
- mot-clé de chaque conseil révélé sur un bandeau incliné (effet surligneur) ;
- récompense visuelle façon Duolingo : confettis aux couleurs de la marque + petit saut du mécano ;
- rendu « fait main » : ombre portée façon sticker et léger grain.
