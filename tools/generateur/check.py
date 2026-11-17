import re, json, os, glob, html.parser
R=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
errs=0; titles={}; descs={}
for f in glob.glob(R+"/**/*.html", recursive=True):
    s=open(f).read()
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try: json.loads(b)
        except Exception as e: print("JSON-LD KO", f, e); errs+=1
    t=re.search(r"<title>(.*?)</title>",s).group(1); titles.setdefault(t,[]).append(f)
    d=re.search(r'name="description" content="(.*?)"',s).group(1); descs.setdefault(d,[]).append(f)
    if len(d)>160 or len(d)<70: print("desc len",len(d),f)
    if len(t)>70: print("title len",len(t),f)
    h1=len(re.findall(r"<h1",s))
    if h1!=1: print("H1 count",h1,f)
    for img in re.findall(r"<img[^>]*>",s):
        if 'alt="' not in img or 'width=' not in img: print("img attr",f,img[:80]); errs+=1
    for u in re.findall(r'(?:href|src)="([^"#]*)', s)+[x.split()[0] for x in re.findall(r'srcset="([^"]*)"',s) for x in x.split(",")]:
        u=u.strip()
        if not u or u.startswith(("http","mailto")): 
            if "flexarion-studio" in u: print("LIEN INTERDIT",u,f); errs+=1
            continue
        p=R+u
        if u.endswith("/"): p+="index.html"
        if not os.path.exists(p): print("BROKEN",u,"in",f); errs+=1
for k,v in titles.items():
    if len(v)>1: print("dup title",k)
for k,v in descs.items():
    if len(v)>1: print("dup desc",k)
json.load(open(R+"/site.webmanifest"))
import xml.dom.minidom as X
X.parse(R+"/sitemap.xml"); X.parse(R+"/devlogs/feed.xml")
print("pages", len(titles), "errors", errs)
