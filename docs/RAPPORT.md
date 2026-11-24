# Rapport de projet — Flexarion (concours SEO)

Ce document trace le travail réalisé sur le site du studio fictif **Flexarion** (BUT Informatique 2e année, IUT d'Aix-Marseille, concours SEO inter-groupes sur le mot-clé « Flexarion »). Chaque tâche significative fait l'objet d'une entrée normalisée.

Équipe projet (créateurs réels) : BARTAL Manal, CHAIB EDDOUR Kawthar, PETIT Noé, SBEGHEN Alexandre.
Agent IA de développement : **FlexaBot** (agent IA conversationnel avec accès à un environnement Linux de travail, outil de génération d'images intégré).

## Journal d'usage de l'IA

Le journal ci-dessous liste de façon factuelle les outils IA utilisés et les consignes (prompts) données. Il est tenu au fil de l'eau.

| Date | Outil | Usage | Relu / validé par un humain |
|---|---|---|---|
| 17/11/2026 | FlexaBot (agent IA) | Lecture du brief et des CM1-CM3, plan de la Phase 1 | Questions de cadrage posées puis validées par Alexandre |
| 17/11/2026 | FlexaBot — génération d'images | 10 visuels (logo, hero, key art, 3 concept arts, 4 couvertures de devlog) | À retravailler par l'équipe |
| 17/11/2026 | FlexaBot (agent IA) | Rédaction des pages, des 4 devlogs, du code HTML/CSS/JSON-LD | À relire par l'équipe |
| 17/11/2026 | Lighthouse 12 (Google, non IA générative) | Audit performance / accessibilité / SEO | — |
| 17/11/2026 | Validateur W3C Nu (non IA) | Validation HTML | — |
| 18/11/2026 | FlexaBot (agent IA) | Application de la revue V1 de l'équipe (forme, code, données structurées) | Revue rédigée par l'équipe ; résultat à vérifier en ligne |
| 18/11/2026 | Validateur Nu local (vnu.jar), Lighthouse 12, Chrome headless (non IA) | Validation HTML/CSS, audits, captures d'écran | — |
| 18/11/2026 | FlexaBot (agent IA) | Rédaction du profil itch.io (HTML ≤ 5 000 caractères) et du README de l'organisation GitHub | À relire et coller par l'équipe |
| 18/11/2026 | FlexaBot (agent IA) | Application de la revue V1.1 (v1.2 du site) : réseaux, icônes, pied de page, équipe, Below Zero, devlogs, README | Revue rédigée par l'équipe ; résultat à vérifier en ligne |
| 18/11/2026 | FlexaBot — génération d'images | 8 avatars illustrés de l'équipe + 1 aperçu de jeu de Below Zero | À retravailler par l'équipe |
| 18/11/2026 | html-validate, Lighthouse 12, Chrome headless / Puppeteer (non IA) | Validation HTML, audits, captures d'écran | — |
| 19/11/2026 | FlexaBot (agent IA) | Application de la revue V1.2 (v1.3 du site) : ASCII art, message console, police, mentions légales, méta descriptions, relief, impression, minification, favicons | Revue rédigée par l'équipe ; résultat à vérifier en ligne |
| 19/11/2026 | fontTools / pyftsubset, Pillow, html-validate, Lighthouse 12, Puppeteer, pyfiglet (non IA) | Sous-ensembles de police, favicons, validation, audits, captures, lettrage ASCII | — |
| 19/11/2026 | FlexaBot (agent IA) | Retouches v1.3.1 (flèche « retour en haut » en SVG) et v1.3.2 (survol des cartes) demandées par l'équipe | Choix visuels validés par l'équipe sur captures |
| 19/11/2026 | FlexaBot (agent IA) | Application de la revue V1.3 (v1.4.0 du site) : animations du menu, du burger, des FAQ et des boutons | Revue rédigée par l'équipe ; ressenti à vérifier sur appareils réels |
| 19/11/2026 | html-validate, Lighthouse 12, Puppeteer / Chrome sous Xvfb (non IA) | Validation, audits, captures de survol et mesures des transitions | — |
| 20/11/2026 | FlexaBot (agent IA) | v1.4.1 : reflet d'attente et fondu à l'apparition des images, à la demande de l'équipe | Rendu validé par l'équipe sur captures |
| 20/11/2026 | html-validate, Lighthouse 12, Puppeteer (non IA) | Validation, audits, captures avec images volontairement retenues | — |
| 20/11/2026 | FlexaBot (agent IA) | v1.4.2 : correction des fondus d'images, invisibles sur une connexion normale en v1.4.1 (signalé par l'équipe) | Testé par l'équipe sur son PC après déploiement |
| 20/11/2026 | Puppeteer, Lighthouse 12, html-validate (non IA) | Mesure de l'opacité image par image (cache vide et cache chaud), LCP observé, audits | — |
| 20/11/2026 | FlexaBot (agent IA) | v1.4.3 : correction de l'animation du menu burger (liens qui bougeaient dans tous les sens sur mobile, signalé par l'équipe) | À vérifier par l'équipe sur téléphone |
| 20/11/2026 | FlexaBot (agent IA) | v1.4.4 : recommandations GreenIT-Analysis (script en ligne et JSON-LD minifiés, feuille d'impression séparée) avec mesures avant / après | Accord de l'équipe sous condition d'absence d'impact sur la vitesse et le SEO |
| 22/11/2026 | FlexaBot — génération d'images | 2 illustrations de devlog (coupe Aix / Sextia, Sacha et le Diapason à Sextia) converties en WebP (480 / 960 / 1280 px) | À retravailler par l'équipe |
| 22/11/2026 | FlexaBot (agent IA) | Rédaction et intégration des devlogs #5 et #6 (v1.5.0), mise à jour de l'accueil, de Below Zero, du studio, du kit presse, du sitemap, du flux RSS et de `llms.txt` | Textes soumis à l'équipe pour relecture avant publication |
| 22/11/2026 | html-validate, Lighthouse 12, Puppeteer, Pillow (non IA) | Validation HTML, audits, captures d'écran, mesure SERP, conversion WebP | — |

**Prompt de mission initial** (donné par l'équipe à l'agent) : « Mission : Développement agentique du site Flexarion (Concours SEO) » — rôle d'agent de développement principal, objectifs (position Google sur « Flexarion », GEO, site techniquement irréprochable, backlinks white hat, documentation de l'IA), périmètre technique, contenu minimum, mentions légales, brand guidelines (identité, palette, positionnement, personas Léo / Chloé / Mehdi), modèle de reporting et stratégie en 4 phases. Le texte complet est conservé dans l'historique de conversation de l'équipe.

**Réponses de cadrage données par l'équipe** : organisation GitHub `flexarion-officiel` ; dépôt déjà initialisé avec un `index.html` de test ; commits au nom de FlexaBot ; HTML/CSS statique validé ; visuels générés par IA ; mise en ligne dès que possible.

---

### Tâche : Analyse du brief et des cours
- Objectif : Extraire du brief et des CM1, CM2, CM3 toutes les contraintes et bonnes pratiques applicables au site.
- Critères de validation : Contraintes du brief listées (pages minimum, calendrier, règles d'équité) ; recommandations SEO/GEO du CM2 et plateformes du CM3 identifiées.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : Extraction texte des PDF (`pdftotext`). Points retenus — **Brief** : 5 pages minimum (accueil, studio, jeu, devlogs ≥ 2 articles, contact/presse), publication au plus tard fin CM2/TD1, interdiction du black hat, du contenu partagé et des liens entre groupes, synthèse réflexive sans IA. **CM1** : positionnement « Pour [cible], [marque] est… contrairement à… », GEO = être cité par les IA (clarté, Q/R, autorité). **CM2** : 3 piliers (technique, on-page, off-page), E-E-A-T, GEO (Q/R, données vérifiables, langage naturel, Schema.org FAQ, auteur identifié), backlinks pertinents, architecture en silo (pas de liens entre silos sauf depuis l'accueil). **CM3** : choix des plateformes selon les personas (Discord, X, YouTube, Instagram pour un studio de jeux), codes propres à chaque réseau, calendrier éditorial.
- Prompts / outils IA utilisés : Prompt de mission initial (ci-dessus) ; lecture automatisée des PDF par l'agent.
- Décisions prises : HTML statique plutôt qu'Astro (validé par l'équipe) ; ville souterraine nommée « Sextia » (référence à Aquae Sextiae) ; héros nommé Sacha Morel ; jeu narratif sans combat ; mentions de lieux réels d'Aix pour les signaux locaux.
- Suite prévue : Relecture de l'univers inventé (noms, chronologie) par l'équipe.

### Tâche : Structure du dépôt et fondations SEO (sitemap, robots, README)
- Objectif : Mettre en place l'arborescence du site à URL propres et les fichiers techniques d'indexation.
- Critères de validation : URL en dossiers (`/studio/`, `/below-zero/`…), `sitemap.xml` valide avec `lastmod`, `robots.txt` pointant vers le sitemap, `README.md`, `.nojekyll`, `.gitignore` excluant les PDF de cours.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : 10 URL indexables dans `sitemap.xml` (avec images), `lastmod` 2026-11-17 ; `robots.txt` (tout autorisé sauf `/tools/`) ; flux RSS `devlogs/feed.xml` ; `site.webmanifest` ; `llms.txt` (résumé factuel du studio pour les moteurs génératifs) ; favicons SVG + PNG ; `.gitignore` (`.DS_Store`, `docs/*.pdf`, `__pycache__/`). XML du sitemap et du flux vérifié par parseur.
- Prompts / outils IA utilisés : Consigne à l'agent : « Créer la structure de base du dépôt + README + sitemap.xml + robots.txt » (prompt de mission, Phase 1).
- Décisions prises : URL descriptives en français ; ajout d'un `llms.txt` et d'un flux RSS pour accélérer la découverte ; générateur Python optionnel dans `tools/generateur/` pour éviter les incohérences entre pages.
- Suite prévue : Soumettre le sitemap dans Google Search Console dès la mise en ligne.

### Tâche : Site technique (HTML, CSS, JSON-LD, performance)
- Objectif : Produire un site statique accessible, rapide et richement balisé.
- Critères de validation : HTML valide W3C, JSON-LD valide, liens internes sans erreur, Lighthouse ≥ 95 dans les 4 catégories, contraste WCAG AA.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - HTML5 sémantique (`header`, `nav`, `main`, `article`, `footer`), `lang="fr"`, lien d'évitement, fil d'Ariane, un seul H1 par page, attributs `alt` sur toutes les images.
  - CSS unique (~5 Ko) intégré dans chaque page ; polices système ; aucune ressource bloquante ; JS limité à `assets/js/contact.js` (différé).
  - JSON-LD en `@graph` : `Organization`+`LocalBusiness` (Aix-en-Provence, 13100, Provence-Alpes-Côte d'Azur, FR, GPS 43.5297 / 5.4474), `WebSite`, `WebPage`/`AboutPage`/`ContactPage`/`CollectionPage`, `BreadcrumbList`, `VideoGame` (Below Zero), `Blog`, `BlogPosting` ×4, `FAQPage` (accueil et page du jeu).
  - Maillage en silo : accueil → silos studio / jeu / devlogs ; les devlogs se citent entre eux et renvoient à la page du jeu avec des ancres naturelles.
  - Validation W3C Nu : **0 erreur, 0 avertissement sur les 11 pages** (après correction d'un saut de niveau de titre sur `/devlogs/`).
  - Vérification automatique (`tools/generateur/check.py`) : tous les blocs JSON-LD sont du JSON valide, 0 lien interne cassé, aucun titre ni description dupliqué, aucun lien vers un autre groupe.
  - Lighthouse 12 (serveur local sans compression gzip, Chrome headless) :

| Page | Mode | Performance | Accessibilité | Bonnes pratiques | SEO |
|---|---|---|---|---|---|
| Accueil | mobile | 99 | 100 | 100 | 100 |
| Accueil | ordinateur | 100 | 100 | 100 | 100 |
| Devlog #2 (causalité) | mobile | 100 | 100 | 100 | 100 |
| Devlog #2 (causalité) | ordinateur | 100 | 100 | 100 | 100 |
| Below Zero | mobile | 100 | 100 | 100 | 100 |
| Below Zero | ordinateur | 100 | 100 | 100 | 100 |

  - Poids total : ~210 Ko (accueil), ~120 Ko (article sur mobile).
- Prompts / outils IA utilisés : Consigne à l'agent (Phase 2 du prompt de mission) : « Site statique propre (HTML5 sémantique), JSON-LD (Organization / LocalBusiness + VideoGame), maillage interne en silo, performance (objectif PageSpeed 100/100, images WebP, zéro JS bloquant), obfuscation des emails en JS ».
- Décisions prises : CSS intégré plutôt que fichier externe (premier audit à 98 sur mobile à cause du CSS bloquant) ; images en 480/960/1280 px ; e-mail masqué (`data-u` / `data-d`) reconstitué en JS avec repli texte lisible.
- Suite prévue : Refaire l'audit PageSpeed Insights sur l'URL en ligne (GitHub Pages compresse en gzip, ce qui devrait porter l'accueil mobile à 100) ; vérifier les données structurées avec l'outil « Test des résultats enrichis » de Google.

### Tâche : Génération des visuels
- Objectif : Produire l'identité visuelle et les illustrations du site dans la palette de marque.
- Critères de validation : Logo, hero, key art, 3 concept arts, image Open Graph 1200×630, une couverture par devlog ; WebP optimisés ; palette respectée.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : 10 images générées (1280×720, logo 1024×1024), converties en WebP (Pillow, qualité 68-76) en 480/960/1280 px. Image Open Graph (`flexarion-og-1200x630.jpg`) composée à partir du hero avec le texte « FLEXARION — Studio indépendant de jeux vidéo SF · Aix-en-Provence » (Pillow, police DejaVu Sans). Favicons PNG dérivés du logo ; `favicon.svg` redessiné à la main en vectoriel d'après le logo. Toutes les images sont signalées comme générées par IA (légendes + mentions légales).
- Prompts / outils IA utilisés : Outil de génération d'images de FlexaBot. Prompts exacts :
  1. **Logo** (1:1) — « Minimalist vector logo mark for an indie sci-fi video game studio called Flexarion: a geometric emblem made of two mirrored chevrons / arches, one on top pointing up and one reflected underneath pointing down, suggesting a city and its underground twin separated by a thin horizontal line, electric cyan #19B9D4 and glacier blue #B7DDE8 strokes on a solid deep navy-black #071421 background, flat design, centered, no text, clean sharp edges, suitable as a favicon »
  2. **Hero, deux villes** (16:9) — « Cinematic wide digital painting: cross-section view of the Provençal city of Aix-en-Provence at dusk on the surface, ochre facades, plane trees, a fountain and a cathedral bell tower, and directly beneath it, separated by a layer of rock, an identical mirrored underground twin city from the year 2306 glowing with electric cyan light, holographic signs, same streets and fountain but futuristic; mysterious atmosphere, color palette deep navy #071421, night blue #123A58, electric cyan #19B9D4, glacier blue #B7DDE8, no text, no logos »
  3. **Key art Below Zero** (16:9) — « Video game key art for a narrative sci-fi game: a young technician in a worn work jacket with a headlamp and a handheld scanner stands at the bottom of a long underground staircase, looking at a vast futuristic city that is an exact copy of a Provençal old town, glowing cyan windows, silhouettes of inhabitants on balconies watching him as if they know him, cold mist, mysterious and intriguing mood, deep navy and electric cyan palette with glacier blue highlights, painterly cinematic lighting, no text »
  4. **Capture causalité** (16:9) — « In-game screenshot style concept of a third-person narrative sci-fi game: split-screen composition, left half a sunny narrow Provençal street in 2156 with an old stone fountain covered in moss and a technician kneeling to repair a pipe, right half the exact same street in 2306 underground, the same fountain now made of glowing glass and cyan light, a visible thin luminous thread connecting the two fountains, minimal clean UI hint in a corner, deep navy and cyan palette, no readable text »
  5. **Concept art, place de Sextia** (16:9) — « Concept art of an underground futuristic plaza in the year 2306 beneath a southern French city: a huge circular cavern with a artificial sky made of glacier blue light panels, terraced buildings copying old Provençal architecture with ochre stone replaced by translucent materials, maglev trams, hanging gardens, small human figures for scale, eerie calm atmosphere, palette deep navy #071421, night blue #123A58, electric cyan #19B9D4, glacier blue #B7DDE8, painterly, no text »
  6. **Habitants de 2306** (16:9) — « Character design sheet style concept art: three inhabitants of an underground city from the year 2306, an elderly woman archivist with pale bioluminescent cyan tattoos, a calm teenage courier with a translucent visor, and a tall tram conductor in a long glacier-blue coat, all looking toward the viewer with a knowing familiar smile, soft studio lighting on a dark navy background, elegant sci-fi clothing inspired by Provençal fabrics reinterpreted futuristically, painterly, no text »
  7. **Couverture devlog #1** (16:9) — « Devlog cover illustration: an architect's drafting table seen from above with two overlapping translucent maps of the same old city, one hand-drawn in warm sepia ink labeled only by street shapes, the other a glowing cyan holographic blueprint, alignment rulers and a compass, dark navy desk, mood of a game studio designing two mirrored cities, no readable text »
  8. **Couverture devlog #2** (16:9) — « Devlog cover illustration about time causality puzzle design: a glowing cyan node graph floating in darkness, nodes shaped like small objects (a key, a seed, a broken lamp, a door) connected by luminous threads that branch from a present timeline at the top to a future timeline at the bottom, some threads bright, some fading, deep navy background, elegant minimal sci-fi style, no readable text »
  9. **Couverture devlog #3** (16:9) — « Devlog cover illustration about sound design for a sci-fi game: a sound designer's microphone and headphones placed in a dark underground stone tunnel, visible cyan sound waves propagating and echoing off curved walls, drops of water falling, distant glowing city lights at the end of the tunnel, deep navy and electric cyan palette, atmospheric, no readable text »
  10. **Couverture devlog #4** (16:9) — « Devlog cover illustration about character design: a character designer's sketchbook open on a dark desk, pencil sketches of futuristic faces evolving from rough lines on the left page to a finished painted portrait of a mysterious woman with subtle cyan bioluminescent markings on the right page, colored pencils, a tablet stylus, soft cyan desk lamp light, deep navy tones, no readable text »
- Décisions prises : Prompts rédigés en anglais (meilleure compréhension par le générateur) ; couleurs hexadécimales de la charte intégrées aux prompts ; « no text » systématique pour éviter les textes illisibles ; image OG composée localement plutôt que générée, pour garantir un texte net. Limites constatées : sur le logo, les « bâtiments » sont stylisés de façon un peu confuse à petite taille, d'où le favicon SVG simplifié ; la couverture du devlog #4 montre des croquis de visages plutôt « masques » que prévu.
- Suite prévue : Retouche des visuels par l'équipe (prévue dès le cadrage) ; éventuelle vectorisation propre du logo.

### Tâche : Rédaction des pages
- Objectif : Rédiger les pages accueil, studio, Below Zero, devlogs (index), contact/presse, mentions légales et 404 dans le ton de la marque.
- Critères de validation : Contenu minimum du brief couvert ; « Flexarion » présent naturellement dans le title, le H1 et le premier paragraphe sans bourrage ; mentions légales conformes (projet fictif, équipe inexistante, projet BUT, 4 étudiants, hébergeur, IA) ; FAQ factuelles pour le GEO.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : Accueil (positionnement, 3 piliers, encadré « Le studio en bref », 3 derniers devlogs, FAQ de 7 questions) ; Le studio (chronologie 2022-2026, 8 membres fictifs avec noms inventés : Inès Valcourt, Théo Marchetti, Samira Benali, Lucas Arnaud, Margaux Delorme, Yanis Okafor, Élise Fabre, Raphaël Costa ; section Aix-en-Provence) ; Below Zero (univers, fiche technique, 4 mécaniques, galerie, FAQ de 5 questions) ; Contact & presse (e-mail masqué et signalé comme fictif, boilerplate, fiche d'identité, visuels téléchargeables, charte) ; Mentions légales ; 404 dans le ton de l'univers. Chaque page signale la nature fictive du projet (pied de page).
- Prompts / outils IA utilisés : Consigne à l'agent : rédiger en français les pages du « Contenu minimum du site » en s'appuyant sur les brand guidelines, le positionnement et les personas du prompt de mission, ton « mystérieux, immersif et intrigant », appliquer les conseils GEO du CM2 (Q/R, faits vérifiables, langage naturel).
- Décisions prises : La FAQ répond honnêtement que Flexarion est fictif (transparence = critère « Trustworthiness » de l'E-E-A-T, et évite de tromper les moteurs génératifs) ; aucune adresse postale inventée (seulement ville / code postal) ; date de sortie du jeu non annoncée pour ne pas inventer de faits trop précis.
- Suite prévue : Relecture humaine complète par l'équipe pour personnaliser la voix de marque ; ajout des liens `sameAs` des réseaux sociaux une fois les comptes créés.

### Tâche : Rédaction des devlogs
- Objectif : Publier 4 articles de devlog originaux de plus de 800 mots, reliés entre eux et à la page du jeu.
- Critères de validation : ≥ 800 mots par article ; un auteur fictif identifié par article ; sommaire, Hn structurés ; liens internes à ancres naturelles ; balisage `BlogPosting`.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : 
  - Devlog #1 « Concevoir deux villes jumelles, Aix 2156 et Sextia 2306 » (Margaux Delorme, artiste 3D) — ~1 290 mots.
  - Devlog #2 « Le présent modifie le futur, nos énigmes de causalité » (Lucas Arnaud, game designer) — ~1 090 mots.
  - Devlog #3 « Écouter sous la ville, le sound design de Sextia » (Élise Fabre, sound designer) — ~1 060 mots.
  - Devlog #4 « Ils vous connaissent déjà, dessiner les habitants de 2306 » (Yanis Okafor, character designer) — ~1 060 mots.
  - Chaque article : couverture LCP, sommaire ancré, 1 visuel intégré, 3 à 4 liens contextuels vers les autres devlogs et la page Below Zero, encadré « projet fictif / rédigé avec assistance IA ».
- Prompts / outils IA utilisés : Consigne à l'agent : « blog de devlogs, 4 articles de 800+ mots, sujets riches et variés : conception des deux villes 2156/2306, mécaniques d'énigmes de causalité temporelle, sound design de la ville souterraine, character design des habitants du futur » ; ton de marque et personas du prompt de mission.
- Décisions prises : Un métier = un article (montre l'expertise de chaque rôle, critère E-E-A-T) ; mention des erreurs et corrections dans chaque devlog pour un ton « vécu » ; dates de publication réelles (17/11/2026) plutôt qu'antidatées.
- Suite prévue : Relecture et enrichissement par l'équipe (anecdotes personnelles) ; échelonner les prochains devlogs (TD2, TD3) pour montrer un site vivant.

### Tâche : Corrections suite à la revue V1
- Objectif : Appliquer l'intégralité du compte rendu de la première version du site rédigé par l'équipe (forme, code source, données structurées, SEO).
- Critères de validation : Chaque point de la revue traité ; HTML et CSS valides ; JSON-LD valide et sans `LocalBusiness` ; aucun lien interne cassé ; mentions légales non indexées ; Lighthouse ≥ 98 sur mobile et ordinateur ; captures d'écran vérifiées.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - **Commun** : bouton « retour en haut » (`.to-top`), visible seulement après 300 px de défilement, défilement doux en CSS (`scroll-behavior: smooth`), désactivé si `prefers-reduced-motion: reduce`, libellé accessible « Retour en haut de la page ».
  - **E-mail** : `flexarion.officiel@gmail.com`, toujours masqué (attributs `data-u` / `data-d` reconstitués en JS, repli « [arobase] / [point] ») ; l'adresse a aussi été retirée du JSON-LD pour qu'elle n'apparaisse jamais en clair dans le HTML (`contactPoint` pointe désormais vers la page contact).
  - **CSS** : une seule feuille globale `assets/css/style.css` (lisible, commentée, ~11 Ko non minifiée) liée par `<link rel="stylesheet">` sur toutes les pages ; plus aucun `<style>` ni attribut `style` (contrôle automatique ajouté dans `check.py`).
  - **JS** : `assets/js/contact.js` remplacé par un script unique `assets/js/main.js` (`defer`) : burger, retour en haut, e-mail.
  - **Indentation** : nouveau module `tools/generateur/fmt.py` qui indente tout le HTML produit (2 espaces, imbrication respectée, JSON-LD indenté à 2 espaces) ; CSS et JS réécrits avec une indentation homogène.
  - **Réseaux sociaux** : GitHub, itch.io, X et Instagram dans le pied de page de chaque page et dans une section « Suivre le studio sur les réseaux » de la page contact (`rel="me noopener"`, nouvel onglet) ; les URL sont dans `sameAs` de l'Organization et dans `llms.txt`.
  - **En-tête** : menu burger sur mobile (< 48 rem) : bouton `aria-expanded` / `aria-controls="menu-principal"`, libellé « Ouvrir / Fermer le menu », fermeture avec Échap. Sans JS, les liens restent accessibles dans le pied de page.
  - **Pied de page** : texte centré, logo Flexarion ajouté, lien « En savoir plus » supprimé, liens externes « Organisation GitHub Flexarion » et « IUT d'Aix-Marseille (amU) » ajoutés, mention courte du projet fictif conservée, lien vers les mentions légales conservé, tailles et retours à la ligne adaptés au mobile (marge basse pour ne pas être masqué par le bouton « retour en haut »).
  - **Accueil** : hero compact, texte posé sur l'image avec un dégradé sombre (contraste conservé) ; H1, introduction et boutons visibles sans défiler sur ordinateur (1366×768) et sur mobile (390×844). Recadrage spécifique au mobile (`<picture>`, 540×608, 53 Ko) pour garder un LCP rapide.
  - **Studio** : mention « Flexarion est un studio fictif… » supprimée du corps de page.
  - **Below Zero** : nouvelle section `#origine-sextia` « D'où vient le nom « Sextia » ? », placée juste après l'univers (là où le nom apparaît pour la première fois) : fondation d'Aquae Sextiae en 122 av. J.-C. par le consul Caius Sextius Calvinus, victoire sur les Salyens (oppidum d'Entremont), étymologie « les eaux de Sextius » → « Aix », sources thermales et thermes Sextius. Chaque mention de « Sextia » dans le texte de la page (hors section et titres) renvoie vers cette ancre ; les textes alternatifs des images ne peuvent pas contenir de lien.
  - **Contact & presse** : suppression de « Cette adresse fait partie de la fiction… », de « (fictif) » pour le responsable communication et de la section charte graphique.
  - **Mentions légales** : `noindex, follow`, retirées du `sitemap.xml` (9 URL) et de `llms.txt` ; toujours liées dans le pied de page ; avertissement complet et 4 étudiants conservés. Phrase sur l'e-mail mise à jour (adresse gérée par les étudiants).
  - **Données structurées** : `LocalBusiness`, adresse, coordonnées GPS et `numberOfEmployees` supprimés ; `Organization` simple avec `alternateName` [« Flexarion Studio », « Studio Flexarion »], `logo` (ImageObject, `icon-512.png` en URL absolue), `foundingDate` 2022, `sameAs` (5 réseaux), description sans le mot « fictif ». `WebSite`, `VideoGame`, `Blog` et `BlogPosting` référencent toujours `#organization`. Balises meta `geo.*` / `ICBM` supprimées pour rester cohérent.
  - **Mot « fictif »** : retiré des titres, meta descriptions, JSON-LD, FAQ (question « Flexarion est-il un vrai studio ? » supprimée), encadré « en bref », page studio, encadrés des devlogs et `llms.txt` ; conservé uniquement dans le pied de page et les mentions légales.
  - **Fraîcheur** : `lastmod` et `dateModified` passés au 2026-11-18 ; mention visible « Mis à jour le 18 novembre 2026 » sur chaque devlog ; `lastBuildDate` du flux RSS mis à jour.
  - **Validation** : validateur Nu (vnu.jar, version locale, le service en ligne du W3C renvoyant une erreur 429 / défi Cloudflare) : **11 pages, 0 erreur, 0 avertissement** ; CSS valide ; `check.py` : JSON-LD valide, 0 lien interne cassé, aucun CSS en ligne, aucune adresse e-mail en clair, aucun « fictif » dans title / description / JSON-LD, mentions légales absentes du sitemap et de `llms.txt`.
  - **Lighthouse 12** (serveur local sans gzip) :

| Page | Mode | Performance | Accessibilité | Bonnes pratiques | SEO |
|---|---|---|---|---|---|
| Accueil | mobile | 99-100 (selon les passages) | 100 | 100 | 100 |
| Accueil | ordinateur | 100 | 100 | 100 | 100 |
| Below Zero | mobile | 100 | 100 | 100 | 100 |
| Below Zero | ordinateur | 100 | 100 | 100 | 100 |
| Devlog #2 | mobile | 100 | 100 | 100 | 100 |
| Devlog #2 | ordinateur | 100 | 100 | 100 | 100 |

- Prompts / outils IA utilisés : Compte rendu de la V1 rédigé par l'équipe, transmis tel quel à l'agent (« Appréciation sur la forme » : commun, header, footer, pages accueil / studio / Below Zero / contact / mentions légales, code source ; « Appréciation globale » : place de la mention « fictif », suppression du LocalBusiness, alternateName et logo, fraîcheur ; « Informations additionnelles » : URL des réseaux). Outils : FlexaBot (modification du générateur Python, du CSS et du JS), vnu.jar, Lighthouse, Chrome headless / Puppeteer pour les captures.
- Décisions prises :
  - CSS externe malgré le léger coût « ressource bloquante » signalé par Lighthouse, conformément à la demande ; compensé par un recadrage mobile plus léger de l'image du hero (le score mobile de l'accueil revient à 99-100).
  - CSS non minifié pour rester lisible (gain possible de ~3 Ko seulement).
  - Burger sans script en ligne : le menu mobile dépend du script différé, et les liens restent disponibles dans le pied de page si JS est désactivé.
  - Suppression des balises `geo.*` en plus du `LocalBusiness`, pour ne déclarer aucune localisation physique dans les métadonnées ; Aix-en-Provence reste présent dans le texte visible.
  - Adresse e-mail retirée du JSON-LD pour respecter l'obfuscation.
  - Mention « fictif » retirée de `llms.txt` (fichier lu par les moteurs génératifs), par cohérence avec la consigne de la garder uniquement dans le pied de page et les mentions légales.
- Suite prévue : Après déploiement, refaire PageSpeed Insights sur l'URL publique, vérifier les données structurées avec le test des résultats enrichis de Google, soumettre à nouveau le sitemap dans Search Console et demander l'indexation des pages modifiées ; supprimer `assets/js/contact.js` du dépôt (`git rm`, avec accord).

### Tâche : Profil itch.io du studio
- Objectif : Fournir une présentation HTML du studio prête à coller dans le profil itch.io (`flexarionofficiel.itch.io`), limitée à 5 000 caractères.
- Critères de validation : ≤ 5 000 caractères ; balises acceptées par itch.io ; mot-clé « Flexarion » et ancrage Aix-en-Provence présents ; liens vers le site officiel et ses pages clés ; ton mystérieux de la marque.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : Fichier HTML d'environ 3 300 caractères (titre, accroche, présentation du studio et de Below Zero, citation, liens vers l'accueil, Below Zero, les devlogs et le contact). L'équipe a ensuite demandé une version enrichie de styles. Le texte est collé manuellement par l'équipe dans itch.io (l'agent n'a pas accès au compte).
- Prompts / outils IA utilisés : « Est-ce que tu peux me faire un html pour le profil itch io ? Sachant que c'est max 5000 caractères, optimise bien. » puis « Est-ce que ce serait possible d'y ajouter des styles ».
- Décisions prises : Liens absolus vers le site (backlink White Hat depuis une plateforme pertinente pour un studio de jeu) ; pas de bourrage de mots-clés.
- Suite prévue : Créer la page du jeu Below Zero sur itch.io avec un lien vers `/below-zero/`.

### Tâche : README de l'organisation GitHub
- Objectif : Rédiger le README de présentation de l'organisation GitHub `flexarion-officiel` (affiché sur la page de l'organisation).
- Critères de validation : Markdown compatible GitHub ; image de marque, présentation du studio et de Below Zero, liens vers le site ; aucun lien vers un autre groupe.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : Fichier `profile/README.md` (≈ 3 300 caractères) : bannière Open Graph liée au site, slogan, liens Site officiel / Below Zero / Devlogs / Presse, accroche, présentation. Il doit être placé dans un dépôt public `flexarion-officiel/.github` ; ce dépôt est hors du périmètre autorisé de l'agent, sa création est donc laissée à l'équipe (ou à un accord explicite).
- Prompts / outils IA utilisés : « Est-ce que pour l'organisation github https://github.com/flexarion-officiel tu peux faire un README ? »
- Décisions prises : Contenu cohérent avec le site (mêmes faits, même ton) pour renforcer l'entité « Flexarion » ; liens absolus vers le site.
- Suite prévue : Création du dépôt `.github` par l'équipe ; renseigner le champ *Website* de l'organisation.

### Tâche : Corrections suite à la revue V1.1 (version 1.2 du site)
- Objectif : Appliquer le compte rendu de la v1.1.0 rédigé par l'équipe (réseaux, icônes, pied de page, pages studio / Below Zero / contact / devlogs, README).
- Critères de validation : Plus aucune référence au réseau supprimé dans le site, la doc et les profils ; icônes issues d'une source libre et conformes aux chartes ; chaque point de la revue traité ; `check.py` sans erreur ; HTML valide ; Lighthouse ≥ 98 ; captures d'écran vérifiées.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - **Réseau professionnel retiré** : le compte ayant été suspendu, toutes ses références sont supprimées (pied de page, page contact, `sameAs` du JSON-LD, `llms.txt`, README, `docs/PHASE4-NETLINKING.md`, ce rapport). Réseaux conservés : GitHub, itch.io, X, Instagram.
  - **Icônes des réseaux** : SVG officiels de [Simple Icons](https://simpleicons.org) v16 (licence CC0 1.0, domaine public), rangés dans le nouveau dossier `assets/icons/` (`github.svg`, `itchio.svg`, `x.svg`, `instagram.svg` + `LISEZMOI.md` de provenance). Tracés non modifiés, proportions conservées, version monochrome blanche, autorisée par les chartes des quatre marques. Icônes décoratives (`alt=""`, `aria-hidden`) et nom accessible porté par le lien (`aria-label`). Crédit et rappel des marques ajoutés dans les mentions légales (section « Crédits des icônes »).
  - **Pied de page** : liens Le studio / Below Zero / Devlogs retirés, lien « Accueil » placé en premier (Accueil · Contact & presse · Mentions légales) ; logo remplacé par `/icon-512.png` (72 × 72, `srcset` 192/512 pour ne charger que la taille utile, `loading="lazy"`) ; « Créateur de Below Zero » retiré ; liens « Organisation GitHub Flexarion » et « IUT d'Aix-Marseille » retirés ; mention « Visuels générés par IA » retirée du pied de page (conservée dans les mentions légales, section « Usage de l'intelligence artificielle », complétée avec les aperçus de jeu et les avatars) ; réseaux sous forme d'icônes rondes.
  - **Le studio** : cartes de l'équipe plus vivantes : 8 avatars illustrés (style cartoon, même fond bleu nuit #123A58 / #071421 et même liseré cyan pour tous), médaillon cerclé de cyan, rôle en pastille, léger soulèvement au survol (désactivé si `prefers-reduced-motion`). WebP 160 et 320 px (2 à 9 Ko), `width`/`height`, `loading="lazy"`, textes alternatifs descriptifs. Mention « avatars générés par IA » sous la grille.
  - **Below Zero** : seule l'image principale est remplacée par un aperçu de jeu (vue à la troisième personne de Sacha sur la grande place de Sextia, fontaine thermale, habitants aux marques cyan, interface holographique discrète, sans combat). WebP 480 / 960 / 1280 + recadrage mobile 540 × 608 via `<picture>`, `fetchpriority="high"` (image LCP). L'image est ajoutée en tête du tableau `image` du `VideoGame` et au kit presse. L'image Open Graph de la page reste le key art (visuel partagé avec la page studio).
  - **Contact & presse** : réseaux en liste verticale (ordinateur et mobile), chaque ligne = logo • pseudo (`flexarion-officiel`, `flexarionofficiel`, `@flexarion_off`, `@flexarion.off`) ; nom accessible « Réseau : pseudo ».
  - **Devlogs** : liste triée du plus récent au plus ancien (index, accueil, flux RSS, `llms.txt`, `blogPost`). Les 4 articles ayant été publiés le même jour, l'heure de publication (17/11/2026, de 9 h à 12 h) les départage dans `datePublished`, `article:published_time` et `pubDate`, sans antidater. Sur chaque article, boutons « Devlog précédent » (`rel="prev"`, article plus ancien, absent sur le n°1) et « Devlog suivant » (`rel="next"`, article plus récent, absent sur le n°4), regroupés dans un `<nav aria-label="Navigation entre les devlogs">`.
  - **README** : encadré « Projet fictif » supprimé (les créateurs réels restent cités), sections « Modifier le site » et « Règles du concours respectées » supprimées, choix techniques et arborescence mis à jour (icônes, avatars, navigation des devlogs).
  - **Fraîcheur** : `lastmod` 2026-11-18 dans le sitemap, `dateModified` 2026-11-18.
  - **Validation** : `check.py` : 11 pages, 0 erreur (JSON-LD valide, 0 lien interne cassé, aucun CSS en ligne, aucune adresse e-mail en clair) ; html-validate : 0 erreur hors règle SRI (non pertinente pour des fichiers servis par le même domaine) ; recherche automatique : 0 occurrence du réseau supprimé dans le dépôt et les profils.
  - **Lighthouse 12** (serveur local sans gzip) :

| Page | Mode | Performance | Accessibilité | Bonnes pratiques | SEO |
|---|---|---|---|---|---|
| Accueil | mobile | 100 | 100 | 100 | 100 |
| Le studio | mobile | 100 | 100 | 100 | 100 |
| Le studio | ordinateur | 100 | 100 | 100 | 100 |
| Below Zero | mobile | 100 | 100 | 100 | 100 |
| Below Zero | ordinateur | 100 | 100 | 100 | 100 |
| Contact | mobile | 100 | 100 | 100 | 100 |
| Devlog #3 | mobile | 100 | 100 | 100 | 100 |

- Prompts / outils IA utilisés : Compte rendu de la v1.1.0 rédigé par l'équipe, transmis tel quel à l'agent, et réponses de cadrage (mention IA conservée dans les mentions légales ; seule l'image principale de Below Zero remplacée ; pseudo après le séparateur ; avatars sur le même fond). Génération d'images (FlexaBot) : un premier avatar décrit précisément (« avatar cartoon stylisé, buste, fond uni bleu #123A58 dans un carré #071421, liseré cyan #19B9D4 », puis le profil du membre), réutilisé comme image de référence pour les 7 autres afin de garder le même style ; aperçu de jeu : « capture d'un jeu d'aventure narratif de SF, caméra à la troisième personne, jeune technicien à la lampe frontale dans une ville souterraine de 2306 sous Aix-en-Provence, fontaine thermale, interface holographique cyan discrète, aucune arme ni combat, palette de la charte ». Outils non IA : Simple Icons (npm / jsDelivr), Pillow (conversion WebP), html-validate, Lighthouse, Puppeteer.
- Décisions prises :
  - Simple Icons plutôt que des logos copiés sur chaque site : licence CC0 explicite, tracés identiques aux logos officiels, un seul format SVG léger.
  - Icônes en blanc monochrome (couleur autorisée par toutes les chartes) plutôt que les couleurs de marque, pour l'harmonie avec la palette sombre du site.
  - Pastille du rôle sur fond #071421 : le cyan sur fond translucide n'atteignait que 3,9:1 de contraste (Lighthouse) ; corrigé à plus de 7:1.
  - Dates des devlogs non antidatées (cohérent avec la décision prise lors de la rédaction) : départage par l'heure de publication.
  - Sans JavaScript, la navigation reste possible via le fil d'Ariane et les liens du contenu (le pied de page ne contient plus les pages principales, à la demande de l'équipe).
- Suite prévue : Déployer, vérifier en ligne (PageSpeed Insights, test des résultats enrichis), soumettre de nouveau le sitemap ; mettre à jour les profils externes si un lien vers le réseau supprimé y figurait ; retravail éventuel des avatars et de l'aperçu de jeu par l'équipe.

### Tâche : Corrections suite à la revue V1.2 (version 1.3 du site)
- Objectif : Appliquer le compte rendu de la v1.2.0 rédigé par l'équipe (ASCII art, message console, police personnalisée sans perte de performance, mentions légales, méta descriptions, visuels moins plats, CSS d'impression, CSS/JS minifiés), plus la correction du favicon pour Google.
- Critères de validation : Chaque point traité ; titres ≤ 60 caractères et descriptions ≤ 155 caractères (≈ 920 px) commençant près du mot-clé « Flexarion » ; aucun décalage de mise en page (CLS = 0) ; Lighthouse ≥ 98 ; contraste AA conservé ; `check.py` sans erreur ; HTML valide.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - **ASCII art** : logo losange + « FLEXARION » en commentaire HTML juste après le `<!doctype html>` de chaque page (≈ 700 octets), avec un indice renvoyant vers la console. Le module `fmt.py` conserve désormais les commentaires.
  - **Message console** : `console.log` stylé (cyan sur fond nuit) dans `main.js` : réplique d'un habitant de Sextia (« Te revoilà, Sacha… »), un indice sur le lien 2156 / 2306 et un lien vers la page Below Zero. Aucun suivi, aucune donnée collectée.
  - **Police** : Exo 2 (SIL Open Font License 1.1, fichier `assets/fonts/OFL.txt`), police variable limitée aux graisses 400 à 800, auto-hébergée en deux sous-ensembles WOFF2 : latin (26,7 Ko, préchargé) et latin étendu (20,4 Ko, téléchargé seulement si un de ses caractères apparaît ; plages Unicode sans chevauchement pour ne jamais charger les deux sur une page française). `font-display: swap` et police de secours « Exo 2 Fallback » (Arial / Helvetica / Liberation Sans) avec `size-adjust: 101.22%`, `ascent-override: 98.69%`, `descent-override: 19.86%`, calculés depuis les métriques réelles des deux polices : CLS = 0. Pile de secours : `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`. Crédit ajouté dans les mentions légales (section « Typographie »).
  - **Mentions légales** : « Dernière mise à jour : 19 novembre 2026 » sous le titre ; nouvelle section finale « Droit applicable » (droit français, tribunaux français compétents) ; lien « Retour à l'accueil » placé juste avant.
  - **Titres et méta descriptions** : mesure de chaque page en caractères et en pixels (Arial 20 px pour les titres, 14 px pour les descriptions). 6 descriptions et 6 titres raccourcis ; le mot « Flexarion » est placé en tête des descriptions modifiées. Contrôle automatique ajouté dans `check.py` (titre > 60 ou description > 155 caractères = erreur).

| Page | Champ | Avant | Après |
|---|---|---|---|
| Accueil | title | Flexarion \| Studio de jeux vidéo SF indépendant à Aix-en-Provence (65 car.) | Flexarion \| Studio de jeux vidéo SF à Aix-en-Provence (53) |
| Below Zero | description | Below Zero, jeu vidéo de Flexarion : … mécaniques de causalité et visuels. (145 car., 910 px) | Flexarion présente Below Zero : en 2156, une ville de 2306 est découverte sous Aix-en-Provence. Univers, énigmes et visuels du jeu. (131, 826 px) |
| Devlogs | title | Devlogs Flexarion : le journal de développement de Below Zero (61) | Devlogs Flexarion : journal de développement de Below Zero (58) |
| Devlog #1 | title | Devlog #1 : concevoir deux villes jumelles (2156 / 2306) \| Flexarion (68) | Devlog #1 : concevoir deux villes jumelles \| Flexarion (54) |
| Devlog #1 | description | Comment l'équipe Flexarion construit … règles de symétrie et lisibilité. (155, 957 px) | Flexarion dévoile comment son équipe bâtit l'Aix de 2156 et sa jumelle souterraine Sextia en 2306 : plans superposés et règles de symétrie. (139, 866 px) |
| Devlog #2 | title | Devlog #2 : les énigmes de causalité de Below Zero \| Flexarion (62) | Devlog #2 : énigmes de causalité de Below Zero \| Flexarion (58) |
| Devlog #2 | description | Le game designer de Flexarion explique … et comment on évite le chaos. (151, 967 px) | Chez Flexarion, le game designer explique comment une action dans l'Aix de 2156 transforme la ville de 2306 de Below Zero, sans chaos. (134, 858 px) |
| Devlog #3 | title | Devlog #3 : le sound design de la ville souterraine \| Flexarion (63) | Devlog #3 : le sound design de Sextia \| Flexarion (49) |
| Devlog #3 | description | Réverbérations, eau thermale et cigales mutées : la sound designer de Flexarion … (148, 922 px) | Chez Flexarion, la sound designer raconte comment l'eau thermale, l'écho et des cigales mutées font sonner la ville souterraine de Below Zero. (142, 887 px) |
| Devlog #4 | title | Devlog #4 : le character design des habitants de 2306 \| Flexarion (65) | Devlog #4 : dessiner les habitants de 2306 \| Flexarion (54) |
| Devlog #4 | description | Du croquis au personnage final : le character designer de Flexarion … (146, 902 px) | Chez Flexarion, le character designer dévoile comment il dessine, du croquis au modèle 3D, des habitants du futur qui reconnaissent le joueur. (142, 884 px) |
| Mentions légales | description | Mentions légales du site Flexarion : … hébergement et usage de l'IA. (148, 918 px) | Mentions légales de Flexarion : projet pédagogique de l'IUT d'Aix-Marseille, étudiants éditeurs, hébergement, usage de l'IA et droit applicable. (144, 877 px) |

  - **Relief des visuels** : variables `--carte` (dégradé bleu nuit en diagonale) et `--ombre` / `--ombre-haute` (ombres superposées + fin reflet intérieur) appliquées aux cartes, encadrés « en bref », FAQ, sommaires, section Sextia et boutons de navigation des devlogs ; lueur cyan très légère en haut de page et en bas à gauche du hero ; ombre douce sous les images et l'en-tête ; halo discret sur le H1. Pas d'animation ajoutée ; contraste du texte inchangé (≥ AA, vérifié par Lighthouse).
  - **Impression** : `@media print` : fond blanc, texte noir, menu, burger, bouton retour en haut, fil d'Ariane, boutons, réseaux et navigation des devlogs masqués ; URL affichée après les liens externes ; pas de coupure dans les cartes, encadrés, figures et titres ; images limitées à la largeur de la page ; réponses des FAQ dépliées (navigateurs compatibles).
  - **Minification** : nouveau module `tools/generateur/minify.py` (Python pur, sans dépendance) appelé à la fin de `build.py` : `style.css` 18,0 Ko → `style.min.css` 13,2 Ko (la v1.2 servait 13,5 Ko non minifiés, alors que la feuille gagne la police, le relief et l'impression), `main.js` 2,4 Ko → `main.min.js` 1,6 Ko. Toutes les pages pointent vers les fichiers minifiés (contrôle ajouté dans `check.py`). Sources lisibles conservées en local et ajoutées au `.gitignore`.
  - **Favicon** : `favicon.ico` multi-tailles (16, 32, 48, 96 px) et `favicon-48.png` générés depuis `icon-512.png` ; `<link rel="icon" href="/favicon.ico" sizes="48x48">` et `favicon-48.png` ajoutés sur toutes les pages (Google demande un favicon d'au moins 48 px, multiple de 48) ; SVG et PNG 32 conservés ; manifeste vérifié (192, 512, SVG).
  - **Fraîcheur** : `lastmod` 2026-11-19 dans le sitemap, `dateModified` et mention « Mis à jour le 19 novembre 2026 » des devlogs.
  - **Validation** : `check.py` : 11 pages, 0 erreur ; html-validate : 0 erreur hors règle SRI (non pertinente pour des fichiers du même domaine) ; JSON-LD valide.
  - **Lighthouse 12** (serveur local sans gzip) :

| Page | Mode | Performance | Accessibilité | Bonnes pratiques | SEO |
|---|---|---|---|---|---|
| Accueil | mobile | 99 | 100 | 100 | 100 |
| Accueil | ordinateur | 100 | 100 | 100 | 100 |
| Le studio | mobile | 99 | 100 | 100 | 100 |
| Le studio | ordinateur | 100 | 100 | 100 | 100 |
| Below Zero | mobile | 100 | 100 | 100 | 100 |
| Below Zero | ordinateur | 100 | 100 | 100 | 100 |
| Devlog #2 | mobile | 100 | 100 | 100 | 100 |
| Devlog #2 | ordinateur | 100 | 100 | 100 | 100 |
| Mentions légales | mobile / ordinateur | 100 | 100 | 100 | 69 (attendu : page volontairement en `noindex`) |

- Prompts / outils IA utilisés : Compte rendu de la v1.2.0 rédigé par l'équipe, transmis tel quel à l'agent (« Commun à toutes les pages » : ASCII art, message secret dans la console, police personnalisée sans baisse de performance avec polices de secours et génériques ; « Mentions légales » : date de mise à jour et section « Droit applicable » ; « Appréciation globale » : méta descriptions trop longues, visuels trop plats, CSS d'impression, CSS/JS minifiés avec sources non minifiées dans le `.gitignore`). Outils non IA : fontTools / pyftsubset (sous-ensembles et instance variable), Pillow (favicons), pyfiglet (lettrage du commentaire ASCII), html-validate, Lighthouse, Puppeteer (captures et PDF d'impression).
- Décisions prises :
  - Une seule famille (Exo 2, variable) pour les titres et le texte : style SF lisible, un seul fichier préchargé ; sans préchargement, le score mobile restait identique (99) : le préchargement est conservé pour afficher la bonne police plus tôt.
  - Sources CSS/JS laissées à leur place (`assets/css/style.css`, `assets/js/main.js`) mais ignorées par Git : édition inchangée, fichiers servis = versions `.min`. Conséquence : ces deux fichiers doivent être retirés de l'index Git (`git rm --cached`, avec accord) ; un clone neuf du dépôt ne contient plus les sources lisibles.
  - Le score Performance mobile de l'accueil et du studio passe de 100 à 99 (LCP 1,9 s → 2,0 s en simulation) : écart de mesure jugé acceptable au regard du gain visuel ; CLS reste à 0.
- Suite prévue : Après déploiement, vérifier le favicon dans les résultats Google (délai de plusieurs jours), PageSpeed Insights sur l'URL publique, et redemander l'indexation des pages dont le titre ou la description a changé.

### Tâche : Flèche du bouton « retour en haut » (version 1.3.1)
- Objectif : Rendre au bouton « retour en haut » une flèche aux bords arrondis : depuis le passage à la police Exo 2 (v1.3.0), le caractère « ↑ » s'affichait avec un dessin jugé étrange par l'équipe.
- Critères de validation : Flèche nette et arrondie, identique sur tous les navigateurs et indépendante de la police ; bouton toujours accessible (nom accessible, focus visible) ; aucun impact sur la performance.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - Premier essai en forçant une police système pour le seul caractère « ↑ » ; deux variantes proposées en captures. L'équipe a préféré la seconde, tout en trouvant la flèche d'avant le changement de police plus réussie (« elle avait des bords arrondis »).
  - Version retenue : caractère remplacé par une petite icône SVG en ligne (tracé de 24 × 24, trait de 2,3 px, extrémités et angles arrondis, couleur `currentColor`), déclarée `aria-hidden="true"` et `focusable="false"` ; le nom accessible du bouton est inchangé. Rendu identique quelle que soit la police chargée, aucune requête supplémentaire.
- Prompts / outils IA utilisés : Demandes de l'équipe transmises à l'agent (« remettre la flèche de retour en haut de page comme elle était avant » ; « la flèche avant le changement de police était bien mieux, elle avait des bords arrondis »). Outils non IA : Puppeteer (captures comparatives).
- Décisions prises : Une icône SVG plutôt qu'un caractère : le dessin ne dépend plus de la police ni du système d'exploitation.
- Suite prévue : Aucune.

### Tâche : Effet de survol des cartes (version 1.3.2 du site)
- Objectif : Étendre à toutes les cartes du site le léger effet de survol déjà présent sur les cartes de l'équipe (page studio), à la demande de l'équipe : FAQ, derniers devlogs de l'accueil, etc.
- Critères de validation : Effet discret et homogène ; uniquement sur les appareils à souris (pas d'effet « collant » au toucher) ; équivalent au clavier ; respect de `prefers-reduced-motion` ; propriétés peu coûteuses (pas de recalcul de mise en page) ; Lighthouse et CLS inchangés.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - Cartes (`.card`), encadrés « en bref » (`.facts`), questions des FAQ et boutons « précédent / suivant » des devlogs : transition de 0,25 s sur `transform`, `border-color` et `box-shadow` ; au survol, élévation de 4 px, liseré cyan et ombre plus profonde.
  - Effet limité à `@media (hover: hover) and (pointer: fine)` ; même rendu au focus clavier (`:focus-within` sur les cartes et les FAQ, `:focus-visible` sur les boutons des devlogs) ; sans déplacement si l'utilisateur demande moins d'animations.
  - Contrôle par captures avec un vrai pointeur (Chrome sous Xvfb, car Chrome sans interface ne déclare pas de souris).
- Prompts / outils IA utilisés : Demande de l'équipe transmise à l'agent (« lorsqu'on passe la souris sur les cartes de l'équipe […] il y a un léger effet. J'aimerais bien que les autres cartes des autres pages […] aient une petite animation hover »). Outils non IA : Puppeteer, Xvfb.
- Décisions prises : Seuls `transform` et `box-shadow` sont animés (pas de changement de taille ni de marge) : aucun décalage de mise en page.
- Suite prévue : Ajustements éventuels après revue (faits en v1.4.0 pour les encadrés « en bref »).

### Tâche : Animations d'interface suite à la revue V1.3 (version 1.4.0 du site)
- Objectif : Appliquer la partie « Animations » du compte rendu de la v1.3.0 : survol des liens du menu (ordinateur), ouverture / fermeture du menu burger (mobile), dépliage / repliage des FAQ, suppression du mouvement des encadrés « facts », changement de couleur animé des boutons. Consigne : animations courtes et sobres, sans perte de fluidité.
- Critères de validation : Durées entre 0,2 et 0,25 s ; propriétés peu coûteuses ; `prefers-reduced-motion` respecté ; menu mobile toujours accessible (`aria-expanded` correct, liens non atteignables au clavier menu fermé) ; FAQ utilisables sans JavaScript et au clavier ; `check.py` sans erreur ; HTML valide ; Lighthouse inchangé ; CLS = 0.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - **Menu (ordinateur)** : soulignement cyan dessiné par un pseudo-élément qui se déploie depuis le centre (`transform: scaleX`, 0,2 s) et couleur du lien en transition (0,2 s) ; même trait que l'indicateur de page courante, qui reste affiché. Survol réservé aux appareils à souris ; même rendu au focus clavier (`:focus-visible`). Hauteur de l'en-tête inchangée.
  - **Menu burger (mobile)** : ouverture et fermeture en `ease-in-out` sur 0,25 s (rangée de grille `0fr` → `1fr` et fondu du contenu). Menu fermé : `visibility: hidden` appliquée à la fin de la transition, donc liens ni visibles ni focalisables. Le script existant est inchangé (`aria-expanded`, libellé du bouton, touche Échap). Bordure du bouton cyan quand le menu est ouvert ; icône « trois barres » → croix en 0,25 s.
  - **FAQ (accueil et Below Zero)** : dépliage et repliage animés de la hauteur en `ease-in-out` sur 0,25 s (Web Animations API, quelques lignes dans `main.js`). Amélioration progressive : sans JavaScript ou avec « réduire les animations », les `<details>` natifs fonctionnent comme avant. Clavier (Entrée, Espace) et clics répétés pendant l'animation gérés ; effet de survol v1.3.2 conservé.
  - **Encadrés « facts »** : élévation de 4 px supprimée ; seul un léger halo (ombre) apparaît au survol, sans mouvement.
  - **Boutons** : transition de 0,2 s (`ease`) sur le fond, la bordure et la couleur du texte pour les boutons d'appel à l'action, le bouton « retour en haut », les boutons « précédent / suivant » des devlogs, les liens vers les réseaux et le bouton burger.
  - **Mouvement réduit** : toutes les transitions et animations deviennent quasi instantanées et le script des FAQ ne s'active pas.
  - **Mesures** (Chrome, captures `v15-*`) : soulignement à 70 % de sa largeur après 80 ms puis complet ; fond du bouton intermédiaire après 90 ms ; FAQ 56 → 90 → 159 px à l'ouverture, 159 → 125 → 56 px à la fermeture ; menu mobile 0 → 66 → 284 px ; menu fermé : `visibility: hidden` et Tab depuis le burger ne rentre pas dans le menu.
  - **Poids** : `style.min.css` 13,8 → 15,1 Ko, `main.min.js` 1,6 → 2,5 Ko.
  - **Validation** : `check.py` : 11 pages, 0 erreur ; html-validate : 0 erreur hors règle SRI ; Lighthouse mobile : accueil 99 / 100 / 100 / 100 (LCP 2,0 s, CLS 0), Below Zero 100 / 100 / 100 / 100 (LCP 1,8 s, CLS 0).
- Prompts / outils IA utilisés : Compte rendu de la v1.3.0 rédigé par l'équipe, transmis tel quel à l'agent (« Animations » : header PC, burger mobile, cartes FAQ, éléments « facts », boutons ; « ne pas en faire trop […] sinon perte de fluidité »). Outils non IA : Puppeteer / Chrome sous Xvfb (captures avec pointeur réel, mesure des transitions), html-validate, Lighthouse 12.
- Décisions prises :
  - Seuls `transform`, `opacity` et les couleurs sont animés, sauf la hauteur du menu mobile et des FAQ, qui ne concerne qu'un élément à la fois, sur 0,25 s, au clic.
  - Pas d'animation d'entrée au chargement ni au défilement : elles retarderaient l'affichage et coûteraient en performance.
- Suite prévue : Tester le ressenti sur un téléphone réel et sur Safari (iOS / macOS) après déploiement.

### Tâche : Chargement progressif des images (version 1.4.1 du site)
- Objectif : Éviter l'effet « vide puis image d'un coup » signalé par l'équipe : afficher un emplacement animé discret pendant le chargement des images, puis les faire apparaître en fondu.
- Critères de validation : Emplacement aux couleurs du site dans le cadre déjà réservé (CLS = 0) ; reflet lent et peu contrasté ; fondu court ; aucune image principale (LCP) masquée ; sans JavaScript, images affichées normalement ; images déjà en cache ou en erreur jamais bloquées invisibles ; `prefers-reduced-motion` respecté ; aucune requête supplémentaire ; Lighthouse inchangé ; `check.py` sans erreur ; HTML valide.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - **Images concernées** : images différées (`loading="lazy"`) du contenu principal : avatars de l'équipe (studio), vignettes des devlogs (accueil, page Devlogs), visuels de la page Below Zero et illustrations insérées dans les devlogs.
  - **Images exclues** : visuels principaux chargés en priorité (`fetchpriority="high"` : hero de l'accueil, visuel de jeu de Below Zero, key art du studio, image de tête de chaque devlog) : ce sont les éléments LCP, un fondu retarderait leur affichage et dégraderait le score ; ils reçoivent seulement un fond uni bleu nuit pendant leur chargement. Exclus aussi : logo de l'en-tête et du pied de page, favicons, icônes des réseaux sociaux.
  - **Pendant le chargement** : fond dégradé `#0d2a42` → `#1a4769` → `#0d2a42` (tons de la palette) parcouru par un reflet en 1,5 s, en boucle, dans le cadre déjà réservé par `width` / `height` (forme ronde conservée pour les avatars).
  - **Une fois chargée** : l'image apparaît en fondu (opacité 0 → 1 en 0,3 s, `ease`) et le reflet s'arrête.
  - **Amélioration progressive** : les classes sont ajoutées par `main.js` uniquement sur les images pas encore chargées à l'exécution du script ; sans JavaScript, ou pour une image déjà en cache, rien ne change. En cas d'erreur de chargement, fond uni fixe, sans animation.
  - **Mouvement réduit** : fond fixe, ni reflet ni fondu.
  - **Poids** : environ 0,4 Ko de CSS et 0,4 Ko de JavaScript minifiés, aucune requête ajoutée.
  - **Tests** (Puppeteer, requêtes d'images retenues volontairement) : reflet visible tant que l'image est retenue, fondu mesuré à mi-parcours (opacité ≈ 0,47), état final opaque ; hero de l'accueil et visuel de Below Zero jamais masqués ; image en erreur : fond fixe ; rechargement depuis le cache : aucune image masquée.
  - **Validation** : `check.py` : 11 pages, 0 erreur ; html-validate : 0 erreur hors règle SRI ; Lighthouse mobile : accueil 99 / 100 / 100 / 100 (LCP 2,0 s), studio 99 / 100 / 100 / 100 (LCP 2,0 s), Below Zero 100 / 100 / 100 / 100 (LCP 1,8 s), CLS = 0 partout.
- Prompts / outils IA utilisés : Demande de l'équipe transmise à l'agent (« Serait-il possible de faire des animations pour les images qui n'ont pas encore chargé ? Car avoir un vide puis les voir apparaître d'un coup, je trouve que cela fait un peu bizarre »). Outils non IA : Puppeteer (requêtes retenues, captures), Pillow (planche de captures), html-validate, Lighthouse 12.
- Décisions prises :
  - Le reflet est dessiné en fond de l'image elle-même : aucun élément ajouté au HTML, aucune modification du générateur.
  - Les images LCP ne sont jamais masquées : la performance passe avant l'effet.
  - Lighthouse signale le reflet comme « animation non composée » (diagnostic sans effet sur le score) : il ne tourne que sur les images en attente et s'arrête dès leur chargement.
- Suite prévue : Vérifier le rendu sur une connexion mobile réelle après déploiement.

### Tâche : Correction des fondus d'images (version 1.4.2 du site)
- Objectif : Corriger la v1.4.1 : sur le PC de l'équipe, aucun fondu n'apparaissait.
- Critères de validation : Fondu réellement visible sans ralentissement réseau, avec cache vide comme avec cache chaud, sur l'accueil, le studio, Below Zero et un devlog ; aucune image bloquée invisible (sans JavaScript, script en échec, image en erreur ou trop lente) ; logos et icônes non concernés ; `prefers-reduced-motion` respecté ; CLS = 0 ; Lighthouse mobile ≈ 99-100 ; `check.py` sans erreur ; HTML valide.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - **Cause** : en v1.4.1, `main.js` (chargé en `defer`) n'animait que les images encore en cours de chargement au moment où il s'exécutait. Sur une connexion normale, les images WebP (légères, en cache 10 minutes) sont déjà chargées à ce moment-là : aucune n'était animée. Les visuels principaux étaient en plus exclus d'office. Les tests de la v1.4.1 retenaient volontairement les images, ce qui masquait le problème.
  - **Principe retenu** : un script d'une ligne dans le `<head>` de chaque page (via `build.py`) ajoute la classe `js` à `<html>` avant le premier affichage. Avec cette classe, les images du contenu partent à l'opacité 0. `main.js` les fait apparaître en fondu dès qu'elles sont à la fois chargées et visibles à l'écran (`IntersectionObserver`), y compris si elles étaient déjà en cache : le fondu se voit donc aussi en faisant défiler la page.
  - **Durées** : 0,3 s (`ease`) pour les images du contenu, 0,2 s pour les visuels principaux (LCP : hero de l'accueil, visuel de Below Zero, key art du studio, image de tête des devlogs), lancés sans attendre l'observateur.
  - **Attente** : fond uni bleu nuit (`#0d2a42`) dès le premier affichage, même sans JavaScript ; reflet lent (1,5 s) réservé aux images différées dont le chargement dure plus de 120 ms (pas de clignotement si l'image arrive vite).
  - **Sécurités** : sans JavaScript, la classe `js` n'existe pas et les images s'affichent normalement ; si `main.js` ne se charge pas, une animation CSS rend les images visibles après 3 s ; une image en erreur est affichée sur fond uni ; une image visible encore en chargement après 3 s est affichée telle quelle ; à l'impression, toutes les images sont visibles. Mouvement réduit : images visibles immédiatement, sans fondu ni reflet. Logos (en-tête, pied de page), favicons et icônes ne sont pas concernés.
  - **Mesures** (Puppeteer, sans ralentissement réseau, opacité relevée à chaque image affichée) : sur les 4 pages, en ordinateur et en mobile, avec cache vide et cache chaud, l'image principale passe par 0,07 → 0,22 → 0,41 → 0,58 puis 1, en environ 0,18 s ; avatars du studio au défilement : 0 → 0,11 → 0,47 → 0,74 → 1 en 0,3 s.
  - **Validation** : `check.py` : 11 pages, 0 erreur ; html-validate : 0 erreur hors règle SRI ; Lighthouse mobile : accueil 99 / 100 / 100 / 100 (LCP 2,0 s), studio 99 / 100 / 100 / 100 (LCP 2,0 s), Below Zero 100 / 100 / 100 / 100 (LCP 1,8 s), CLS = 0 : scores identiques à la v1.4.1.
  - **Impact réel sur le LCP** : Lighthouse simule le chargement et ne voit pas de différence, mais un relevé dans Chrome (processeur ralenti 4×, réseau mobile émulé, médiane de 5 chargements) montre que l'image principale de l'accueil s'affiche environ 0,2 s plus tard qu'en v1.4.1 (≈ 0,48 s → ≈ 0,67 s), car elle attend `main.js` ; studio inchangé ; Below Zero variable (0,47 à 0,69 s). C'est le coût assumé du fondu sur les visuels principaux.
- Prompts / outils IA utilisés : Retour de l'équipe transmis à l'agent (« Personnellement j'ai testé sur mon pc et les fondus ne fonctionnent pas »). Outils non IA : Puppeteer (opacité image par image, cache vide / chaud, LCP observé, images retenues ou en erreur, script bloqué), Pillow (planche du fondu), html-validate, Lighthouse 12.
- Décisions prises :
  - Fondu déclenché quand l'image est chargée et visible, et non au seul chargement : sur une bonne connexion, les images plus bas dans la page sont chargées avant d'être vues, et leur fondu serait passé inaperçu.
  - Visuels principaux inclus, avec un fondu plus court (0,2 s) et lancé sans délai, pour limiter l'effet sur le LCP.
  - Script en ligne limité à une instruction, sans dépendance ni donnée.
- Suite prévue : Vérifier le rendu sur le PC de l'équipe et PageSpeed Insights (données réelles) après déploiement ; si le LCP de l'accueil se dégrade nettement, retirer le fondu du seul hero de l'accueil.

### Tâche : Correction de l'animation du menu mobile (version 1.4.3 du site)
- Objectif : Sur mobile, à l'ouverture et à la fermeture du menu burger, les liens se déplaçaient dans tous les sens : les stabiliser tout en gardant une animation douce.
- Critères de validation : Liens à leur place définitive pendant toute l'animation ; seules la translation et l'opacité du panneau animées (0,25 s, `ease-in-out`, ouverture et fermeture) ; contenu de la page immobile ; accessibilité conservée (`aria-expanded`, touche Échap, liens non atteignables au clavier menu fermé, croix du bouton) ; mouvement réduit : instantané ; menu ordinateur inchangé ; Lighthouse et CLS inchangés ; `check.py` sans erreur ; HTML valide.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails :
  - **Cause** : en v1.4.0, l'ouverture animait la hauteur du menu (`grid-template-rows` de `0fr` à `1fr`). La liste héritait de la règle ordinateur `flex-wrap: wrap` : tant que la hauteur était insuffisante, les liens passaient sur plusieurs colonnes puis se réorganisaient à chaque image de l'animation.
  - **Correction** : le menu mobile devient un panneau superposé sous l'en-tête (`position: absolute`, fond plein `#071421`, bordure et ombre, au-dessus du contenu). Le contenu de la page ne bouge plus et les liens sont disposés une fois pour toutes en colonne (`flex-wrap: nowrap`). Seuls `opacity` (0 → 1) et `transform` (`translateY(-10px)` → 0) sont animés, en 0,25 s `ease-in-out`, dans les deux sens. Panneau défilable si plus haut que l'écran.
  - **Accessibilité** : menu fermé en `visibility: hidden` à la fin de la transition (liens ni visibles ni focalisables) ; script inchangé (`aria-expanded`, libellé du bouton, Échap qui referme et rend le focus au bouton) ; morphose du bouton en croix conservée.
  - **Mesures** (Puppeteer, largeurs 375 et 414 px, position de chaque lien relevée à chaque image) : une seule disposition des liens par rapport au panneau sur toute l'ouverture et toute la fermeture ; position du contenu de la page constante ; panneau de −10 px à 0 ; opacité progressive ; Tab n'entre pas dans le menu fermé. Mouvement réduit : menu visible immédiatement. Menu ordinateur inchangé.
  - **Validation** : `check.py` : 11 pages, 0 erreur ; html-validate : 0 erreur hors règle SRI ; Lighthouse mobile (accueil) : 99 / 100 / 100 / 100, LCP 2,0 s, CLS 0.
- Prompts / outils IA utilisés : Retour de l'équipe transmis à l'agent (sur mobile, les liens du menu burger bougent dans tous les sens à l'ouverture et à la fermeture) et accord de l'équipe pour la correction (« Oui fais le s'il te plait »). Outils non IA : Puppeteer (positions image par image, planches de l'animation), Pillow, html-validate, Lighthouse 12.
- Décisions prises : Panneau superposé plutôt que menu qui pousse le contenu : aucune remise en page pendant l'animation, et seules des propriétés peu coûteuses sont animées.
- Suite prévue : Vérifier sur un téléphone réel (Android et iOS) après déploiement.

### Tâche : Recommandations GreenIT-Analysis (version 1.4.4 du site)
- Objectif : Corriger les deux remarques de l'extension GreenIT-Analysis (EcoIndex) sur le site en ligne : « CSS ou JS non minifiés » et « pas de feuille de style d'impression », à la condition fixée par l'équipe : aucun impact sur la vitesse, les performances ou le SEO.
- Critères de validation : Plus aucun script ou style en ligne non minifié ; feuille d'impression détectée ; contenu JSON-LD strictement identique ; impression identique ; feuille d'impression non bloquante et en priorité minimale ; Lighthouse mobile et LCP réel inchangés (au bruit de mesure près) ; `check.py` sans erreur ; HTML valide.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS (voir la réserve sur Lighthouse en local ci-dessous)
- Détails :
  - **Diagnostic** (règles lues dans le code source de GreenIT-Analysis) : l'extension regroupe le texte des scripts en ligne (hors JSON-LD) et le juge non minifié s'il contient au moins deux retours à la ligne ; le script d'une ligne du `<head>` (v1.4.2), indenté sur trois lignes par le générateur, suffisait à déclencher la remarque. Pour l'impression, elle cherche une balise `<link rel="stylesheet" media="print">` (ou `<style media="print">`) et ignore les règles `@media print` placées dans la feuille principale.
  - **Scripts en ligne** : le générateur (`fmt.py`) conserve désormais sur une seule ligne, sans espaces ajoutés, tout script ou style en ligne d'une ligne ; le JSON-LD est sérialisé de façon compacte (`separators=(",", ":")`) sur une ligne. Contenu JSON-LD vérifié identique sur les 11 pages (comparaison des objets décodés). Pages HTML : environ 130 lignes et 1 à 2 Ko de moins chacune.
  - **Feuille d'impression** : règles `@media print` déplacées de `style.css` vers une nouvelle source `assets/css/print.css` (ignorée par Git comme les autres sources), minifiée en `print.min.css` (1,2 Ko) par `minify.py` et chargée sur chaque page par `<link rel="stylesheet" href="/assets/css/print.min.css" media="print">` juste après la feuille principale. `style.min.css` passe de 16,1 à 14,9 Ko.
  - **Contrôles ajoutés à `check.py`** : lien `print.min.css` avec `media="print"` sur chaque page, plus de `@media print` dans `style.min.css`, aucun script ou style en ligne sur plusieurs lignes ou entouré d'espaces.
  - **Équivalent GreenIT** (mêmes règles, appliquées par Puppeteer sur 5 pages) : avant, 1 ressource non minifiée sur 3 (« inline js ») et 0 feuille d'impression ; après, 0 sur 4 et 1 feuille d'impression.
  - **Chargement** : Chrome attribue à `print.min.css` la priorité « VeryLow » (la plus basse) et l'indique « non-blocking » ; `style.min.css` reste la seule ressource bloquante, comme avant.
  - **Impression** : PDF A4 de l'accueil, du studio et d'un devlog générés avant et après : même nombre de pages et rendu identique au pixel près.
  - **Mesures avant / après** (Lighthouse 12 mobile, médiane de 3 passages, serveur local HTTP/1.1) :

| Page | Version | Performance | Accessibilité | Bonnes pratiques | SEO | LCP | CLS | TBT |
|---|---|---|---|---|---|---|---|---|
| Accueil | 1.4.3 | 99 | 100 | 100 | 100 | 2,03 s | 0 | 28 ms |
| Accueil | 1.4.4 | 99 | 100 | 100 | 100 | 2,03 s | 0 | 28 ms |
| Studio | 1.4.3 | 99 | 100 | 100 | 100 | 1,95 s | 0 | 30 ms |
| Studio | 1.4.4 | 99 | 100 | 100 | 100 | 2,03 s | 0 | 29 ms |
| Below Zero | 1.4.3 | 100 | 100 | 100 | 100 | 1,80 s | 0 | 31 ms |
| Below Zero | 1.4.4 | 99 à 100 | 100 | 100 | 100 | 1,95 s | 0 | 35 ms |

  - **LCP réel de l'accueil** (Chrome, processeur ralenti 4×, réseau mobile émulé, médiane de 5 chargements) : 668 ms avant, 672 ms après (écart dans le bruit).
  - **Réserve** : en HTTP/1.1 local, la simulation de Lighthouse ajoute environ 0,15 s au LCP du studio et de Below Zero dans 2 passages sur 3 (Below Zero : 100 → 99) ; sans le lien d'impression, Below Zero revient à 100 et 1,80 s à chaque passage : l'écart vient de la requête supplémentaire, que la simulation place sur une nouvelle connexion. En HTTP/2 (protocole de GitHub Pages, testé en local avec certificat de test), aucun écart systématique : studio 1,43-1,59 s avant contre 1,54 s après, Below Zero 1,58-1,74 s avant contre 1,43-1,59 s après, score 100 dans 11 passages sur 12.
- Prompts / outils IA utilisés : Demande de l'équipe transmise à l'agent (« Si cela n'a aucun impact sur la vitesse, les performances, le seo, etc, alors fais le »). Outils non IA : code source de GreenIT-Analysis (lecture des règles), Puppeteer (règles GreenIT, priorités réseau, PDF d'impression, LCP réel), poppler / Pillow (comparaison des PDF), html-validate, Lighthouse 12, serveur HTTP/2 de test (Node.js).
- Décisions prises :
  - Lien d'impression placé dans le `<head>` après la feuille principale : le placer en fin de page ne changeait rien aux mesures.
  - Feuille d'impression conservée malgré la réserve en HTTP/1.1, car le site est servi en HTTP/2 et le LCP réel est inchangé ; retour arrière simple si PageSpeed Insights montre un écart sur le site en ligne (réintégrer `print.css` dans `style.min.css` et retirer le lien).
- Suite prévue : Après déploiement, relancer GreenIT-Analysis et PageSpeed Insights (accueil, studio, Below Zero) et comparer avec les mesures de la v1.4.3.

### Tâche : Ajout de deux nouveaux devlogs (version 1.5.0 du site)
- Objectif : Rédiger et intégrer deux nouveaux articles de devlog (> 800 mots chacun, ton et structure alignés sur les 4 premiers, favorables au référencement local aixois et aux moteurs de réponse) avec chacun une illustration générée par IA, et mettre à jour l'ensemble des pages, flux et données structurées concernés.
- Critères de validation : Plus de 800 mots par article ; faits et univers cohérents (Aix 2156 / Sextia 2306, Sacha Morel, Diapason, jeu sans combat sur PC sans date de sortie) ; nature fictive du studio et du jeu rappelée explicitement tout en s'appuyant sur des lieux réels d'Aix-en-Provence ; titres ≤ 60 caractères, méta descriptions ≤ 155 caractères et ≤ 920 px ; deux visuels WebP multi-tailles dans la palette du site ; maillage interne complet (`accueil`, `studio`, `below-zero`, `devlogs`, `contact`, navigation précédent / suivant) ; `sitemap.xml`, `devlogs/feed.xml`, `llms.txt` et JSON-LD à jour ; `check.py` sans erreur ; HTML valide ; Lighthouse mobile ≈ 99-100.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS (textes validés par l'équipe, publiés le 22/11/2026, commits `6ba6d3b` et `cf1ecfd`, tag `v1.5.0`)
- Détails :
  - **Devlog #5 — « Concevoir Sextia à partir du vrai Aix-en-Provence »** (`/devlogs/concevoir-sextia-vrai-aix/`, 1 297 mots, par Élise Fabre) : explique la transposition du vrai Aix-en-Provence (cours Mirabeau, fontaine de la Rotonde, thermes Sextius, vieille ville, quartier Mazarin, fondation antique d'*Aquae Sextiae* en 122 av. J.-C. par Caius Sextius Calvinus) vers la cité souterraine Sextia de 2306, avec encadré « Repères clés » et rappel explicite que Flexarion et Below Zero sont fictifs.
  - **Devlog #6 — « Accessibilité et rythme d'un jeu sans combat »** (`/devlogs/accessibilite-rythme-jeu-sans-combat/`, 1 173 mots, par Théo Marchetti) : détaille comment Below Zero maintient la tension narrative sans combat ni barre de vie, le rôle du Diapason et de Sacha Morel, la respiration entre 2156 et 2306 et les options d'accessibilité motrice, visuelle, cognitive et auditive sur PC.
  - **Cohérence des rôles** : sur la page du studio et dans les précédents devlogs, Élise Fabre est « Sound designer » et Théo Marchetti « Développeur gameplay » (Inès Valcourt étant directrice créative et Lucas Arnaud game designer). Ces intitulés ont été conservés pour garder le JSON-LD et la page studio cohérents, tout en ancrant chaque article dans la collaboration avec la direction artistique / les environnements 3D (#5) et le game design (#6).
  - **Visuels générés par IA** : deux illustrations 16:9 dans la palette (`#071421`, `#123A58`, `#19B9D4`, `#B7DDE8`, `#E8EDF0`), converties en WebP `480 / 960 / 1280 px` : `devlog-sextia-aix-*.webp` et `devlog-accessibilite-rythme-*.webp`, avec attributs `alt` descriptifs et mention dans le kit presse.
  - **Mises à jour liées** : date `LASTMOD` / `MOD` portée au `2026-11-22`, bloc « Derniers devlogs » de l'accueil (#6, #5, #4), index `/devlogs/` (6 articles et méta description mise à jour), liens ajoutés dans `/studio/`, `/below-zero/` et `/contact/`, boutons précédent / suivant entre les 6 articles, `sitemap.xml`, `devlogs/feed.xml` (`lastBuildDate` au `22 novembre 2026`), `llms.txt`, `README.md`, et espacement `.prose .facts` dans `style.css` / `style.min.css`.
  - **Validation** : `check.py` : 13 pages, 0 erreur ; `serp.py` : tous les titres (≤ 58 car.) et descriptions (≤ 144 car., ≤ 887 px) dans les limites ; `html-validate` : 0 erreur hors règle SRI ; aucun mot interdit.
  - **Lighthouse mobile** : devlog #5 (`99 / 100 / 100 / 100`, LCP 2,1 s, CLS 0), devlog #6 (`99 / 100 / 100 / 100`, LCP 2,0 s, CLS 0), index `/devlogs/` (`99 / 100 / 100 / 100`, LCP 2,0 s, CLS 0), accueil (`99 / 100 / 100 / 100`, LCP 2,1 s, CLS 0).
- Prompts / outils IA utilisés :
  - Consigne de l'équipe : ajouter deux devlogs (« Concevoir Sextia à partir du vrai Aix » et « Accessibilité et rythme d'un jeu sans combat ») et mettre à jour tous les fichiers liés (sitemap, flux RSS, `llms.txt`, maillage interne, rapport).
  - Prompt image #5 (`GenerateImage`, 16:9) : coupe géologique entre le vrai Aix-en-Provence au crépuscule (cours Mirabeau, fontaine de la Rotonde à trois vasques, façades calcaires) et Sextia en 2306 dans une cavité souterraine (colonnes de verre minéral, canaux thermaux cyan, ciel artificiel bleu glacier), palette `#071421 #123A58 #19B9D4 #B7DDE8 #E8EDF0`, sans texte.
  - Prompt image #6 (`GenerateImage`, 16:9) : scène d'exploration calme sans arme sur une place souterraine de Sextia, jeune technicien à lampe frontale tenant un diapason lumineux émettant des ondes cyan vers une fontaine thermale devant des habitants silencieux, palette `#071421 #123A58 #19B9D4 #B7DDE8 #E8EDF0`, sans texte.
  - Outils non IA : Pillow (conversion WebP multi-tailles), `serp.py`, `html-validate`, Lighthouse 12, Puppeteer (captures `v150-*`).
- Décisions prises :
  - Ajout d'un bloc `.facts` (« Repères clés ») en tête de chaque nouvel article pour renforcer la lisibilité et l'extraction factuelle par les moteurs de réponse (GEO), avec marge verticale dédiée (`.prose .facts`).
  - Travail préparé sur l'environnement de travail sans commit ni push avant relecture des deux textes par l'équipe.
- Suite prévue : Relecture des deux textes par l'équipe, éventuels ajustements, puis transfert, commit et mise en ligne (et contrôle Search Console du sitemap mis à jour).

### Tâche : Retrait de la mention IA en bas des devlogs (version 1.5.1 du site)
- Objectif : Retirer l'encadré « Ce devlog a été rédigé avec l'assistance d'une IA… » affiché en bas de chaque devlog, la mention de l'usage de l'IA devant figurer uniquement dans les mentions légales, comme convenu avec l'équipe.
- Critères de validation : Plus aucun encadré de ce type sur les 6 devlogs ; section « Usage de l'intelligence artificielle » des mentions légales inchangée ; `check.py` sans erreur ; aucune autre page modifiée.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : Suppression de la ligne `<aside class="note">` dans le gabarit des articles (`tools/generateur/c_devlogs.py`), puis régénération du site. Seules les 6 pages de devlogs changent. Les légendes d'images « visuel généré par IA » n'ont pas été touchées.
- Prompts / outils IA utilisés : Consigne de l'équipe : « retirer cette mention dans tous les devlogs, seule la mention des mentions légales doit rester ».
- Décisions prises : Correction traitée comme un correctif (numéro de version 1.5.1).
- Suite prévue : Mise en ligne effectuée (commits e169974 et 7903e28, tag v1.5.1).

### Tâche : Suppression de l'effet de survol des encadrés « fiche technique » (version 1.5.2 du site)
- Objectif : Retirer le halo cyan qui apparaissait au survol des encadrés `.facts` (fiche technique de Below Zero, encadrés des devlogs), à la demande de l'équipe.
- Critères de validation : Aucun effet visuel au survol des encadrés `.facts` ; style de base des encadrés inchangé ; effets des autres cartes inchangés ; `check.py` sans erreur.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS
- Détails : Suppression de la transition `.facts` et de la règle `.facts:hover` dans `assets/css/style.css`, puis régénération de `style.min.css`. Aucune page HTML n'est modifiée.
- Prompts / outils IA utilisés : Consigne de l'équipe : « J'aimerais qu'il n'y ait aucun effet de survol ».
- Décisions prises : Correction traitée comme un correctif (numéro de version 1.5.2).
- Suite prévue : Mise en ligne effectuée (commits 858e6fd et db57ea5, tag v1.5.2).

### Tâche : Pages carte de Sextia, devlog #7 et LinkedIn (version 1.6.0 du site)
- Objectif : Faire progresser le site sur des mots-clés secondaires (studio de jeu vidéo, jeu vidéo indépendant, science-fiction, SF, Aix-en-Provence, ville futuriste) avec deux contenus originaux et substantiels, et ajouter la page LinkedIn de l'organisation aux profils officiels.
- Critères de validation : Contenus originaux (pas de paraphrase du devlog #5), White Hat (brief 3.4 : pas de bourrage, pas de contenu dupliqué, aucun lien vers les sites d'autres groupes) ; mots-clés placés naturellement dans le title (≤ 60 car.), la meta description (≤ 155 car.), le H1, les H2, les `alt` et les ancres internes ; faits réels sur les lieux d'Aix vérifiables et prudents ; carte SVG légère et accessible ; un seul H1 par page ; nouvelles URL dans `sitemap.xml` ; `devlogs/feed.xml`, `llms.txt`, `README.md`, JSON-LD, précédent / suivant à jour ; `check.py` sans erreur ; HTML valide ; Lighthouse mobile ≈ 100 ; aucune mention d'IA en bas d'article ni dans le pied de page.
- Réalisé par : FlexaBot (agent IA)
- Résultat : PASS (préparé en local, en attente de validation des textes par l'équipe)
- Détails :
  - **Carte commentée de Sextia** (`/below-zero/carte-sextia/`, 1 517 mots, nouveau module `tools/generateur/c_carte.py`) : carte stylisée en SVG inline (palette du site, `role="img"`, `<title>` et `<desc>`, aucun attribut `style`) qui situe six lieux réels d'Aix-en-Provence (pavillon Vendôme, thermes de Sextius, cathédrale Saint-Sauveur, place des Prêcheurs, cours Mirabeau, Rotonde). Une fiche par lieu : le lieu réel aujourd'hui, le lieu en 2156 dans Below Zero, sa fonction dans Sextia en 2306. Angle distinct du devlog #5 : la société de Sextia et la fonction de chaque lieu, et non la méthode de production. JSON-LD : `BreadcrumbList`, `WebPage` et `Map` rattachée à l'`Organization` et au `VideoGame`, avec les six lieux en `mentions`.
  - **Devlog #7 — « Créer un studio de jeu vidéo indépendant à Aix-en-Provence »** (`/devlogs/creer-studio-jeu-video-aix/`, 1 368 mots, par Inès Valcourt, directrice créative) : histoire du studio depuis la game jam de 2022, choix d'Aix, choix de la science-fiction narrative sans combat, débuts, ordre des recrutements (cohérent avec la frise de la page Studio), écosystème entre Aix et Marseille (sans partenaire réel nommé ni chiffre inventé), conseils. `BlogPosting` rattaché à l'`Organization` (`about`).
  - **Visuel du devlog #7** : illustration 16:9 générée par IA dans la palette, convertie en WebP `480 / 960 / 1280 px` (`devlog-studio-aix-*.webp`, 17 à 86 Ko).
  - **LinkedIn** (`https://www.linkedin.com/company/flexarion-officiel`) : ajouté à `SOCIAL_DATA` (`sameAs` de l'`Organization` sur toutes les pages, pied de page, page Contact, `llms.txt`), avec `rel="me noopener"` comme les autres réseaux. LinkedIn n'étant plus dans Simple Icons, pictogramme monochrome simplifié dessiné pour le site (`assets/icons/linkedin.svg`), crédits mis à jour dans `assets/icons/LISEZMOI.md` et dans les mentions légales (date de mise à jour au 24/11/2026 ; section IA inchangée).
  - **Maillage interne** : liens vers la carte depuis `/below-zero/` (section « D'où vient le nom Sextia ? »), l'accueil (carte « Une SF ancrée en Provence »), `/studio/` et le devlog #5 ; liens vers le devlog #7 depuis `/studio/` (frise), `/below-zero/` (coulisses) et la carte. Ancres descriptives (« carte commentée de Sextia sous Aix », « création d'un studio de jeu vidéo indépendant à Aix-en-Provence »).
  - **Mises à jour liées** : `LASTMOD` et `MOD` au `2026-11-24`, « Derniers devlogs » de l'accueil (#7, #6, #5), index `/devlogs/` (7 articles, description mise à jour), précédent / suivant (#6 → #7, #7 dernier), `sitemap.xml` (13 URL indexables dont les 2 nouvelles), `devlogs/feed.xml` (7 items, `lastBuildDate` au 24/11/2026), `llms.txt`, `README.md`, styles `.carte` et `.lieu` dans `style.css` (sans effet de survol).
  - **Accessibilité** : encadrés « Repères » des devlogs #5, #6, #7 et de la carte passés en `role="note"` pour que leur `aria-label` soit valide.
  - **Corrections d'incohérences (demandées par l'équipe)** : devlog #4, paragraphe final reformulé (plus de mention d'outils d'IA dans le corps ; légendes « visuel généré par IA » conservées) ; FAQ de l'accueil (HTML et JSON-LD `FAQPage`) : « une directrice créative, Inès Valcourt » au lieu de « un directeur créatif » ; `README.md` : feuille d'impression décrite comme fichier séparé `print.min.css` chargé en `media="print"`.
  - **Date de publication du devlog #7** : 24/11/2026 à 15:00 (heure de Paris), identique dans l'article (`<time datetime="2026-11-24T15:00:00+01:00">`), `article:published_time`, le JSON-LD (`datePublished`), le flux RSS (`pubDate` `Tue, 24 Nov 2026 15:00:00 +0100`) ; `sitemap.xml` en `lastmod` 2026-11-24 (format date seule). GitHub Pages ne permet pas de programmer une publication : la mise en ligne réelle a lieu au push.
  - **Vérification des faits réels de la carte de Sextia** (sources consultées le 24/11/2026) :
    - Rotonde : mise en eau en 1860, 12 m de haut, place du Général-de-Gaulle, statues de la Justice (vers le cours), de l'Agriculture (vers Marseille, « Commerce et Agriculture » selon Wikipédia et le CRT) et des Beaux-Arts (vers Avignon) : **confirmé** ; « une douzaine de mètres » précisé en « 12 mètres », « inaugurée » en « mise en eau ». Sources : https://www.aixenprovence.fr/Fontaine-de-la-Rotonde, https://fr.wikipedia.org/wiki/Fontaine_de_la_Rotonde, https://www.aixenprovencetourism.com/it/vedere/piazze-e-fontane/, https://provence-alpes-cotedazur.com/que-faire/culture-et-patrimoine/lieux/fontaine-de-la-rotonde-aix-en-provence-fr-2867121/
    - Pavillon Vendôme : construction à partir de 1665 (campagne 1664-1667), deux atlantes encadrant l'entrée et soutenant le balcon, jardin à la française, propriété de la commune, musée d'expositions : **confirmé** ; « cardinal Louis de Vendôme » **corrigé** en « Louis de Mercœur, duc de Vendôme et gouverneur de Provence » (titre retenu par les sources consultées), « pavillon de plaisance » remplacé par « maison de campagne hors des remparts ». Sources : https://fr.wikipedia.org/wiki/Pavillon_de_Vendôme, https://pop.culture.gouv.fr/notice/merimee/PA00081103
    - Thermes de Sextius : établissement thermal moderne à l'ouest de la vieille ville, sur le cours Sextius, qui conserve une piscine voûtée d'époque romaine : **confirmé et précisé** (formulation « près de vestiges » remplacée). Source : https://fr.wikipedia.org/wiki/Thermes_Sextius (article « Thermes romains d'Aix-en-Provence »).
    - Cathédrale Saint-Sauveur : baptistère octogonal du VIe siècle remployant des colonnes antiques, cloître roman de la fin du XIIe siècle, portail gothique des XVe-XVIe siècles, triptyque du Buisson ardent de Nicolas Froment (1475-1476) : **confirmé et précisé** (« premiers siècles chrétiens » remplacé par « VIe siècle », date du triptyque « vers 1476 »). Sources : https://www.aixenprovence.fr/Cathedrale-Saint-Sauveur, https://fr.wikipedia.org/wiki/Cathédrale_Saint-Sauveur_d'Aix-en-Provence, https://pop.culture.gouv.fr/notice/palissy/PM13001017
    - Place des Prêcheurs : nom venu des dominicains (couvent fondé en 1272), église de la Madeleine ancienne église conventuelle des Prêcheurs, fontaine-obélisque de Jean-Pancrace Chastel (1758) entre la place des Prêcheurs et la place de la Madeleine, grand marché les mardis, jeudis et samedis matin avec la place de Verdun : **confirmé et précisé** (« fontaine du XVIIIe siècle » précisée, « plusieurs matinées » précisé). Sources : https://www.aixenprovence.fr/Fontaine-des-Precheurs, https://www.aixenprovence.fr/Operation-archeologique-no568-Eglise-de-la-Madeleine, https://fr.wikipedia.org/wiki/Église_de_la_Madeleine_d'Aix-en-Provence, https://pop.culture.gouv.fr/notice/merimee/PA00080997 (cité par Wikipédia), https://provence-alpes-cotedazur.com/que-faire/culture-et-patrimoine/lieux/places-comtales-aix-en-provence-fr-5191394/
    - Cours Mirabeau : aménagé à partir de 1649 à l'emplacement du rempart sud, appelé « le Cours », renommé en 1876 en l'honneur de Mirabeau, élu du tiers état d'Aix en 1789, fontaines des Neuf-Canons, moussue et du Roi René (à l'extrémité est) : **confirmé et précisé** ; « eau tiède » **corrigé** en « eau chaude » (source des Bagniers). Source : https://fr.wikipedia.org/wiki/Cours_Mirabeau
    - Autres faits de la page (Aquae Sextiae, Caius Sextius comme fondateur, orientation nord-ouest / nord / est des lieux) : **confirmés** par les mêmes sources (coordonnées Wikipédia). Les éléments « en 2156 » et « en 2306 » relèvent de la fiction.
  - **Renfort SEO White Hat** (combinaisons « jeu vidéo » + SF / science-fiction, ville futuriste / souterraine, Aix-en-Provence, 2156 / 2306 / voyage dans le temps / causalité temporelle) :
    - Titles revus : `/below-zero/` (« Below Zero, jeu vidéo SF à Aix-en-Provence | Flexarion »), `/studio/` (« Studio Flexarion : jeu vidéo indépendant à Aix-en-Provence »), carte (« Carte de Sextia, ville du jeu vidéo SF sous Aix | Flexarion »), devlogs #1, #2 et #5 ; title de l'accueil inchangé (centré sur Flexarion) ; « Flexarion » conservé dans chaque title.
    - Meta descriptions revues : accueil, `/below-zero/`, `/studio/`, carte, devlog #2. H1 revus : `/below-zero/` et `/studio/`. H2 revus : accueil (jeu phare), `/below-zero/` (univers, mécaniques, visuels), `/studio/` (« Pourquoi un studio de jeu vidéo à Aix-en-Provence ? »), carte. `alt` du key art de `/studio/` et ancres internes (accueil → Below Zero, studio → Below Zero) rendus descriptifs.
    - Contenu ajouté : section « Quel genre de jeu vidéo est Below Zero ? » sur `/below-zero/` (jeu vidéo de science-fiction, ville futuriste souterraine, voyage dans le temps sans machine entre 2156 et 2306, causalité temporelle, ancrage à Aix-en-Provence) et deux questions de FAQ (voyage dans le temps, pourquoi Aix-en-Provence), reprises dans le JSON-LD `FAQPage`.
    - JSON-LD `VideoGame` (déjà présent) enrichi : `genre` + « Voyage dans le temps », `temporalCoverage` `2156/2306`, `keywords` étendus, description précisant « en développement sur PC » ; aucune date de sortie ni note n'est déclarée.
  - **Validation** : `check.py` : 15 pages, 0 erreur ; `html-validate` : 0 erreur sur toutes les pages (hors règles `doctype-style` et `require-sri`) ; un seul H1 par page ; titles ≤ 59 caractères, descriptions ≤ 144 caractères. Lighthouse 12 mobile (serveur local) : accueil `99 / 100 / 100 / 100` (LCP 2,1 s, CLS 0), `/below-zero/` `99 / 100 / 100 / 100` (LCP 2,0 s, CLS 0), carte `100 / 100 / 100 / 100` (LCP 1,5 s, CLS 0), devlog #7 `100 / 100 / 100 / 100` (LCP 1,8 s, CLS 0, mesure précédente).
- Prompts / outils IA utilisés :
  - Consigne de l'équipe : créer une carte commentée de Sextia sous Aix et un récit de la création du studio, optimisés pour les mots-clés autour du studio, de la science-fiction et d'Aix, avec du contenu original, et ajouter le LinkedIn de l'organisation ; validation du contenu avant toute mise en ligne.
  - Prompt image #7 (`GenerateImage`, 16:9) : intérieur d'un petit studio de jeu vidéo indépendant dans un bâtiment en pierre provençal d'Aix-en-Provence au crépuscule, fenêtre en arc sur les toits, un clocher et la Sainte-Victoire, équipe de dos devant des écrans cyan montrant une ville souterraine futuriste, palette `#071421 #123A58 #19B9D4 #B7DDE8 #E8EDF0`, sans texte.
  - Consigne de l'équipe (suite) : corriger les incohérences, garder la publication du devlog #7 à 15 h, vérifier soi-même les faits réels avec des sources fiables, et renforcer le positionnement sur « jeu vidéo » associé à « SF », « ville », « Aix » et aux termes du temps.
  - Vérification des faits : `WebSearch` et `WebFetch` (Wikipédia FR, Ville d'Aix-en-Provence, base POP / Mérimée / Palissy, Office de tourisme d'Aix, Comité régional de tourisme).
  - Outils non IA : Pillow (WebP), `html-validate`, Lighthouse 12, Puppeteer (captures `v160-*`).
- Décisions prises :
  - Carte en SVG inline plutôt qu'en image générée : plus légère, nette à toutes les tailles, accessible et cohérente avec la palette.
  - Carte placée sous `/below-zero/` (contenu d'univers) et récit du studio publié comme devlog #7, pour équilibrer le site entre le jeu, le studio et la science-fiction.
  - Rappel de la nature fictive dans le corps des pages uniquement (pas dans les titres, descriptions ni JSON-LD, conformément au contrôle de `check.py`).
  - Title de l'accueil laissé inchangé pour ne pas faire régresser la requête « Flexarion » ; title du studio distinct de celui de l'accueil pour éviter la cannibalisation.
  - Décision de l'équipe (24/11/2026) : l'usage de l'IA n'est mentionné **que** dans les mentions légales (section « Usage de l'intelligence artificielle », inchangée) et dans ce rapport, qui reste le document de traçabilité. Retrait, depuis le générateur (`c_main.py`, `c_devlogs.py`), de toutes les autres mentions sur les pages servies : légendes « visuel généré par IA » des devlogs #1 à #4 (légendes descriptives conservées), légende de l'aperçu de jeu et phrase d'introduction de la section Visuels de `/below-zero/` (reformulées en « visuel de travail » / « visuels de travail »), légende du key art et phrase sur les avatars de `/studio/` (légende reformulée, phrase supprimée), consigne de crédit du kit presse de `/contact/` (désormais « © Flexarion »). Contrôle final par recherche (`IA`, `AI`, « intelligence artificielle », « généré(e)s », noms d'outils) : 0 occurrence dans les 32 fichiers servis hors mentions légales. Le `README.md` et `docs/PHASE4-NETLINKING.md` (documents internes) conservent leurs mentions.
- Suite prévue : Relecture des textes par l'équipe, ajustements éventuels, puis transfert, commit, mise en ligne et tag v1.6.0 ; soumission des deux nouvelles URL dans Search Console.

---

## Synthèse réflexive

*Cette partie sera rédigée par les étudiants, sans aucune aide d'IA générative, conformément au brief (partie 6).*
