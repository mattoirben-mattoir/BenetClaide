# Épisode 0 « Karibu ! » — maquette

- `centre-auto-alonzo-episode0-karibu-maquette.mp4` : 17,4 s, 1080×1920, musique + bruitages. Piste bruitages seule : `audio-bruitages.wav`.
- **Photo de référence du personnage** : `assets/alonzo-reference.jpg` (recadrage 9:16 de la photo validée : Alonzo à l'atelier, micro orange à la poitrine). Le dessin est calqué sur cette pose. **C'est la base de toute la série.**
- **Le micro est son accessoire** : tenu à la poitrine (comme sur la photo), porté à la bouche quand il parle (ondes de voix), lancé en l'air et rattrapé pendant le saut, levé pour le titre, puis tendu vers le spectateur pour la question finale (« à vous de répondre »).
- Bulle : « Eh oui… c'est moi, Alonzo ! » (pas besoin de dire « en dessin », on le voit).
- **Calé sur Alpajo (143,6 BPM)** : l'animation est écrite en « temps de conception » puis recalée par une courbe de temps (`WARP` dans `anim.html`) pour que chaque coup tombe sur un temps de la musique (piste démarrée à 0,76 s) : clin d'œil 2,00 s · bulle + « ALONZO » 3,67 s · saut 5,76 s · micro rattrapé 6,18 s · crissement 6,80 s (demi-temps) · klaxon 7,01 s · facepalm 8,27 s · « Pas avec moi ! » 8,89 s · tenue de travail 9,73 → titre 10,36 s · micro lancé 13,70 s · clé rattrapée + question 14,12 s · logo 14,95 s. Les bruitages suivent la même courbe.
- **Dernier plan : il troque le micro contre une clé** (le micro monte, « pouf » au sommet, une clé plate redescend et il la rattrape sur le temps) : on passe du présentateur au mécanicien.
- **Tenue de travail complète** : le changement balaie maintenant tout le corps — tee-shirt bleu, puis **pantalon cargo** (poches latérales à rabat, surpiqûres, chiffon rouge qui dépasse) et **chaussures de travail** (au lieu des mocassins de ville).
- **Corrections de cohérence** : l'ombre au sol reste au sol pendant le saut (elle rétrécit) ; « ATTENDEZ… » et l'étiquette maquette disparaissent avant la fin du dessin ; le bloc « Épisode 1 » s'efface avant le lancer du micro ; la clé ne chevauche pas le logo ; « TÛT ! TÛT ! » et les bulles ne touchent plus le personnage. Dates vérifiées : 25/11/2026 = mercredi (Karibu), 04/12/2026 = vendredi (Épisode 1).
- **Direction artistique / couleurs** : trait d'encre bleu nuit sur chaque partie du personnage (lisible sur fond clair comme sur le bleu) ; peau chaude avec lumière (crâne, nez, avant-bras) et ombre propre ; barbe courte taillée le long de la mâchoire + moustache, comme sur les photos (les joues restent visibles) ; lunettes sport relevées avec liseré de lumière pour se détacher du crâne ; chemise blanche avec volume (ombre côté droit, plis), fleur crème et feuilles vertes comme sa boutonnière ; tee-shirt de travail **bleu marque** (#084990) **simple** (col rond, logo), nettement séparé du pantalon bleu nuit ; mocassins vernis avec reflet et pampille ; ombre portée au sol. Le bandeau bleu/rouge du décor est remonté en fronton pour ne plus passer derrière sa tête.
- Mascotte = Alonzo d'après ses photos : crâne rasé, lunettes de soleil relevées sur la tête, barbe noire courte, silhouette fine, pantalon bleu marine, ceinture noire, mocassins.
- **Deux transitions de tenue** : (1) vrai Alonzo en chemise blanche → Alonzo dessiné en chemise blanche + fleur (2 s) ; (2) « Ah non. Pas avec moi ! » → le tee-shirt de travail bleu marine + logo tombe du ciel et s'enfile par-dessus (9,4–9,95 s, whoosh / swoosh / pop). Il reste en tee-shirt pour le titre et la fin — c'est sa tenue pour les épisodes.
- **Maquette** : les 2 premières secondes utilisent la photo de référence d'Alonzo. Elles seront
  remplacées par le vrai plan d’Alonzo, le gérant (« Karibu ! » + clin d'œil + 1 s immobile), puis la transformation reprend sa pose.

Déroulé : vrai plan « Karibu ! » → clin d'œil, flash, croquis blanc qui dessine la mascotte → « Eh oui… c’est moi, Alonzo, en dessin ! » (bandeau ALONZO)
→ la voiture du client arrive en trombe (« Ça va passer… ») → « Ah non. Pas avec moi ! » → titre « GARDE LE CAP ! »
+ « Épisode 1 · vendredi 4 décembre » (jingle de série) → Alonzo montre la voiture du client : « Et sa voiture ? Donnez-lui un prénom ! » + logo + contact.

Re-rendu : `video/build.sh episode0-karibu 17.4 centre-auto-alonzo-episode0-karibu-maquette.mp4` depuis la racine.

## V2 (relecture motion design)
- **Pneu avant à plat lisible** : la voiture s'affaisse sur la roue avant, pneu écrasé avec bourrelet, jante basse, petits jets d'air à l'arrivée ; sourcil triste et grosse moue.
- **Bulles lisibles sur téléphone** : texte 52 px (64 px gras pour « Ça va passer… »), largeur calée sur le texte, mots affichés entiers (plus de « Ça va pas »). « Ça va passer… » apparaît d'un bloc et tremble ; « Ah non. Pas avec moi ! » d'un bloc, tenu jusqu'au titre.
- **Zones de sécurité Facebook** : voiture (x 664, échelle 0,95), Alonzo (HOME x 280, MASC x 720), pouce et flèche sortis de la colonne des boutons à droite (> 940 px).
- **Fin** : logo et contact agrandis, appel à l'action « QUEL PRÉNOM ? » qui pulse sur le temps + « Répondez en commentaire », flèche qui rebondit sur la voiture ; la bulle se limite à « Et sa voiture ? ».
- **Croquis de transformation** : il est maintenant dessiné à l'échelle de la photo (1,6) et la recouvre exactement (il était à l'échelle 1).
- Aucun timing modifié : les bruitages et le calage Alpajo restent valables.

## V3 (décor)
- **Le vrai garage de Combani** comme décor (`video/set-garage.js`, partagé avec l'Épisode 1) à la place du rideau gris : façade, bandeau bleu, panneau « CENTRE AUTO ALONZO », baie d'atelier, tonnelle, parvis.
- Alonzo se présente debout sur le parvis (MASC y 640, étiquette « ALONZO » sous ses pieds) ; sous-titre de la série, contact et appel à l'action posés sur des fonds blancs pour rester lisibles sur la façade.
- Timings inchangés : l'aperçu Alpajo se refait en remplaçant simplement la piste son.
