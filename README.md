# Flexarion — site officiel (projet pédagogique)

Site du studio **Flexarion**, studio indépendant (fictif) de jeux vidéo de science-fiction basé à Aix-en-Provence, et de son jeu phare **Below Zero**.

> ⚠️ **Projet fictif.** Flexarion, Below Zero et l'équipe de 8 personnes présentée sur le site n'existent pas. Ce site est réalisé dans le cadre d'un concours SEO entre groupes du BUT Informatique (2e année) de l'IUT d'Aix-Marseille, module « Plan de communication & webmarketing à l'ère de l'IA ».
>
> Créateurs réels : BARTAL Manal, CHAIB EDDOUR Kawthar, PETIT Noé, SBEGHEN Alexandre.

- Site en ligne : https://flexarion-officiel.github.io/
- Organisation GitHub : https://github.com/flexarion-officiel

## Choix techniques

- HTML5 sémantique statique, **sans framework ni étape de build obligatoire**, servi par GitHub Pages.
- CSS unique (`assets/css/style.css`, ~5 Ko) **intégré dans chaque page** (`<style>`) pour supprimer toute ressource bloquante.
- Zéro JavaScript bloquant : un seul script de 0,3 Ko, différé, sur la page contact (reconstitution de l'adresse e-mail masquée).
- Images WebP en 3 tailles (480 / 960 / 1280 px) avec `srcset`, `width`/`height`, `loading="lazy"` sauf l'image LCP (`fetchpriority="high"`).
- Données structurées JSON-LD : `Organization` + `LocalBusiness` (Aix-en-Provence, coordonnées GPS), `WebSite`, `WebPage`, `BreadcrumbList`, `VideoGame`, `Blog`, `BlogPosting`, `FAQPage`.
- SEO : title / meta description uniques, canonical, Open Graph, Twitter Cards, `sitemap.xml`, `robots.txt`, flux RSS, page 404 personnalisée.
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
├── mentions-legales/           Mentions légales (projet fictif, éditeurs, hébergeur, IA)
├── 404.html
├── assets/css/style.css        Source du CSS (intégré dans les pages)
├── assets/js/contact.js        Obfuscation de l'e-mail
├── assets/img/                 Visuels WebP (générés par IA) + image Open Graph
├── favicon.svg, favicon-32.png, apple-touch-icon.png, icon-192.png, icon-512.png
├── site.webmanifest, sitemap.xml, robots.txt, llms.txt, .nojekyll
├── tools/generateur/           Générateur Python optionnel (régénère toutes les pages)
└── docs/                       RAPPORT.md (journal IA), PHASE4-NETLINKING.md
```

## Modifier le site

Deux options :

1. **Éditer directement** les fichiers `index.html` (simple, mais le CSS et l'en-tête sont dupliqués dans chaque page).
2. **Régénérer** avec le générateur (Python 3, aucune dépendance) : modifier les textes dans `tools/generateur/c_main.py` (pages) ou `c_devlogs.py` (articles), le CSS dans `assets/css/style.css`, puis :

```bash
python3 -B tools/generateur/build.py   # régénère les pages, sitemap, RSS, llms.txt, manifest
python3 -B tools/generateur/check.py   # vérifie JSON-LD, liens internes, H1, alt, titres
```

Penser à mettre à jour `LASTMOD` dans `build.py` à chaque modification de contenu.

## Déploiement (GitHub Pages)

1. Dépôt `flexarion-officiel/flexarion-officiel.github.io`, branche `main`, contenu à la racine.
2. *Settings → Pages* : source « Deploy from a branch », branche `main`, dossier `/ (root)`.
3. Après publication : déclarer le site dans Google Search Console, soumettre `https://flexarion-officiel.github.io/sitemap.xml` et demander l'indexation des pages principales.

Les PDF de cours (`docs/*.pdf`) sont exclus du dépôt via `.gitignore`.

## Règles du concours respectées

White hat uniquement : contenu original, pas de bourrage de mots-clés, pas de cloaking, aucun lien vers les sites des autres groupes.
