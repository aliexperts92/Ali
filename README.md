# Signature Restaurant — Website

A stunning, fully responsive multi-page website for **Signature**, the
MICHELIN-recommended fine-dining restaurant at Signia by Hilton La Cantera
Resort & Spa, San Antonio, TX. Built with **Flask + Jinja2**, vanilla CSS and
vanilla JavaScript — no build step, no heavy frameworks.

> French technique. Texas soul.

---

## Features

- **8 pages + custom 404**: Home, Menu, Experience/About, Private Events,
  Gallery, Reservations, Contact, and a styled 404.
- **Design system**: CSS custom properties for the full palette + type scale,
  fluid typography with `clamp()`, CSS Grid/Flexbox, mobile-first.
- **Cinematic motion**: full-screen Ken-Burns hero, transparent→solid sticky
  nav, scroll-reveal via `IntersectionObserver`, hover micro-interactions —
  all respecting `prefers-reduced-motion`.
- **Vanilla JS only**: nav scroll state, full-screen mobile menu, scroll
  reveal, accessible gallery lightbox, dynamic footer year.
- **Forms**: Contact + Events inquiry forms POST to Flask, validate
  server-side, flash a styled success message, and append to
  `submissions.json` (falls back to logging).
- **SEO**: per-page `<title>` + meta description, Open Graph tags,
  JSON-LD `Restaurant` structured data, `/robots.txt`, `/sitemap.xml`.
- **Accessibility**: semantic HTML5, skip link, ARIA on the menu toggle,
  lightbox dialog and form fields, keyboard-focusable interactions.

---

## Quick start

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the development server
export FLASK_APP=app.py            # Windows (PowerShell): $env:FLASK_APP="app.py"
export FLASK_DEBUG=1               # optional: auto-reload
flask run
```

Then open <http://127.0.0.1:5000>.

You can also run it directly:

```bash
python app.py
```

---

## Production

Use a WSGI server rather than the Flask dev server. Uncomment your preferred
option in `requirements.txt`, then:

```bash
# waitress (cross-platform)
pip install waitress
waitress-serve --listen=0.0.0.0:8000 app:app

# gunicorn (Linux/macOS)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Set a strong `SECRET_KEY` (used for flash messages) via environment in
production and update `app.config["SECRET_KEY"]` to read from it.

---

## Project structure

```
signature-website/
├── app.py                 # Flask app, routes, form handlers, robots/sitemap
├── data.py                # All verified business + menu + team content
├── requirements.txt
├── README.md
├── _IMAGE-LIST.md         # Every image needed: path, size, descriptive brief
├── .gitignore
├── static/
│   ├── css/style.css      # Design tokens + components
│   ├── js/main.js         # Nav, scroll reveal, lightbox, year
│   └── images/            # Drop real images here (see _IMAGE-LIST.md)
└── templates/
    ├── base.html
    ├── index.html, menu.html, experience.html,
    ├── events.html, gallery.html, reservations.html, contact.html,
    ├── 404.html
    └── partials/
        ├── _nav.html, _footer.html, _awards.html,
        ├── _reservation-cta.html, _icons.html
```

---

## Adding images

The site ships with tasteful CSS gradient fallbacks so it looks polished even
before any photos are added. To add real imagery:

1. Drop files into `static/images/` using the exact filenames in
   [`_IMAGE-LIST.md`](./_IMAGE-LIST.md).
2. For the home hero, follow the `<!-- TODO -->` comment in
   `templates/index.html` to switch the hero block to the image variant.

---

## Content & data

All copy and data live in `data.py` and come from the verified business brief.
Search the templates for `<!-- TODO -->` to find places where you should
confirm a seasonal price or insert a real photo. **No prices were invented** —
unconfirmed items are shown as `Market` or `Seasonal`.

Replace `"Your Studio"` in `data.py` (`SITE["studio"]`) with your agency name
for the footer credit.
