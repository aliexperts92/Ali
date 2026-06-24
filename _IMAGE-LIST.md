# Image List — Signature Restaurant

Every image the site references, with the exact file path, intended dimensions,
and a descriptive brief. Drop the final assets into `static/images/` using the
**exact filenames** below. Until then, the site shows tasteful CSS gradient /
placeholder fallbacks, so nothing looks broken.

**General direction:** cinematic, warm, intimate, rustic-elegant. Candlelight,
brass, reclaimed wood, white-plastered walls, golf-course / Hill Country views.
Prefer dark, moody food photography with shallow depth of field. Export
optimized JPEG/WebP. All `<img>` use `loading="lazy"` except above-the-fold.

| File path | Dimensions | Brief |
|---|---|---|
| `static/images/hero-dining-room.jpg` | 1920×1080 | Candlelit rustic-elegant dining room with wagon-wheel chandelier and golf-course view. Primary home hero (cinematic, dark). |
| `static/images/og-signature.jpg` | 1200×630 | Social share card — plated signature dish or dining room with subtle logo space. Used in Open Graph / Twitter meta. |
| `static/images/intro-plating.jpg` | 1000×1250 | Close-up of an elegant plated dish; shallow depth of field. Home "Philosophy" split. |
| `static/images/dish-octopus.jpg` | 900×1200 | Grilled Spanish octopus over avocado purée, confit potatoes, chorizo, salsa verde. |
| `static/images/dish-venison.jpg` | 900×1200 | Texas axis venison, cherry jus, baby carrots, potato pavé. |
| `static/images/dish-duck.jpg` | 900×1200 | Black tea-smoked Pekin duck breast, black Chinese rice, daikon slaw. |
| `static/images/dish-scallops.jpg` | 900×1200 | Pan-seared Gulf sea scallops, golden seared crust. |
| `static/images/chef-weissman.jpg` | 900×1200 | Portrait — Chef Andrew Weissman (consulting/founding chef). |
| `static/images/chef-carpenter.jpg` | 1000×1250 | Portrait — Chef John Carpenter (executive chef). Also used in home chef-highlight split. |
| `static/images/chef-torres.jpg` | 900×1200 | Portrait — Chef Jaime Torres (executive sous chef). |
| `static/images/chef-leopoldo.jpg` | 900×1200 | Portrait — Chef Stéphane Leopoldo (executive pastry chef). |
| `static/images/story-dining-room.jpg` | 1000×1250 | Wide rustic-elegant interior: white-plastered walls, antiques, reclaimed Joske's wood. Experience "Story" split. |
| `static/images/events-private-room.jpg` | 1000×1250 | Private dining room set for a celebration; warm lighting. Events split. |
| `static/images/gallery-dining-room.jpg` | 1400×1050 | Candlelit dining room, wagon-wheel chandeliers. Gallery. |
| `static/images/gallery-open-kitchen.jpg` | 1200×1200 | View into the glowing open kitchen, chefs at work. Gallery. |
| `static/images/gallery-fireplace.jpg` | 1050×1400 | French limestone fireplace mantle with antiques. Gallery. |
| `static/images/gallery-patio-view.jpg` | 1400×1050 | Outdoor patio overlooking golf course and Hill Country at dusk. Gallery. |
| `static/images/gallery-dessert.jpg` | 1200×1200 | Royal Chocolate dessert with raspberry-basil sorbet. Gallery. |
| `static/images/gallery-wine.jpg` | 1050×1400 | Wine cellar / pour; Wine Spectator award context. Gallery. |
| `static/images/gallery-garden.jpg` | 1400×1050 | On-site kitchen garden with herbs and produce. Gallery. |
| `static/images/gallery-table-setting.jpg` | 1200×1200 | Elegant table setting — brass, linen, candlelight. Gallery. |

## Notes

- The gallery uses CSS masonry; varied aspect ratios are fine — the layout
  adapts. The dimensions above are suggested minimums for crispness.
- For the home hero photo, after adding `hero-dining-room.jpg`, follow the
  `<!-- TODO -->` comment in `templates/index.html` to enable the image variant
  (`hero__media--img` + `--hero-img` custom property).
- Optional dev stand-ins: you may temporarily reference Unsplash Source URLs,
  but keep the local path plan and `alt` text as the source of truth.
