# Update Log

## 2026-07-19

* **Creation**: [Vhen Joseph — Knowledge Wiki](index.md) bundle created following OKF v0.1.
* **Creation**: [About](about.md), [What I Believe](beliefs.md), [What I'm Building](building.md), [Candice](candice.md), [The Path Here](path.md), [What I Reach For](stack.md), and [Say Hi](contact.md) authored from the content of vhenjoseph.com.

## 2026-08-03

* **Reorganized**: markdown sources kept in `wiki/`, generated pages moved to `wiki/html/`. `_render.py` now outputs to `html/`; canonical URLs updated to `/wiki/html/`.
* **Links**: fixed cross-page `.md` links (root-absolute → bundle-relative) and pointed the main site's Wiki entry at `wiki/html/`. All links verified resolving.

## 2026-08-03 (content refresh)

* **Updated**: [What I'm Building](building.md), [Candice](candice.md), and [What I Reach For](stack.md) refreshed to reflect the native Apple app, the self-maintaining OKF vault with hybrid retrieval, and the privacy/safety engineering (PII masking, prompt-injection screening, daily self-audit).

## 2026-10-05 (Plasmie)

* **Added**: [Plasmie](plasmie.md) — the private, fully on-device work memory that sits
  alongside Candice. Linked from the wiki index, nav and `llms.txt`.
* **Changed**: the home page's Candice band is now a two-card carousel. The next card
  peeks past the edge rather than being announced by a control, so the affordance is the
  layout itself; native scroll-snap does the swiping, and the dots are progressive
  enhancement that the section works without.
* **Added**: Plasmie's mascot as inline SVG, drawn from the app's own shape data and face
  spec (idle: dot eyes and a smile; hi: happy eyes and a grin) rather than redrawn by eye.
