# Phase 4 — Netlinking white hat et profils Flexarion

Textes prêts à coller pour créer des profils cohérents autour de **Flexarion** et pointer vers le site officiel `https://flexarion-officiel.github.io/`.

## Règles communes (à respecter partout)

- **White hat uniquement** : un seul profil par plateforme, contenu adapté à chaque réseau (CM3 : « pas dupliquer le même contenu partout »), aucun achat de liens, aucun échange de liens avec les autres groupes du cours, **aucun lien vers un autre site Flexarion**.
- **Cohérence de marque (NAP)** : toujours le même nom « Flexarion », la même localisation « Aix-en-Provence, France », la même date de création (2022), le même logo (`assets/img/flexarion-logo-512.webp` / `icon-512.png`) et la même bannière (`assets/img/flexarion-og-1200x630.jpg`).
- **Transparence** : chaque bio mentionne qu'il s'agit d'un studio fictif / projet étudiant (évite tout signalement pour usurpation et renforce la fiabilité).
- **Ancres naturelles** : varier « Flexarion », « le site du studio Flexarion », « Below Zero », « nos devlogs », plutôt que répéter un mot-clé exact.
- **Liens utiles** :
  - Accueil : https://flexarion-officiel.github.io/
  - Jeu : https://flexarion-officiel.github.io/below-zero/
  - Devlogs : https://flexarion-officiel.github.io/devlogs/
  - Presse : https://flexarion-officiel.github.io/contact/
- Après création de chaque profil : ajouter son URL dans la liste `SOCIALS` de `tools/generateur/build.py` (elle alimente `sameAs`, le pied de page et `llms.txt`) ; la section réseaux de la page contact est dans `c_main.py`. Puis régénérer le site. C'est un signal fort pour Google et les moteurs génératifs.
- Vérifier pour chaque lien s'il est `nofollow` (clic droit → Inspecter). Les liens `nofollow` restent utiles pour la découverte et la notoriété, même s'ils ne transmettent pas d'autorité (CM2).

## Choix des plateformes selon les personas (CM3)

| Persona | Plateformes prioritaires | Contenu attendu |
|---|---|---|
| Léo, 13 ans | YouTube (Shorts), TikTok | Formats courts, « avant / après » d'une action dans le présent et sa conséquence en 2306 |
| Chloé, 16 ans | Discord, Instagram | Lore, fan-arts, théories, artworks de Sextia, sondages de choix narratifs |
| Mehdi, 21 ans | Reddit, X, itch.io / IndieDB, Twitch | Devlogs techniques, systèmes de causalité, discussions de game design |
| Presse / pros | LinkedIn, X, GitHub, Medium / Dev.to | Coulisses du studio, articles d'expertise, code |

Ordre recommandé de création : **GitHub (déjà fait) → itch.io → IndieDB → Dev.to → X → Discord → Instagram → YouTube → LinkedIn → Medium**.

---

## 1. itch.io (page de studio + page de jeu)

**Nom du profil** : Flexarion
**Tagline du jeu** : Sous Aix-en-Provence, une ville de 2306 vous attend. Elle vous connaît déjà.

**Bio du profil (studio)** :
> Flexarion est un studio indépendant de jeux vidéo de science-fiction basé à Aix-en-Provence, fondé en 2022. Nous créons des aventures narratives où chaque décision du joueur transforme l'univers du jeu. Notre premier titre : Below Zero.
> Projet étudiant (BUT Informatique, IUT d'Aix-Marseille) : le studio et son équipe sont fictifs.
> Site officiel : https://flexarion-officiel.github.io/

**Description de la page « Below Zero »** :
> **2156.** Sous le centre historique d'Aix-en-Provence, des techniciens découvrent une cavité immense. À l'intérieur : une ville entière, identique à celle de la surface, mais qui semble appartenir à l'année **2306**.
>
> Vous êtes Sacha Morel, jeune technicien des réseaux souterrains. Les habitants de cette ville du futur vous saluent par votre prénom. Ils se souviennent de choses que vous n'avez pas encore faites.
>
> - Explorez deux époques construites sur le même plan
> - Modifiez le futur par vos actions dans le présent
> - Reliez les indices dans votre Carnet de causalité
> - Aucun combat : seulement des énigmes, des choix et plusieurs fins
>
> Below Zero est en développement. Suivez sa fabrication dans [les devlogs du studio Flexarion](https://flexarion-officiel.github.io/devlogs/) et découvrez l'univers complet sur [la page officielle de Below Zero](https://flexarion-officiel.github.io/below-zero/).
>
> *Projet pédagogique fictif — visuels générés par IA.*

**Tags** : science-fiction, narrative, puzzle, exploration, time-travel, mystery, french
**Statut** : In development

---

## 2. IndieDB (fiche studio + fiche jeu)

**Company / Developer — Résumé** :
> Flexarion — studio indépendant de jeux vidéo de science-fiction narratifs, Aix-en-Provence (France), depuis 2022. Studio fictif créé dans le cadre d'un projet étudiant.

**Company — Description** :
> Flexarion réunit huit métiers autour d'une même idée : la science-fiction la plus troublante se cache sous nos pieds. Nous concevons des jeux où les décisions du joueur influencent directement l'univers, loin des aventures spatiales centrées sur le combat. Notre premier jeu, Below Zero, se déroule dans deux versions d'Aix-en-Provence séparées par cent cinquante ans.
> Plus d'informations sur [le site du studio Flexarion](https://flexarion-officiel.github.io/).

**Game — Below Zero — Summary** :
> Aventure narrative de science-fiction : en 2156, une ville de 2306 est découverte sous Aix-en-Provence. Vos actions dans le présent modifient le futur.

**Premier article IndieDB (reprise adaptée, pas copiée, du devlog #2)** :
> Titre : « Une action, une conséquence : comment fonctionnent les énigmes de Below Zero »
> Résumé de 150-200 mots reformulé + lien final : « Lire le devlog complet sur [le blog de Flexarion](https://flexarion-officiel.github.io/devlogs/enigmes-causalite-temporelle/) ».

---

## 3. GitHub — organisation `flexarion-officiel`

**Display name** : Flexarion
**Description (160 caractères max.)** :
> Studio indépendant de jeux vidéo SF à Aix-en-Provence (projet étudiant). Code source du site officiel — projet étudiant BUT Informatique, IUT d'Aix-Marseille.

**Website** : https://flexarion-officiel.github.io/
**Location** : Aix-en-Provence, France

**Profil README** (dépôt `flexarion-officiel/.github`, fichier `profile/README.md`) :
```markdown
# Flexarion

Studio indépendant de jeux vidéo de science-fiction, Aix-en-Provence — depuis 2022.
Nous créons des aventures narratives où chaque choix modifie l'univers du jeu.

🎮 **Below Zero** — en 2156, une ville de 2306 est découverte sous Aix-en-Provence.
🌐 Site officiel : [flexarion-officiel.github.io](https://flexarion-officiel.github.io/)
📓 Devlogs : [journal de développement](https://flexarion-officiel.github.io/devlogs/)

> Projet pédagogique fictif — BUT Informatique, IUT d'Aix-Marseille.
```

**Dépôt du site — description** : « Site officiel du studio Flexarion (HTML statique, GitHub Pages) » + champ *Website* renseigné + *topics* : `flexarion`, `github-pages`, `seo`, `static-site`, `indie-game`.

---

## 4. LinkedIn — page entreprise

**Nom** : Flexarion
**Slogan (120 car.)** : Studio indépendant de jeux vidéo de science-fiction narratifs, à Aix-en-Provence.
**Secteur** : Développement de jeux vidéo · **Taille** : 2-10 employés · **Siège** : Aix-en-Provence, France · **Fondée en** : 2022
**Site web** : https://flexarion-officiel.github.io/

**À propos** :
> Flexarion est un studio indépendant de jeux vidéo de science-fiction fondé en 2022 à Aix-en-Provence. Pour les amateurs de jeux narratifs, nous créons des expériences immersives où les décisions du joueur influencent directement l'univers du jeu.
>
> Notre premier titre, Below Zero, explore deux versions d'Aix-en-Provence séparées par 150 ans. Game design, level design, sound design, character design : nous partageons nos méthodes dans nos devlogs.
>
> ℹ️ Flexarion est un studio fictif, créé par des étudiants du BUT Informatique de l'IUT d'Aix-Marseille dans le cadre d'un projet de communication digitale.

**Premier post (ton posé, storytelling pro — CM3)** :
> Comment construire deux fois la même ville sans qu'elle devienne un copier-coller ? 🏙️
> Chez Flexarion, nous partons d'un « squelette » unique pour l'Aix de 2156 et la Sextia de 2306, puis chaque époque reçoit son habillage. Résultat : la symétrie devient un outil de navigation, pas seulement un effet de style.
> Nos 5 règles de symétrie sont détaillées dans notre dernier devlog 👉 https://flexarion-officiel.github.io/devlogs/concevoir-deux-villes-aix-2156-2306/
> #gamedev #leveldesign #AixEnProvence #jeuvideo

---

## 5. YouTube — chaîne

**Nom** : Flexarion · **Identifiant** : @flexarion-officiel (ou @flexarionstudio)
**Description de la chaîne** :
> Bienvenue chez Flexarion, studio indépendant de jeux vidéo de science-fiction à Aix-en-Provence.
> Devlogs vidéo, concept arts et coulisses de Below Zero, notre aventure narrative où le présent modifie le futur.
> 🌐 Site officiel : https://flexarion-officiel.github.io/
> 📓 Devlogs écrits : https://flexarion-officiel.github.io/devlogs/
> Projet étudiant fictif (BUT Informatique, IUT d'Aix-Marseille) — visuels générés par IA.

**Liens de la chaîne** : « Site officiel » → accueil ; « Below Zero » → page du jeu.

**Idées de vidéos** : Short 15 s « Tu répares une fontaine en 2156… voici ce qu'elle devient en 2306 » (Léo) ; vidéo 3-5 min « Comment sonne une ville souterraine ? » reprenant le devlog #3 (lien en description vers [le devlog sound design de Flexarion](https://flexarion-officiel.github.io/devlogs/sound-design-ville-souterraine/)).

---

## 6. X (Twitter)

**Nom** : Flexarion · **@** : @flexarion_off
**Bio (160 car.)** :
> Studio indé de jeux vidéo SF à Aix-en-Provence 🛰️ Below Zero : sous la ville, 2306 vous attend. Projet étudiant fictif.

**Localisation** : Aix-en-Provence · **Site** : https://flexarion-officiel.github.io/

**Tweet épinglé** :
> En 2156, on découvre une ville sous Aix-en-Provence.
> Elle est identique à la nôtre. Elle date de 2306.
> Et ses habitants vous connaissent déjà.
> Below Zero, par Flexarion 👇
> https://flexarion-officiel.github.io/below-zero/

---

## 7. Medium et Dev.to

**Bio (les deux)** :
> Flexarion — studio indépendant (fictif) de jeux vidéo SF à Aix-en-Provence. Nous écrivons sur le game design narratif, le level design et le développement web du site du studio.

**Stratégie** : ne **pas** recopier les devlogs (contenu dupliqué). Publier des articles complémentaires, puis renvoyer vers le site :
- **Dev.to** (public tech, Mehdi) : « Construire un site de studio de jeux en HTML pur et viser 100/100 sur Lighthouse » — JSON-LD `VideoGame`, CSS intégré, images WebP responsive. Lien final : « Le résultat : [le site du studio Flexarion](https://flexarion-officiel.github.io/) ».
- **Medium** : « Écrire des énigmes où le présent modifie le futur : 5 leçons de game design » — synthèse originale, lien vers [notre devlog détaillé sur la causalité](https://flexarion-officiel.github.io/devlogs/enigmes-causalite-temporelle/).
- Si une plateforme propose une « URL canonique » (Dev.to et Medium le permettent à l'import), l'utiliser uniquement si l'article reprend un devlog du site.

---

## 8. Discord — serveur communautaire

**Nom du serveur** : Flexarion · Below Zero
**Description** :
> Le QG de la communauté Flexarion 🌌 Théories sur Sextia, fan-arts, coulisses du développement de Below Zero et annonces du studio. Projet étudiant fictif — bienvenue à tous les curieux.

**Salons proposés** : `#annonces` (devlogs, lien vers le site), `#règlement`, `#théories-sextia`, `#fan-arts`, `#choix-et-conséquences` (sondages narratifs), `#devlogs`, `#présentations`.
**Message de bienvenue** :
> Bienvenue sous la surface. Ici, on parle de Below Zero, le jeu narratif du studio Flexarion. Commence par lire l'univers sur https://flexarion-officiel.github.io/below-zero/ puis viens nous dire : à ton avis, pourquoi les habitants de 2306 connaissent-ils Sacha ?

**Charte de modération (CM3)** : respect, pas de spoil hors salon dédié, pas de pub ; réponse sous 24 h ; toute situation sensible remontée à un humain de l'équipe (pas de réponse automatique IA sur ces sujets).

---

## 9. Instagram

**Nom** : Flexarion · **@** : @flexarion.off
**Bio (150 car.)** :
> 🎮 Studio indé de jeux vidéo SF · Aix-en-Provence
> Below Zero : 2156 en haut, 2306 en dessous
> Projet étudiant fictif ↓
**Lien** : https://flexarion-officiel.github.io/ (ou la page du dernier devlog)

**Premières publications (3 à 5 / semaine, CM3)** : carrousel « Aix 2156 / Sextia 2306 » (avant-après des visuels), Reel de 10 s sur le key art, portraits des habitants de 2306 (Mémé Lune, Iléa, Aurèle) avec une question en légende pour susciter des théories, Story sondage « Tu répares la vanne ou tu l'ignores ? ».
**Hashtags** : #Flexarion #BelowZero #IndieGame #GameDev #ScienceFiction #AixEnProvence #ConceptArt

---

## Bonus — autres plateformes à fort potentiel

- **Reddit** (Mehdi) : publier un retour d'expérience de game design dans un subreddit francophone de création de jeux, en respectant ses règles d'autopromotion.
- **TikTok** (Léo) : mêmes formats courts que les YouTube Shorts, ton plus spontané.
- **Annuaires / mentions locales** : présentation du projet sur le site ou les réseaux de l'IUT, si l'enseignant l'autorise (lien thématique et local fort).

## Suivi

| Plateforme | Créé le | URL du profil | Lien vers le site | Ajouté au `sameAs` |
|---|---|---|---|---|
| GitHub | 11/2026 | https://github.com/flexarion-officiel | à vérifier (champ Website) | ✅ |
| LinkedIn | 11/2026 | https://www.linkedin.com/in/flexarion-officiel/ | à vérifier | ✅ |
| itch.io | 11/2026 | https://flexarionofficiel.itch.io/ | à vérifier | ✅ |
| X | 11/2026 | https://x.com/flexarion_off | à vérifier | ✅ |
| Instagram | 11/2026 | https://www.instagram.com/flexarion.off/ | à vérifier | ✅ |
| IndieDB | | | | |
| Dev.to | | | | |
| Medium | | | | |
| Discord | | | | |
| YouTube | | | | |
