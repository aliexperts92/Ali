"""Signature Restaurant — Flask application.

A multi-page marketing site for Signature, the fine-dining restaurant at
Signia by Hilton La Cantera Resort & Spa, San Antonio, TX.

All business data is sourced from the verified brief and centralised in
``data.py`` so templates stay clean and copy lives in one place.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
from pathlib import Path

from flask import (
    Flask,
    Response,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

import data

BASE_DIR = Path(__file__).resolve().parent
SUBMISSIONS_FILE = BASE_DIR / "submissions.json"

app = Flask(__name__)
# Used only to enable flash messages; not security-sensitive for this site.
app.config["SECRET_KEY"] = "signature-restaurant-dev-key-change-me"


@app.context_processor
def inject_globals() -> dict:
    """Make site-wide data + helpers available to every template."""
    return {
        "site": data.SITE,
        "awards": data.AWARDS,
        "hours": data.HOURS,
        "nav_links": data.NAV_LINKS,
        "current_year": _dt.date.today().year,
    }


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _save_submission(kind: str, payload: dict) -> None:
    """Append a form submission to submissions.json.

    Failures are swallowed so the guest never sees a backend error; we simply
    fall back to logging to the console.
    """
    record = {
        "kind": kind,
        "submitted_at": _dt.datetime.utcnow().isoformat() + "Z",
        **payload,
    }
    try:
        if SUBMISSIONS_FILE.exists():
            existing = json.loads(SUBMISSIONS_FILE.read_text(encoding="utf-8"))
            if not isinstance(existing, list):
                existing = []
        else:
            existing = []
        existing.append(record)
        SUBMISSIONS_FILE.write_text(
            json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    except Exception as exc:  # noqa: BLE001 - never surface to the guest
        app.logger.warning("Could not write submission file: %s", exc)
        app.logger.info("Submission (%s): %s", kind, record)


def _clean(value: str | None, limit: int = 2000) -> str:
    return (value or "").strip()[:limit]


# --------------------------------------------------------------------------- #
# Routes
# --------------------------------------------------------------------------- #
@app.route("/")
def index():
    return render_template(
        "index.html",
        page_id="home",
        meta_title=f"{data.SITE['name']} — French Technique. Texas Soul.",
        meta_description=(
            "Signature is a MICHELIN-recommended fine-dining restaurant at "
            "Signia by Hilton La Cantera, San Antonio — French technique meets "
            "Texas Hill Country soul."
        ),
        experiences=data.EXPERIENCES,
        signature_dishes=data.SIGNATURE_DISHES[:4],
        team=data.TEAM,
    )


@app.route("/menu")
def menu():
    return render_template(
        "menu.html",
        page_id="menu",
        meta_title=f"The Menu — {data.SITE['name']}",
        meta_description=(
            "Seasonal New American and French-inspired menus at Signature: an "
            "eight-course tasting menu, à la carte dinner, Sunday brunch and "
            "Signature Hour."
        ),
        tasting=data.TASTING_MENU,
        menu_sections=data.MENU_SECTIONS,
        brunch=data.BRUNCH,
        signature_hour=data.SIGNATURE_HOUR,
        sourcing=data.SOURCING_NOTE,
    )


@app.route("/experience")
def experience():
    return render_template(
        "experience.html",
        page_id="experience",
        meta_title=f"The Experience — {data.SITE['name']}",
        meta_description=(
            "The story, setting, rituals and culinary team behind Signature — a "
            "rustic-elegant fine-dining experience on the grounds of La Cantera "
            "Resort."
        ),
        rituals=data.RITUALS,
        setting=data.SETTING,
        team=data.TEAM,
    )


@app.route("/events", methods=["GET", "POST"])
def events():
    if request.method == "POST":
        payload = {
            "name": _clean(request.form.get("name"), 120),
            "email": _clean(request.form.get("email"), 200),
            "phone": _clean(request.form.get("phone"), 60),
            "date": _clean(request.form.get("date"), 40),
            "party_size": _clean(request.form.get("party_size"), 20),
            "event_type": _clean(request.form.get("event_type"), 80),
            "message": _clean(request.form.get("message")),
        }
        errors = []
        if not payload["name"]:
            errors.append("Please share your name.")
        if not EMAIL_RE.match(payload["email"]):
            errors.append("Please provide a valid email address.")

        if errors:
            for err in errors:
                flash(err, "error")
        else:
            _save_submission("event_inquiry", payload)
            flash(
                "Thank you — your event inquiry has been received. Our events "
                "team will be in touch shortly.",
                "success",
            )
            return redirect(url_for("events", submitted=1) + "#inquire")

    return render_template(
        "events.html",
        page_id="events",
        meta_title=f"Private Events — {data.SITE['name']}",
        meta_description=(
            "Host private dinners, celebrations and corporate gatherings at "
            "Signature, on the grounds of Signia by Hilton La Cantera."
        ),
        event_types=data.EVENT_TYPES,
    )


@app.route("/gallery")
def gallery():
    return render_template(
        "gallery.html",
        page_id="gallery",
        meta_title=f"Gallery — {data.SITE['name']}",
        meta_description=(
            "A glimpse of Signature — plated dishes, the open kitchen, the "
            "rustic-elegant dining room and Hill Country views."
        ),
        images=data.GALLERY_IMAGES,
    )


@app.route("/reservations")
def reservations():
    return render_template(
        "reservations.html",
        page_id="reservations",
        meta_title=f"Reservations — {data.SITE['name']}",
        meta_description=(
            "Reserve your table at Signature via OpenTable. Reservations "
            "recommended; tables fill quickly."
        ),
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        payload = {
            "name": _clean(request.form.get("name"), 120),
            "email": _clean(request.form.get("email"), 200),
            "phone": _clean(request.form.get("phone"), 60),
            "message": _clean(request.form.get("message")),
        }
        errors = []
        if not payload["name"]:
            errors.append("Please share your name.")
        if not EMAIL_RE.match(payload["email"]):
            errors.append("Please provide a valid email address.")

        if errors:
            for err in errors:
                flash(err, "error")
        else:
            _save_submission("contact", payload)
            flash(
                "Thank you for reaching out — we'll respond as soon as we can.",
                "success",
            )
            return redirect(url_for("contact", submitted=1) + "#contact-form")

    return render_template(
        "contact.html",
        page_id="contact",
        meta_title=f"Contact & Directions — {data.SITE['name']}",
        meta_description=(
            "Find Signature at 16401 La Cantera Pkwy, San Antonio, TX. Hours, "
            "directions, map and contact details."
        ),
    )


# --------------------------------------------------------------------------- #
# SEO endpoints
# --------------------------------------------------------------------------- #
@app.route("/robots.txt")
def robots():
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {request.url_root.rstrip('/')}/sitemap.xml",
    ]
    return Response("\n".join(lines) + "\n", mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    routes = [
        "index",
        "menu",
        "experience",
        "events",
        "gallery",
        "reservations",
        "contact",
    ]
    today = _dt.date.today().isoformat()
    urls = []
    for endpoint in routes:
        loc = request.url_root.rstrip("/") + url_for(endpoint)
        urls.append(
            "  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{today}</lastmod>\n"
            "  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    return Response(xml, mimetype="application/xml")


@app.errorhandler(404)
def not_found(_err):
    return (
        render_template(
            "404.html",
            page_id="404",
            meta_title=f"Page Not Found — {data.SITE['name']}",
            meta_description="The page you are looking for could not be found.",
        ),
        404,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
