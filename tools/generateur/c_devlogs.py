from build import pic, BASE, ORG, LASTMOD, esc

AUTHORS = {
 "margaux": ("Margaux Delorme", "Artiste 3D environnements"),
 "lucas": ("Lucas Arnaud", "Game designer"),
 "elise": ("Élise Fabre", "Sound designer"),
 "yanis": ("Yanis Okafor", "Character designer"),
}

ARTICLES = [
 dict(slug="concevoir-deux-villes-aix-2156-2306", num=1, img="devlog-deux-villes", author="margaux",
  title="Devlog #1 : concevoir deux villes jumelles (2156 / 2306) | Flexarion",
  h1="Devlog #1 : concevoir deux villes jumelles, Aix 2156 et Sextia 2306",
  short="Concevoir deux villes jumelles",
  desc="Comment l'équipe Flexarion construit Aix-en-Provence en 2156 et sa jumelle souterraine Sextia en 2306 : plans superposés, règles de symétrie et lisibilité.",
  alt="Deux plans superposés de la même ville, l'un à l'encre sépia, l'autre en hologramme cyan, sur la table de travail de Flexarion"),
 dict(slug="enigmes-causalite-temporelle", num=2, img="devlog-causalite", author="lucas",
  title="Devlog #2 : les énigmes de causalité de Below Zero | Flexarion",
  h1="Devlog #2 : le présent modifie le futur, nos énigmes de causalité",
  short="Les énigmes de causalité temporelle",
  desc="Le game designer de Flexarion explique comment une action dans l'Aix de 2156 transforme la ville de 2306 dans Below Zero, et comment on évite le chaos.",
  alt="Graphe lumineux reliant une clé, une graine, une lanterne et une porte entre deux lignes temporelles"),
 dict(slug="sound-design-ville-souterraine", num=3, img="devlog-son", author="elise",
  title="Devlog #3 : le sound design de la ville souterraine | Flexarion",
  h1="Devlog #3 : écouter sous la ville, le sound design de Sextia",
  short="Le sound design de la ville souterraine",
  desc="Réverbérations, eau thermale et cigales mutées : la sound designer de Flexarion raconte comment elle fait sonner la ville souterraine de Below Zero.",
  alt="Micro et casque posés dans un tunnel de pierre où des ondes sonores cyan se propagent vers une ville lointaine"),
 dict(slug="character-design-habitants-futur", num=4, img="devlog-personnages", author="yanis",
  title="Devlog #4 : le character design des habitants de 2306 | Flexarion",
  h1="Devlog #4 : ils vous connaissent déjà, dessiner les habitants de 2306",
  short="Le character design des habitants de 2306",
  desc="Du croquis au personnage final : le character designer de Flexarion dévoile comment il dessine des habitants du futur qui reconnaissent le joueur.",
  alt="Carnet de croquis ouvert montrant l'évolution d'un visage futuriste jusqu'à un portrait aux marques cyan"),
]
DATE = "2026-11-17"
DATE_FR = "17 novembre 2026"

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
<figcaption>Concept art de la grande place de Sextia. Les terrasses reprennent les gabarits des immeubles de surface (visuel généré par IA, retravail prévu).</figcaption>
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
<figcaption>Capture de travail : la même fontaine dans les deux époques, reliée par un fil de causalité (visuel généré par IA).</figcaption>
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
<figcaption>Dans cette scène, le silence relatif de l'escalier contraste avec la rumeur de la ville qui monte de la cavité (visuel généré par IA).</figcaption>
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
<figcaption>Planche de recherche : Mémé Lune, Iléa et Aurèle, trois habitants de Sextia (visuel généré par IA, retravail prévu).</figcaption>
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
<p>Les visuels montrés dans cet article sont des recherches générées avec l'aide d'outils d'IA, qui servent de point de départ et seront retravaillés. Pour découvrir l'univers complet du jeu, rendez-vous sur la <a href="/below-zero/">page de Below Zero</a>, et pour savoir comment ces voix prennent vie, lisez le <a href="/devlogs/sound-design-ville-souterraine/">devlog sur le sound design de la ville souterraine</a>.</p>
"""

PAGES = []
for a in ARTICLES:
    n, role = AUTHORS[a["author"]]
    others = [b for b in ARTICLES if b is not a]
    rel = "".join(f'<li><a href="{url(b)}">{b["short"]}</a></li>' for b in others)
    body = f"""<article class="wrap">
<header>
<p class="kicker">Devlog n°{a['num']} · Below Zero</p>
<h1>{a['h1']}</h1>
<p class="meta">Par {n}, {role.lower()} chez Flexarion · Publié le <time datetime="{DATE}">{DATE_FR}</time></p>
</header>
<figure>
{pic(a['img'], a['alt'], lcp=True)}
</figure>
<div class="prose">
{BODIES[a['num']]}
<aside class="note" aria-label="Précision">Flexarion et Below Zero sont des créations fictives réalisées dans le cadre d'un projet pédagogique (BUT Informatique, IUT d'Aix-Marseille). Ce devlog a été rédigé avec l'assistance d'une IA. Détails dans les <a href="/mentions-legales/">mentions légales</a>.</aside>
<h2>Les autres devlogs de Flexarion</h2>
<ul>{rel}</ul>
<p><a class="btn ghost" href="/devlogs/">Tous les devlogs</a> <a class="btn" href="/below-zero/">Découvrir Below Zero</a></p>
</div>
</article>"""
    words = len(__import__("re").sub("<[^>]+>", " ", BODIES[a["num"]]).split())
    a["words"] = words
    ld = [{
      "@type": "BlogPosting", "@id": BASE + url(a) + "#article", "headline": a["h1"], "description": a["desc"],
      "image": {"@type": "ImageObject", "url": f"{BASE}/assets/img/{a['img']}-1280.webp", "width": 1280, "height": 720},
      "datePublished": DATE, "dateModified": LASTMOD, "inLanguage": "fr-FR", "wordCount": words,
      "author": {"@type": "Person", "name": n, "jobTitle": role, "worksFor": {"@id": ORG}},
      "publisher": {"@id": ORG}, "mainEntityOfPage": {"@id": BASE + url(a) + "#webpage"},
      "isPartOf": {"@id": BASE + "/devlogs/#blog"}, "about": {"@id": BASE + "/below-zero/#videogame"},
      "articleSection": "Devlog"}]
    PAGES.append(dict(path=url(a), title=a["title"], desc=a["desc"], body=body, jsonld=ld, ogtype="article",
        date=DATE, author=n, image=f"/assets/img/{a['img']}-1280.webp", imgalt=a["alt"],
        crumbs=[("/devlogs/", "Devlogs"), (url(a), a["short"])]))
