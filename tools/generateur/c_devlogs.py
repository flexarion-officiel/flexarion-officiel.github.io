from build import pic, BASE, ORG, LASTMOD, esc

AUTHORS = {
 "ines": ("Inès Valcourt", "Directrice créative"),
 "margaux": ("Margaux Delorme", "Artiste 3D environnements"),
 "lucas": ("Lucas Arnaud", "Game designer"),
 "elise": ("Élise Fabre", "Sound designer"),
 "yanis": ("Yanis Okafor", "Character designer"),
 "theo": ("Théo Marchetti", "Développeur gameplay"),
}

ARTICLES = [
 dict(slug="concevoir-deux-villes-aix-2156-2306", num=1, date="2026-11-17T09:00:00+01:00", date_fr="17 novembre 2026", rss="Tue, 17 Nov 2026 09:00:00 +0100", img="devlog-deux-villes", author="margaux",
  title="Devlog #1 : deux villes jumelles, 2156 et 2306 | Flexarion",
  h1="Devlog #1 : concevoir deux villes jumelles, Aix 2156 et Sextia 2306",
  short="Concevoir deux villes jumelles",
  desc="Flexarion dévoile comment son équipe bâtit l'Aix de 2156 et sa jumelle souterraine Sextia en 2306 : plans superposés et règles de symétrie.",
  alt="Deux plans superposés de la même ville, l'un à l'encre sépia, l'autre en hologramme cyan, sur la table de travail de Flexarion"),
 dict(slug="enigmes-causalite-temporelle", num=2, date="2026-11-17T10:00:00+01:00", date_fr="17 novembre 2026", rss="Tue, 17 Nov 2026 10:00:00 +0100", img="devlog-causalite", author="lucas",
  title="Devlog #2 : causalité temporelle en jeu vidéo | Flexarion",
  h1="Devlog #2 : le présent modifie le futur, nos énigmes de causalité",
  short="Les énigmes de causalité temporelle",
  desc="Chez Flexarion, le game designer explique comment, dans le jeu vidéo Below Zero, une action dans l'Aix de 2156 transforme la ville de 2306.",
  alt="Graphe lumineux reliant une clé, une graine, une lanterne et une porte entre deux lignes temporelles"),
 dict(slug="sound-design-ville-souterraine", num=3, date="2026-11-17T11:00:00+01:00", date_fr="17 novembre 2026", rss="Tue, 17 Nov 2026 11:00:00 +0100", img="devlog-son", author="elise",
  title="Devlog #3 : le sound design de Sextia | Flexarion",
  h1="Devlog #3 : écouter sous la ville, le sound design de Sextia",
  short="Le sound design de la ville souterraine",
  desc="Chez Flexarion, la sound designer raconte comment l'eau thermale, l'écho et des cigales mutées font sonner la ville souterraine de Below Zero.",
  alt="Micro et casque posés dans un tunnel de pierre où des ondes sonores cyan se propagent vers une ville lointaine"),
 dict(slug="character-design-habitants-futur", num=4, date="2026-11-17T12:00:00+01:00", date_fr="17 novembre 2026", rss="Tue, 17 Nov 2026 12:00:00 +0100", img="devlog-personnages", author="yanis",
  title="Devlog #4 : dessiner les habitants de 2306 | Flexarion",
  h1="Devlog #4 : ils vous connaissent déjà, dessiner les habitants de 2306",
  short="Le character design des habitants de 2306",
  desc="Chez Flexarion, le character designer dévoile comment il dessine, du croquis au modèle 3D, des habitants du futur qui reconnaissent le joueur.",
  alt="Carnet de croquis ouvert montrant l'évolution d'un visage futuriste jusqu'à un portrait aux marques cyan"),
 dict(slug="concevoir-sextia-vrai-aix", num=5, date="2026-11-22T18:00:00+01:00", date_fr="22 novembre 2026", rss="Sun, 22 Nov 2026 18:00:00 +0100", img="devlog-sextia-aix", author="elise",
  title="Devlog #5 : une ville de jeu vidéo née d'Aix | Flexarion",
  h1="Devlog #5 : concevoir Sextia à partir du vrai Aix-en-Provence",
  short="Concevoir Sextia à partir du vrai Aix",
  desc="Chez Flexarion, voyez comment le vrai Aix-en-Provence (cours Mirabeau, Rotonde, thermes Sextius) inspire Sextia en 2306 dans Below Zero.",
  alt="Vue en coupe entre Aix-en-Provence au crépuscule, avec la fontaine de la Rotonde et le cours Mirabeau, et sa jumelle souterraine Sextia de 2306 illuminée de cyan"),
 dict(slug="accessibilite-rythme-jeu-sans-combat", num=6, date="2026-11-22T19:00:00+01:00", date_fr="22 novembre 2026", rss="Sun, 22 Nov 2026 19:00:00 +0100", img="devlog-accessibilite-rythme", author="theo",
  title="Devlog #6 : accessibilité et jeu sans combat | Flexarion",
  h1="Devlog #6 : accessibilité et rythme d'un jeu sans combat",
  short="Accessibilité et rythme d'un jeu sans combat",
  desc="Dans Below Zero de Flexarion, sans combat, Théo Marchetti explique comment le Diapason, Sacha Morel et l'accessibilité tiennent le rythme.",
  alt="Sacha Morel avec sa lampe frontale et son Diapason émettant des ondes cyan vers une fontaine thermale de Sextia, devant des habitants silencieux"),
 dict(slug="creer-studio-jeu-video-aix", num=7, date="2026-11-24T15:00:00+01:00", date_fr="24 novembre 2026", rss="Tue, 24 Nov 2026 15:00:00 +0100", img="devlog-studio-aix", author="ines",
  title="Devlog #7 : créer un studio de jeu vidéo à Aix | Flexarion",
  h1="Devlog #7 : créer un studio de jeu vidéo indépendant à Aix-en-Provence",
  short="Créer un studio de jeu vidéo indépendant à Aix",
  desc="Inès Valcourt, directrice créative de Flexarion, raconte la création du studio de jeu vidéo indépendant à Aix-en-Provence et son choix de la SF.",
  alt="Le studio de jeu vidéo Flexarion à Aix-en-Provence à la tombée de la nuit : l'équipe travaille sur des écrans cyan montrant une ville souterraine, devant une fenêtre ouverte sur les toits d'Aix et la Sainte-Victoire"),
]
# Les 4 devlogs ont été publiés le 17/11/2026 : l'heure de publication (réelle, échelonnée)
# départage l'ordre. Affichage : du plus récent au plus ancien
ARTICLES.sort(key=lambda a: a["date"], reverse=True)
DATE = ARTICLES[0]["date"]  # date du devlog le plus récent
DATE_FR = ARTICLES[0]["date_fr"]
MOD = "2026-11-24"
MOD_FR = "24 novembre 2026"

def url(a): return f"/devlogs/{a['slug']}/"

BODIES = {}

BODIES[1] = """
<p class="lead">Chez Flexarion, nous avons une contrainte de départ un peu folle : construire deux fois la même ville. Une fois en 2156, à la surface d'Aix-en-Provence. Une seconde fois en 2306, à plusieurs dizaines de mètres sous nos pieds. Dans <a href="/below-zero/">Below Zero</a>, ces deux villes doivent se ressembler au point de troubler le joueur, tout en restant immédiatement distinguables. Voici comment nous nous y prenons.</p>

<nav class="toc" aria-label="Sommaire de l'article"><strong>Au sommaire</strong><ol>
<li><a href="#un-seul-plan">Un seul plan pour deux villes</a></li>
<li><a href="#aix-2156">Aix 2156 : une ville familière, mais fatiguée</a></li>
<li><a href="#sextia-2306">Sextia 2306 : la même ville, deux siècles plus tard</a></li>
<li><a href="#regles">Nos cinq règles de symétrie</a></li>
<li><a href="#lisibilite">Le piège de la lisibilité</a></li>
<li><a href="#suite">Et maintenant ?</a></li>
</ol></nav>

<h2 id="un-seul-plan">Un seul plan pour deux villes</h2>
<p>La première décision a été la plus structurante : les deux villes partagent un seul et même plan. Nous ne dessinons pas une Aix-en-Provence puis une copie futuriste ; nous dessinons un squelette commun, une sorte de « carte maîtresse », à partir de laquelle chaque époque est habillée. Ce squelette contient les rues, les places, les fontaines, les volumes des bâtiments et, surtout, les points d'ancrage : les endroits précis où le joueur pourra plus tard constater qu'une action dans le présent a modifié le futur.</p>
<p>Concrètement, dans notre moteur, chaque bâtiment existe sous la forme d'un « gabarit » neutre. Un gabarit, c'est un volume, une emprise au sol, des ouvertures et une hauteur. Sur ce gabarit, nous posons deux habillages : l'habillage 2156, en pierre de Bibémus, volets écaillés et câbles apparents, puis l'habillage 2306, en verre minéral, structures porteuses lumineuses et végétation contrôlée. Si un gabarit change, les deux villes changent en même temps. C'est la garantie technique que la ressemblance ne se dégradera pas au fil des mois de production.</p>
<p>Cette méthode a un coût. Elle nous interdit certaines libertés : impossible d'ajouter une tour spectaculaire dans Sextia si elle n'a pas d'équivalent à la surface. Mais c'est précisément cette contrainte qui rend le jeu dérangeant. Quand le joueur reconnaît la forme d'une place qu'il vient de traverser, avec deux siècles d'écart, quelque chose se fige dans son esprit. C'est l'émotion que nous cherchons.</p>

<h2 id="aix-2156">Aix 2156 : une ville familière, mais fatiguée</h2>
<p>Pour la ville de surface, nous sommes partis de ce que nous voyons tous les jours depuis nos bureaux aixois : les façades ocre, les platanes du cours Mirabeau, les fontaines moussues, la silhouette de la cathédrale Saint-Sauveur, la Sainte-Victoire à l'horizon. Nous ne voulions pas d'une reconstitution touristique. L'Aix de 2156 est une ville qui a traversé les canicules et les restrictions d'eau du XXIIe siècle. Les platanes sont soutenus par des tuteurs métalliques, les fontaines sont souvent à sec, et les réseaux techniques ont été ajoutés en surface, faute de pouvoir creuser davantage.</p>
<p>Ce dernier détail n'est pas anodin. Sacha Morel, le personnage que l'on incarne, est technicien de maintenance des réseaux souterrains. Son métier justifie qu'il connaisse chaque regard d'égout, chaque canalisation, chaque vieille galerie. Le level design de la surface est donc pensé « à hauteur de technicien » : on lit la ville par ses tuyaux, ses armoires électriques et ses plaques de fonte autant que par ses monuments.</p>
<p>Nous avons aussi choisi une lumière précise : une fin de journée d'été, chaude, légèrement voilée par la poussière. Cette palette chaude est importante, car elle s'oppose frontalement à celle de la ville souterraine.</p>

<h2 id="sextia-2306">Sextia 2306 : la même ville, deux siècles plus tard</h2>
<p>La ville souterraine porte un nom que les habitants emploient sans l'expliquer : Sextia, en écho à Aquae Sextiae, le nom antique d'Aix. Elle occupe une cavité immense, creusée autour des sources thermales qui ont fait la réputation de la ville depuis l'Antiquité. Le plafond de la cavité imite un ciel, grâce à des panneaux de lumière bleu glacier, et les bâtiments reprennent exactement les gabarits de la surface, mais avec des matériaux qui n'existent pas encore en 2156.</p>
<p>Notre règle était simple à énoncer et difficile à tenir : rien dans Sextia ne doit être gratuitement futuriste. Chaque élément doit pouvoir s'expliquer comme l'évolution logique de son équivalent de surface. La fontaine de la Rotonde n'est plus en pierre, mais elle est toujours une fontaine, au même endroit, avec le même nombre de vasques. Les platanes sont devenus des colonnes végétales qui filtrent l'air, mais ils sont alignés exactement comme sur le cours. Le joueur doit pouvoir se dire : « je connais cet endroit », avant de se demander : « mais comment est-ce possible ? »</p>
<p>La palette, elle, bascule vers le froid : bleu nuit, cyan électrique, reflets glacier. Ce n'est pas qu'une question d'esthétique. La température des couleurs est notre premier outil pour que le joueur sache en une fraction de seconde dans quelle époque il se trouve, même sur une capture d'écran.</p>

<figure>
""" + pic("below-zero-concept-place-2306", "Concept art de Flexarion : grande place souterraine de Sextia en 2306, sous un ciel artificiel de panneaux lumineux") + """
<figcaption>Concept art de la grande place de Sextia. Les terrasses reprennent les gabarits des immeubles de surface.</figcaption>
</figure>

<h2 id="regles">Nos cinq règles de symétrie</h2>
<p>Au bout de quelques semaines de prototypage, nous avons formalisé cinq règles, affichées au mur du studio. Elles guident toutes les décisions d'environnement.</p>
<ol>
<li><strong>Même squelette, deux peaux.</strong> Aucune rue, aucun volume ne peut exister dans une seule époque, sauf exception scénarisée et validée par la direction créative.</li>
<li><strong>La chaleur en haut, le froid en bas.</strong> Les teintes chaudes appartiennent à 2156, les teintes froides à 2306. Les rares exceptions sont des indices.</li>
<li><strong>Chaque monument a une descendance.</strong> Quand un lieu de surface est important pour l'histoire, nous écrivons en une phrase ce qu'il est devenu en 2306 et pourquoi.</li>
<li><strong>Les ancrages se voient de loin.</strong> Un point d'ancrage causal doit être visible depuis au moins deux rues dans chaque ville, pour que le joueur puisse le repérer avant de s'en approcher.</li>
<li><strong>Le joueur ne doit jamais se perdre deux fois.</strong> S'il apprend à s'orienter à la surface, ce savoir doit lui servir sous terre. La symétrie est une aide à la navigation, pas seulement un effet de style.</li>
</ol>

<h2 id="lisibilite">Le piège de la lisibilité</h2>
<p>Nos premiers tests ont révélé un problème que nous n'avions pas anticipé. À force de rendre les deux villes semblables, certains testeurs ne savaient plus s'ils étaient à la surface ou dans Sextia, surtout dans les ruelles étroites où le ciel est peu visible. Le trouble était là, mais il devenait de la confusion, et la confusion n'est pas une émotion intéressante.</p>
<p>Nous avons corrigé cela avec trois signaux redondants : la température de couleur déjà évoquée, une signature sonore propre à chaque époque (notre sound designer en parle dans le <a href="/devlogs/sound-design-ville-souterraine/">devlog consacré au son de la ville souterraine</a>) et un petit détail d'interface, la date affichée sur l'outil de Sacha. Un joueur attentif n'a besoin que d'un seul de ces signaux ; un joueur distrait en a toujours au moins un sous les yeux.</p>
<p>Ce travail sur la lisibilité nous a aussi appris à doser le mystère. Le jeu doit poser des questions, mais jamais sur des choses que le joueur devrait savoir pour avancer. On peut s'interroger sur l'origine de Sextia ; on ne doit pas s'interroger sur l'endroit où l'on se trouve.</p>

<h2 id="suite">Et maintenant ?</h2>
<p>Le squelette commun couvre aujourd'hui le centre historique, du cours Mirabeau au quartier de la cathédrale. La prochaine étape concerne les galeries qui relient les deux villes : un espace intermédiaire où les époques se mélangent et où nos règles de symétrie seront volontairement bousculées. C'est aussi là que se cachent les énigmes les plus retorses, dont le principe est expliqué dans le <a href="/devlogs/enigmes-causalite-temporelle/">devlog sur nos énigmes de causalité temporelle</a>.</p>
<p>Si vous découvrez Flexarion avec cet article, la page <a href="/below-zero/">consacrée à Below Zero</a> présente l'univers et les mécaniques du jeu, et la page <a href="/studio/">Le studio</a> vous dit qui se cache derrière ces deux villes.</p>
"""

BODIES[2] = """
<p class="lead">« Chaque action réalisée dans le présent peut modifier le futur. » Cette phrase résume la promesse de <a href="/below-zero/">Below Zero</a>, et c'est aussi la phrase qui a donné le plus de nuits blanches à l'équipe de game design de Flexarion. Promettre que tout compte, c'est facile. Le faire sans transformer le jeu en chaos ingérable, c'est une autre affaire.</p>

<nav class="toc" aria-label="Sommaire de l'article"><strong>Au sommaire</strong><ol>
<li><a href="#principe">Le principe : une action, une conséquence visible</a></li>
<li><a href="#exemple">Un exemple concret : la fontaine des Quatre-Dauphins</a></li>
<li><a href="#graphe">Le graphe de causalité</a></li>
<li><a href="#memoire">Quand les habitants se souviennent avant vous</a></li>
<li><a href="#erreurs">Ce que nous avons raté (et corrigé)</a></li>
<li><a href="#conclusion">Ce que nous retenons</a></li>
</ol></nav>

<h2 id="principe">Le principe : une action, une conséquence visible</h2>
<p>Dans Below Zero, le joueur incarne Sacha Morel, un jeune technicien qui circule entre l'Aix-en-Provence de 2156 et Sextia, la ville souterraine de 2306. La mécanique centrale tient en une règle : ce que Sacha fait à la surface laisse une trace dans la ville du futur. Réparer une canalisation, déplacer un objet, confier un message à quelqu'un, laisser une porte ouverte… tout peut se propager deux siècles plus tard.</p>
<p>Mais « tout » ne veut pas dire « n'importe quoi ». Nous avons distingué trois catégories d'actions. Les <strong>actions décoratives</strong> n'ont aucun effet sur le futur : ramasser une canette, s'asseoir sur un banc. Les <strong>actions d'ancrage</strong> produisent un changement visible et localisé dans Sextia. Enfin, les <strong>actions pivots</strong>, rares, modifient durablement la ville du futur et orientent l'histoire vers l'une des fins possibles.</p>
<p>La distinction est essentielle pour le joueur. S'il pensait que chaque geste anodin pouvait bouleverser le futur, il serait paralysé. Nous signalons donc les ancrages grâce au Diapason, l'outil de Sacha, qui vibre doucement quand un objet « résonne » avec son équivalent de 2306.</p>

<h2 id="exemple">Un exemple concret : la fontaine des Quatre-Dauphins</h2>
<p>Prenons une énigme du premier chapitre, volontairement simple. Dans Sextia, une place est plongée dans le noir : la fontaine centrale, qui alimentait autrefois l'éclairage du quartier grâce à un circuit hydraulique, est sèche. Un habitant explique à Sacha que « la fontaine s'est tue il y a cent cinquante ans, quand le technicien a oublié la vanne ».</p>
<p>Le joueur remonte à la surface. Dans l'Aix de 2156, la fontaine équivalente fonctionne encore, mais une vanne de maintenance fuit. Sacha peut la réparer correctement, la réparer à la hâte ou l'ignorer. S'il la répare correctement, la place de 2306 sera illuminée lors de sa prochaine descente. S'il bâcle la réparation, elle clignotera, et un nouvel indice apparaîtra. S'il l'ignore, la place restera dans le noir et il devra trouver un autre chemin.</p>
<p>Cette petite énigme contient déjà tout le vocabulaire du jeu : une observation dans le futur, une hypothèse, une action dans le présent, puis la vérification de la conséquence. Nous l'appelons la <strong>boucle observer, supposer, agir, vérifier</strong>. Toutes les énigmes de Below Zero sont des variations de cette boucle.</p>

<figure>
""" + pic("below-zero-capture-causalite", "Capture de travail de Below Zero : la même fontaine en 2156 et en 2306, reliées par un fil de lumière") + """
<figcaption>Capture de travail : la même fontaine dans les deux époques, reliée par un fil de causalité.</figcaption>
</figure>

<h2 id="graphe">Le graphe de causalité</h2>
<p>Côté production, chaque énigme est décrite dans un graphe. Chaque nœud représente un état du monde (« vanne réparée », « place éclairée »), chaque arête une relation de cause à effet. Notre développeur gameplay a construit un petit éditeur qui vérifie automatiquement deux propriétés : aucune boucle impossible (un effet ne peut pas être sa propre cause) et aucune impasse (depuis n'importe quel état, il existe au moins un chemin vers la suite de l'histoire).</p>
<p>Ce deuxième point était un vrai risque. Dans un jeu où le présent modifie le futur, il est tentant de punir le joueur en lui fermant des portes. Nous avons décidé que Below Zero ne bloquerait jamais une partie. Une erreur peut rendre le chemin plus long, plus étrange ou plus triste, mais jamais impossible. C'est une décision de design autant qu'une décision éthique : nous voulons que le joueur ose expérimenter.</p>
<p>Le joueur, lui, ne voit pas ce graphe technique. Il dispose du Carnet de causalité, un journal où Sacha note les liens qu'il a découverts. Les liens confirmés sont tracés en cyan, les hypothèses en pointillés. Remplir ce carnet est une récompense en soi, et beaucoup de testeurs nous ont dit y passer plus de temps que prévu, à relier des indices comme un enquêteur.</p>

<h2 id="memoire">Quand les habitants se souviennent avant vous</h2>
<p>La mécanique la plus singulière de Below Zero est aussi celle qui sert le mieux le mystère : les habitants de 2306 connaissent Sacha. Ils se souviennent de choses qu'il n'a pas encore faites. Un vieil archiviste le remercie pour une lettre qu'il n'a jamais écrite. Une conductrice de tram lui reproche une porte qu'il n'a pas encore fermée.</p>
<p>Pour le game design, ces souvenirs sont des indices déguisés. Ils indiquent au joueur ce qu'il est censé faire, ou ce qu'il pourrait faire, sans jamais le formuler comme un objectif classique. Ils créent aussi une tension narrative : faut-il accomplir ce que le futur attend, ou tenter de s'y soustraire ? Les deux options sont jouables, et c'est là que les fins divergent. Notre character designer détaille dans le <a href="/devlogs/character-design-habitants-futur/">devlog sur le design des habitants de 2306</a> comment leurs visages trahissent cette familiarité troublante.</p>

<h2 id="erreurs">Ce que nous avons raté (et corrigé)</h2>
<p>Notre premier prototype proposait une vingtaine d'ancrages dès le premier quartier. Résultat : les testeurs couraient d'un objet à l'autre, déclenchaient des changements sans les comprendre, et finissaient par ignorer le futur. Nous avons divisé ce nombre par trois et ajouté un temps de pause : quand Sacha redescend dans Sextia, une courte séquence met en scène le changement provoqué. Le joueur voit la conséquence avant de reprendre le contrôle.</p>
<p>Nous avions aussi sous-estimé l'importance du retour en arrière. Les joueurs veulent comprendre ce qui s'est passé, pas seulement le constater. Le Carnet de causalité permet donc désormais de « rejouer » mentalement une chaîne : on sélectionne un changement du futur, et le carnet remonte jusqu'à l'action qui l'a provoqué.</p>

<h2 id="conclusion">Ce que nous retenons</h2>
<p>Concevoir des énigmes de causalité, c'est concevoir une conversation entre deux époques. Le joueur doit toujours avoir une question en tête, un moyen d'y répondre, et une preuve visible de sa réponse. Le reste, l'étrangeté, l'inquiétude, la sensation que le futur vous observe, vient naturellement quand cette conversation est bien rythmée.</p>
<p>Pour comprendre comment ces deux époques sont construites visuellement, lisez notre <a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">devlog sur la conception des deux villes</a>. Et pour une vue d'ensemble du projet, rendez-vous sur la <a href="/below-zero/">page de Below Zero</a>.</p>
"""

BODIES[3] = """
<p class="lead">On imagine souvent qu'un jeu de science-fiction doit sonner « électronique ». Pour la ville souterraine de <a href="/below-zero/">Below Zero</a>, nous avons pris le contre-pied : Sextia sonne d'abord comme une grotte habitée, pleine d'eau, de pierre et de souvenirs. Je suis la sound designer de Flexarion, et voici comment nous construisons, son par son, l'identité acoustique des deux villes.</p>

<nav class="toc" aria-label="Sommaire de l'article"><strong>Au sommaire</strong><ol>
<li><a href="#deux-signatures">Deux villes, deux signatures sonores</a></li>
<li><a href="#eau">L'eau comme fil conducteur</a></li>
<li><a href="#reverb">Sculpter la réverbération d'une cavité</a></li>
<li><a href="#voix">Les voix des habitants</a></li>
<li><a href="#musique">Une musique qui se souvient</a></li>
<li><a href="#accessibilite">Le son au service de l'accessibilité</a></li>
</ol></nav>

<h2 id="deux-signatures">Deux villes, deux signatures sonores</h2>
<p>Le premier rôle du son, dans Below Zero, est de dire au joueur où il se trouve. Comme notre artiste 3D l'explique dans le <a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">devlog sur la conception des deux villes</a>, les deux époques partagent le même plan. Les yeux peuvent hésiter ; les oreilles, elles, ne doivent jamais se tromper.</p>
<p>À la surface, en 2156, l'ambiance est sèche et ouverte. On entend des cigales, beaucoup, parfois trop, car l'été dure plus longtemps qu'aujourd'hui. On entend aussi les ventilateurs des façades, les drones de livraison qui passent haut, et le grésillement des câbles électriques ajoutés à la hâte. Les sons rebondissent peu : l'espace respire.</p>
<p>Dans Sextia, en 2306, tout est enveloppé. Le moindre pas revient en écho, l'eau circule partout, et un bourdonnement très grave, à peine audible, rappelle que l'on est sous des dizaines de mètres de roche. Ce bourdonnement est devenu la signature de la ville souterraine. En test, plusieurs joueurs nous ont dit qu'ils le « sentaient » plus qu'ils ne l'entendaient, ce qui était exactement l'objectif.</p>

<h2 id="eau">L'eau comme fil conducteur</h2>
<p>Aix-en-Provence est une ville d'eau. Ses fontaines, ses sources chaudes et ses anciens thermes sont au cœur de son histoire depuis l'époque romaine. Il était naturel que l'eau devienne le fil conducteur sonore du jeu. En surface, elle est rare : une fontaine qui coule encore est un événement, et nous la mixons légèrement plus fort que la réalité pour attirer l'attention du joueur.</p>
<p>Sous terre, l'eau est omniprésente, mais domestiquée. Elle circule dans des conduits de verre, ruisselle le long des façades végétalisées et alimente l'éclairage de certains quartiers. Pour la créer, nous avons enregistré de l'eau dans des conditions très différentes : robinets, canalisations de cave, gouttes dans un seau métallique, et même le bruit d'un aquarium. Les enregistrements sont ensuite superposés et filtrés pour obtenir une texture à la fois familière et légèrement irréelle.</p>
<p>L'eau joue aussi un rôle de gameplay. Quand Sacha répare une canalisation dans le présent, le son de l'eau change dans le futur : un filet devient une cascade, un silence devient un murmure. Le joueur entend parfois la conséquence de son action avant de la voir, et ce décalage crée un petit frisson que nous aimons beaucoup.</p>

<h2 id="reverb">Sculpter la réverbération d'une cavité</h2>
<p>La réverbération est le son de l'espace lui-même. Pour Sextia, une réverbération unique aurait été monotone et peu crédible. Nous avons donc découpé la ville en zones acoustiques : grandes places sous la voûte, ruelles étroites, intérieurs habités, galeries techniques. Chaque zone a ses propres paramètres de durée, de densité et de couleur.</p>
<p>Pour trouver ces réglages, nous avons fait ce que fait tout studio indépendant avec peu de moyens : nous sommes allés écouter. Parkings souterrains, caves voûtées, passages couverts du centre ancien, tunnels piétons… Nous avons enregistré des claquements de mains et des réponses impulsionnelles simples, puis nous nous en sommes inspirés pour régler nos réverbérations numériques. Le but n'était pas de reproduire un lieu réel, mais de comprendre comment la pierre, le béton ou le métal « colorent » un son.</p>
<p>Il y a une exception volontaire : les points d'ancrage causaux. À proximité, la réverbération se modifie subtilement et intègre un écho inversé, comme si le son revenait avant d'avoir été émis. C'est un indice auditif discret qui accompagne la vibration du Diapason, l'outil de Sacha.</p>

<figure>
""" + pic("below-zero-key-art", "Key art de Below Zero : Sacha, technicien à la lampe frontale, face à la ville souterraine illuminée et à ses habitants") + """
<figcaption>Dans cette scène, le silence relatif de l'escalier contraste avec la rumeur de la ville qui monte de la cavité.</figcaption>
</figure>

<h2 id="voix">Les voix des habitants</h2>
<p>Les habitants de Sextia parlent français, mais un français qui a évolué pendant deux siècles. Nous avons travaillé avec la direction créative pour définir quelques tournures, quelques mots nouveaux et une intonation légèrement plus chantante, héritée du parler provençal. L'objectif n'est pas de rendre les dialogues difficiles à comprendre, mais de faire sentir une distance.</p>
<p>Côté traitement, les voix de 2306 reçoivent un léger effet de proximité : on a l'impression qu'elles sont toujours un peu trop près, un peu trop intimes. C'est cohérent avec le récit, puisque ces personnages connaissent Sacha mieux qu'il ne se connaît lui-même. Notre character designer revient sur cette familiarité dans le <a href="/devlogs/character-design-habitants-futur/">devlog consacré aux habitants du futur</a>.</p>

<h2 id="musique">Une musique qui se souvient</h2>
<p>La bande originale repose sur un principe simple : chaque thème existe en deux versions. La version de surface est jouée avec des instruments acoustiques, guitare, piano un peu désaccordé, galoubet et tambourin pour un clin d'œil provençal. La version de Sextia reprend les mêmes mélodies avec des synthétiseurs analogiques, des nappes lentes et des voix traitées.</p>
<p>Lors des transitions entre les deux villes, la musique ne se coupe pas : elle se transforme. Une mélodie commencée à la guitare dans l'Aix de 2156 se termine en nappe électronique dans Sextia. Le joueur traverse les époques sans rupture, ce qui renforce l'idée que les deux villes sont une seule et même ville, séparée par le temps.</p>

<h2 id="accessibilite">Le son au service de l'accessibilité</h2>
<p>Parce que le son porte des informations de gameplay, nous devons penser aux joueurs qui ne l'entendent pas, ou mal. Chaque indice sonore important a donc un équivalent visuel : sous-titres détaillés, indicateurs de direction pour les sons d'ancrage, et une option qui affiche les changements d'ambiance à l'écran. À l'inverse, nous travaillons à rendre les menus et le Carnet de causalité lisibles par des descriptions audio.</p>
<p>Le sound design de Below Zero est encore en chantier, et une partie des sons actuels sont des maquettes. Mais l'identité est posée : une surface brûlante et sèche, une profondeur humide et enveloppante, et entre les deux, l'eau qui relie tout. Pour découvrir les autres facettes du jeu, la <a href="/below-zero/">page de Below Zero</a> présente l'univers complet, et notre <a href="/devlogs/enigmes-causalite-temporelle/">devlog sur les énigmes de causalité</a> explique comment le son s'intègre aux énigmes.</p>
"""

BODIES[4] = """
<p class="lead">Dans <a href="/below-zero/">Below Zero</a>, les habitants de la ville souterraine de 2306 reconnaissent le héros. Ils lui sourient, l'appellent par son prénom, lui parlent de souvenirs communs qu'il n'a pas encore vécus. Mon travail de character designer chez Flexarion consiste à rendre cette familiarité crédible et inquiétante dès le premier regard, avant même le premier mot.</p>

<nav class="toc" aria-label="Sommaire de l'article"><strong>Au sommaire</strong><ol>
<li><a href="#probleme">Le problème : dessiner quelqu'un qui vous connaît</a></li>
<li><a href="#silhouettes">Des silhouettes héritées de la surface</a></li>
<li><a href="#marques">Les marques lumineuses</a></li>
<li><a href="#trois">Trois habitants, trois relations à Sacha</a></li>
<li><a href="#sacha">Et Sacha dans tout ça ?</a></li>
<li><a href="#methode">Notre méthode, du croquis au modèle 3D</a></li>
</ol></nav>

<h2 id="probleme">Le problème : dessiner quelqu'un qui vous connaît</h2>
<p>Un personnage hostile est facile à lire : posture fermée, regard dur, silhouette anguleuse. Un personnage bienveillant aussi. Mais comment dessiner quelqu'un qui vous regarde comme un vieil ami alors que vous le rencontrez pour la première fois ? C'est la question qui a occupé mes premiers mois de travail sur le projet.</p>
<p>La réponse est venue de l'observation. En regardant des photos de retrouvailles, on remarque que la familiarité passe moins par le sourire que par le regard : des yeux légèrement plissés, une tête un peu inclinée, une distance physique réduite. Les habitants de Sextia ont donc tous une posture tournée vers Sacha. Dans les scènes, ils s'approchent un pas plus près que la norme, et leur regard s'attarde une demi-seconde de trop. Ces détails sont minuscules, mais ensemble ils produisent un malaise doux, exactement le ton mystérieux que Flexarion recherche.</p>

<h2 id="silhouettes">Des silhouettes héritées de la surface</h2>
<p>Comme pour l'architecture, détaillée dans le <a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">devlog sur la conception des deux villes jumelles</a>, nous avons voulu que les habitants de 2306 descendent visiblement de ceux de 2156. Pas de combinaisons spatiales argentées ni de casques intégraux : les vêtements de Sextia sont des évolutions de pièces que l'on porte aujourd'hui en Provence. Le châle devient une étole thermorégulée, la veste de travail devient un manteau long aux coutures lumineuses, les motifs des tissus provençaux se retrouvent, stylisés, sur des matières techniques.</p>
<p>Cette continuité sert l'histoire. Quand Sacha croise un habitant vêtu d'un motif qu'il a vu le matin même sur un marché de la surface, le joueur comprend sans explication que les deux villes sont liées. Le costume devient un indice.</p>

<figure>
""" + pic("below-zero-habitants-2306", "Concept art Flexarion de trois habitants de Sextia en 2306 : une archiviste âgée aux tatouages cyan, une jeune coursière à visière et un conducteur de tram") + """
<figcaption>Planche de recherche : Mémé Lune, Iléa et Aurèle, trois habitants de Sextia.</figcaption>
</figure>

<h2 id="marques">Les marques lumineuses</h2>
<p>Le seul élément ouvertement futuriste du character design, ce sont les marques lumineuses que portent certains habitants sur la peau. Elles ne sont pas décoratives. Dans l'univers du jeu, elles enregistrent les souvenirs importants de chaque personne, comme une écriture vivante. Plus un habitant a de souvenirs liés à Sacha, plus ses marques sont nombreuses et brillantes.</p>
<p>C'est un outil de lecture très efficace pour le joueur. Un personnage couvert de marques cyan a beaucoup à dire sur le passé de Sacha, ou sur son avenir. Et lorsque le joueur modifie le présent, les marques changent : certaines s'éteignent, d'autres apparaissent. C'est l'une des manières dont la <a href="/devlogs/enigmes-causalite-temporelle/">mécanique de causalité temporelle</a> se rend visible sur les personnages eux-mêmes.</p>
<p>Nous avons beaucoup itéré sur leur forme. Les premiers essais ressemblaient à des circuits imprimés, trop froids, trop « robot ». Nous sommes finalement partis des lignes de la Sainte-Victoire et des courbes des fontaines aixoises. Les marques actuelles évoquent des cartes, des courants d'eau, des lignes de relief : la géographie d'Aix inscrite sur la peau de ses descendants.</p>

<h2 id="trois">Trois habitants, trois relations à Sacha</h2>
<p>Pour tester nos principes, nous avons d'abord développé trois personnages, chacun incarnant une manière différente de connaître le héros.</p>
<h3>Mémé Lune, l'archiviste</h3>
<p>Âgée, couverte de marques, elle conserve la mémoire de Sextia. Elle parle à Sacha avec la tendresse d'une grand-mère et semble savoir comment l'histoire se termine. Son design joue sur la douceur : rondeurs, couleurs chaudes cachées sous les bleus, mains toujours jointes. Elle rassure, mais ce qu'elle sait inquiète.</p>
<h3>Iléa, la coursière</h3>
<p>Adolescente, rapide, insolente. Elle connaît Sacha comme on connaît une légende : elle a entendu parler de lui toute sa vie. Sa visière translucide cache en partie ses yeux, ce qui rend ses réactions plus difficiles à lire. C'est volontaire : Iléa est le personnage dont la loyauté évolue le plus selon les choix du joueur. Elle parle particulièrement aux joueurs et joueuses qui aiment les récits à choix multiples.</p>
<h3>Aurèle, le conducteur de tram</h3>
<p>Grand, élégant, toujours souriant. Il traite Sacha comme un collègue de longue date et lui fait des reproches sur des fautes qu'il n'a pas encore commises. Son long manteau bleu glacier, inspiré des uniformes de transport, en fait une silhouette immédiatement reconnaissable de loin, utile pour le guidage du joueur dans les grandes places.</p>

<h2 id="sacha">Et Sacha dans tout ça ?</h2>
<p>Le héros a été le personnage le plus difficile à dessiner, précisément parce qu'il doit rester ordinaire. Sacha Morel est un technicien de vingt-quatre ans, pas un élu, pas un soldat. Sa tenue est fonctionnelle : veste de travail usée, lampe frontale, outils à la ceinture. Sa silhouette doit pouvoir se fondre dans l'Aix de 2156, puis paraître déplacée dans Sextia. Ce contraste rappelle constamment au joueur qu'il est un étranger dans un monde qui, lui, ne le considère pas du tout comme un étranger.</p>

<h2 id="methode">Notre méthode, du croquis au modèle 3D</h2>
<p>Chaque personnage suit le même parcours au studio. Tout commence par une fiche d'une page rédigée avec la direction créative : qui est cette personne, que sait-elle de Sacha, que veut-elle ? Viennent ensuite des dizaines de silhouettes noires, sans détail, pour trouver une forme lisible de loin. Puis des croquis de visages et d'expressions, des planches de costumes, et enfin un modèle 3D réalisé avec notre artiste 3D.</p>
<p>À chaque étape, nous testons les personnages dans le moteur, dans la vraie lumière de Sextia. Un costume superbe sur fond blanc peut devenir illisible sous les éclairages cyan de la ville souterraine. Cette vérification en contexte nous a fait abandonner plusieurs designs que nous aimions beaucoup, mais c'est le prix de la cohérence.</p>
<p>Ces planches sont des recherches de travail : elles servent de point de départ et évolueront encore avant la version finale du jeu. Pour découvrir l'univers complet du jeu, rendez-vous sur la <a href="/below-zero/">page de Below Zero</a>, et pour savoir comment ces voix prennent vie, lisez le <a href="/devlogs/sound-design-ville-souterraine/">devlog sur le sound design de la ville souterraine</a>.</p>
"""


BODIES[5] = """
<p class="lead">Sextia, la ville souterraine de 2306 dans <a href="/below-zero/">Below Zero</a>, n'a pas été dessinée dans le vide : elle naît d'un relevé patient des rues, des places et de l'eau d'Aix-en-Provence. Si le studio Flexarion et l'intrigue de Below Zero sont entièrement fictifs, le décor qui nourrit nos deux époques s'appuie, lui, sur une géographie bien réelle — du cours Mirabeau aux thermes Sextius, jusqu'aux fondations antiques d'Aquae Sextiae.</p>

<div class="facts" role="note" aria-label="Repères clés de l'article"><dl>
<dt>Thème</dt><dd>Transposition du vrai Aix-en-Provence vers Sextia (2306)</dd>
<dt>Lieux réels transposés</dt><dd>Cours Mirabeau, fontaine de la Rotonde, thermes Sextius, vieille ville, quartier Mazarin</dd>
<dt>Racines historiques</dt><dd>Aquae Sextiae (122 av. J.-C.), Caius Sextius Calvinus, sources thermales</dd>
<dt>Cadre</dt><dd>Lieux et histoire réels ; studio Flexarion et jeu Below Zero fictifs</dd>
</dl></div>

<nav class="toc" aria-label="Sommaire de l'article"><strong>Au sommaire</strong><ol>
<li><a href="#reperages">Partir du terrain : nos repérages dans Aix-en-Provence</a></li>
<li><a href="#mirabeau-rotonde">Du cours Mirabeau à la Rotonde : transposer la colonne vertébrale</a></li>
<li><a href="#thermes-aquae">Des thermes Sextius à Aquae Sextiae : le rôle fondateur de l'eau</a></li>
<li><a href="#vieille-ville">La vieille ville et le quartier Mazarin : pierre, ombre et proportions</a></li>
<li><a href="#methode">Ce que l'on garde, ce que l'on transforme en 2306</a></li>
<li><a href="#equilibre">Rechercher le vrai Aix sans faire une carte postale</a></li>
</ol></nav>

<h2 id="reperages">Partir du terrain : nos repérages dans Aix-en-Provence</h2>
<p>Quand l'équipe de direction artistique et d'environnements a posé les bases de Sextia avec Inès Valcourt et Margaux Delorme, nous avons commencé par marcher dans Aix-en-Provence carnet et enregistreur en main. Mon rôle de sound designer m'amenait déjà à écouter la résonance des placettes et des passages couverts ; très vite, ce travail de terrain est devenu commun à toute la direction visuelle et sonore.</p>
<p>Nous cherchions ce qui rend Aix immédiatement reconnaissable sans afficher de panneau indicateur : la hauteur modérée des façades, le grain blond de la pierre de Bibémus, la façon dont une ruelle étroite débouche soudain sur une place claire, et surtout la présence constante de l'eau. En transposant la ville sous terre pour 2306, nous voulions qu'une personne qui connaît Aix-en-Provence ressente une familiarité physique — les distances entre deux carrefours, l'angle d'une perspective — avant même de comprendre ce qu'elle regarde.</p>

<h2 id="mirabeau-rotonde">Du cours Mirabeau à la Rotonde : transposer la colonne vertébrale</h2>
<p>Dans la réalité comme dans Below Zero, l'axe structurant de la ville reste la ligne qui relie la place de la Rotonde au cours Mirabeau. À la surface de 2156, cet axe a souffert des sécheresses répétées : la grande fontaine de la Rotonde tourne au ralenti et les platanes centenaires s'appuient sur des tuteurs métalliques. Sous terre, dans Sextia, cette même ligne devient l'artère lumineuse et hydraulique de la cité.</p>
<h3>La fontaine de la Rotonde</h3>
<p>Inaugurée en 1860 à l'entrée du cours Mirabeau, la fontaine de la Rotonde est un repère circulaire à trois vasques et douze mètres de haut. Dans Sextia, nous avons conservé sa silhouette étagée, son bassin circulaire et son rôle de point de convergence des avenues. Simplement, la fonte et la pierre cèdent la place à un verre minéral translucide où l'eau thermale circule à ciel ouvert, éclairée de cyan. Le joueur qui contourne la Rotonde à la surface retrouve exactement le même rayon de marche deux cents mètres plus bas.</p>
<h3>Le cours Mirabeau</h3>
<p>Sur le cours Mirabeau, la double rangée de platanes forme une voûte végétale qui coupe la chaleur d'été. En 2306, sous une cavité rocheuse privée de soleil, des platanes ordinaires ne survivraient pas : nous les avons transposés en colonnes végétales bioluminescentes, espacées au mètre près selon l'alignement réel des troncs. Côté façade sud et nord, la différence historique entre anciens hôtels particuliers et cafés devient une distinction fonctionnelle entre ateliers d'archives et lieux de passage.</p>

<h2 id="thermes-aquae">Des thermes Sextius à Aquae Sextiae : le rôle fondateur de l'eau</h2>
<p>L'histoire réelle d'Aix-en-Provence offre à Below Zero sa prémisse la plus solide. En 122 avant notre ère, le consul romain Caius Sextius Calvinus établit un poste fortifié près des sources chaudes de la région, après sa victoire sur la confédération salyenne d'Entremont. Le lieu prend le nom latin d'<em>Aquae Sextiae</em> — « les eaux de Sextius » — et c'est de ce mot <em>Aquae</em> que dérive le nom actuel d'Aix.</p>
<p>Aujourd'hui encore, les thermes Sextius rappellent la permanence de ces sources chaudes sous le tissu urbain. Pour Sextia en 2306, cette histoire n'est pas un simple clin d'œil : elle explique pourquoi une ville souterraine peut exister. L'eau thermale fournit la chaleur douce, l'énergie hydraulique des quartiers et la vapeur qui donne à la cavité son acoustique feutrée. Les habitants de 2306 ont gardé le nom de « Sextia » parce qu'ils vivent littéralement autour des mêmes veines d'eau que les fondateurs antiques.</p>
<p>Lorsque Sacha Morel inspecte une vanne ou un canal d'amenée près des thermes en 2156, il agit donc sur l'artère vitale de la ville future. Ce choix ancre la fiction dans une réalité géologique et historique que chacun peut vérifier en se promenant à Aix-en-Provence.</p>

<h2 id="vieille-ville">La vieille ville et le quartier Mazarin : pierre, ombre et proportions</h2>
<p>Aix ne se résume pas à son grand boulevard. Pour que Sextia sonne juste, il fallait capter le contraste entre le lacis médiéval de la vieille ville et la géométrie régulière du quartier Mazarin.</p>
<ul>
<li><strong>La vieille ville et les abords de la cathédrale Saint-Sauveur :</strong> rues serrées, passages voûtés, petites places irrégulières comme la place d'Albertas ou la place des Cardeurs. En 2306, ces ruelles deviennent des galeries resserrées dans la roche, aux plafonds bas, où les voix portent loin et où l'on découvre les ateliers des habitants.</li>
<li><strong>Le quartier Mazarin et la fontaine des Quatre-Dauphins :</strong> tracé au XVIIe siècle selon un plan orthogonal net. Dans Sextia, cette rigueur géométrique sert de repère calme : les carrefours à angle droit accueillent les conduits principaux d'eau claire et servent de zone de test pour nos énigmes de causalité temporelle.</li>
<li><strong>Les petites fontaines de quartier :</strong> moussues à la surface, cristallines sous terre, elles marquent autant de points d'ancrage entre 2156 et 2306, comme le détaille déjà notre <a href="/devlogs/enigmes-causalite-temporelle/">devlog sur les énigmes de causalité</a>.</li>
</ul>

<h2 id="methode">Ce que l'on garde, ce que l'on transforme en 2306</h2>
<p>Pour éviter que Sextia ne devienne une simple maquette peinte en bleu, la direction artistique applique une grille de transposition en trois temps pour chaque lieu retenu, en prolongement des règles décrites dans le <a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">devlog sur nos deux villes jumelles</a> :</p>
<ol>
<li><strong>Conserver l'empreinte et l'usage :</strong> une place reste un lieu de rencontre, un lavoir ou une fontaine reste un point d'eau, un passage couvert reste un raccourci piéton.</li>
<li><strong>Traduire la matière :</strong> la pierre calcaire ocre et les tuiles romaines deviennent des parements de basalte clair, du verre minéral et des nervures porteuses discrètement rétroéclairées.</li>
<li><strong>Justifier chaque détail par le quotidien de Sextia :</strong> si un ciel artificiel glacier remplace l'azur provençal, c'est pour réguler le rythme jour-nuit des habitants ; si des câbles disparaissent, c'est que l'eau et les réseaux souterrains portent l'énergie.</li>
</ol>

<h2 id="equilibre">Rechercher le vrai Aix sans faire une carte postale</h2>
<p>Le piège classique d'un décor inspiré d'une ville réelle est de multiplier les monuments connus au détriment de la crédibilité. Nous avons volontairement écarté l'idée d'une « visite guidée » : dans Below Zero, certains quartiers entiers sont des rues ordinaires d'habitation, des locaux techniques municipaux ou des cours intérieures fermées, car Sacha Morel connaît d'abord la ville par ses réseaux souterrains.</p>
<p>Il reste important de le rappeler clairement : si le cours Mirabeau, la Rotonde, la vieille ville et les thermes Sextius existent bel et bien à Aix-en-Provence, le studio Flexarion, l'Aix de 2156 et la cité souterraine de Sextia appartiennent à une œuvre de fiction. Pour voir ce que deviennent six de ces lieux dans les deux époques du jeu, consultez notre <a href="/below-zero/carte-sextia/">carte commentée de Sextia sous Aix</a>. Ce va-et-vient entre patrimoine réel et projection futuriste est aussi ce qui donne sa couleur acoustique au jeu, explorée dans le <a href="/devlogs/sound-design-ville-souterraine/">devlog sur le sound design de Sextia</a>, et son rythme calme sans affrontement, détaillé dans notre <a href="/devlogs/accessibilite-rythme-jeu-sans-combat/">devlog sur l'accessibilité et le rythme sans combat</a>.</p>
"""

BODIES[6] = """
<p class="lead"><a href="/below-zero/">Below Zero</a> ne comporte aucun combat, aucune barre de vie et aucun chronomètre mortel. Pourtant, explorer seul une ville souterraine qui vous connaît déjà doit rester prenant du début à la fin. En tant que développeur gameplay chez Flexarion, je travaille avec le game design de Lucas Arnaud sur une question centrale : comment tenir le rythme et ouvrir le jeu au plus grand nombre quand on retire toute violence ?</p>

<div class="facts" role="note" aria-label="Repères clés de l'article"><dl>
<dt>Thème</dt><dd>Rythme narratif et accessibilité dans un jeu d'aventure sans combat</dd>
<dt>Protagoniste et outil</dt><dd>Sacha Morel, équipé du Diapason et du Carnet de causalité</dd>
<dt>Plateforme</dt><dd>PC en priorité (consoles à l'étude), en développement, sortie non annoncée</dd>
<dt>Principe clé</dt><dd>Zéro game over punitif, progression par observation et causalité (univers fictif)</dd>
</dl></div>

<nav class="toc" aria-label="Sommaire de l'article"><strong>Au sommaire</strong><ol>
<li><a href="#tension">Tenir la tension sans ennemis ni barre de vie</a></li>
<li><a href="#diapason">Le Diapason et Sacha Morel : un outil de lecture du monde</a></li>
<li><a href="#rythme">Micro-rythme et respiration entre 2156 et 2306</a></li>
<li><a href="#accessibilite">Des options d'accessibilité pensées dès le prototype</a></li>
<li><a href="#erreurs-rythme">Ce que nos tests ont corrigé sur la courbe d'attention</a></li>
<li><a href="#suite-dev">Ce qui reste à affiner sur PC</a></li>
</ol></nav>

<h2 id="tension">Tenir la tension sans ennemis ni barre de vie</h2>
<p>Dans beaucoup de productions de science-fiction, la tension vient de l'urgence : esquiver une menace, gérer des munitions, recommencer un passage après un échec. Dès la création de Flexarion — studio fictif imaginé autour d'un projet narratif exigeant — nous avons voulu prouver que l'enquête et le trouble psychologique suffisent à maintenir l'attention.</p>
<p>Dans Below Zero, la tension repose sur trois moteurs précis :</p>
<ul>
<li><strong>L'asymétrie de savoir :</strong> les habitants de Sextia en 2306 saluent Sacha Morel par son prénom et évoquent des gestes qu'il n'a pas encore accomplis. Chaque dialogue devient un suspense calme : qu'est-ce que mon double du présent va déclencher ?</li>
<li><strong>Le poids irréversible des choix pivots :</strong> même si aucune erreur ne bloque l'aventure, certaines décisions marquent durablement la cité souterraine et ferment ou ouvrent des liens avec ses habitants.</li>
<li><strong>La satisfaction du déclic :</strong> comprendre pourquoi une fontaine sèche en 2306 répond à une vanne grippée en 2156 procure une montée d'adrénaline intellectuelle qui remplace avantageusement un duel.</li>
</ul>

<h2 id="diapason">Le Diapason et Sacha Morel : un outil de lecture du monde</h2>
<p>Pour que l'exploration reste fluide sans flèches géantes au-dessus des décors, Sacha Morel dispose d'un instrument de chantier détourné : le <strong>Diapason</strong>. Dans la fiction, il s'agit d'un appareil de diagnostic acoustique utilisé par les techniciens des réseaux souterrains pour détecter les fuites dans la roche.</p>
<p>Manette ou souris en main, lever le Diapason sert de pont entre le joueur et le système de causalité. À l'approche d'un objet ou d'un mécanisme qui « résonne » entre 2156 et 2306, l'outil réagit simultanément sur trois canaux :</p>
<ol>
<li><strong>Visuel :</strong> des anneaux cyan concentriques se déploient autour des branches de l'outil, plus serrés à mesure que l'on vise la source, avec un contour discret sur l'élément actif.</li>
<li><strong>Sonore :</strong> une note harmonique pure se superpose à l'ambiance, modulée selon la distance (en lien direct avec le travail décrit dans notre <a href="/devlogs/sound-design-ville-souterraine/">devlog sur le sound design</a>).</li>
<li><strong>Tactile et textuel :</strong> légère vibration optionnelle sur manette, complétée par une ligne brève d'état lisible à l'écran pour les personnes jouant sans son ou sans retour haptique.</li>
</ol>
<p>Sacha n'est jamais pressé par un minuteur : il peut ranger le Diapason, ouvrir son <a href="/devlogs/enigmes-causalite-temporelle/">Carnet de causalité</a> et vérifier ses hypothèses à son propre rythme.</p>

<h2 id="rythme">Micro-rythme et respiration entre 2156 et 2306</h2>
<p>Un jeu sans combat court un danger précis : devenir monotone si toutes les scènes se ressemblent. Côté programmation gameplay, nous avons structuré la progression autour d'une alternance régulière entre quatre temps distincts :</p>
<ul>
<li><strong>L'observation en surface (2156) :</strong> rythme posé, lumière chaude, bruits urbains clairsemés, prise d'informations techniques.</li>
<li><strong>La descente vers Sextia (2306) :</strong> SAS de transition de quelques secondes où la musique acoustique glisse vers les synthétiseurs et où l'on sent la bascule thermique.</li>
<li><strong>L'enquête sociale sous terre :</strong> discussions avec Mémé Lune, Iléa ou Aurèle (voir le <a href="/devlogs/character-design-habitants-futur/">devlog sur les habitants du futur</a>), où les répliques changent selon ce que Sacha vient de modifier.</li>
<li><strong>La vérification :</strong> courte scène cadrée montrant la conséquence concrète d'un geste dans le décor, avant de rendre la main au joueur.</li>
</ul>
<p>Cette respiration évite les longues traversées à vide. Chaque trajet entre Aix et Sextia doit durer moins d'une minute entre deux indices ou deux rencontres signifiantes.</p>

<h2 id="accessibilite">Des options d'accessibilité pensées dès le prototype</h2>
<p>Choisir un jeu sans combat permet d'abaisser d'emblée la barrière des réflexes rapides. Mais « sans combat » ne signifie pas automatiquement « accessible ». Nous intégrons dès le code de base — et non en fin de production — plusieurs leviers réglables indépendamment depuis le menu pause :</p>
<h3>Accessibilité motrice</h3>
<ul>
<li>Réattribution complète du clavier et de la souris sur PC, avec possibilité de jouer entièrement à une main ou au clavier seul.</li>
<li>Maintien des touches remplaçable par une simple pression (pour courir, activer le Diapason ou interagir).</li>
<li>Zéro QTE chronométré : aucune énigme ne demande une manipulation rapide ou précise à la milliseconde.</li>
</ul>
<h3>Accessibilité visuelle et cognitive</h3>
<ul>
<li>Taille des sous-titres et des polices d'interface réglable sur quatre paliers, avec fond opaque derrière les dialogues.</li>
<li>Mode « repères renforcés » qui augmente le contraste des points d'ancrage du Diapason et ajoute une icône claire pour ne pas dépendre uniquement de la distinction cyan / blanc.</li>
<li>Possibilité de réduire ou couper les tremblements de caméra, les halos lumineux et les transitions rapides.</li>
<li>Synthèse du Carnet de causalité : un résumé en langage simple rappelle à tout moment la dernière piste ouverte sans pénalité.</li>
</ul>
<h3>Accessibilité auditive</h3>
<p>Comme nos énigmes utilisent l'eau et les résonances de Sextia, chaque signal sonore utile possède son double visuel : sous-titres indiquant le locuteur et l'ambiance, plus un indicateur directionnel discret autour du réticule quand le Diapason capte un écho causal.</p>

<h2 id="erreurs-rythme">Ce que nos tests ont corrigé sur la courbe d'attention</h2>
<p>Lors de nos premiers tests internes sur la tranche jouable du centre-ville d'Aix, nous avons observé un décrochage curieux : certains testeurs restaient bloqués vingt minutes à tourner autour d'une place sans oser agir, par peur de « gâcher » leur partie.</p>
<p>Nous avons donc ajouté deux garde-fous techniques : d'une part, le Carnet de causalité distingue visuellement les actions réversibles à tout moment des rares actions pivots (annoncées par un dialogue clair avant validation) ; d'autre part, un système de remarques contextuelles de Sacha, désactivable dans les options, suggère une piste si le joueur inspecte trois fois le même secteur sans nouveau lien. Le rythme a immédiatement retrouvé son élan sans trahir le plaisir de chercher par soi-même.</p>

<h2 id="suite-dev">Ce qui reste à affiner sur PC</h2>
<p>Below Zero est en cours de développement prioritairement pour PC (les versions consoles restent à l'étude et aucune date de sortie n'est annoncée). Nos prochains chantiers gameplay portent sur la navigation au lecteur d'écran dans le Carnet de causalité et sur le réglage fin du tempo des dialogues pour les chapitres suivants. Pour découvrir le contexte complet du jeu, rendez-vous sur la <a href="/below-zero/">page Below Zero</a> ou faites connaissance avec l'équipe sur <a href="/studio/">Le studio</a>.</p>
"""

BODIES[7] = """
<p class="lead">On me demande souvent pourquoi un studio de jeu vidéo indépendant s'est installé à Aix-en-Provence plutôt qu'à Paris, Lyon ou Montréal, et pourquoi nous faisons de la science-fiction sans vaisseaux ni lasers. Pour ce septième devlog, je quitte un instant la fabrication de <a href="/below-zero/">Below Zero</a> pour raconter la nôtre : comment Flexarion est né en 2022, ce que nous avons appris en route et ce qu'Aix nous apporte chaque jour.</p>

<div class="facts" role="note" aria-label="Repères clés de l'article"><dl>
<dt>Fondation</dt><dd>2022, à Aix-en-Provence, quelques mois après une game jam</dd>
<dt>Fondateurs</dt><dd>Inès Valcourt, Théo Marchetti et Samira Benali</dd>
<dt>Équipe</dt><dd>8 personnes et 8 métiers depuis 2024</dd>
<dt>Spécialité</dt><dd>Jeux vidéo de science-fiction narratifs, sans combat</dd>
<dt>Cadre</dt><dd>Récit d'un studio fictif, ancré dans une ville réelle</dd>
</dl></div>

<nav class="toc" aria-label="Sommaire de l'article"><strong>Au sommaire</strong><ol>
<li><a href="#game-jam">Une game jam au printemps 2022</a></li>
<li><a href="#pourquoi-aix">Pourquoi créer un studio de jeu vidéo à Aix-en-Provence</a></li>
<li><a href="#pourquoi-sf">Pourquoi la science-fiction narrative</a></li>
<li><a href="#debuts">Les débuts : un prototype bancal et une table trop petite</a></li>
<li><a href="#equipe">Grandir jusqu'à huit sans perdre l'esprit indépendant</a></li>
<li><a href="#ecosysteme">Un écosystème du jeu vidéo entre Aix et Marseille</a></li>
<li><a href="#conseils">Ce que nous dirions à qui veut fonder un studio indé</a></li>
</ol></nav>

<h2 id="game-jam">Une game jam au printemps 2022</h2>
<p>Tout commence par un week-end de game jam à Aix-en-Provence, au printemps 2022. Je venais du théâtre, où j'écrivais et mettais en scène de petites pièces, et je n'avais jamais livré un jeu. Théo Marchetti et Samira Benali, eux, codaient depuis des années, mais cherchaient une histoire à raconter. Le thème imposé tenait en un mot que nous avons tous interprété différemment. Nous en avons tiré une idée simple : déplacer un objet dans le présent et voir, sur un second écran, ce qu'il devient cent ans plus tard.</p>
<p>Le prototype de quarante-huit heures était bancal. La caméra tremblait, la moitié des objets ne réagissait pas et la fin plantait une fois sur deux. Pourtant, les personnes qui l'ont essayé restaient devant l'écran à tester des hypothèses, à revenir en arrière, à se demander « et si… ». Ce soir-là, en rentrant par le cours Mirabeau, nous avons compris que ce n'était pas le jeu qui comptait, mais cette envie de chercher. Quelques mois plus tard, nous fondions Flexarion.</p>

<h2 id="pourquoi-aix">Pourquoi créer un studio de jeu vidéo à Aix-en-Provence</h2>
<p>La réponse honnête commence par une évidence : nous y vivions déjà. Mais rester à Aix est vite devenu un choix assumé, pour trois raisons.</p>
<p>La première est créative. Aix est une ville née de l'eau chaude, il y a plus de deux mille ans, sous le nom d'Aquae Sextiae. Ses fontaines, ses places et ses sources thermales racontent déjà une histoire de strates et de temps superposés. Pour un studio qui voulait faire de la science-fiction à hauteur humaine, c'était un décor tout trouvé : il suffisait de se demander ce qu'il y aurait sous nos pieds deux siècles plus tard. Cette intuition est devenue Sextia, la ville souterraine de 2306, dont vous pouvez parcourir les lieux sur notre <a href="/below-zero/carte-sextia/">carte commentée de Sextia sous Aix</a>.</p>
<p>La deuxième est humaine. Une ville de taille moyenne permet de garder un rythme de travail raisonnable : on vient au studio à pied ou à vélo, on teste un prototype avec des amis le soir même, on croise des joueurs dans la rue. Pour un petit studio indépendant, cette proximité vaut beaucoup.</p>
<p>La troisième est pratique. Entre Aix et Marseille, la région rassemble des universités, des écoles du numérique et une communauté du jeu vidéo active. Nous n'avions pas besoin de partir pour trouver des collègues de talent.</p>

<h2 id="pourquoi-sf">Pourquoi la science-fiction narrative</h2>
<p>Quand on annonce « studio de science-fiction », beaucoup imaginent des batailles spatiales. Ce n'est pas notre science-fiction. Celle qui nous intéresse pose une question sur le présent en déplaçant légèrement le décor : que devient une ville après des décennies de sécheresse ? Que retient un lieu des gestes de ceux qui l'ont traversé ? Que ressent-on face à des inconnus qui se souviennent de nous ?</p>
<p>Ce choix a une conséquence directe sur nos jeux : pas de combat. Nous voulions que la tension vienne du mystère et des conséquences, pas des réflexes. C'est un pari exigeant, que Théo détaille dans le <a href="/devlogs/accessibilite-rythme-jeu-sans-combat/">devlog sur le rythme d'un jeu sans combat</a>. Il nous permet aussi de toucher des joueurs qui ne se reconnaissent pas dans les jeux d'action, et c'est l'une des grandes forces d'un studio de jeu vidéo indépendant : choisir ses propres règles.</p>

<h2 id="debuts">Les débuts : un prototype bancal et une table trop petite</h2>
<p>La première année, Flexarion tenait autour d'une seule table, dans un local partagé du centre d'Aix. Samira a écrit les premières briques du moteur qui synchronise aujourd'hui les deux villes à partir d'un plan unique. Théo a reconstruit le prototype de la game jam pour qu'il ne plante plus. Moi, je remplissais des carnets de questions : pourquoi la ville du futur serait-elle sous terre ? Pourquoi ses habitants connaîtraient-ils le héros ? Qui est Sacha Morel, et pourquoi un technicien des réseaux souterrains plutôt qu'un explorateur ?</p>
<p>Nous avons fait beaucoup d'erreurs. Nous avons d'abord imaginé un jeu bien trop grand, avec une ville entière à reproduire. Nous avons perdu des semaines sur un système de dialogues que personne n'utilisait. Nous avons aussi appris à jeter : une bonne idée qui ne sert pas le mystère n'a pas sa place dans le jeu. C'est à ce moment qu'est née la règle qui structure encore Below Zero, celle d'un seul plan pour deux époques, expliquée par Margaux dans le <a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">devlog sur nos deux villes jumelles</a>.</p>

<h2 id="equipe">Grandir jusqu'à huit sans perdre l'esprit indépendant</h2>
<p>L'ordre des recrutements dit beaucoup de nos priorités. En 2023, avant toute communication, nous avons accueilli Lucas Arnaud au game design et Margaux Delorme aux environnements 3D : il fallait d'abord des énigmes solides et une ville crédible. En 2024 sont arrivés Yanis Okafor pour les personnages, Élise Fabre pour le son et la musique, puis Raphaël Costa pour la communication. Nous sommes huit depuis, et chacun signe au moins un devlog : c'est notre façon de montrer qu'un jeu se fabrique à plusieurs voix.</p>
<p>Rester indépendant, pour nous, ce n'est pas un slogan. C'est garder la main sur nos choix créatifs, avancer à un rythme soutenable et refuser les fonctionnalités ajoutées uniquement parce qu'elles sont à la mode. Cela veut aussi dire accepter d'aller moins vite : Below Zero n'a pas encore de date de sortie, et nous préférons l'annoncer quand le jeu sera prêt.</p>

<h2 id="ecosysteme">Un écosystème du jeu vidéo entre Aix et Marseille</h2>
<p>Un petit studio ne vit pas seul. Autour de nous, entre Aix et Marseille, il existe des game jams régulières, des rencontres entre développeurs, des formations au jeu vidéo et un public curieux. C'est dans ces rendez-vous que nous testons nos prototypes, que nous écoutons les critiques et que nous croisons parfois nos futurs collègues.</p>
<p>La ville elle-même fait partie de cet écosystème. Nos repérages se font à pied, carnet en main, de la Rotonde à la cathédrale Saint-Sauveur. Élise enregistre l'eau des fontaines, Margaux photographie les façades, Yanis observe les gens sur les terrasses. Le <a href="/devlogs/concevoir-sextia-vrai-aix/">devlog sur la conception de Sextia à partir du vrai Aix</a> raconte en détail ce travail de terrain.</p>

<h2 id="conseils">Ce que nous dirions à qui veut fonder un studio indé</h2>
<p>Si vous rêvez de créer votre studio de jeu vidéo, à Aix ou ailleurs, voici ce que nos premières années nous ont appris :</p>
<ol>
<li><strong>Partez d'une sensation, pas d'un genre.</strong> Notre point de départ n'était pas « faire de la SF », mais l'envie de chercher que nous avions vue chez les joueurs de la game jam.</li>
<li><strong>Ancrez votre univers dans un lieu que vous connaissez.</strong> Vous saurez le décrire avec une précision qu'aucune documentation ne remplace.</li>
<li><strong>Recrutez dans l'ordre de vos besoins.</strong> Le jeu d'abord, la communication ensuite.</li>
<li><strong>Montrez votre travail tôt.</strong> Un prototype bancal testé par dix personnes vaut mieux qu'un document parfait que personne ne lit.</li>
<li><strong>Protégez votre rythme.</strong> Un studio indépendant qui s'épuise ne finit pas ses jeux.</li>
</ol>
<p>Quatre ans après cette game jam, Flexarion reste un petit studio de science-fiction narrative qui creuse sous la réalité, au sens propre comme au figuré. Pour découvrir toute l'équipe, rendez-vous sur la page <a href="/studio/">Le studio Flexarion</a> ; pour l'univers du jeu, sur la <a href="/below-zero/">page de Below Zero</a>.</p>
"""

PAGES = []
for a in ARTICLES:
    n, role = AUTHORS[a["author"]]
    others = [b for b in ARTICLES if b is not a]
    chrono = sorted(ARTICLES, key=lambda b: b["date"])
    i = chrono.index(a)
    newer = chrono[i + 1] if i + 1 < len(chrono) else None
    older = chrono[i - 1] if i > 0 else None
    pn = ""
    if older:
        pn += f'<a class="pn prev" href="{url(older)}" rel="prev"><span class="pn-dir"><span aria-hidden="true">← </span>Devlog précédent</span><span class="pn-title">{older["short"]}</span></a>'
    if newer:
        pn += f'<a class="pn next" href="{url(newer)}" rel="next"><span class="pn-dir">Devlog suivant<span aria-hidden="true"> →</span></span><span class="pn-title">{newer["short"]}</span></a>'
    pn = f'<nav class="pager" aria-label="Navigation entre les devlogs">{pn}</nav>'
    rel = "".join(f'<li><a href="{url(b)}">{b["short"]}</a></li>' for b in others)
    body = f"""<article class="wrap">
<header>
<p class="kicker">Devlog n°{a['num']} · Below Zero</p>
<h1>{a['h1']}</h1>
<p class="meta">Par {n}, {role.lower()} chez Flexarion · Publié le <time datetime="{a['date']}">{a['date_fr']}</time> · Mis à jour le <time datetime="{MOD}">{MOD_FR}</time></p>
</header>
<figure>
{pic(a['img'], a['alt'], lcp=True)}
</figure>
<div class="prose">
{BODIES[a['num']]}
<h2>Les autres devlogs de Flexarion</h2>
<ul>{rel}</ul>
<p><a class="btn ghost" href="/devlogs/">Tous les devlogs</a> <a class="btn" href="/below-zero/">Découvrir Below Zero</a></p>
</div>
{pn}
</article>"""
    words = len(__import__("re").sub("<[^>]+>", " ", BODIES[a["num"]]).split())
    a["words"] = words
    ld = [{
      "@type": "BlogPosting", "@id": BASE + url(a) + "#article", "headline": a["h1"], "description": a["desc"],
      "image": {"@type": "ImageObject", "url": f"{BASE}/assets/img/{a['img']}-1280.webp", "width": 1280, "height": 720},
      "datePublished": a["date"], "dateModified": LASTMOD, "inLanguage": "fr-FR", "wordCount": words,
      "author": {"@type": "Person", "name": n, "jobTitle": role, "worksFor": {"@id": ORG}},
      "publisher": {"@id": ORG}, "mainEntityOfPage": {"@id": BASE + url(a) + "#webpage"},
      "isPartOf": {"@id": BASE + "/devlogs/#blog"}, "about": {"@id": ORG if a["num"] == 7 else BASE + "/below-zero/#videogame"},
      "articleSection": "Devlog"}]
    PAGES.append(dict(path=url(a), title=a["title"], desc=a["desc"], body=body, jsonld=ld, ogtype="article",
        date=a["date"], author=n, image=f"/assets/img/{a['img']}-1280.webp", imgalt=a["alt"],
        crumbs=[("/devlogs/", "Devlogs"), (url(a), a["short"])]))
