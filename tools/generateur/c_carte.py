# Page « Carte commentée de Sextia sous Aix » (/below-zero/carte-sextia/), version 1.6.0
from build import BASE, ORG, LASTMOD
GAME = BASE + "/below-zero/#videogame"
PATH = "/below-zero/carte-sextia/"

# Carte stylisée (pas un tracé cartographique exact) : SVG inline, palette du site, aucun attribut style
F = 'font-family="Exo 2, system-ui, Arial, sans-serif"'
def marker(n, x, y, label, lx, ly, anchor="start"):
    return (f'<g><circle cx="{x}" cy="{y}" r="15" fill="#071421" stroke="#19B9D4" stroke-width="3"/>'
            f'<text x="{x}" y="{y + 5}" text-anchor="middle" font-size="15" font-weight="700" fill="#E8EDF0" {F}>{n}</text>'
            f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" font-size="16" fill="#E8EDF0" {F}>{label}</text></g>')

SVG = ('<svg viewBox="0 0 800 500" role="img" aria-labelledby="carte-titre carte-desc" xmlns="http://www.w3.org/2000/svg">'
 '<title id="carte-titre">Carte stylisée de Sextia sous le centre d\'Aix-en-Provence</title>'
 '<desc id="carte-desc">Plan simplifié du centre historique d\'Aix-en-Provence, nord en haut. Six lieux réels sont numérotés dans l\'ordre du parcours : '
 '1, le pavillon Vendôme au nord-ouest ; 2, les thermes de Sextius à l\'ouest de la vieille ville ; 3, la cathédrale Saint-Sauveur au nord ; '
 '4, la place des Prêcheurs à l\'est ; 5, le cours Mirabeau au sud ; 6, la Rotonde à l\'extrémité ouest du cours. '
 'Une ligne cyan en pointillés figure les veines d\'eau thermale autour desquelles est creusée Sextia, la ville souterraine de 2306 du jeu Below Zero.</desc>'
 '<rect width="800" height="500" rx="14" fill="#071421"/>'
 '<g stroke="#123A58" stroke-width="1">' + "".join(f'<path d="M{x} 0V500"/>' for x in range(50, 800, 50)) + "".join(f'<path d="M0 {y}H800"/>' for y in range(50, 500, 50)) + '</g>'
 # centre historique
 '<path d="M215 120 Q300 70 420 78 Q560 92 640 170 Q680 250 640 330 Q600 365 520 368 L235 372 Q185 330 190 250 Q192 170 215 120Z" fill="#123A58" stroke="#B7DDE8" stroke-opacity=".45" stroke-width="2"/>'
 f'<text x="470" y="330" text-anchor="middle" font-size="14" fill="#B7DDE8" fill-opacity=".8" {F}>centre historique</text>'
 # veines thermales (Sextia 2306)
 '<path d="M95 300 C170 230 230 180 265 175 C330 165 360 240 430 260 C500 280 560 300 620 420" fill="none" stroke="#19B9D4" stroke-width="3" stroke-dasharray="9 7" stroke-opacity=".85"/>'
 # cours Mirabeau et platanes
 '<path d="M195 395H560" stroke="#B7DDE8" stroke-width="10" stroke-linecap="round"/>'
 '<g fill="#19B9D4">' + "".join(f'<circle cx="{x}" cy="383" r="3"/><circle cx="{x}" cy="407" r="3"/>' for x in range(240, 560, 26)) + '</g>'
 # Rotonde
 '<circle cx="170" cy="395" r="26" fill="none" stroke="#B7DDE8" stroke-width="3"/>'
 # parcours
 '<path d="M140 120 L265 175 L400 105 L580 215 L420 395 L170 395" fill="none" stroke="#E8EDF0" stroke-opacity=".5" stroke-width="2" stroke-dasharray="2 7" stroke-linecap="round"/>'
 + marker(1, 140, 120, "Pavillon Vendôme", 162, 104)
 + marker(2, 265, 175, "Thermes de Sextius", 286, 200)
 + marker(3, 400, 105, "Cathédrale Saint-Sauveur", 422, 88)
 + marker(4, 580, 215, "Place des Prêcheurs", 602, 220)
 + marker(5, 420, 395, "Cours Mirabeau", 420, 440, "middle")
 + marker(6, 170, 395, "La Rotonde", 170, 448, "middle") +
 # boussole
 '<g stroke="#B7DDE8" stroke-width="2" fill="none"><circle cx="740" cy="62" r="26"/><path d="M740 44V80M733 52l7-8 7 8"/></g>'
 f'<text x="740" y="108" text-anchor="middle" font-size="14" fill="#B7DDE8" {F}>N</text>'
 # légende
 '<g><path d="M30 470H70" stroke="#19B9D4" stroke-width="3" stroke-dasharray="9 7"/>'
 f'<text x="80" y="475" font-size="14" fill="#E8EDF0" {F}>veines thermales de Sextia (2306)</text>'
 '<path d="M330 470H370" stroke="#E8EDF0" stroke-opacity=".5" stroke-width="2" stroke-dasharray="2 7" stroke-linecap="round"/>'
 f'<text x="380" y="475" font-size="14" fill="#E8EDF0" {F}>parcours de la carte</text>'
 f'<text x="770" y="475" text-anchor="end" font-size="13" fill="#B7DDE8" {F}>carte stylisée, échelle non respectée</text></g>'
 f'<text x="30" y="40" font-size="20" font-weight="700" fill="#E8EDF0" {F}>Sextia sous Aix</text>'
 f'<text x="30" y="62" font-size="14" fill="#B7DDE8" {F}>Below Zero · six lieux, trois époques</text>'
 '</svg>')

LIEUX = [
 ("pavillon-vendome", "Le pavillon Vendôme, la Maison des retours",
  "Construit à partir de 1665 pour Louis de Mercœur, duc de Vendôme et gouverneur de Provence, comme maison de campagne hors des remparts, le pavillon se dresse au nord-ouest du centre historique, au milieu d'un jardin à la française. Deux atlantes encadrent son entrée et soutiennent le balcon. Propriété de la ville, il accueille aujourd'hui des expositions.",
  "Les bassins du jardin sont vides depuis longtemps et les parterres sont protégés par des voiles d'ombrage. Sous l'allée principale, une ancienne galerie de drainage sert de premier accès au réseau : c'est là que Sacha Morel commence sa tournée.",
  "Le pavillon garde ses proportions, mais les habitants l'appellent la Maison des retours : on y accueille ceux qui viennent de la surface. Les atlantes sont devenus des piliers qui soutiennent un fragment du ciel artificiel, et le jardin est un potager sous lumière tracé selon les mêmes allées."),
 ("thermes-sextius", "Les thermes de Sextius, le Cœur chaud",
  "À l'ouest de la vieille ville, sur le cours Sextius, l'établissement thermal moderne porte le nom du fondateur romain d'Aquae Sextiae et conserve une piscine voûtée d'époque romaine. L'eau chaude qui a fait naître Aix y coule toujours.",
  "La régie des eaux y a installé un poste de pompage. C'est au cours d'une intervention de maintenance sur ce réseau que la paroi cède et que la cavité de Sextia est découverte.",
  "Le Cœur chaud est la centrale de Sextia : il distribue la chaleur et l'énergie de l'eau thermale à tous les quartiers. Dans le hall, une vieille vanne est exposée comme une relique ; les habitants la montrent à Sacha avec un sourire entendu."),
 ("cathedrale-saint-sauveur", "La cathédrale Saint-Sauveur, le Puits des voix",
  "Au nord de la vieille ville, la cathédrale Saint-Sauveur réunit plusieurs époques en un seul édifice : un baptistère octogonal du VIe siècle qui remploie des colonnes antiques, un cloître roman de la fin du XIIe siècle et un portail gothique des XVe et XVIe siècles. Elle abrite le triptyque du Buisson ardent, peint par Nicolas Froment vers 1476.",
  "Ses murs épais gardent la fraîcheur : pendant les canicules, la ville en a fait un refuge. On y entend parler à voix basse de bruits venus de sous les dalles : l'un des premiers indices du jeu.",
  "L'édifice est devenu le Puits des voix, la mémoire de la cité, où les habitants enregistrent leurs souvenirs. Certains parlent de Sacha au passé, alors qu'il n'a pas encore vécu ce qu'ils racontent. Les époques de l'édifice réel y restent lisibles comme des strates de verre."),
 ("place-des-precheurs", "La place des Prêcheurs, la place des Échanges",
  "À l'est de la vieille ville, la place doit son nom aux frères prêcheurs, les dominicains, installés là au XIIIe siècle ; l'église de la Madeleine, ancienne église de leur couvent, la borde. Une fontaine-obélisque de Jean-Pancrace Chastel (1758) se dresse vers la place de la Madeleine. Avec la place de Verdun, elle accueille le grand marché d'Aix les mardis, jeudis et samedis matin.",
  "Le marché sert aussi de point de distribution d'eau les jours de restriction. Les files d'attente y font circuler des rumeurs utiles à noter dans le Carnet de causalité.",
  "La place des Échanges est le marché de Sextia. On y échange une réparation contre un objet, un service contre un souvenir. L'obélisque est devenu un mât lumineux qui donne l'heure du ciel artificiel, et une marchande garde pour Sacha un objet qu'il n'a pas encore perdu."),
 ("cours-mirabeau", "Le cours Mirabeau, la Grande Allée",
  "Aménagé à partir de 1649 à l'emplacement du rempart sud et simplement appelé « le Cours » à l'origine, il porte depuis 1876 le nom de Mirabeau, élu du tiers état d'Aix en 1789. Bordé de platanes, il est ponctué de fontaines : la fontaine des Neuf-Canons, la fontaine moussue, alimentée par une eau chaude, et, à son extrémité est, la fontaine du Roi René.",
  "Les platanes tiennent grâce à des tuteurs métalliques et la plupart des fontaines sont à sec. Seule la fontaine moussue coule encore : un détail facile à manquer, et l'un des liens avec la ville d'en dessous.",
  "La Grande Allée est l'artère lumineuse de Sextia, bordée de colonnes végétales qui suivent l'alignement des anciens platanes. Ses fontaines sont devenues des stations du réseau d'eau dont le débit sert d'horloge aux habitants."),
 ("rotonde", "La Rotonde, le Carrefour des trois veilleuses",
  "Mise en eau en 1860 au centre de la place du Général-de-Gaulle, à l'extrémité ouest du cours Mirabeau, la fontaine de la Rotonde mesure 12 mètres de haut. Elle est couronnée de trois statues qui représentent la Justice, l'Agriculture et les Beaux-Arts, tournées respectivement vers le cours Mirabeau, Marseille et Avignon.",
  "La Rotonde reste le grand carrefour de la ville, mais la fontaine tourne au ralenti. Sacha y revient souvent pour vérifier, d'un coup d'œil, si un geste fait ailleurs a changé quelque chose.",
  "Au même endroit, Sextia a bâti le Carrefour des trois veilleuses. Les trois statues y incarnent les principes de la cité : le partage de l'eau, la culture sous lumière et la garde de la mémoire. Elles regardent dans les mêmes directions qu'à la surface, ce qui aide le joueur à s'orienter."),
]

def fiche(i, l):
    k, t, today, y2156, y2306 = l
    return (f'<section class="lieu" id="{k}" aria-labelledby="t-{k}"><h3 id="t-{k}">{i}. {t}</h3><dl>'
            f'<dt>Aujourd\'hui à Aix-en-Provence</dt><dd>{today}</dd>'
            f'<dt>En 2156, dans Below Zero</dt><dd>{y2156}</dd>'
            f'<dt>Dans Sextia, en 2306</dt><dd>{y2306}</dd></dl></section>')

TOC = "".join(f'<li><a href="#{l[0]}">{l[1]}</a></li>' for l in LIEUX)
FICHES = "".join(fiche(i + 1, l) for i, l in enumerate(LIEUX))

INTRO = """
<p class="lead">Sous le centre d'Aix-en-Provence, Below Zero imagine une ville futuriste entière : Sextia, une cité de l'an 2306 découverte en 2156 par Sacha Morel. Cette carte commentée suit six lieux réels d'Aix, du pavillon Vendôme à la Rotonde, et montre ce que chacun devient dans les deux époques de notre jeu vidéo de science-fiction, entre 2156 et 2306.</p>

<div class="facts" role="note" aria-label="Repères de la carte"><dl>
<dt>Parcours</dt><dd>Six lieux réels du centre d'Aix-en-Provence</dd>
<dt>Trois époques</dt><dd>Aix aujourd'hui, Aix en 2156 dans le jeu, Sextia en 2306</dd>
<dt>Type de carte</dt><dd>Carte stylisée, nord en haut, distances et échelle non respectées</dd>
<dt>Cadre</dt><dd>Lieux et faits historiques réels ; studio Flexarion, Below Zero et Sextia fictifs</dd>
</dl></div>
"""

BODY_A = """
<h2 id="pourquoi">Une carte pour lire Sextia, la ville futuriste sous Aix</h2>
<p>Dans le <a href="/devlogs/concevoir-sextia-vrai-aix/">devlog sur la conception de Sextia à partir du vrai Aix</a>, Élise Fabre racontait comment l'équipe a relevé les rues, les places et l'eau de la ville pour bâtir le décor. Cette page prend l'angle inverse : elle décrit le monde du jeu tel que ses habitants le vivent. Quelle fonction a chaque lieu dans la société de Sextia, et qu'en reste-t-il à la surface en 2156 ?</p>
<p>Nous avons retenu six lieux qui forment une boucle autour de la vieille ville, du nord-ouest jusqu'au carrefour de la Rotonde, et qui jouent chacun un rôle distinct dans l'histoire.</p>

<h2 id="lire-la-carte">Comment lire la carte : trois époques sur un même plan</h2>
<p>Les deux villes de Below Zero partageant un seul plan, une carte suffit pour les deux époques ; les numéros suivent l'ordre du parcours. La ligne cyan en pointillés figure les veines d'eau thermale autour desquelles la cavité de Sextia a été creusée ; elles ne correspondent à aucun relevé géologique réel.</p>
"""

FIG = '<figure class="carte">' + SVG + '<figcaption>Carte stylisée de Sextia sous le centre d\'Aix-en-Provence : six lieux réels numérotés, les veines thermales de la ville souterraine et le parcours proposé. Les distances ne sont pas à l\'échelle.</figcaption></figure>'

BODY_B = """
<nav class="toc" aria-label="Les six lieux de la carte"><strong>Les six lieux de la carte</strong><ol>""" + TOC + """</ol></nav>

<h2 id="six-lieux">Six lieux d'Aix-en-Provence, de nos jours à 2306</h2>
<p>Chaque fiche suit la même grille : le lieu tel qu'on le voit aujourd'hui à Aix (faits réels), puis ce qu'il devient en 2156 et en 2306 dans l'univers du jeu.</p>
""" + FICHES + """

<h2 id="hors-carte">Ce que la carte de science-fiction ne montre pas encore</h2>
<p>Cette carte reste volontairement incomplète : les quartiers d'habitation et les galeries qui relient les lieux n'y figurent pas, pour ne pas dévoiler les énigmes du jeu.</p>
<p>Une règle traverse le parcours : un lieu de Sextia garde l'emplacement de son modèle aixois, mais change presque toujours de fonction. Le pavillon de plaisance devient un lieu d'accueil, l'établissement thermal une centrale, la cathédrale une mémoire, le marché un lieu de troc. C'est en comparant ces usages que le joueur comprend ce que le futur attend de Sacha. Ces liens entre les époques sont détaillés dans le <a href="/devlogs/enigmes-causalite-temporelle/">devlog sur les énigmes de causalité temporelle</a>.</p>

<h2 id="explorer">Explorer Below Zero, jeu vidéo de science-fiction, et le studio Flexarion</h2>
<p>Cette carte ouvre l'univers de <a href="/below-zero/">Below Zero, notre jeu de science-fiction narratif sans combat</a>. Le <a href="/devlogs/concevoir-deux-villes-aix-2156-2306/">devlog sur les deux villes jumelles</a> explique comment un seul plan sert aux deux époques. Pour savoir pourquoi un studio de jeu vidéo indépendant a choisi Aix pour décor, lisez <a href="/devlogs/creer-studio-jeu-video-aix/">l'histoire de la création du studio à Aix-en-Provence</a> ou rencontrez <a href="/studio/">l'équipe du studio Flexarion</a>.</p>
<p>Rappel : ces six lieux existent bel et bien à Aix-en-Provence ; le studio Flexarion, l'Aix de 2156 et la cité de Sextia appartiennent à une œuvre de fiction.</p>
"""

BODY = f"""<div class="wrap">
<p class="kicker">Univers de Below Zero</p>
<h1>Carte de Sextia : six lieux d'Aix-en-Provence dans la ville futuriste de 2306</h1>
<div class="prose">
{INTRO}
{BODY_A}
</div>
{FIG}
<div class="prose">
{BODY_B}
<p><a class="btn" href="/below-zero/">Découvrir Below Zero</a> <a class="btn ghost" href="/devlogs/">Lire les devlogs</a></p>
</div>
</div>"""

import re as _re
WORDS = len(_re.sub("<[^>]+>", " ", INTRO + BODY_A + BODY_B).split())

TITLE = "Carte de Sextia, ville du jeu vidéo SF sous Aix | Flexarion"
DESC = "Sextia, ville futuriste du jeu vidéo SF Below Zero : carte de six lieux réels d'Aix-en-Provence revus en 2156 et 2306 par le studio Flexarion."
H1 = "Carte de Sextia : six lieux d'Aix-en-Provence dans la ville futuriste de 2306"

AIX = {"@type": "City", "name": "Aix-en-Provence", "containedInPlace": {"@type": "AdministrativeArea", "name": "Bouches-du-Rhône"}}
PLACES = ["Pavillon Vendôme", "Thermes de Sextius", "Cathédrale Saint-Sauveur d'Aix-en-Provence", "Place des Prêcheurs", "Cours Mirabeau", "Fontaine de la Rotonde"]
MAP = {"@type": "Map", "@id": BASE + PATH + "#carte", "name": "Carte commentée de Sextia sous Aix-en-Provence",
  "description": "Carte stylisée situant six lieux réels du centre d'Aix-en-Provence et leur transposition dans Sextia, la ville souterraine de 2306 du jeu Below Zero.",
  "inLanguage": "fr-FR", "dateModified": LASTMOD, "wordCount": WORDS,
  "author": {"@id": ORG}, "publisher": {"@id": ORG}, "creator": {"@id": ORG},
  "isPartOf": {"@id": BASE + PATH + "#webpage"}, "about": {"@id": GAME},
  "genre": "Science-fiction", "keywords": "Sextia, Below Zero, Aix-en-Provence, ville futuriste, science-fiction, studio de jeu vidéo",
  "spatialCoverage": AIX,
  "mentions": [{"@type": "Place", "name": n, "containedInPlace": {"@type": "City", "name": "Aix-en-Provence"}} for n in PLACES]}

PAGES = [dict(path=PATH, title=TITLE, desc=DESC, body=BODY, jsonld=[MAP],
  crumbs=[("/below-zero/", "Below Zero"), (PATH, "Carte de Sextia")],
  image="/assets/img/devlog-sextia-aix-1280.webp",
  imgalt="Vue en coupe d'Aix-en-Provence et de Sextia, la ville futuriste souterraine de 2306 du jeu Below Zero")]
