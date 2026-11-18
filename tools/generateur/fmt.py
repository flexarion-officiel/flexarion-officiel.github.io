"""Mise en forme (indentation à 2 espaces) du HTML produit par le générateur.

Règle : un élément qui ne contient que des éléments de type « bloc » est
développé sur plusieurs lignes ; tout autre élément (texte, liens, etc.)
est écrit sur une seule ligne.
"""
import re
from html.parser import HTMLParser

VOID = {"meta", "link", "img", "br", "hr", "input", "source", "path", "rect", "circle"}
BLOCK = {"html", "head", "body", "header", "nav", "main", "footer", "section", "article", "aside",
         "div", "ul", "ol", "li", "dl", "dt", "dd", "figure", "figcaption", "p", "h1", "h2", "h3",
         "h4", "h5", "h6", "details", "summary", "blockquote", "title", "meta", "link", "script",
         "button", "noscript", "picture", "source"}
RAW = {"script", "style"}


class Node:
    def __init__(self, tag, start="", parent=None):
        self.tag, self.start, self.parent, self.children = tag, start, parent, []


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.root = Node("#root")
        self.cur = self.root
        self.decl = ""

    def handle_decl(self, d):
        self.decl = f"<!{d}>"

    def handle_starttag(self, tag, attrs):
        n = Node(tag, self.get_starttag_text(), self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, self.get_starttag_text(), self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, d):
        self.cur.children.append(d)

    def handle_entityref(self, name):
        self.cur.children.append(f"&{name};")

    def handle_charref(self, name):
        self.cur.children.append(f"&#{name};")


def inline(n):
    if isinstance(n, str):
        return re.sub(r"\s+", " ", n)
    if n.tag in VOID:
        return n.start
    inner = "".join(inline(c) for c in n.children)
    inner = re.sub(r"\s+", " ", inner)
    if n.tag in ("p", "li", "dd", "dt", "h1", "h2", "h3", "figcaption", "summary", "title", "a", "button"):
        inner = inner.strip()
    return f"{n.start}{inner}</{n.tag}>"


def is_container(n):
    if isinstance(n, str) or n.tag in VOID or n.tag in RAW:
        return False
    if any(isinstance(c, str) and c.strip() for c in n.children):
        return False
    elems = [c for c in n.children if not isinstance(c, str)]
    return bool(elems) and any(c.tag in BLOCK for c in elems)


def out(n, depth, lines):
    pad = "  " * depth
    if isinstance(n, str):
        if n.strip():
            lines.append(pad + re.sub(r"\s+", " ", n).strip())
        return
    if n.tag in RAW:
        body = "".join(c for c in n.children if isinstance(c, str)).strip("\n")
        if not body.strip():
            lines.append(pad + f"{n.start}</{n.tag}>")
            return
        lines.append(pad + n.start)
        for l in body.splitlines():
            lines.append(pad + "  " + l if l.strip() else "")
        lines.append(pad + f"</{n.tag}>")
        return
    if is_container(n):
        lines.append(pad + n.start)
        for c in n.children:
            out(c, depth + 1, lines)
        lines.append(pad + f"</{n.tag}>")
    else:
        lines.append(pad + inline(n))


def pretty(doc):
    b = Builder()
    b.feed(doc)
    lines = [b.decl] if b.decl else []
    for c in b.root.children:
        # <html> et ses enfants directs (head, body) restent au niveau 0 / 1
        out(c, 0, lines)
    return "\n".join(lines) + "\n"
