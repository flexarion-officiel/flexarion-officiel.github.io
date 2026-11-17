import json, os, html, importlib, sys
sys.path.insert(0, os.path.dirname(__file__))
BASE = "https://flexarion-officiel.github.io"
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
LASTMOD = "2026-11-17"
ORG = BASE + "/#organization"
SITE = BASE + "/#website"

LOGO_SVG = ('<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false"><rect width="64" height="64" rx="12" fill="#071421"/>'
 '<path d="M9 29 32 7l23 22" fill="none" stroke="#19B9D4" stroke-width="3.5" stroke-linejoin="round"/>'
 '<path d="M9 35l23 22 23-22" fill="none" stroke="#B7DDE8" stroke-width="3.5" stroke-linejoin="round"/>'
 '<path d="M5 32h54" stroke="#19B9D4" stroke-width="2"/>'
 '<path d="M21 28v-6l4-4 4 4v6M35 28v-6l4-4 4 4v6" fill="none" stroke="#19B9D4" stroke-width="2.4"/>'
 '<path d="M21 36v6l4 4 4-4v-6M35 36v6l4 4 4-4v-6" fill="none" stroke="#B7DDE8" stroke-width="2.4"/></svg>')

NAV = [("/", "Accueil"), ("/studio/", "Le studio"), ("/below-zero/", "Below Zero"), ("/devlogs/", "Devlogs"), ("/contact/", "Contact &amp; presse")]

ORG_NODE = {
  "@type": ["Organization", "LocalBusiness"],
  "@id": ORG,
  "name": "Flexarion",
  "alternateName": "Studio Flexarion",
  "description": "Flexarion est un studio indépendant (fictif) de jeux vidéo de science-fiction narratifs basé à Aix-en-Provence, fondé en 2022, auteur du jeu Below Zero.",
  "url": BASE + "/",
  "logo": {"@type": "ImageObject", "url": BASE + "/icon-512.png", "width": 512, "height": 512},
  "image": BASE + "/assets/img/flexarion-og-1200x630.jpg",
  "foundingDate": "2022",
  "foundingLocation": {"@type": "Place", "name": "Aix-en-Provence"},
  "numberOfEmployees": {"@type": "QuantitativeValue", "value": 8},
  "knowsAbout": ["jeu vidéo narratif", "science-fiction", "game design", "énigmes temporelles", "sound design"],
  "address": {"@type": "PostalAddress", "addressLocality": "Aix-en-Provence", "postalCode": "13100", "addressRegion": "Provence-Alpes-Côte d'Azur", "addressCountry": "FR"},
  "geo": {"@type": "GeoCoordinates", "latitude": 43.5297, "longitude": 5.4474},
  "areaServed": "FR",
  "email": "contact@flexarion-officiel.github.io",
  "contactPoint": {"@type": "ContactPoint", "contactType": "presse", "email": "contact@flexarion-officiel.github.io", "availableLanguage": "fr", "areaServed": "FR"},
  "sameAs": ["https://github.com/flexarion-officiel"]
}
SITE_NODE = {"@type": "WebSite", "@id": SITE, "url": BASE + "/", "name": "Flexarion", "inLanguage": "fr-FR", "publisher": {"@id": ORG}}

CSS = open(os.path.join(OUT, "assets/css/style.css"), encoding="utf-8").read().split("*/", 1)[1].strip()

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
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
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
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<meta name="robots" content="{robots}">
{canon}<meta name="author" content="Flexarion">
<meta name="theme-color" content="#071421">
<meta name="geo.region" content="FR-13">
<meta name="geo.placename" content="Aix-en-Provence">
<meta name="geo.position" content="43.5297;5.4474">
<meta name="ICBM" content="43.5297, 5.4474">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="Devlogs Flexarion" href="/devlogs/feed.xml">
<style>{CSS}</style>
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
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-head">
<div class="wrap">
<a class="brand" href="/" aria-label="Flexarion, retour à l’accueil">{LOGO_SVG}<span>Flexarion</span></a>
<nav class="nav" aria-label="Navigation principale"><ul>{nav}</ul></nav>
</div>
</header>
{bc}
<main id="contenu">
{p["body"]}
</main>
<footer class="site-foot">
<div class="wrap">
<p><strong>Flexarion</strong> — studio indépendant de jeux vidéo de science-fiction, Aix-en-Provence (Bouches-du-Rhône, Provence-Alpes-Côte d’Azur, France). Créateur de <a href="/below-zero/">Below Zero</a>.</p>
<ul>
<li><a href="/studio/">Le studio</a></li>
<li><a href="/below-zero/">Below Zero</a></li>
<li><a href="/devlogs/">Devlogs</a></li>
<li><a href="/contact/">Contact &amp; presse</a></li>
<li><a href="/mentions-legales/">Mentions légales</a></li>
</ul>
<p class="meta">Flexarion est un studio fictif imaginé pour un projet pédagogique du BUT Informatique de l’IUT d’Aix-Marseille. Visuels générés par IA. <a href="/mentions-legales/">En savoir plus</a>.</p>
</div>
</footer>
{p.get("scripts", "")}</body>
</html>
'''
    if path.endswith(".html"):
        fp = OUT + path
    else:
        fp = OUT + path + "index.html"
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(doc)
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
