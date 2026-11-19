import json, os, html, importlib, sys
sys.path.insert(0, os.path.dirname(__file__))
from fmt import pretty
BASE = "https://flexarion-officiel.github.io"
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LASTMOD = "2026-11-19"
ORG = BASE + "/#organization"
SITE = BASE + "/#website"

LOGO_SVG = ('<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" rx="12" fill="#071421"/>'
 '<path d="M9 29 32 7l23 22" fill="none" stroke="#19B9D4" stroke-width="3.5" stroke-linejoin="round"/>'
 '<path d="M9 35l23 22 23-22" fill="none" stroke="#B7DDE8" stroke-width="3.5" stroke-linejoin="round"/>'
 '<path d="M5 32h54" stroke="#19B9D4" stroke-width="2"/>'
 '<path d="M21 28v-6l4-4 4 4v6M35 28v-6l4-4 4 4v6" fill="none" stroke="#19B9D4" stroke-width="2.4"/>'
 '<path d="M21 36v6l4 4 4-4v-6M35 36v6l4 4 4-4v-6" fill="none" stroke="#B7DDE8" stroke-width="2.4"/></svg>')

# ASCII art inséré en commentaire juste après le doctype de chaque page
ASCII = r"""
         /\
        /  \       ___ _    _____  __   _   ___ ___ ___  _  _
       / /\ \     | __| |  | __\ \/ /  /_\ | _ \_ _/ _ \| \| |
    ==<======>==  | _|| |__| _| >  <  / _ \|   /| | (_) | .` |
       \ \/ /     |_| |____|___/_/\_\/_/ \_\_|_\___\___/|_|\_|
        \  /
         \/       Studio de jeux vidéo de science-fiction · Aix-en-Provence

    2156 à la surface. 2306 en dessous.
    Tu lis le code source ? Tu es donc déjà descendu d'un niveau.
    Ouvre la console : quelqu'un t'y attend.
"""

# Versions minifiées servies par le site (générées depuis les sources par minify.py)
CSS_HREF = "/assets/css/style.min.css"
JS_SRC = "/assets/js/main.min.js"
FONT_PRELOAD = "/assets/fonts/exo2-latin.woff2"

NAV = [("/", "Accueil"), ("/studio/", "Le studio"), ("/below-zero/", "Below Zero"), ("/devlogs/", "Devlogs"), ("/contact/", "Contact &amp; presse")]

# (réseau, URL, pseudo, icône Simple Icons CC0 dans /assets/icons/)
SOCIAL_DATA = [
    ("GitHub", "https://github.com/flexarion-officiel", "flexarion-officiel", "github"),
    ("itch.io", "https://flexarionofficiel.itch.io/", "flexarionofficiel", "itchio"),
    ("X", "https://x.com/flexarion_off", "@flexarion_off", "x"),
    ("Instagram", "https://www.instagram.com/flexarion.off/", "@flexarion.off", "instagram"),
]
SOCIALS = [(n, u) for n, u, _, _ in SOCIAL_DATA]

ORG_NODE = {
    "@type": "Organization",
    "@id": ORG,
    "name": "Flexarion",
    "alternateName": ["Flexarion Studio", "Studio Flexarion"],
    "description": "Flexarion est un studio indépendant de jeux vidéo de science-fiction narratifs, fondé en 2022 à Aix-en-Provence et créateur du jeu Below Zero.",
    "url": BASE + "/",
    "logo": {"@type": "ImageObject", "@id": BASE + "/#logo", "url": BASE + "/icon-512.png", "contentUrl": BASE + "/icon-512.png", "width": 512, "height": 512, "caption": "Logo Flexarion"},
    "image": {"@id": BASE + "/#logo"},
    "foundingDate": "2022",
    "knowsAbout": ["jeu vidéo narratif", "science-fiction", "game design", "énigmes temporelles", "sound design"],
    "contactPoint": {"@type": "ContactPoint", "contactType": "presse", "url": BASE + "/contact/", "availableLanguage": "fr"},
    "sameAs": [u for _, u in SOCIALS],
}
SITE_NODE = {"@type": "WebSite", "@id": SITE, "url": BASE + "/", "name": "Flexarion", "alternateName": "Studio Flexarion", "inLanguage": "fr-FR", "publisher": {"@id": ORG}}

def icon(slug, size=20):
    return f'<img class="ico" src="/assets/icons/{slug}.svg" width="{size}" height="{size}" alt="" aria-hidden="true" loading="lazy" decoding="async">'

def social_list():
    """Pied de page : icônes seules, nom accessible via aria-label."""
    lis = "".join(f'<li><a href="{u}" rel="me noopener" target="_blank" aria-label="Flexarion sur {n} ({h})" title="{n}">{icon(i, 24)}</a></li>' for n, u, h, i in SOCIAL_DATA)
    return f'<ul class="socials" aria-label="Flexarion sur les réseaux sociaux">{lis}</ul>'

def social_rows():
    """Page contact : icône • pseudo, liste verticale."""
    lis = "".join(f'<li><a href="{u}" rel="me noopener" target="_blank" aria-label="{n} : {h}">{icon(i)}<span class="sep" aria-hidden="true">•</span><span>{h}</span></a></li>' for n, u, h, i in SOCIAL_DATA)
    return f'<ul class="social-rows">{lis}</ul>'


def esc(s): return html.escape(s, quote=True)

def render(p):
    path = p["path"]; url = BASE + path
    img = p.get("image", "/assets/img/flexarion-og-1200x630.jpg")
    img_abs = BASE + img
    crumbs = p.get("crumbs", [])
    graph = [ORG_NODE, SITE_NODE]
    webpage = {"@type": p.get("pagetype", "WebPage"), "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["desc"],
               "isPartOf": {"@id": SITE}, "about": {"@id": ORG}, "inLanguage": "fr-FR", "dateModified": LASTMOD,
               "primaryImageOfPage": {"@type": "ImageObject", "url": img_abs}}
    if crumbs:
        webpage["breadcrumb"] = {"@id": url + "#breadcrumb"}
        items = [("/", "Accueil")] + crumbs
        graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (u, n) in enumerate(items)]})
    graph.append(webpage)
    graph += p.get("jsonld", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)
    nav = "".join(f'<li><a href="{u}"' + (' aria-current="page"' if (u == path or (u != "/" and path.startswith(u))) else "") + f'>{n}</a></li>' for u, n in NAV)
    bc = ""
    if crumbs:
        items = [("/", "Accueil")] + crumbs
        lis = "".join((f'<li><a href="{u}">{esc(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{esc(n)}</li>') for i, (u, n) in enumerate(items))
        bc = f'<nav class="crumbs wrap" aria-label="Fil d’Ariane"><ol>{lis}</ol></nav>'
    robots = p.get("robots", "index, follow, max-image-preview:large")
    canon = "" if p.get("nocanon") else f'<link rel="canonical" href="{url}">\n'
    extra_head = p.get("head", "")
    ogtype = p.get("ogtype", "website")
    art = ""
    if ogtype == "article":
        art = f'<meta property="article:published_time" content="{p["date"]}">\n<meta property="article:modified_time" content="{LASTMOD}">\n<meta property="article:author" content="{esc(p["author"])}">\n'
    doc = f'''<!doctype html>
<!--{ASCII}-->
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<meta name="robots" content="{robots}">
{canon}<meta name="author" content="Flexarion">
<meta name="theme-color" content="#071421">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="Devlogs Flexarion" href="/devlogs/feed.xml">
<link rel="preload" href="{FONT_PRELOAD}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{CSS_HREF}">
{extra_head}<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Flexarion">
<meta property="og:title" content="{esc(p.get("ogtitle", p["title"]))}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img_abs}">
<meta property="og:image:alt" content="{esc(p.get("imgalt", "Flexarion, studio de jeux vidéo de science-fiction à Aix-en-Provence"))}">
{art}<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p.get("ogtitle", p["title"]))}">
<meta name="twitter:description" content="{esc(p["desc"])}">
<meta name="twitter:image" content="{img_abs}">
<script type="application/ld+json">
{ld}
</script>
</head>
<body id="haut">
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-head">
<div class="wrap head-in">
<a class="brand" href="/" aria-label="Flexarion, retour à l’accueil">{LOGO_SVG}<span>Flexarion</span></a>
<button class="burger" type="button" aria-expanded="false" aria-controls="menu-principal" aria-label="Ouvrir le menu"><span class="burger-bar"></span></button>
<nav class="nav" id="menu-principal" aria-label="Navigation principale"><ul>{nav}</ul></nav>
</div>
</header>
{bc}
<main id="contenu">
{p["body"]}
</main>
<footer class="site-foot">
<div class="wrap">
<p class="foot-logo"><a href="/" aria-label="Flexarion, accueil"><img src="/icon-512.png" srcset="/icon-192.png 192w, /icon-512.png 512w" sizes="72px" width="72" height="72" alt="Logo Flexarion" loading="lazy" decoding="async"></a></p>
<p><strong>Flexarion</strong>, studio indépendant de jeux vidéo de science-fiction à Aix-en-Provence.</p>
<nav aria-label="Plan du site"><ul class="foot-links">
<li><a href="/">Accueil</a></li>
<li><a href="/contact/">Contact &amp; presse</a></li>
<li><a href="/mentions-legales/">Mentions légales</a></li>
</ul></nav>
{social_list()}
<p class="meta">Flexarion est un studio fictif imaginé pour un projet pédagogique du BUT Informatique de l’IUT d’Aix-Marseille.</p>
</div>
</footer>
<a class="to-top" href="#haut" aria-label="Retour en haut de la page"><span aria-hidden="true">↑</span></a>
<script src="{JS_SRC}" defer></script>
</body>
</html>
'''
    if path.endswith(".html"):
        fp = OUT + path
    else:
        fp = OUT + path + "index.html"
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(pretty(doc))
    return fp

def pic(name, alt, w=1280, h=720, lcp=False, sizes="(max-width: 72rem) 100vw, 72rem", cls=""):
    attrs = 'fetchpriority="high" decoding="async"' if lcp else 'loading="lazy" decoding="async"'
    return (f'<img src="/assets/img/{name}-1280.webp" srcset="/assets/img/{name}-480.webp 480w, /assets/img/{name}-960.webp 960w, /assets/img/{name}-1280.webp 1280w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}" {attrs}' + (f' class="{cls}"' if cls else "") + '>')

if __name__ == "__main__":
    pages = []
    for mod in ["c_main", "c_devlogs"]:
        pages += importlib.import_module(mod).PAGES
    for p in pages:
        print(render(p))
    import extras; extras.run(pages)
    import minify; minify.run()
