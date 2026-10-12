# Épisode 1 « Le prénom ! » — maquette

- `centre-auto-alonzo-episode1-prenom-maquette.mp4` : **28,4 s**, 1080×1920, sans voix off, musique de synthèse + bruitages. Piste bruitages seule : `audio-bruitages.wav` (pour poser Alpajo).
- **Contenu** : celui de la vidéo « 3 conseils pneus » (version mécano, `mecano/`), raconté dans la série : pression, usure & vibrations, équilibrage & parallélisme, carte « Besoin d'un check-up ? ».
- **Écrit directement sur la grille musicale** : Alpajo, 143,6 BPM, 17 mesures de 4 temps, un premier temps à 0 s. Pour la version Alpajo, caler la piste pour qu'un premier temps tombe à 0 s.
- **Le prénom est une constante** : `NAME` en haut de la partie épisode de `anim.html` (maquette : « TITINE »). On remplace par le prénom gagnant du vote de l'Épisode 0, puis on refait le rendu.
- Personnage et bulles repris de l'Épisode 0 (Alonzo en tenue de travail dès le début). **Décor** : le vrai garage de Combani, dessiné d'après la photo de la façade (`video/set-garage.js`, partagé entre les épisodes) : façade grise, bandeau bleu « ENTRETIEN & RÉPARATION · TOUTES MARQUES », panneau blanc « CENTRE AUTO ALONZO », baie d'atelier avec pont et néons, tonnelle blanche à gauche, bordure jaune et noire, parvis en béton. Pas de logos de réseau (Top Garage, Groupauto).
- **Un outil par conseil** : le micro devient un manomètre (1/3), le manomètre une loupe (2/3), la loupe une clé (3/3), toujours avec le « pouf » au sommet du lancer.

| Mesure | Temps | Contenu |
|---|---|---|
| M1 | 0–1,7 s | Accroche : gros plan qui suit la voiture, pneu avant à plat, air qui fuit, plaque « ??? » |
| M2 | 1,7–3,3 s | Jingle « GARDE LE CAP ! », dézoom + secousse, Alonzo arrive en sautant |
| M3 | 3,3–5,0 s | Gros plan sur la plaque : **le prénom**, confettis. « VOUS L'AVEZ BAPTISÉE ! » |
| M4 | 5,0–6,7 s | Gros plan client « Ça va passer… » → gros plan Alonzo (facepalm, « Pas avec moi ! ») → le micro devient un manomètre |
| M5–7 | 6,7–11,7 s | **1/3 VÉRIFIEZ LA PRESSION · CHAQUE MOIS** : « Avec la chaleur, la pression varie ! » → gros plan : flexible du compresseur sur la valve, cadran du rouge au bleu, le pneu se regonfle (✓) → « À FROID, AVANT DE ROULER » |
| M8–10 | 11,7–16,7 s | **2/3 SURVEILLEZ L'USURE · ET LES VIBRATIONS** : le manomètre devient une loupe → gros plan : la loupe balaie la bande de roulement, un côté usé, puis ça vibre (alerte) → « Ça vibre au volant ? Passez nous voir ! » |
| M11–12 | 16,7–20,1 s | **3/3 ÉQUILIBRAGE · & PARALLÉLISME** : la loupe devient une clé → médaillon : le pneu vu de face penche, la clé cliquette, il se redresse sur le pointillé (✓) → « Bien réglés, vos pneus durent plus longtemps ! » |
| M13 | 20,1–21,7 s | « PNEUS AU TOP ! » · moins de conso, plus de sécurité. La voiture saute, confettis, le client lève le pouce sans conviction |
| M14 | 21,7–23,4 s | « Vous vérifiez tous les combien ? » · CHAQUE MOIS / JAMAIS… · « Répondez en commentaire » |
| M15–16 | 23,4–26,7 s | Carte de fin : « BESOIN D'UN CHECK-UP ? », logo, « Appelez-nous » +262 639 29 17 02, 32 Route de Coconi · Combani. « On vous attend à Combani ! » |
| M17 | 26,7–28,4 s | Teaser : le ciel s'assombrit, le nuage du Kashkazi arrive, une goutte éclate sur le pare-brise. « PROCHAIN ÉPISODE · VENDREDI 18 DÉCEMBRE » |

- **Écart avec le script V1** (`serie/scripts-saison1.md`) : 28 s au lieu de 18 (exception assumée pour l'épisode qui installe la série). Le parallélisme est déjà traité ici : l'Ép. 4 (« Ça tire à droite ») devra approfondir le nid-de-poule plutôt que répéter le conseil.
- **Découpage caméra** (V2, plus dynamique) : un cadre par temps fort, calé sur la musique (`SHOT` / `KEYS` dans `anim.html`). Gros plan qui suit la voiture (accroche) → dézoom brutal + secousse sur le jingle → gros plan sur la plaque pour le prénom → champ-contrechamp client / Alonzo → lents travellings avant sur les idées, coupe franche entre les deux → gros plan sur le pneu qui se regonfle → plan large + secousse au saut → poussée lente jusqu'au teaser. Petit « punch » de zoom sur chaque premier temps de mesure, flou de mouvement sur les mouvements rapides. Bulles et textes restent à l'écran (hors caméra), les queues de bulles suivent les personnages.
- Zones de sécurité Facebook respectées après l'accroche (rien d'important au-delà de x 940, ni dans les 450 px du bas).

Re-rendu : `SFX_BPM=143.6 video/build.sh episode1-prenom 28.45 centre-auto-alonzo-episode1-prenom-maquette.mp4` depuis la racine (≈ 6 min). Bruitages seuls : `SFX_MUSIC=0 python3 ../video/sfx.py sfx-events.json 28.45 audio-bruitages.wav` depuis ce dossier.
