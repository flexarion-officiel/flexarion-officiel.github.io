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
  - **Réseaux sociaux** : GitHub, LinkedIn, itch.io, X et Instagram dans le pied de page de chaque page et dans une section « Suivre le studio sur les réseaux » de la page contact (`rel="me noopener"`, nouvel onglet) ; les 5 URL sont dans `sameAs` de l'Organization et dans `llms.txt`.
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

---

## Synthèse réflexive

*Cette partie sera rédigée par les étudiants, sans aucune aide d'IA générative, conformément au brief (partie 6).*
