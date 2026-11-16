# Concours SEO inter étudiants portant sur le mot clé Flexarion

## Contexte

Pour notre projet, tu vas analyser les 3 cours et le “brief" en PDF, tu vas prendre connaissance des informations données, et réfléchir uniquement avec ces données quand elles seront utiles. Ce projet consiste à créer un site web et faire en sorte qu'il soit le mieux référencé possible. D'autres équipes sont en compétition avec nous. pour référencer le site, on utilisera des méthodes que l'on te précisera ultérieurement. 
Dans ce projet, nous sommes tous un studio de développement de jeux vidéo
indépendant, spécialisé dans la science-fiction, basé à Aix-en-Provence. Chaque groupe incarne son propre
studio « Flexarion ».

## Notre mission

On doit concevoir, publier et optimiser un véritable site web pour notre studio Flexarion, puis développer une présence sur les réseaux sociaux cohérente avec notre identité de marque. L'objectif final est double :
- Obtenir la meilleure position possible sur Google pour le mot-clé « Flexarion »
- Optimiser le GEO au maximum

## Site web

Notre site doit comporter au minimum :
- Une page d'accueil qui présente le studio et son positionnement.
- Une page « Le studio » : histoire, équipe, localisation à Aix-en-Provence.
- Une page dédiée à votre jeu phare : univers, mécaniques de jeu, visuels.
- Un blog de « devlogs » (journal de développement) avec au moins 2 articles publiés avant le TD4.
- Une page contact / presse.

## Brand Guidelines (à compléter)

### Identité
- Nom : Flexarion
- Type : Studio de jeux vidéo indépendant
- Genre : Science-fiction
- Localisation : Aix-en-Provence
- Ton : [à définir]
- Jeu phare : [à définir]
- Univers : [à définir]
- Équipe fictive : [à définir]
- Date création : [à définir]
- Palette : [à définir]

### Positionnement
Pour [cible], Flexarion est le studio SF qui [bénéfice], contrairement à [concurrents] qui [limite].

### Personas
- [Nom] : [âge, intérêts, plateformes]

## Réalisation

Tu dois travailler dans le dépôt Git suivant : `/Users/alexandre/Documents/IUT/BUT2/Projets/r3.13/flexarion.github.io`. Tu n'as pas le droit de sortir de ce dernier. Pour toutes les commandes « sensibles » telles que `rm`, `mv`, `git rm`, et autres, ton accord préalable sera requis. Tu feras les commits Git en ton nom, pas le mien, en respectant les conventions de commit.

Pour chaque tâche effectuée, écris dans un fichier markdown un rapport suivant la template ci-dessous :
```
    ### Tâche : [nom]
    - Objectif :
    - Critères Tester :
    - Réalisé par :
    - Résultat tests : PASS/FAIL
    - Détails :
    - Prompts/outils IA :
    - Décisions :
    - Suivant :
```

Tu pourras créer ce fichier RAPPORT.md dans un répertoire `docs/`.

## Informations importantes relatives au projet

Pour rattraper le retard et viser la première place sur le mot-clé vierge « Flexarion », la stratégie ne repose pas sur qui a publié en premier, mais sur l'autorité de domaine, la vitesse d'indexation forcée et la densité du maillage externe (netlinking) tout en respectant scrupuleusement le cadre « White Hat » imposé par le brief.

### 1. Le choix de l'hébergement et l'indexation immédiate (J0)

Puisque le brief déconseille un nom de domaine neuf (effet Sandbox) et autorise GitHub Pages ou du HTML/CSS statique, c'est de loin l'arme la plus redoutable face à des groupes qui vont s'enliser sur des WordPress.com lents ou des pages Notion mal structurées :   Stack technique ultra-rapide : Générer un site statique propre (HTML5 sémantique pur ou Astro) hébergé sur flexarion.github.io (ou flexarion-studio.github.io si flexarion est déjà pris par un autre groupe). Le domaine github.io bénéficie d'une autorité de domaine (DA) colossale auprès de Google.   Forcer le passage du Googlebot : Ne surtout pas attendre que Google découvre le site tout seul. Dès la mise en ligne des pages minimales (Accueil, Studio, Jeu, Contact), connecter immédiatement le site à la Google Search Console via une balise meta HTML, soumettre le fichier sitemap.xml et utiliser l'outil « Inspection de l'URL > Demander une indexation » sur chaque page. Le site sera indexé en moins de 24 à 48 heures.

### 2. Dominer le SEO On-Page et la structure technique

Là où la majorité des étudiants se contenteront de rédiger du texte générique par IA, la différence se fera sur le balisage chirurgical et les signaux envoyés aux moteurs : Données structurées (Schema.org) : Intégrer dans le `<head>` un script JSON-LD combinant Organization / LocalBusiness (avec l'adresse exacte à Aix-en-Provence et les coordonnées GPS) et VideoGame (pour le jeu de science-fiction). Cela permet de déclencher des Rich Snippets dans les résultats de recherche.   Architecture en silo : Comme demandé pour le TD3, structurer le maillage interne de façon stricte. Les articles de devlog (minimum 2 requis, mais en publier 4 ou 5 bien charpentés de 800+ mots donnera un avantage décisif) doivent tous pointer vers la page du jeu phare et vers la page d'accueil avec des ancres variées incluant « Flexarion Studio ».   Sémantique locale et métier : Ne pas bourrer le mot « Flexarion » (interdit par les règles d'équité), mais enrichir tout le champ lexical autour de : studio indépendant de jeux vidéo, Aix-en-Provence, développement SF, moteur de jeu, game design, devlog.   Performance pure : Obtenir un score de 100/100 sur Google PageSpeed Insights (images en .webp avec attributs alt renseignés, zéro JavaScript bloquant). Cela garantit également le maximum de points sur le « score de secours » prévu par le brief en cas d'aléa d'indexation.

### 3. La vraie bataille : le Netlinking (SEO Off-Page) et l'occupation de la SERP

Sur un mot-clé inventé où 10 ou 15 groupes s'affrontent avec le même nom, Google départagera le n°1 grâce aux backlinks (liens entrants) et aux signaux d'entité :   Les plateformes de jeux vidéo (le coup maître) : Puisque Flexarion est un studio de jeu indé, créer une vraie page studio et une page projet (avec une démo jouable minimale ou des visuels/trailers) sur itch.io (flexarion.itch.io) et IndieDB. Ces sites ont une autorité énorme dans le gaming et permettent de placer un lien en dofollow (ou à fort trafic référent) vers le site principal.   Écosystème tech & réseaux sociaux : Le brief demande au moins un réseau social au TD2. Créer des profils complets au nom de « Flexarion Studio » sur LinkedIn (page entreprise), GitHub (organisation avec un vrai dépôt de code du jeu et un README.md pointant vers le site), YouTube (poster un court teaser vidéo avec le lien du site en description), X/Twitter et Medium/Dev.to (pour relayer les devlogs avec lien canonique vers le site).   Indexation des backlinks : Non seulement ces profils vont pousser le site principal en n°1 grâce à leurs liens, mais ils vont eux-mêmes truster la première page de Google, repoussant les sites des groupes concurrents plus bas dans le classement.

### 4. Sécuriser les 9 points dédiés à l'IA (Notes 1 & 2)

L'usage documenté de l'IA pèse 4 points sur la note SEO et 5 points sur la note de communication :   Journaliser dès la première minute : Mettre en place un tableau (Notion ou Markdown) qui archive chaque prompt utilisé (génération de lore SF, structuration des balises meta, création du logo, génération du JSON-LD) en notant le modèle utilisé, le prompt initial, les erreurs de l'IA et la correction humaine apportée.   Rédiger la synthèse réflexive 100 % à la main : Le brief est intraitable sur ce point. Valoriser dans cet écrit (1 à 2 pages sans aucune IA) le fait que l'IA est excellente pour générer du volume ou du code structurel (JSON-LD, balises), mais médiocre sur l'originalité créative (tendance aux mêmes clichés SF que les autres groupes) et aveugle sur la stratégie de netlinking réel.