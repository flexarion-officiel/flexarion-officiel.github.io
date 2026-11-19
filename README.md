# Flexarion — site officiel

Site du studio **Flexarion**, studio indépendant de jeux vidéo de science-fiction basé à Aix-en-Provence, et de son jeu phare **Below Zero**.

Site réalisé dans le cadre du module « Plan de communication & webmarketing à l'ère de l'IA » du BUT Informatique (2e année) de l'IUT d'Aix-Marseille, par BARTAL Manal, CHAIB EDDOUR Kawthar, PETIT Noé et SBEGHEN Alexandre.

- Site en ligne : https://flexarion-officiel.github.io/
- Organisation GitHub : https://github.com/flexarion-officiel

## Choix techniques

- HTML5 sémantique statique, **sans framework ni étape de build obligatoire**, servi par GitHub Pages.
- **Une seule feuille de style globale**, servie minifiée (`assets/css/style.min.css`) et liée par `<link rel="stylesheet">` sur chaque page ; aucun `<style>` ni attribut `style` dans le HTML. Feuille d'impression (`@media print`) intégrée.
- Zéro JavaScript bloquant : un seul script minifié `assets/js/main.min.js` (~1,6 Ko, `defer`) pour le menu burger mobile, le bouton « retour en haut », la reconstitution de l'adresse e-mail masquée et un message caché dans la console. Sans JavaScript, les pages restent reliées par le fil d'Ariane, les liens du contenu et le pied de page.
- Images WebP en 3 tailles (480 / 960 / 1280 px) avec `srcset`, `width`/`height`, `loading="lazy"` sauf l'image LCP (`fetchpriority="high"`), recadrage mobile dédié pour les visuels de tête (accueil, Below Zero) ; avatars de l'équipe en 160 / 320 px.
- Icônes des réseaux sociaux en SVG issues de [Simple Icons](https://simpleicons.org) (licence CC0), version monochrome, rangées dans `assets/icons/`.
- Devlogs classés du plus récent au plus ancien, avec boutons « Devlog précédent » / « Devlog suivant » (`rel="prev"` / `rel="next"`) sur chaque article.
- Police **Exo 2** (SIL Open Font License 1.1) auto-hébergée dans `assets/fonts/` : sous-ensembles WOFF2 latin (préchargé, ~27 Ko) et latin étendu (chargé seulement si nécessaire), `font-display: swap`, police de secours aux métriques ajustées (`size-adjust`, `ascent-override`…) pour éviter tout décalage de mise en page, puis polices système et génériques (`system-ui`, `Arial`, `sans-serif`).
- Favicons : `favicon.ico` (16/32/48/96 px), `favicon-48.png`, `favicon-32.png`, `favicon.svg`, `apple-touch-icon.png`, icônes 192/512 du manifeste.
- Données structurées JSON-LD : `Organization` (avec `alternateName`, `logo`, `sameAs` vers les réseaux), `WebSite`, `WebPage`, `BreadcrumbList`, `VideoGame`, `Blog`, `BlogPosting`, `FAQPage`.
- SEO : title / meta description uniques, canonical, Open Graph, Twitter Cards, `sitemap.xml`, `robots.txt`, flux RSS, page 404 personnalisée. Les mentions légales sont en `noindex, follow` et absentes du sitemap.
- HTML généré avec une indentation de 2 espaces (module `tools/generateur/fmt.py`).
- GEO : `llms.txt` à la racine, FAQ factuelles, encadrés « en bref » avec faits vérifiables.

## Structure

```
/
├── index.html                  Accueil (studio + positionnement + FAQ)
├── studio/                     Le studio : histoire, équipe, Aix-en-Provence
├── below-zero/                 Jeu phare : univers, mécaniques, visuels, FAQ
├── devlogs/                    Index des devlogs + feed.xml (RSS)
│   ├── concevoir-deux-villes-aix-2156-2306/
│   ├── enigmes-causalite-temporelle/
│   ├── sound-design-ville-souterraine/
│   └── character-design-habitants-futur/
├── contact/                    Contact & kit presse
├── mentions-legales/           Mentions légales (noindex : nature du projet, éditeurs, hébergeur, IA, crédits)
├── 404.html
├── assets/css/style.min.css    Feuille de style globale unique (minifiée)
├── assets/js/main.min.js       Menu burger, retour en haut, e-mail masqué, message console (minifié)
├── assets/fonts/               Police Exo 2 (WOFF2) + licence OFL.txt
├── assets/img/                 Visuels WebP (générés par IA), avatars de l'équipe + image Open Graph
├── assets/icons/               Icônes SVG des réseaux sociaux (Simple Icons, CC0)
├── favicon.ico, favicon.svg, favicon-48.png, favicon-32.png, apple-touch-icon.png, icon-192.png, icon-512.png
├── site.webmanifest, sitemap.xml, robots.txt, llms.txt, .nojekyll
├── tools/generateur/           Générateur Python (source des pages, sitemap, RSS, llms.txt)
└── docs/                       RAPPORT.md (journal IA), PHASE4-NETLINKING.md
```

## Régénérer le site

Les sources CSS et JS lisibles (`assets/css/style.css`, `assets/js/main.js`) sont conservées en local mais ignorées par Git (`.gitignore`) : seules les versions minifiées sont publiées. Après une modification des textes (`tools/generateur/c_main.py`, `c_devlogs.py`), du CSS ou du JS :

```bash
python3 -B tools/generateur/build.py   # pages, sitemap, RSS, llms.txt, manifeste + minification CSS/JS (minify.py)
python3 -B tools/generateur/check.py   # JSON-LD, liens internes, H1, alt, longueur des titres et descriptions
```

La minification est faite en Python pur (`tools/generateur/minify.py`, aucune dépendance) ; elle peut aussi être lancée seule : `python3 -B tools/generateur/minify.py`.

## Réseaux officiels

- GitHub : https://github.com/flexarion-officiel
- itch.io : https://flexarionofficiel.itch.io/
- X : https://x.com/flexarion_off
- Instagram : https://www.instagram.com/flexarion.off/

## Déploiement (GitHub Pages)

1. Dépôt `flexarion-officiel/flexarion-officiel.github.io`, branche `main`, contenu à la racine.
2. *Settings → Pages* : source « Deploy from a branch », branche `main`, dossier `/ (root)`.
3. Après publication : déclarer le site dans Google Search Console, soumettre `https://flexarion-officiel.github.io/sitemap.xml` et demander l'indexation des pages principales.

Les PDF de cours (`docs/*.pdf`) sont exclus du dépôt via `.gitignore`.
