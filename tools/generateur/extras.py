from build import BASE, OUT, LASTMOD, LOGO_SVG
import json
def run(pages):
    urls = [p for p in pages if not p["path"].endswith(".html") and "noindex" not in p.get("robots", "")]
    pri = {"/": "1.0", "/below-zero/": "0.9", "/studio/": "0.8", "/devlogs/": "0.8", "/contact/": "0.6", "/mentions-legales/": "0.3"}
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    for p in urls:
        img = p.get("image", "/assets/img/flexarion-og-1200x630.jpg")
        sm += f'  <url>\n    <loc>{BASE}{p["path"]}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <priority>{pri.get(p["path"], "0.7")}</priority>\n    <image:image><image:loc>{BASE}{img}</image:loc></image:image>\n  </url>\n'
    open(OUT + "/sitemap.xml", "w").write(sm + "</urlset>\n")
    open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {BASE}/sitemap.xml\n")
    from c_devlogs import ARTICLES, AUTHORS, url
    from xml.sax.saxutils import escape
    items = "".join(f'''  <item>
    <title>{escape(a["h1"])}</title>
    <link>{BASE}{url(a)}</link>
    <guid isPermaLink="true">{BASE}{url(a)}</guid>
    <pubDate>{a["rss"]}</pubDate>
    <description>{escape(a["desc"])}</description>
  </item>
''' for a in ARTICLES)
    open(OUT + "/devlogs/feed.xml", "w").write(f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>Devlogs Flexarion</title>
  <link>{BASE}/devlogs/</link>
  <atom:link href="{BASE}/devlogs/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Le journal de développement de Below Zero par le studio Flexarion (Aix-en-Provence).</description>
  <language>fr-fr</language>
  <lastBuildDate>Tue, 24 Nov 2026 15:00:00 +0100</lastBuildDate>
{items}</channel>
</rss>
''')
    svg = LOGO_SVG.replace(' aria-hidden="true" focusable="false"', ' xmlns="http://www.w3.org/2000/svg"')
    open(OUT + "/favicon.svg", "w").write(svg + "\n")
    json.dump({"name": "Flexarion — studio de jeux vidéo SF", "short_name": "Flexarion", "lang": "fr", "start_url": "/", "scope": "/",
               "display": "standalone", "background_color": "#071421", "theme_color": "#071421",
               "description": "Studio indépendant de jeux vidéo de science-fiction à Aix-en-Provence, créateur de Below Zero.",
               "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
                         {"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]},
              open(OUT + "/site.webmanifest", "w"), ensure_ascii=False, indent=2)
    from build import SOCIALS
    socials = "\n".join(f"- {n} : {u}" for n, u in SOCIALS)
    dl = "\n".join(f"- [{a['h1']}]({BASE}{url(a)}) : {a['desc']}" for a in ARTICLES)
    open(OUT + "/llms.txt", "w").write(f"""# Flexarion

> Flexarion est un studio indépendant de jeux vidéo de science-fiction narratifs basé à Aix-en-Provence (Bouches-du-Rhône, France), fondé en 2022. Son jeu phare est Below Zero.

## Faits clés
- Nom : Flexarion
- Activité : studio indépendant de jeux vidéo, genre science-fiction, jeux narratifs sans combat
- Localisation : Aix-en-Provence, Provence-Alpes-Côte d'Azur, France
- Création : 2022
- Équipe : 8 métiers — directrice créative, 2 développeurs, game designer, artiste 3D, character designer, sound designer, responsable communication
- Positionnement : expériences immersives où les décisions du joueur influencent directement l'univers du jeu
- Jeu phare : Below Zero (aventure narrative de science-fiction, PC, en développement, date de sortie non annoncée)
- Site officiel : {BASE}/

## Below Zero en résumé
En 2156, une deuxième ville est découverte sous Aix-en-Provence. Elle ressemble exactement à celle de la surface mais semble appartenir à l'année 2306 ; ses habitants l'appellent Sextia, en référence à Aquae Sextiae, nom latin d'Aix-en-Provence, ville fondée en 122 av. J.-C. par le consul Caius Sextius Calvinus près de sources thermales. Le joueur incarne Sacha Morel, un jeune technicien des réseaux souterrains, que les habitants du futur connaissent déjà. Chaque action réalisée dans le présent peut modifier le futur. Mécaniques : exploration de deux époques sur un même plan, énigmes de causalité temporelle (boucle observer, supposer, agir, vérifier), mémoire des habitants, carnet de causalité, plusieurs fins.

## Pages principales
- [Accueil]({BASE}/) : présentation du studio Flexarion et de son positionnement, FAQ
- [Le studio]({BASE}/studio/) : histoire depuis 2022, équipe, ancrage à Aix-en-Provence
- [Below Zero]({BASE}/below-zero/) : univers, mécaniques, visuels, FAQ du jeu
- [Carte de Sextia]({BASE}/below-zero/carte-sextia/) : carte commentée de six lieux réels d'Aix-en-Provence (pavillon Vendôme, thermes de Sextius, cathédrale Saint-Sauveur, place des Prêcheurs, cours Mirabeau, Rotonde) et de leur transposition en 2156 et dans Sextia en 2306
- [Devlogs]({BASE}/devlogs/) : journal de développement
- [Contact et presse]({BASE}/contact/) : kit presse, fiche d'identité, visuels

## Devlogs
{dl}

## Réseaux officiels
{socials}
""")
