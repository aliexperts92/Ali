"""Verified business + content data for Signature Restaurant.

Everything here comes from the provided brief. No values are invented.
Where a value is seasonal or unconfirmed it is tagged as a placeholder via the
``note`` field and surfaced in the UI as "Seasonal" / "Market".
"""

SITE = {
    "name": "Signature",
    "full_name": "Signature Restaurant",
    "tagline": "French technique. Texas soul.",
    "parent": (
        "Located within Signia by Hilton La Cantera Resort & Spa, overlooking "
        "the resort golf course and the Texas Hill Country."
    ),
    "address_line": "16401 La Cantera Pkwy",
    "address_city": "San Antonio, TX 78256",
    "address_full": "16401 La Cantera Pkwy, San Antonio, TX 78256, United States",
    "phone": "(210) 247-0176",
    "phone_href": "tel:+12102470176",
    "domain": "signaturerestaurant.com",
    "opentable": "https://www.opentable.com/r/signature-san-antonio",
    "instagram": "https://www.instagram.com/signaturesanantonio",
    "instagram_handle": "@signaturesanantonio",
    "lat": 29.5991695,
    "lng": -98.6187483,
    "cuisine": (
        "New American / French-inspired fine dining — French cooking techniques "
        "applied to the best seasonal, locally sourced Texas Hill Country "
        "ingredients."
    ),
    "price_point": "$$$$",
    "payments": "AMEX · Discover · Mastercard · Visa",
    "est": "2016",
    "opentable_rating": "4.9",
    "google_rating": "4.7",
    "studio": "Your Studio",  # TODO: replace with your studio / agency name
}

NAV_LINKS = [
    {"endpoint": "index", "label": "Home"},
    {"endpoint": "menu", "label": "Menu"},
    {"endpoint": "experience", "label": "Experience"},
    {"endpoint": "events", "label": "Events"},
    {"endpoint": "gallery", "label": "Gallery"},
    {"endpoint": "contact", "label": "Contact"},
]

HOURS = [
    {"label": "Dinner — Mon–Sat", "value": "5:30 PM – 10:00 PM"},
    {"label": "Dinner — Sunday", "value": "5:30 PM – 9:00 PM"},
    {"label": "Signature Hour — Mon–Fri", "value": "4:30 PM – 6:00 PM"},
    {"label": "Sunday Brunch", "value": "10:00 AM – 1:30 PM"},
]

AWARDS = [
    {"name": "MICHELIN Guide Recommended", "detail": "2024–2025"},
    {"name": "OpenTable Top 100 Restaurants in America", "detail": "2024"},
    {"name": "Wine Spectator Best of Award of Excellence", "detail": "2024"},
    {"name": "USA Today Readers' Choice", "detail": "Best Restaurant"},
    {"name": "OpenTable Rating", "detail": "4.9 ★ (thousands of reviews)"},
    {"name": "Google Rating", "detail": "4.7 ★"},
]

# Short, prominent ribbon shown on the home hero / awards bar.
AWARDS_RIBBON = [
    "MICHELIN Recommended",
    "OpenTable Top 100",
    "Wine Spectator Award of Excellence",
]

EXPERIENCES = [
    {
        "title": "The Open Kitchen",
        "body": (
            "Watch French technique meet Texas fire from a dining room built "
            "around the glow of the open kitchen."
        ),
        "icon": "flame",
    },
    {
        "title": "Hill Country Views",
        "body": (
            "Windows frame the rolling greens of the golf course and the rugged "
            "beauty of the Texas Hill Country."
        ),
        "icon": "vista",
    },
    {
        "title": "Seasonal Tasting Menu",
        "body": (
            "An eight-course journey from Chef John Carpenter, rewritten with "
            "the seasons roughly every three weeks."
        ),
        "icon": "leaf",
    },
    {
        "title": "Wine & Signature Hour",
        "body": (
            "A celebrated cellar and a playful weekday Signature Hour of "
            "cocktails, beer and wine by the glass."
        ),
        "icon": "glass",
    },
]

# Featured dishes (real, from reviews & guides). Prices intentionally omitted
# where unconfirmed — surfaced as "Seasonal" / "Market" in the UI.
SIGNATURE_DISHES = [
    {
        "name": "Spanish Octopus",
        "desc": (
            "Grilled tender and crisp over avocado purée, confit potatoes, "
            "Spanish chorizo and salsa verde."
        ),
        "image": "dish-octopus.jpg",
    },
    {
        "name": "Texas Axis Venison",
        "desc": "Deftly cooked, cherry jus, baby carrots and potato pavé.",
        "image": "dish-venison.jpg",
    },
    {
        "name": "Black Tea-Smoked Pekin Duck",
        "desc": "Black Chinese rice, Asian cabbage and daikon slaw.",
        "image": "dish-duck.jpg",
    },
    {
        "name": "Pan-Seared Sea Scallops",
        "desc": "Fresh from the Gulf, seared to a silken, golden crust.",
        "image": "dish-scallops.jpg",
    },
]

TASTING_MENU = {
    "title": "The Tasting Menu",
    "chef": "Chef John Carpenter",
    "summary": (
        "An eight-course seasonal dinner, updated approximately every three "
        "weeks. Offered Friday & Saturday only."
    ),
    "price": "$135–$150 per person",
    "pairing": "Optional sommelier wine pairings ~$75",
    "note": "Seasonal — changes regularly. Table participation required; no substitutions.",
}

# À la carte dinner, grouped per the brief. Prices left as Market/Seasonal where
# not provided in the verified data.
MENU_SECTIONS = [
    {
        "title": "To Begin",
        "eyebrow": "Amuse & Openers",
        "items": [
            {
                "name": "Hamachi Crudo",
                "desc": "Hawaiian tuna flown in fresh, dressed with restraint.",
                "price": "Market",
            },
            {
                "name": "Fried Oysters & Caviar",
                "desc": "Fried oyster bruschetta crowned with caviar.",
                "price": "Market",
            },
            {
                "name": "Pan-Seared Hudson Valley Foie Gras",
                "desc": "A classic indulgence, seared to order.",
                "price": "Market",
            },
        ],
    },
    {
        "title": "Small Plates",
        "eyebrow": "To Share",
        "items": [
            {
                "name": "Spanish Octopus",
                "desc": (
                    "Grilled tender and crisp, avocado purée, confit potatoes, "
                    "Spanish chorizo, salsa verde."
                ),
                "price": "Market",
            },
            {
                "name": "Pork Belly",
                "desc": "A melt-in-your-mouth appetizer.",
                "price": "Market",
            },
            {
                "name": "Rabbit Vol-au-Vent",
                "desc": "Hill Country rabbit in delicate puff pastry.",
                "price": "Market",
            },
        ],
    },
    {
        "title": "From the Sea",
        "eyebrow": "Gulf & Beyond",
        "items": [
            {
                "name": "Chilean Sea Bass",
                "desc": "Buttery, wood-kissed, impeccably sourced.",
                "price": "Market",
            },
            {
                "name": "Roasted Branzino",
                "desc": "Ginger-chile glaze.",
                "price": "Market",
            },
            {
                "name": "Halibut",
                "desc": "Finished with fresh herbs.",
                "price": "Market",
            },
            {
                "name": "Pan-Seared Sea Scallops",
                "desc": "Seared to a silken, golden crust.",
                "price": "Market",
            },
        ],
    },
    {
        "title": "From the Ranch",
        "eyebrow": "Texas Proteins",
        "items": [
            {
                "name": "Texas Axis Venison",
                "desc": "Cherry jus, baby carrots, potato pavé.",
                "price": "Market",
            },
            {
                "name": "Australian Wagyu Coulotte",
                "desc": "Rich, marbled, wood-fired.",
                "price": "Market",
            },
            {
                "name": "Black Tea-Smoked Pekin Duck Breast",
                "desc": "Black Chinese rice, Asian cabbage, daikon slaw.",
                "price": "Market",
            },
            {
                "name": "Prime Beef Tenderloin",
                "desc": "Or house-aged sirloin.",
                "price": "Market",
            },
        ],
    },
    {
        "title": "Garden & Sides",
        "eyebrow": "From the Kitchen Garden",
        "items": [
            {
                "name": "Spring Pea Risotto",
                "desc": "Bright, seasonal, from the garden.",
                "price": "Seasonal",
            },
            {
                "name": "Gold Leaf Risotto",
                "desc": "A gilded house signature.",
                "price": "Market",
            },
            {
                "name": "Classic Caesar Salad",
                "desc": "Crisp, anchovy-forward, table-side spirit.",
                "price": "Market",
            },
            {
                "name": "Snap Bean Salad",
                "desc": "Garden snap beans, lightly dressed.",
                "price": "Seasonal",
            },
        ],
    },
    {
        "title": "Pastry & Desserts",
        "eyebrow": "Chef Stéphane Leopoldo",
        "items": [
            {
                "name": "Warm Torta di Ricotta",
                "desc": "Candied almonds, blueberries, yuzu buttermilk ice cream.",
                "price": "Market",
            },
            {
                "name": "Royal Chocolate",
                "desc": (
                    "Almond-hazelnut sponge, praline crunch, milk & dark "
                    "chocolate mousse, raspberry-basil sorbet."
                ),
                "price": "Market",
            },
            {
                "name": "Seasonal Petit Fours",
                "desc": "Plus palate cleansers and post-prandial truffles.",
                "price": "Seasonal",
            },
        ],
    },
]

BRUNCH = {
    "title": "Sunday Brunch",
    "hours": "Sunday 10:00 AM – 1:30 PM",
    "items": [
        "Poached eggs with cured salmon & avocado on a biscuit, hollandaise",
        "Polenta",
        "Quiche Lorraine",
        "French-style omelets",
        "Lobster roll",
        (
            "The Signature Breakfast Burger — Wagyu beef, house-baked brioche, "
            "house-cured bacon, sunny-side-up egg"
        ),
    ],
    "note": "Served with fresh fruit.",
}

SIGNATURE_HOUR = {
    "title": "Signature Hour",
    "hours": "Monday–Friday 4:30 PM – 6:00 PM",
    "summary": (
        "Weekday cocktails, select beers and wine by the glass — a more playful, "
        "accessible way to enjoy the menu."
    ),
}

SOURCING_NOTE = (
    "Our cooking begins with the land: produce and herbs from our own on-site "
    "kitchen garden, fresh Gulf seafood, Hawaiian tuna flown in fresh, Texas "
    "venison, quail, pheasant and rabbit, and Pacific Northwest lamb — French "
    "technique in service of the Hill Country's best."
)

RITUALS = [
    {
        "title": "A Choice of Water",
        "body": "Citrus, cucumber or mint to begin — a small, thoughtful welcome.",
    },
    {
        "title": "Amuse-Bouche",
        "body": "A single perfect bite from the kitchen to open the meal.",
    },
    {
        "title": "Sorbet Palate Cleanser",
        "body": "A cool, bright pause served between courses.",
    },
    {
        "title": "Truffles & Petit Fours",
        "body": "Post-prandial truffles and petit fours to close, unhurried.",
    },
]

SETTING = [
    {
        "title": "A Countryside Mansion",
        "body": (
            "A rustic-elegant dining room of white-plastered walls, antiques and "
            "wagon-wheel chandeliers — quietly luxurious, unmistakably Texan."
        ),
    },
    {
        "title": "Reclaimed History",
        "body": (
            "Built with reclaimed wood salvaged from San Antonio's historic "
            "Joske's department store, with a limestone fireplace mantle brought "
            "from an old property in France."
        ),
    },
    {
        "title": "Open Kitchen & Views",
        "body": (
            "Windows into the open kitchen and out across the rolling greens of "
            "the golf course and the rugged Hill Country, with an outdoor patio."
        ),
    },
]

TEAM = [
    {
        "name": "Chef Andrew Weissman",
        "role": "Consulting / Founding Chef",
        "bio": (
            "James Beard Award-nominated (four-time finalist) and a 1996 "
            "Culinary Institute of America (Hyde Park) graduate. Founder of San "
            "Antonio's legendary Le Rêve."
        ),
        "image": "chef-weissman.jpg",
    },
    {
        "name": "Chef John Carpenter",
        "role": "Executive Chef (since 2022)",
        "bio": (
            "New-World interpretations of classic Old-World dishes, plated with "
            "an unconventional Texas spirit."
        ),
        "image": "chef-carpenter.jpg",
    },
    {
        "name": "Chef Jaime Torres",
        "role": "Executive Sous Chef",
        "bio": "Steward of the line and the daily pursuit of perfection.",
        "image": "chef-torres.jpg",
    },
    {
        "name": "Chef Stéphane Leopoldo",
        "role": "Executive Pastry Chef",
        "bio": (
            "Paris-trained — a pastry apprentice from age 15 — with degrees in "
            "both pastry and chocolate. Formerly taught at Culinary Institute "
            "Lenôtre, Houston."
        ),
        "image": "chef-leopoldo.jpg",
    },
]

EVENT_TYPES = [
    "Private Dining",
    "Celebration / Anniversary",
    "Corporate / Client Dinner",
    "Rehearsal Dinner",
    "Other",
]

# Gallery placeholders — see _IMAGE-LIST.md for the full brief on each asset.
GALLERY_IMAGES = [
    {"file": "gallery-dining-room.jpg", "alt": "Candlelit rustic-elegant dining room with wagon-wheel chandeliers", "category": "Setting"},
    {"file": "gallery-open-kitchen.jpg", "alt": "View into the glowing open kitchen", "category": "Setting"},
    {"file": "dish-octopus.jpg", "alt": "Grilled Spanish octopus over avocado purée", "category": "Plating"},
    {"file": "dish-venison.jpg", "alt": "Texas axis venison with cherry jus and potato pavé", "category": "Plating"},
    {"file": "gallery-fireplace.jpg", "alt": "French limestone fireplace mantle and antiques", "category": "Setting"},
    {"file": "dish-scallops.jpg", "alt": "Pan-seared Gulf sea scallops", "category": "Plating"},
    {"file": "gallery-patio-view.jpg", "alt": "Outdoor patio overlooking the golf course and Hill Country", "category": "Views"},
    {"file": "dish-duck.jpg", "alt": "Black tea-smoked Pekin duck breast", "category": "Plating"},
    {"file": "gallery-dessert.jpg", "alt": "Royal Chocolate dessert with raspberry-basil sorbet", "category": "Pastry"},
    {"file": "gallery-wine.jpg", "alt": "Wine Spectator award-winning cellar selection", "category": "Wine"},
    {"file": "gallery-garden.jpg", "alt": "On-site kitchen garden with herbs and produce", "category": "Garden"},
    {"file": "gallery-table-setting.jpg", "alt": "Elegant table setting with brass and linen", "category": "Setting"},
]
