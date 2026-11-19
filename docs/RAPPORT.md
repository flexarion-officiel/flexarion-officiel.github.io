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

---

## Synthèse réflexive

*Cette partie sera rédigée par les étudiants, sans aucune aide d'IA générative, conformément au brief (partie 6).*
