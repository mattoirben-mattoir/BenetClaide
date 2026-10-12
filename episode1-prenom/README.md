# Épisode 1 « Le prénom ! » — maquette

- `centre-auto-alonzo-episode1-prenom-maquette.mp4` : 18,4 s, 1080×1920, sans voix off, musique de synthèse + bruitages. Piste bruitages seule : `audio-bruitages.wav` (pour poser Alpajo).
- **Écrit directement sur la grille musicale** : Alpajo, 143,6 BPM, 11 mesures de 4 temps (18,38 s), un premier temps à 0 s. Pour la version Alpajo, caler la piste pour qu'un premier temps tombe à 0 s.
- **Le prénom est une constante** : `NAME` en haut de la partie épisode de `anim.html` (maquette : « TITINE »). On remplace par le prénom gagnant du vote de l'Épisode 0, puis on refait le rendu.
- Personnage, bulles, décor : repris de l'Épisode 0 (Alonzo en tenue de travail dès le début).

| Mesure | Temps | Contenu |
|---|---|---|
| M1 | 0–1,7 s | Accroche, cadrage serré : la voiture arrive en boitant, pneu avant à plat, air qui fuit, plaque « ??? » sur la portière |
| M2 | 1,7–3,3 s | Jingle « GARDE LE CAP ! » sur le temps, le cadre s'ouvre sur le garage, Alonzo arrive en sautant |
| M3 | 3,3–5,0 s | La plaque se retourne : **le prénom**, confettis, la voiture rougit. « VOUS L'AVEZ BAPTISÉE ! » |
| M4 | 5,0–6,7 s | « Ça va passer… » (grande bulle qui tremble) → facepalm → « Ah non. Pas avec moi ! » → le micro monte, « pouf », un manomètre redescend |
| M5–6 | 6,7–10,0 s | **Idée 1** : « VÉRIFIEZ LA PRESSION » + cadran, aiguille dans le rouge (alerte), « CHAQUE MOIS · À FROID » |
| M7–8 | 10,0–13,4 s | **Idée 2** : « LA BONNE VALEUR ? » → « Portière conducteur » ou « Trappe à carburant » |
| M9 | 13,4–15,0 s | Le pneu se regonfle, la voiture saute et sourit, confettis. « PNEU AU TOP ! » · moins de conso, plus de sécurité. Le client lève le pouce, sans conviction |
| M10 | 15,0–16,7 s | Question : « Vous vérifiez tous les combien ? » · CHAQUE MOIS / JAMAIS… · « Répondez en commentaire » + logo et contact |
| M11 | 16,7–18,4 s | Teaser : le ciel s'assombrit, le nuage du Kashkazi arrive (sourcils froncés, tonnerre), une goutte éclate sur le pare-brise. « PROCHAIN ÉPISODE · VENDREDI 18 DÉCEMBRE » |

- **Écart avec le script V1** (`serie/scripts-saison1.md`) : une seule thématique, la pression, en 2 idées (règle « 2 idées max »). L'usure (Ép. 2) et le parallélisme (Ép. 4) ne sont plus dévoilés ici. La V3 « 3 conseils pneus » reste un post hors série.
- **Découpage caméra** (V2, plus dynamique) : un cadre par temps fort, calé sur la musique (`SHOT` / `KEYS` dans `anim.html`). Gros plan qui suit la voiture (accroche) → dézoom brutal + secousse sur le jingle → gros plan sur la plaque pour le prénom → champ-contrechamp client / Alonzo → lents travellings avant sur les idées, coupe franche entre les deux → gros plan sur le pneu qui se regonfle → plan large + secousse au saut → poussée lente jusqu'au teaser. Petit « punch » de zoom sur chaque premier temps de mesure, flou de mouvement sur les mouvements rapides. Bulles et textes restent à l'écran (hors caméra), les queues de bulles suivent les personnages.
- Zones de sécurité Facebook respectées après l'accroche (rien d'important au-delà de x 940, ni dans les 450 px du bas).

Re-rendu : `SFX_BPM=143.6 video/build.sh episode1-prenom 18.4 centre-auto-alonzo-episode1-prenom-maquette.mp4` depuis la racine. Bruitages seuls : `SFX_MUSIC=0 python3 ../video/sfx.py sfx-events.json 18.4 audio-bruitages.wav` depuis ce dossier.
