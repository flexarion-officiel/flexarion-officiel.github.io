from build import pic, BASE, ORG, LASTMOD, esc
from c_devlogs import ARTICLES, AUTHORS, url as aurl, DATE, DATE_FR
import json

GAME = BASE + "/below-zero/#videogame"

def faq_block(qas, title="Questions fréquentes"):
    html = f'<section class="faq" aria-labelledby="faq"><h2 id="faq">{title}</h2>' + "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qas) + '</section>'
    import re
    ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in qas]}
    return html, ld

def article_cards(lst):
    out = '<div class="grid">'
    for a in lst:
        n, role = AUTHORS[a["author"]]
        out += f'''<article class="card">
{pic(a["img"], a["alt"], sizes="(max-width: 40rem) 92vw, 24rem")}
<h3><a href="{aurl(a)}">{a["short"]}</a></h3>
<p class="meta">Devlog n°{a["num"]} · {n}, {role.lower()}</p>
<p>{a["desc"]}</p>
</article>'''
    return out + '</div>'

PAGES = []

# ---------------- ACCUEIL ----------------
home_faq = [
 ("Qu'est-ce que Flexarion ?", "Flexarion est un studio indépendant de jeux vidéo de science-fiction basé à Aix-en-Provence. Fondé en 2022, il réunit huit personnes et conçoit des jeux narratifs où les décisions du joueur modifient directement l'univers du jeu. Il s'agit d'un studio fictif créé pour un projet étudiant."),
 ("Où se trouve le studio Flexarion ?", "Le studio est installé à Aix-en-Provence, dans les Bouches-du-Rhône (région Provence-Alpes-Côte d'Azur, France). La ville est aussi le décor de son jeu phare, Below Zero."),
 ("Quel est le jeu phare de Flexarion ?", "Son jeu phare s'appelle Below Zero. En 2156, une seconde ville identique à Aix-en-Provence est découverte sous la surface ; elle semble appartenir à l'année 2306. Le joueur incarne un jeune technicien que les habitants du futur connaissent déjà."),
 ("Quel genre de jeu développe Flexarion ?", "Le studio développe des jeux vidéo de science-fiction narratifs : aventure, exploration et énigmes de causalité, sans combat. Chaque action dans le présent peut modifier le futur."),
 ("Quand Flexarion a-t-il été créé ?", "Le studio a été créé en 2022 à Aix-en-Provence, à la suite d'une game jam."),
 ("Combien de personnes travaillent chez Flexarion ?", "L'équipe fictive compte huit personnes : un directeur créatif, deux développeurs, un game designer, une artiste 3D, un character designer, une sound designer et un responsable communication."),
 ("Flexarion est-il un vrai studio ?", "Non. Flexarion est un studio fictif imaginé par quatre étudiants du BUT Informatique de l'IUT d'Aix-Marseille dans le cadre d'un concours pédagogique de référencement. L'équipe et le jeu n'existent pas ; les détails sont dans les mentions légales."),
]
fh, fld = faq_block(home_faq)
cards = article_cards(ARTICLES[:3])
home = f'''
<section class="hero" aria-labelledby="titre">
{pic("flexarion-hero-deux-villes-aix", "Aix-en-Provence au crépuscule et, sous la roche, sa ville jumelle de 2306 illuminée de cyan : l'univers du studio Flexarion", lcp=True, sizes="100vw")}
<div class="hero-txt">
<p class="kicker">Studio de jeux vidéo · Aix-en-Provence</p>
<h1 id="titre">Flexarion, le studio de science-fiction qui creuse sous la réalité</h1>
<p class="lead">Flexarion est un studio indépendant de jeux vidéo de science-fiction fondé en 2022 à Aix-en-Provence. Nous créons des expériences narratives immersives où chacune de vos décisions transforme l'univers du jeu. Et si la ville que vous connaissez par cœur avait une jumelle, deux siècles plus tard, juste sous vos pieds ?</p>
<p><a class="btn" href="/below-zero/">Découvrir Below Zero</a><a class="btn ghost" href="/studio/">Rencontrer le studio</a></p>
</div>
</section>
<div class="wrap">
<section aria-labelledby="positionnement">
<h2 id="positionnement">Ce qui rend Flexarion différent</h2>
<div class="prose">
<p>La plupart des jeux de science-fiction parlent de vaisseaux, de combats et de planètes lointaines. Nous avons choisi une autre voie : <strong>des récits de SF à hauteur humaine, où le joueur ne sauve pas la galaxie mais découvre une vérité</strong>. Nos jeux reposent sur trois piliers.</p>
</div>
<div class="grid">
<div class="card"><h3>Vos choix ont des conséquences</h3><p>Une porte laissée ouverte, une réparation bâclée, une promesse tenue : dans nos jeux, le moindre geste peut se propager et changer le monde. Pas de choix cosmétiques.</p></div>
<div class="card"><h3>Le mystère avant l'action</h3><p>Aucun combat, mais des énigmes, des indices et des personnages qui en savent plus que vous. Nous voulons éveiller la curiosité et faire douter de ce que l'on croit voir.</p></div>
<div class="card"><h3>Une SF ancrée en Provence</h3><p>Nos univers partent de lieux réels : les fontaines, les places et les sources chaudes d'Aix-en-Provence deviennent le décor d'une science-fiction inattendue.</p></div>
</div>
</section>
<section aria-labelledby="jeu">
<h2 id="jeu">Notre jeu phare : Below Zero</h2>
<div class="prose">
<p>En 2156, des travaux sous Aix-en-Provence mettent au jour une seconde ville, identique à celle de la surface, mais qui semble appartenir à l'année 2306. Vous incarnez Sacha Morel, un jeune technicien. Problème : les habitants de cette ville du futur vous connaissent déjà. En explorant les deux époques, vous comprenez qu'elles sont liées et que chaque action dans le présent modifie le futur.</p>
<p><a href="/below-zero/">Explorer l'univers, les mécaniques et les visuels de Below Zero</a></p>
</div>
</section>
<section aria-labelledby="chiffres">
<h2 id="chiffres">Le studio en bref</h2>
<div class="facts"><dl>
<dt>Activité</dt><dd>Studio indépendant de jeux vidéo de science-fiction narratifs</dd>
<dt>Localisation</dt><dd>Aix-en-Provence (13), Provence-Alpes-Côte d'Azur, France</dd>
<dt>Création</dt><dd>2022</dd>
<dt>Équipe</dt><dd>8 personnes</dd>
<dt>Jeu phare</dt><dd><a href="/below-zero/">Below Zero</a> (en développement, PC)</dd>
<dt>Statut</dt><dd>Studio fictif, projet pédagogique du BUT Informatique</dd>
</dl></div>
</section>
<section aria-labelledby="devlogs">
<h2 id="devlogs">Derniers devlogs</h2>
<p class="prose">Notre journal de développement raconte les coulisses de Below Zero, du level design au sound design.</p>
{cards}
<p><a class="btn ghost" href="/devlogs/">Lire tous les devlogs</a></p>
</section>
{fh}
</div>
'''
PAGES.append(dict(path="/", title="Flexarion | Studio de jeux vidéo SF indépendant à Aix-en-Provence",
  ogtitle="Flexarion, studio de jeux vidéo de science-fiction à Aix-en-Provence",
  desc="Flexarion est un studio indépendant de jeux vidéo de science-fiction narratifs basé à Aix-en-Provence depuis 2022, créateur de Below Zero.",
  body=home, jsonld=[fld]))

# ---------------- STUDIO ----------------
team = [
 ("Inès Valcourt", "Directrice créative", "Elle définit l'univers et l'histoire de Below Zero. Ancienne scénariste de théâtre, elle a imaginé la ville souterraine en observant les fontaines d'Aix."),
 ("Théo Marchetti", "Développeur gameplay", "Il programme les mécaniques de jeu et l'éditeur de causalité qui vérifie que chaque énigme a une solution."),
 ("Samira Benali", "Développeuse moteur et outils", "Elle s'occupe du moteur, des performances et du système qui synchronise les deux villes à partir d'un plan unique."),
 ("Lucas Arnaud", "Game designer", "Il imagine les énigmes, les interactions et la boucle « observer, supposer, agir, vérifier »."),
 ("Margaux Delorme", "Artiste 3D environnements", "Elle crée les environnements et les bâtiments d'Aix en 2156 et de Sextia en 2306."),
 ("Yanis Okafor", "Character designer", "Il dessine les personnages, de Sacha Morel aux habitants du futur qui le reconnaissent."),
 ("Élise Fabre", "Sound designer", "Elle compose la musique et crée les effets sonores, de l'eau thermale aux échos de la cavité."),
 ("Raphaël Costa", "Responsable communication", "Il s'occupe de la promotion du studio, des réseaux sociaux et des relations presse."),
]
team_html = "".join(f'<div class="card"><h3>{n}</h3><p class="meta">{r}</p><p>{d}</p></div>' for n, r, d in team)
studio = f'''
<div class="wrap">
<p class="kicker">Le studio</p>
<h1>Le studio Flexarion : huit passionnés de SF à Aix-en-Provence</h1>
<div class="prose">
<p class="lead">Flexarion est né en 2022 d'une conviction simple : la science-fiction la plus troublante n'est pas celle des étoiles lointaines, mais celle qui se cache sous nos pieds. Installé à Aix-en-Provence, notre studio indépendant réunit huit personnes autour d'un même goût pour les récits mystérieux et les choix qui comptent.</p>
</div>
<figure>
{pic("below-zero-key-art", "Key art de Below Zero, le jeu du studio Flexarion : un technicien face à une ville souterraine illuminée", lcp=True)}
<figcaption>Below Zero, le premier jeu de Flexarion (visuel généré par IA).</figcaption>
</figure>
<section class="prose" aria-labelledby="histoire">
<h2 id="histoire">Notre histoire</h2>
<p>Tout commence lors d'une game jam organisée à Aix-en-Provence au printemps 2022. Trois participants, une future directrice créative et deux développeurs, y prototypent en quarante-huit heures un petit jeu où le joueur modifie un objet dans le présent pour en voir l'effet dans le futur. Le prototype est bancal, mais l'idée reste. Quelques mois plus tard, ils fondent Flexarion.</p>
<ol>
<li><strong>2022 :</strong> création du studio Flexarion à Aix-en-Provence par trois fondateurs.</li>
<li><strong>2023 :</strong> premiers prototypes de Below Zero et arrivée d'un game designer et d'une artiste 3D.</li>
<li><strong>2024 :</strong> l'équipe atteint huit personnes avec un character designer, une sound designer et un responsable communication.</li>
<li><strong>2025 :</strong> première tranche jouable de Below Zero couvrant le centre historique d'Aix et de Sextia.</li>
<li><strong>2026 :</strong> ouverture du site officiel et publication des premiers <a href="/devlogs/">devlogs</a>.</li>
</ol>
<h2 id="vision">Notre vision</h2>
<p>Pour les amateurs de jeux vidéo narratifs, Flexarion est le studio de science-fiction qui propose des expériences immersives originales où les décisions du joueur influencent directement l'univers du jeu, là où beaucoup d'aventures de SF privilégient l'action, l'exploration spatiale ou les combats. Nous voulons surprendre, intriguer, et pousser chaque joueur à remettre en question sa perception de la réalité.</p>
<p>Nos jeux s'adressent aussi bien aux collégiens qui découvrent les jeux d'aventure entre amis, qu'aux lycéennes passionnées de lore et d'histoires à choix multiples, ou aux étudiants qui aiment décortiquer des systèmes complexes et des univers dystopiques.</p>
</section>
<section aria-labelledby="equipe">
<h2 id="equipe">L'équipe</h2>
<p class="prose">Huit métiers, une seule obsession : que chaque détail serve le mystère.</p>
<div class="grid">{team_html}</div>
</section>
<section class="prose" aria-labelledby="aix">
<h2 id="aix">Pourquoi Aix-en-Provence ?</h2>
<p>Aix-en-Provence n'est pas seulement l'adresse du studio, c'est notre première source d'inspiration. La ville est née autour de sources d'eau chaude, il y a plus de deux mille ans, sous le nom d'Aquae Sextiae. Ses fontaines, ses places, le cours Mirabeau et la silhouette de la montagne Sainte-Victoire nourrissent directement les décors de nos jeux.</p>
<p>Travailler ici, c'est aussi profiter d'un écosystème vivant : universités, écoles du numérique et communauté régionale du jeu vidéo entre Aix et Marseille. C'est dans cette région que nous recrutons, testons nos prototypes et rencontrons nos premiers joueurs.</p>
<p>Pour découvrir comment la ville se transforme en terrain de jeu, lisez notre <a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">devlog sur la conception des deux villes jumelles</a>, ou plongez dans l'univers de <a href="/below-zero/">Below Zero</a>.</p>
</section>
<p class="note">Flexarion est un studio fictif : l'équipe présentée ci-dessus n'existe pas. Ce site a été réalisé par des étudiants du BUT Informatique de l'IUT d'Aix-Marseille (voir les <a href="/mentions-legales/">mentions légales</a>).</p>
</div>
'''
team_ld = {"@type": "AboutPage", "@id": BASE + "/studio/#about", "url": BASE + "/studio/", "mainEntity": {"@id": ORG}}
PAGES.append(dict(path="/studio/", pagetype="AboutPage", title="Le studio Flexarion : histoire, équipe et Aix-en-Provence",
  desc="L'histoire du studio Flexarion depuis 2022, son équipe de huit personnes et ses racines à Aix-en-Provence, source d'inspiration de Below Zero.",
  body=studio, crumbs=[("/studio/", "Le studio")], image="/assets/img/below-zero-key-art-1280.webp"))

# ---------------- BELOW ZERO ----------------
game_faq = [
 ("Quelle est l'histoire de Below Zero ?", "En 2156, une deuxième ville est découverte sous Aix-en-Provence. Identique à celle de la surface, elle semble appartenir à l'année 2306. Le joueur incarne Sacha Morel, un jeune technicien que les habitants de cette ville du futur connaissent déjà, et doit comprendre le lien entre les deux villes."),
 ("Below Zero est-il un jeu de combat ?", "Non. Below Zero est un jeu d'aventure narratif sans combat, fondé sur l'exploration de deux époques et des énigmes de causalité : chaque action dans le présent peut modifier le futur."),
 ("Sur quelles plateformes sortira Below Zero ?", "Below Zero est développé en priorité pour PC. Les versions consoles sont à l'étude. Aucune date de sortie n'est annoncée."),
 ("Below Zero a-t-il plusieurs fins ?", "Oui. Les actions dites « pivots » modifient durablement la ville de 2306 et orientent l'histoire vers plusieurs fins différentes."),
 ("Qui développe Below Zero ?", "Below Zero est développé par Flexarion, un studio indépendant (fictif) basé à Aix-en-Provence et fondé en 2022."),
]
gfh, gfld = faq_block(game_faq, "Below Zero en questions")
bz = f'''
<div class="wrap">
<p class="kicker">Le jeu phare de Flexarion</p>
<h1>Below Zero : la ville d'en dessous vous attendait</h1>
<figure>
{pic("below-zero-key-art", "Key art de Below Zero par Flexarion : Sacha, technicien à la lampe frontale, découvre la ville souterraine de 2306 dont les habitants l'observent", lcp=True)}
<figcaption>Key art de Below Zero (visuel généré par IA, retravail prévu).</figcaption>
</figure>
<div class="prose">
<p class="lead">Below Zero est le premier jeu de Flexarion : une aventure narrative de science-fiction où l'on explore deux versions d'Aix-en-Provence, séparées par cent cinquante ans et quelques dizaines de mètres de roche. Ici, il n'y a pas d'ennemis à abattre. Seulement une question : pourquoi le futur vous connaît-il déjà ?</p>
</div>
<div class="facts"><dl>
<dt>Genre</dt><dd>Aventure narrative de science-fiction, énigmes</dd>
<dt>Studio</dt><dd>Flexarion (Aix-en-Provence)</dd>
<dt>Mode</dt><dd>Solo</dd>
<dt>Plateforme</dt><dd>PC (consoles à l'étude)</dd>
<dt>Statut</dt><dd>En développement, sortie non annoncée</dd>
<dt>Langue</dt><dd>Français</dd>
</dl></div>
<section class="prose" aria-labelledby="univers">
<h2 id="univers">L'univers : deux Aix, deux siècles</h2>
<p>Nous sommes en 2156. Sous le centre historique d'Aix-en-Provence, des travaux de maintenance sur le réseau des eaux thermales révèlent une cavité immense. À l'intérieur, une ville entière. Mêmes rues, mêmes places, mêmes fontaines que la surface. Mais tout y est différent : les bâtiments sont faits de verre minéral, les platanes sont devenus des colonnes végétales, et les calendriers affichent l'année 2306.</p>
<p>Ses habitants l'appellent Sextia. Ils vivent là, paisiblement, sous un ciel artificiel bleu glacier. Et lorsque Sacha Morel, jeune technicien des réseaux souterrains, y pose le pied pour la première fois, ils le saluent par son prénom.</p>
<blockquote>« Te revoilà, Sacha. Tu as encore oublié la vanne, n'est-ce pas ? »</blockquote>
<p>Sacha n'a jamais vu ces gens. Pourtant, ils se souviennent de lui, de ses gestes, de ses erreurs. En faisant la navette entre les deux villes, il découvre qu'elles sont liées : ce qu'il fait à la surface en 2156 change ce qu'il trouve sous terre en 2306. Résoudre ce mystère, c'est comprendre la vérité sur cette étrange connexion, et sur lui-même.</p>
</section>
<section aria-labelledby="mecaniques">
<h2 id="mecaniques">Les mécaniques de jeu</h2>
<div class="grid">
<div class="card"><h3>Exploration de deux époques</h3><p>Parcourez l'Aix de 2156 et Sextia en 2306, deux villes bâties sur le même plan. Ce que vous apprenez à la surface vous aide à vous orienter sous terre.</p></div>
<div class="card"><h3>Causalité temporelle</h3><p>Réparer, déplacer, donner, laisser faire : vos actions dans le présent transforment la ville du futur. Le Diapason de Sacha vibre près des objets qui « résonnent » entre les époques.</p></div>
<div class="card"><h3>Mémoire des habitants</h3><p>Les habitants de 2306 se souviennent de choses que vous n'avez pas encore faites. Leurs souvenirs sont des indices… ou des pièges.</p></div>
<div class="card"><h3>Carnet de causalité</h3><p>Notez les liens découverts entre les deux villes, testez vos hypothèses et remontez chaque conséquence jusqu'à sa cause.</p></div>
</div>
<div class="prose">
<p>Toutes les énigmes suivent une même boucle : <strong>observer</strong> le futur, <strong>supposer</strong> un lien, <strong>agir</strong> dans le présent, puis <strong>vérifier</strong> la conséquence. Aucune erreur ne bloque la partie : elle rend seulement le chemin plus long, plus étrange ou plus triste. Les actions les plus importantes, dites « pivots », mènent à plusieurs fins. Notre game designer détaille ce système dans le <a href="/devlogs/enigmes-causalite-temporelle/">devlog sur les énigmes de causalité temporelle</a>.</p>
</div>
</section>
<section aria-labelledby="visuels">
<h2 id="visuels">Visuels et concept arts</h2>
<p class="prose">Premières images de recherche de Below Zero. Ces visuels ont été générés avec l'aide d'une IA et seront retravaillés par l'équipe.</p>
<div class="grid">
<figure>{pic("below-zero-capture-causalite", "Capture de travail de Below Zero : la même fontaine dans l'Aix de 2156 et dans Sextia en 2306, reliées par un fil lumineux", sizes="(max-width: 40rem) 92vw, 24rem")}<figcaption>Une même fontaine, deux époques, un fil de causalité.</figcaption></figure>
<figure>{pic("below-zero-concept-place-2306", "Concept art de la grande place souterraine de Sextia en 2306, sous un ciel artificiel bleu glacier", sizes="(max-width: 40rem) 92vw, 24rem")}<figcaption>La grande place de Sextia et son ciel artificiel.</figcaption></figure>
<figure>{pic("below-zero-habitants-2306", "Concept art de trois habitants de Sextia en 2306 qui reconnaissent le héros de Below Zero", sizes="(max-width: 40rem) 92vw, 24rem")}<figcaption>Mémé Lune, Iléa et Aurèle, habitants de 2306.</figcaption></figure>
<figure>{pic("flexarion-hero-deux-villes-aix", "Vue en coupe d'Aix-en-Provence et de sa ville jumelle souterraine de 2306 dans Below Zero", sizes="(max-width: 40rem) 92vw, 24rem")}<figcaption>Aix en surface, Sextia en dessous.</figcaption></figure>
</div>
</section>
<section class="prose" aria-labelledby="coulisses">
<h2 id="coulisses">Dans les coulisses du développement</h2>
<ul>
<li><a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">Comment nous concevons deux villes jumelles à partir d'un seul plan</a></li>
<li><a href="/devlogs/enigmes-causalite-temporelle/">Comment une action dans le présent modifie le futur</a></li>
<li><a href="/devlogs/sound-design-ville-souterraine/">Comment sonne une ville creusée autour de sources chaudes</a></li>
<li><a href="/devlogs/character-design-habitants-futur/">Comment dessiner des personnages qui vous connaissent déjà</a></li>
</ul>
</section>
{gfh}
</div>
'''
vg = {"@type": "VideoGame", "@id": GAME, "name": "Below Zero", "url": BASE + "/below-zero/",
  "description": "Aventure narrative de science-fiction : en 2156, une ville identique à Aix-en-Provence mais datant de 2306 est découverte sous la surface. Le joueur incarne un jeune technicien que les habitants du futur connaissent déjà ; chaque action dans le présent modifie le futur.",
  "image": [BASE + "/assets/img/below-zero-key-art-1280.webp", BASE + "/assets/img/below-zero-capture-causalite-1280.webp", BASE + "/assets/img/below-zero-concept-place-2306-1280.webp"],
  "genre": ["Science-fiction", "Aventure narrative", "Énigmes"], "gamePlatform": "PC", "applicationCategory": "Game",
  "playMode": "SinglePlayer", "inLanguage": "fr", "creativeWorkStatus": "En développement",
  "author": {"@id": ORG}, "publisher": {"@id": ORG}, "creator": {"@id": ORG},
  "gameLocation": [{"@type": "Place", "name": "Aix-en-Provence (2156)"}, {"@type": "Place", "name": "Sextia, ville souterraine (2306)"}],
  "character": [{"@type": "Person", "name": "Sacha Morel", "description": "Jeune technicien des réseaux souterrains, personnage joueur (fictif)"}],
  "keywords": "Below Zero, Flexarion, jeu narratif, science-fiction, Aix-en-Provence, causalité temporelle"}
PAGES.append(dict(path="/below-zero/", title="Below Zero, le jeu de SF narratif du studio Flexarion",
  desc="Below Zero, jeu vidéo de Flexarion : en 2156, une ville de 2306 est découverte sous Aix-en-Provence. Univers, mécaniques de causalité et visuels.",
  body=bz, jsonld=[vg, gfld], crumbs=[("/below-zero/", "Below Zero")], image="/assets/img/below-zero-key-art-1280.webp",
  imgalt="Key art de Below Zero, jeu du studio Flexarion"))

# ---------------- DEVLOGS INDEX ----------------
dv = f'''
<div class="wrap">
<p class="kicker">Journal de développement</p>
<h1>Les devlogs de Flexarion : dans les coulisses de Below Zero</h1>
<div class="prose">
<p class="lead">Chaque devlog de Flexarion ouvre une porte sur la fabrication de Below Zero. Level design, game design, son, personnages : l'équipe raconte ses choix, ses doutes et ses erreurs, métier par métier.</p>
</div>
<h2>Tous les articles</h2>
{article_cards(ARTICLES)}
<p class="prose">Envie de commencer par le jeu lui-même ? La <a href="/below-zero/">page de Below Zero</a> résume l'univers et les mécaniques. Vous pouvez aussi suivre les devlogs grâce au <a href="/devlogs/feed.xml">flux RSS</a>.</p>
</div>
'''
blog = {"@type": "Blog", "@id": BASE + "/devlogs/#blog", "name": "Devlogs Flexarion", "url": BASE + "/devlogs/", "inLanguage": "fr-FR",
  "publisher": {"@id": ORG}, "about": {"@id": GAME},
  "blogPost": [{"@id": BASE + aurl(a) + "#article"} for a in ARTICLES]}
PAGES.append(dict(path="/devlogs/", pagetype="CollectionPage", title="Devlogs Flexarion : le journal de développement de Below Zero",
  desc="Les devlogs du studio Flexarion : conception des deux villes, énigmes de causalité, sound design et character design du jeu Below Zero.",
  body=dv, jsonld=[blog], crumbs=[("/devlogs/", "Devlogs")], image="/assets/img/devlog-deux-villes-1280.webp"))

# ---------------- CONTACT ----------------
ct = f'''
<div class="wrap">
<p class="kicker">Contact &amp; presse</p>
<h1>Contacter Flexarion : presse, partenaires et joueurs</h1>
<div class="prose">
<p class="lead">Une question sur Flexarion ou sur Below Zero, une demande d'interview, une envie de tester le jeu ? Voici comment joindre le studio et où trouver notre kit presse.</p>
<h2 id="ecrire">Nous écrire</h2>
<p>Adresse e-mail du studio : <a id="email" href="/contact/#email" data-u="contact" data-d="flexarion-officiel.github.io">contact [arobase] flexarion-officiel [point] github [point] io</a></p>
<p class="note">Cette adresse fait partie de la fiction : Flexarion est un studio imaginaire et ce courriel n'est pas relevé. L'adresse est masquée aux robots collecteurs et reconstituée dans votre navigateur.</p>
<p>Localisation : Aix-en-Provence (13100), Bouches-du-Rhône, Provence-Alpes-Côte d'Azur, France. Le studio ne reçoit pas de public.</p>
<h2 id="presse">Kit presse</h2>
<h3>Flexarion en quelques lignes</h3>
<blockquote>Flexarion est un studio indépendant de jeux vidéo de science-fiction fondé en 2022 à Aix-en-Provence. Ses huit membres créent des expériences narratives immersives où les décisions du joueur influencent directement l'univers du jeu. Son premier titre, Below Zero, se déroule dans deux versions d'Aix-en-Provence séparées par cent cinquante ans.</blockquote>
<h3>Fiche d'identité</h3>
</div>
<div class="facts"><dl>
<dt>Nom</dt><dd>Flexarion</dd>
<dt>Fondation</dt><dd>2022, Aix-en-Provence</dd>
<dt>Équipe</dt><dd>8 personnes</dd>
<dt>Spécialité</dt><dd>Jeux vidéo de science-fiction narratifs</dd>
<dt>Jeu</dt><dd>Below Zero, aventure narrative (PC, en développement)</dd>
<dt>Contact presse</dt><dd>Raphaël Costa, responsable communication (fictif)</dd>
</dl></div>
<div class="prose">
<h3>Visuels disponibles</h3>
<p>Les visuels ci-dessous peuvent être repris pour illustrer un article sur Flexarion ou Below Zero, avec la mention « Flexarion, visuel généré par IA ».</p>
<ul>
<li><a href="/assets/img/flexarion-logo-512.webp">Logo Flexarion (512 × 512, WebP)</a> · <a href="/favicon.svg">version vectorielle (SVG)</a></li>
<li><a href="/assets/img/below-zero-key-art-1280.webp">Key art de Below Zero (1280 × 720)</a></li>
<li><a href="/assets/img/flexarion-hero-deux-villes-aix-1280.webp">Les deux villes, vue en coupe (1280 × 720)</a></li>
<li><a href="/assets/img/below-zero-capture-causalite-1280.webp">Capture de travail : la fontaine des deux époques (1280 × 720)</a></li>
<li><a href="/assets/img/below-zero-concept-place-2306-1280.webp">Concept art : la grande place de Sextia (1280 × 720)</a></li>
<li><a href="/assets/img/below-zero-habitants-2306-1280.webp">Concept art : habitants de 2306 (1280 × 720)</a></li>
</ul>
<h3>Charte graphique</h3>
<p>Noir profond <code>#071421</code>, bleu nuit <code>#123A58</code>, cyan électrique <code>#19B9D4</code>, bleu glacier <code>#B7DDE8</code>, blanc froid <code>#E8EDF0</code>. Ton : mystérieux, immersif, intrigant.</p>
<h2 id="suivre">Suivre le studio</h2>
<p>Retrouvez le code source de ce site sur <a href="https://github.com/flexarion-officiel">l'organisation GitHub de Flexarion</a>. Pour les coulisses du jeu, lisez nos <a href="/devlogs/">devlogs</a>.</p>
</div>
</div>
'''
cp = {"@type": "ContactPoint", "contactType": "presse", "email": "contact@flexarion-officiel.github.io", "availableLanguage": "fr", "areaServed": "FR"}
PAGES.append(dict(path="/contact/", pagetype="ContactPage", title="Contact et kit presse du studio Flexarion",
  desc="Contacter le studio Flexarion à Aix-en-Provence et télécharger le kit presse de Below Zero : présentation, fiche d'identité, logo et visuels.",
  body=ct, crumbs=[("/contact/", "Contact & presse")],   scripts='<script src="/assets/js/contact.js" defer></script>\n'))

# ---------------- MENTIONS ----------------
ml = '''
<div class="wrap prose">
<h1>Mentions légales du site Flexarion</h1>
<p class="lead">Flexarion est un projet fictif. Ce site a été créé dans le cadre d'un concours de référencement entre groupes d'étudiants du BUT Informatique de l'IUT d'Aix-Marseille.</p>
<h2>Nature fictive du projet</h2>
<ul>
<li>Le studio Flexarion, le jeu Below Zero, leurs personnages et leur histoire sont <strong>entièrement fictifs</strong>.</li>
<li><strong>L'équipe de développement présentée sur ce site n'existe pas</strong> : les noms et les rôles des huit membres sont inventés. Toute ressemblance avec des personnes réelles serait fortuite.</li>
<li>Ce site est un <strong>projet pédagogique</strong> réalisé dans le cadre du module « Plan de communication et webmarketing à l'ère de l'IA » du BUT Informatique, 2e année, de l'IUT d'Aix-Marseille (département Informatique). Il participe à un concours SEO entre groupes d'étudiants autour du mot-clé « Flexarion ».</li>
<li>Aucun produit n'est vendu et aucun service n'est proposé. L'adresse e-mail indiquée sur le site est fictive.</li>
</ul>
<h2>Éditeurs du site</h2>
<p>Ce site est édité, à titre non commercial, par les étudiants suivants, véritables créateurs du projet :</p>
<ul>
<li>BARTAL Manal</li>
<li>CHAIB EDDOUR Kawthar</li>
<li>PETIT Noé</li>
<li>SBEGHEN Alexandre</li>
</ul>
<p>Directeurs de la publication : les étudiants listés ci-dessus. Établissement de rattachement : IUT d'Aix-Marseille, Aix-Marseille Université.</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par GitHub Pages, service de GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis (<a href="https://pages.github.com/">pages.github.com</a>). Le code source est publié sur l'organisation GitHub <a href="https://github.com/flexarion-officiel">flexarion-officiel</a>.</p>
<h2>Usage de l'intelligence artificielle</h2>
<p>Conformément aux consignes du projet, l'usage de l'IA est documenté :</p>
<ul>
<li>Les <strong>visuels</strong> du site (logo, illustrations, concept arts, captures de travail) ont été <strong>générés par intelligence artificielle</strong> et pourront être retravaillés par les étudiants.</li>
<li>Les textes et le code du site ont été produits avec l'assistance d'un agent IA, à partir de l'identité de marque définie par les étudiants.</li>
<li>Le détail des outils et des consignes utilisés est tenu dans le journal d'usage de l'IA du projet (fichier <code>docs/RAPPORT.md</code> du dépôt).</li>
</ul>
<h2>Données personnelles et cookies</h2>
<p>Ce site ne dépose aucun cookie, n'utilise aucun outil de mesure d'audience ni de publicité, et ne collecte aucune donnée personnelle via un formulaire. L'hébergeur GitHub peut enregistrer des journaux techniques (adresse IP notamment) pour des raisons de sécurité, selon sa propre politique de confidentialité.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes et visuels de ce site sont réalisés pour un usage pédagogique. Ils ne peuvent pas être réutilisés à des fins commerciales sans l'accord des étudiants éditeurs. Les noms de lieux réels (Aix-en-Provence, cours Mirabeau, Sainte-Victoire…) ne sont utilisés que comme cadre de fiction.</p>
<h2>Liens</h2>
<p>Conformément au règlement du concours, ce site ne contient aucun lien vers les sites des autres groupes participants.</p>
<p><a href="/">Retour à l'accueil de Flexarion</a></p>
</div>
'''
PAGES.append(dict(path="/mentions-legales/", title="Mentions légales | Flexarion, projet étudiant fictif",
  desc="Mentions légales de Flexarion : projet fictif du BUT Informatique (IUT d'Aix-Marseille), étudiants éditeurs, hébergement GitHub Pages, usage de l'IA.",
  body=ml, crumbs=[("/mentions-legales/", "Mentions légales")]))

# ---------------- 404 ----------------
nf = '''
<div class="wrap prose">
<p class="kicker">Erreur 404</p>
<h1>Cette page n'existe pas… ou pas encore</h1>
<p class="lead">Peut-être existera-t-elle en 2306. En attendant, voici quelques chemins sûrs pour remonter à la surface de Flexarion.</p>
<ul>
<li><a href="/">Accueil du studio Flexarion</a></li>
<li><a href="/below-zero/">Découvrir Below Zero</a></li>
<li><a href="/devlogs/">Lire les devlogs</a></li>
<li><a href="/contact/">Contact &amp; presse</a></li>
</ul>
</div>
'''
PAGES.append(dict(path="/404.html", title="Page introuvable | Flexarion", desc="Cette page du site Flexarion est introuvable. Retrouvez le studio, le jeu Below Zero et les devlogs depuis l'accueil.",
  body=nf, robots="noindex, follow", nocanon=True))
