"""Minification des sources CSS et JS du site (Python 3, sans dépendance).

Sources éditables (ignorées par Git, voir .gitignore) :
  assets/css/style.css  ->  assets/css/style.min.css  (fichier servi)
  assets/css/print.css  ->  assets/css/print.min.css  (impression, chargée avec media="print")
  assets/js/main.js     ->  assets/js/main.min.js     (fichier servi)

Lancé automatiquement à la fin de build.py, ou seul : python3 -B tools/generateur/minify.py
Limite volontaire du minifieur JS : pas de littéraux d'expression régulière dans main.js.
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def _split_strings(src, quotes):
    """Découpe en segments (est_chaine, texte) pour ne jamais modifier l'intérieur des chaînes."""
    out, buf, i = [], "", 0
    while i < len(src):
        c = src[i]
        if c in quotes:
            j = i + 1
            while j < len(src) and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            out.append((False, buf)); buf = ""
            out.append((True, src[i:j + 1])); i = j + 1
        else:
            buf += c; i += 1
    out.append((False, buf))
    return out


def minify_css(css):
    res = []
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    for is_str, part in _split_strings(css, "\"'"):
        if is_str:
            res.append(part); continue
        part = re.sub(r"\s+", " ", part)
        part = re.sub(r"\s*([{};,>])\s*", r"\1", part)
        part = re.sub(r"\s*:\s*", ":", part)       # aucun sélecteur « a :hover » dans la feuille
        part = part.replace(";}", "}")
        res.append(part)
    out = "".join(res).strip()
    # « and(» invalide dans une media query : on remet l'espace
    return re.sub(r"\band\(", "and (", out) + "\n"


_ID = re.compile(r"[A-Za-z0-9_$]")


def minify_js(js):
    out, i, n = [], 0, len(js)
    pending_space = False
    while i < n:
        c = js[i]
        if js.startswith("//", i):
            i = js.find("\n", i); i = n if i < 0 else i; pending_space = True; continue
        if js.startswith("/*", i):
            i = js.index("*/", i) + 2; pending_space = True; continue
        if c in "\"'`":
            j = i + 1
            while js[j] != c:
                j += 2 if js[j] == "\\" else 1
            tok = js[i:j + 1]; i = j + 1
        elif c.isspace():
            pending_space = True; i += 1; continue
        else:
            tok = c; i += 1
        if pending_space and out:
            prev = out[-1][-1]
            # espace nécessaire seulement entre deux caractères d'identifiant, ou pour « + + » / « - - »
            if (_ID.match(prev) and _ID.match(tok[0])) or (prev in "+-" and tok[0] == prev):
                out.append(" ")
        pending_space = False
        out.append(tok)
    return "".join(out) + "\n"


def run():
    pairs = [("assets/css/style.css", "assets/css/style.min.css", minify_css),
             ("assets/css/print.css", "assets/css/print.min.css", minify_css),
             ("assets/js/main.js", "assets/js/main.min.js", minify_js)]
    for src, dst, fn in pairs:
        s = os.path.join(ROOT, src)
        if not os.path.exists(s):
            print("source absente, minification ignorée :", src); continue
        txt = open(s, encoding="utf-8").read()
        mini = fn(txt)
        open(os.path.join(ROOT, dst), "w", encoding="utf-8").write(mini)
        print(f"{dst} : {len(txt.encode())} -> {len(mini.encode())} octets")


if __name__ == "__main__":
    run()
