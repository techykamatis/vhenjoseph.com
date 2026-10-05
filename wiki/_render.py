#!/usr/bin/env python3
"""Render the OKF markdown bundle to browsable HTML for vhenjoseph.com/wiki.

Canonical source stays the .md files (OKF v0.1). Run: python3 _render.py
"""
import re
import glob
import os
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "html")
BASE = "https://vhenjoseph.com/"
OG_IMAGE = BASE + "og-20260709-012144.png"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("beliefs.html", "Beliefs"),
    ("building.html", "Building"),
    ("candice.html", "Candice"),
    ("plasmie.html", "Plasmie"),
    ("path.html", "Path"),
    ("stack.html", "Stack"),
    ("contact.html", "Contact"),
]

JSONLD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Vhen Joseph",
  "jobTitle": "AI Product Engineer Lead",
  "url": "https://vhenjoseph.com/",
  "email": "vhenjoseph@gmail.com",
  "address": {"@type": "PostalAddress", "addressLocality": "Kuala Lumpur", "addressCountry": "MY"},
  "sameAs": [
    "https://linkedin.com/in/vhenjoseph",
    "https://github.com/techykamatis",
    "https://candiceai.vhenjoseph.com/"
  ]
}
</script>'''

CLARITY = '''<script type="text/javascript">
  (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
  })(window, document, "clarity", "script", "y0rbsvyb9k");
</script>'''

CSS = '''
:root{--paper:#F5F3EF;--surface:#fff;--wash:#EFEBE4;--ink:#1A1A1A;--body:#3A3630;--muted:#8B8378;--line:rgba(26,26,26,.14);--contrast:#1A1A1A;--con-ink:#F5F3EF}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--body);line-height:1.7;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
font-size:18px;-webkit-font-smoothing:antialiased}
a{color:var(--ink);text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--muted)}
a:hover{text-decoration-color:var(--ink)}
.topbar{background:var(--contrast);color:var(--con-ink)}
.topbar .wrap{max-width:820px;margin:0 auto;padding:.85rem 1.2rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}
.brand{color:var(--con-ink);text-decoration:none;font-weight:700;letter-spacing:-.02em;font-size:1.1rem}
.brand:hover{text-decoration:none}
.topbar .site{color:var(--muted);text-decoration:none;font-size:.9rem}
nav.main{background:#111;border-top:1px solid rgba(245,243,239,.12)}
nav.main .wrap{max-width:820px;margin:0 auto;padding:.35rem 1.2rem;display:flex;gap:.15rem;flex-wrap:wrap}
nav.main a{color:#cfc7ba;text-decoration:none;font-size:.88rem;padding:.35rem .6rem;border-radius:6px}
nav.main a:hover,nav.main a.active{background:rgba(245,243,239,.12);color:var(--con-ink)}
main{max-width:720px;margin:0 auto;padding:2rem 1.2rem 3.5rem}
h1{font-family:Georgia,"Times New Roman",serif;font-weight:700;color:var(--ink);
font-size:clamp(34px,6vw,54px);line-height:1.08;letter-spacing:-.03em;margin:.2rem 0 1.2rem}
h2{font-family:Georgia,"Times New Roman",serif;color:var(--ink);font-size:1.5rem;
letter-spacing:-.02em;margin:2.4rem 0 .5rem}
p{margin:.9rem 0}
ul{padding-left:1.2rem}li{margin:.35rem 0}
strong{color:var(--ink)}
.pill{display:inline-block;font-size:.7rem;font-weight:700;text-transform:uppercase;
letter-spacing:1px;color:var(--muted);border:1px solid var(--line);padding:.2rem .6rem;border-radius:999px;margin-bottom:1rem}
.pill+h1{margin-top:.2rem}
.lead{color:var(--muted)}
footer{background:var(--contrast);color:var(--con-ink);margin-top:1rem}
footer .wrap{max-width:720px;margin:0 auto;padding:1.6rem 1.2rem;font-size:.9rem;color:#cfc7ba}
footer a{color:var(--con-ink)}
'''


def parse(md_path):
    raw = open(md_path, encoding="utf-8").read()
    meta, body = {}, raw
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        body = m.group(2)
    return meta, body


def title_of(meta, body, slug):
    if meta.get("title"):
        return meta["title"]
    h = re.search(r"^#\s+(.+)$", body, re.M)
    return h.group(1).strip() if h else slug


def render(md_path):
    slug = os.path.splitext(os.path.basename(md_path))[0]
    meta, body = parse(md_path)
    title = title_of(meta, body, slug)
    desc = meta.get("description", "Vhen Joseph — AI Product Engineer Lead, Kuala Lumpur.")

    html_body = markdown.markdown(body, extensions=["extra", "sane_lists"])
    html_body = re.sub(r'href="/([^"/:]+?)\.md"', r'href="\1.html"', html_body)
    html_body = re.sub(r'href="([^":/]+?)\.md"', r'href="\1.html"', html_body)
    html_body = re.sub(r"^\s*<h1>.*?</h1>", "", html_body, count=1, flags=re.S)

    pill = f'<span class="pill">{meta["type"]}</span>' if meta.get("type") else ""
    nav_parts = []
    for href, label in NAV:
        cls = ' class="active"' if href == slug + ".html" else ""
        nav_parts.append(f'<a href="{href}"{cls}>{label}</a>')
    nav = "".join(nav_parts)

    page_title = f"{title} — Vhen Joseph" if slug != "index" else "Vhen Joseph — Knowledge Wiki"

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{page_title}</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="{BASE}wiki/html/{slug}.html" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{BASE}wiki/html/{slug}.html" />
<meta property="og:title" content="{page_title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:image" content="{OG_IMAGE}" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="Vhen Joseph — AI Product Engineer, Kuala Lumpur" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{page_title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{OG_IMAGE}" />
<style>{CSS}</style>
{JSONLD}
{CLARITY}
</head>
<body>
<header class="topbar"><div class="wrap">
  <a class="brand" href="index.html">Vhen Joseph</a>
  <a class="site" href="{BASE}">&larr; vhenjoseph.com</a>
</div></header>
<nav class="main"><div class="wrap">{nav}</div></nav>
<main>
  {pill}
  <h1>{title}</h1>
  {html_body}
</main>
<footer><div class="wrap">
  <strong>Vhen Joseph</strong> — AI Product Engineer Lead, Kuala Lumpur<br>
  <a href="mailto:vhenjoseph@gmail.com">vhenjoseph@gmail.com</a> ·
  <a href="https://linkedin.com/in/vhenjoseph">LinkedIn</a> ·
  <a href="https://github.com/techykamatis">GitHub</a> ·
  <a href="{BASE}">Main site</a><br>
  <span style="opacity:.6">Structured with the Open Knowledge Format (OKF v0.1).</span>
</div></footer>
</body>
</html>'''


def main():
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for md_path in sorted(glob.glob(os.path.join(HERE, "*.md"))):
        slug = os.path.splitext(os.path.basename(md_path))[0]
        if slug == "log":
            continue
        open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8").write(render(md_path))
        n += 1
        print("rendered", "html/" + slug + ".html")
    print(f"done: {n} pages")


if __name__ == "__main__":
    main()
