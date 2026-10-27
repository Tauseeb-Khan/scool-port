# Scholars' Paradise: website concept (developer notes)

A single-page concept redesign of scholarsgroup.in. Plain HTML, CSS and JavaScript: **no framework, no npm, no libraries.**
`python3 build.py` joins the source files into one file, `dist/index.html`, which can be opened in a browser or hosted anywhere.

## Folder map

| Path | What it holds |
|---|---|
| `src/page.html` | The page markup. Every section has a numbered comment (`01 HERO`, `02 ABOUT` ...). `@@NAME@@` marks values that `build.py` fills in. |
| `src/style.css` | All styles, in 21 numbered sections. **Brand colours are the variables in section 01.** |
| `src/script.js` | All behaviour. Order: 1 DATA, 2 HELPERS, 3 MODULES (`initHero()`, `initReels()` ...), 4 START. |
| `scenes.py` | The hand-drawn SVG scenes for "Life at Scholars’" and the social reels. |
| `build.py` | Content data (campuses, classes, FAQ, menu) and the code that builds the HTML lists and the JSON-LD. |
| `assets/` | Logo, "Admission Open" image, venture logos, hero and classroom illustrations. |
| `dist/index.html` | The built site. Do not edit by hand; edit the sources and rebuild. |

## How to change common things

* **Colours:** `src/style.css`, section 01.
* **A campus (name, areas):** `build.py` (`CAMPUSES`) and `src/script.js` (`CAMPUSES`). Keep both lists in the same order.
* **FAQ text:** `build.py` (`FAQ`). It feeds both the visible FAQ and the FAQ structured data, so they never disagree.
* **Menu pages (About, Fees, Notices ...):** `src/script.js`, the `PAGES` object. Fees, transport and calendar are the `DOCUMENTS` functions below it.
* **Phone / e-mail:** `build.py` (top) and `src/script.js` (top).

## Conventions

* CSS class names are `block__element--modifier` (for example `hero__slide`, `campus-card`, `overlay__side`).
* JavaScript state classes always start with `is-` (`is-active`, `is-open`, `is-visible`).
* Each JavaScript feature is one `init...` function; to remove a feature, delete its function and its call in section 4.
* Animations are CSS keyframes (section 19 of the stylesheet) and are switched off for visitors who prefer reduced motion.

## SEO and accessibility already in place

* One `<h1>`; sections use `<h2>`; landmarks `header / nav / main / footer`; skip link.
* Title, description, Open Graph and Twitter tags. Per-page title and description are set by `setSeo()` when a menu or campus page opens.
* JSON-LD: school, six campuses, FAQ, and a breadcrumb for overlay pages.
* Real `<details>` for the FAQ, labelled form fields, `aria-label` on icon links, visible keyboard focus.

## What is placeholder and must be replaced before going live

1. **Presentation helpers (remove):** `.concept-banner`, the "Show my changes" button (`#toggle-changes`), every `data-improved="..."` attribute and the `body.show-changes` CSS.
2. **Real URLs instead of `#page-...` / `#branch-...`.** Search engines index real paths such as `/campus/kalyanpur/`. Menu and campus pages need to be real pages (or server-rendered routes). The content in `PAGES` is the starting text.
3. **Content the school must supply:** fees, transport routes and timings, academic calendar, vision and mission, full notice texts, descriptions of Study Center / NEET / Learning Labs / Hive / Booster, each campus' address, phone, map coordinates and opening hours (also add them to the JSON-LD in `build.py`), CISCE affiliation number.
4. **Forms:** the admission forms only show a thank-you message. They need a backend (or a service) and server-side validation.
5. **Images:** the gallery and reel previews are drawn illustrations. Replace them with the school’s photos (use `<img>` with `width`, `height`, `alt`, `loading="lazy"`). Logos are inlined as base64 to keep the demo to one file; serve them as normal files on the live site. The Hifz and Hive logos were cropped from a screenshot, so ask the school for the original files.
6. **Social reels:** each preview links to the real Instagram reel. To play the real video, embed it (see the comment in `src/page.html`, section 11).
7. **Fonts:** Poppins loads from Google Fonts; self-host it if required.
8. **Search files:** add `robots.txt`, `sitemap.xml` and a `<link rel="canonical">`.
9. **Demo data:** the area-to-campus mapping and the schematic map are examples. The numbers in the counters are the figures shown on the current site.

## Checks done on this build

Loaded at 1280 px and 390 px wide: no horizontal scroll and no JavaScript errors; all 27 menu pages and the campus pages open; popup, counters, reels, FAQ and forms work. Not tested: older browsers, screen readers, real-device touch.
