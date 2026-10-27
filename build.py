"""Builds the single-file website:  dist/index.html
Run:  python3 build.py   (needs Python 3 and the Pillow-free standard library only)
Content lives in the DATA block below. Markup lives in src/page.html, styles in src/style.css,
behaviour in src/script.js, images in assets/. Illustrations for the gallery are in scenes.py."""
import base64, json, os, re
import scenes

HERE = os.path.dirname(os.path.abspath(__file__))
def read(path):          return open(os.path.join(HERE, path), encoding='utf-8').read()
def b64(path):           return base64.b64encode(open(os.path.join(HERE, path), 'rb').read()).decode()

# ============================== DATA ========================================
SITE = 'https://scholarsgroup.in/'
PHONE, PHONE_HREF, EMAIL = '+91-6393477299', '+916393477299', 'info@scholarsgroup.in'
SOCIAL = [('Facebook', 'https://www.facebook.com/ScholarsParadiseOfficial/',
           '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z"/>'),
          ('Instagram', 'https://www.instagram.com/scholarsparadiseofficial/',
           '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8"/>'),
          ('YouTube', 'https://www.youtube.com/@spischoolLucknow',
           '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3z"/>')]
# (name, slug, colour, areas served [demo mapping], pin position on the schematic map)
CAMPUSES = [('Vikas Nagar', 'vikas-nagar', '#029547', ['Vikas Nagar', 'Jankipuram'], (90, 90)),
            ('Gaurabagh', 'gaurabagh', '#123075', ['Gaurabagh', 'Alambagh'], (150, 220)),
            ('Muazzam Nagar', 'muazzam-nagar', '#f74c3a', ['Muazzam Nagar', 'Chowk'], (250, 200)),
            ('Kursi', 'kursi', '#2575fc', ['Kursi Road', 'Faizabad Road'], (300, 80)),
            ('Kalyanpur', 'kalyanpur', '#e8a200', ['Kalyanpur', 'Telibagh'], (200, 40)),
            ('Ring Road', 'ring-road', '#02a5cc', ['Ring Road', 'Sitapur Road'], (345, 150))]
CLASSES = ['Nursery', 'LKG', 'UKG'] + ['Class %d' % n for n in range(1, 9)]
TITLE = 'Best ICSE English Medium School in Lucknow | Scholars’ Paradise'
DESC = ('Scholars’ Paradise International School, Lucknow: ICSE English medium school, Nursery to Class 8, '
        'LEAD smart classes and six campuses. Admissions open 2026–27.')
FAQ = [("Which board does Scholars’ Paradise follow?", "The school follows the ICSE curriculum in English medium, from Nursery to Class 8."),
       ("Which classes are available?", "Nursery to Class 8. Branch-wise class availability is confirmed by each campus, so please check the campus page or call the school."),
       ("Where are the campuses in Lucknow?", "There are six campuses: Vikas Nagar, Gaurabagh, Muazzam Nagar, Kursi, Kalyanpur and Ring Road. Use the campus finder to see the one nearest to your home."),
       ("Are admissions open for 2026–27?", "Yes. Admissions are open for 2026–27. Fill in the admission enquiry form and the nearest campus will call you back."),
       ("Does the school have smart classrooms?", "Yes. The school uses LEAD smart classes, digital tools and activity-based learning in its classrooms."),
       ("Is the campus safe for young children?", "The school describes a safe, hygienic environment with CCTV surveillance and a low student-teacher ratio."),
       ("Does the school offer Hifz along with regular studies?", "Yes. Scholars’ Hifz Academy offers Quran memorisation with Tajweed alongside regular ICSE schooling."),
       ("What are the school fees?", "Fees depend on the class and campus. Please submit an enquiry or call %s and the campus will share the current fee structure." % PHONE)]
NAV = [('About', 'about', [('about', 'Our School'), ('why-choose-us', 'Why Choose Us'), ('vision', 'Vision &amp; Mission'), ('values', 'Core Values')]),
       ('Academic', 'admission-process', [('admission-process', 'Admission Process'), ('fees', 'Fees Structure'), ('transport', 'Transport'), ('calendar', 'Academic Calendar')]),
       ('Campuses', 'campuses', [('branch-' + c[1], c[0]) for c in CAMPUSES]),
       ('Ventures', 'ventures', [('hifz', 'Hifz Academy'), ('study-center', 'Study Center'), ('neet', 'NEET'), ('learning-labs', 'Learning Labs'), ('hive', 'Hive'), ('booster', 'Booster')]),
       ('Notices', 'notices', []), ('Blogs', 'blogs', []), ('Contact Us', 'contact', [])]

# ============================== HELPERS =====================================
def icon(paths, cls='card__icon'):
    """Inline SVG icon. pathLength=1 lets the CSS animate the stroke being drawn."""
    paths = re.sub(r'<(path|circle|rect|polygon|ellipse|line)\b', r'<\1 pathLength="1"', paths)
    return '<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % (cls, paths)
I = dict(
    user='<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>',
    book='<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5zM4 19.5V22h16"/>',
    screen='<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    heart='<path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/>',
    home='<path d="M3 11l9-8 9 8M5 10v10h14V10"/>', clock='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    shield='<path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    people='<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3 3-5 6-5s6 2 6 5M15 15c3 0 6 1 6 4"/>',
    bus='<rect x="3" y="4" width="18" height="13" rx="3"/><path d="M3 11h18M7 20v-3M17 20v-3"/>',
    phone='<path d="M5 4h4l2 5-2 1a11 11 0 0 0 5 5l1-2 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    mail='<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    pin='<path d="M12 22s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    cap='<path d="M2 9l10-5 10 5-10 5zM6 11v5c3 3 9 3 12 0v-5"/>', play='<circle cx="12" cy="12" r="9"/><path d="M10 8l6 4-6 4z"/>',
    tent='<path d="M3 21l9-16 9 16zM12 5V2"/>', sprout='<path d="M12 21v-9M12 12c0-4-3-6-7-6 0 4 3 6 7 6zM12 14c0-3 2-5 6-5 0 3-2 5-6 5z"/>',
    openbook='<path d="M12 6c-3-2-6-2-9-1v13c3-1 6-1 9 1 3-2 6-2 9-1V5c-3-1-6-1-9 1zM12 6v13"/>')

def social_links(cls='social', label='Social media'):
    return '<nav class="%s" aria-label="%s">%s</nav>' % (cls, label, ''.join(
        '<a href="%s" target="_blank" rel="noopener" aria-label="%s"><svg viewBox="0 0 24 24" aria-hidden="true">%s</svg></a>' % (u, n, p) for n, u, p in SOCIAL))

def campus_building(color, name):
    """Small illustrated school building. Used for the campus cards."""
    return ('<svg viewBox="0 0 220 170" role="img" aria-label="Illustration of the %s campus building">'
            '<rect y="142" width="220" height="28" fill="#e8ecf6"/><g class="body"><rect x="35" y="70" width="150" height="73" fill="#fff4dc"/>'
            '<polygon points="25,72 110,28 195,72" fill="%s"/><rect x="52" y="76" width="116" height="20" rx="3" fill="%s" stroke="#fef100"/>'
            '<text x="110" y="90" text-anchor="middle" style="fill:#fff;font-size:9px;font-weight:700">%s</text>'
            '<path d="M98 143v-30a12 12 0 0 1 24 0v30z" fill="%s"/><g class="window" fill="#8fd3ff"><rect x="48" y="102" width="30" height="24" rx="3"/><rect x="142" y="102" width="30" height="24" rx="3"/></g>'
            '<line x1="188" y1="30" x2="188" y2="72" stroke="#bbb" stroke-width="2"/><polygon class="flag" points="188,30 208,30 208,42 188,42" fill="#fef100"/></g>'
            '<rect x="17" y="122" width="6" height="22" fill="#6b4226"/><circle cx="20" cy="114" r="14" fill="#2e9d54"/></svg>'
            % (name, color, color, name.upper(), color))

def mini_building(color):
    return ('<svg viewBox="0 0 24 24" aria-hidden="true" width="26" height="26"><polygon points="2,10 12,3 22,10" fill="%s"/><rect x="4" y="10" width="16" height="11" fill="#fff4dc" stroke="#d9d2c0" stroke-width=".6"/>'
            '<rect x="6" y="13" width="4" height="4" fill="#8fd3ff"/><rect x="14" y="13" width="4" height="4" fill="#8fd3ff"/><rect x="10.5" y="15" width="3" height="6" fill="%s"/></svg>' % (color, color))

def wheel(cx, cy, r):
    return ('<g class="wheel"><circle cx="%s" cy="%s" r="%s" fill="#222"/><circle cx="%s" cy="%s" r="2.6" fill="#ddd"/>'
            '<path d="M%s %sv%sM%s %sh%s" stroke="#999" stroke-width="1.2"/></g>' % (cx, cy, r, cx, cy, cx, cy - r + 1.5, 2 * r - 3, cx - r + 1.5, cy, 2 * r - 3))
BUS = ('<rect width="110" height="34" rx="8" fill="#f2b705"/><rect y="20" width="110" height="3" fill="#d89b00"/><g fill="#8fd3ff"><rect x="8" y="4" width="14" height="11" rx="2"/>'
       '<rect x="26" y="4" width="14" height="11" rx="2"/><rect x="44" y="4" width="14" height="11" rx="2"/><rect x="62" y="4" width="14" height="11" rx="2"/><path d="M88 4h12a6 6 0 0 1 6 6v5H88z"/></g>'
       '<text x="8" y="31" style="fill:#123075;font-size:7px;font-weight:700">SCHOLARS’ PARADISE</text><circle cx="107" cy="25" r="2.6" fill="#fff7b0"/>' + wheel(26, 35, 8.5) + wheel(84, 35, 8.5))
VAN = ('<rect y="4" width="80" height="24" rx="6" fill="#fff" stroke="#c9d2ea"/><polygon points="4,9 20,9 27,18 4,18" fill="#8fd3ff"/><g fill="#8fd3ff"><rect x="34" y="9" width="12" height="9" rx="2"/>'
       '<rect x="50" y="9" width="12" height="9" rx="2"/><rect x="66" y="9" width="10" height="9" rx="2"/></g><rect y="20" width="80" height="4" fill="#029547"/>'
       '<text x="30" y="27.4" style="fill:#123075;font-size:4.6px;font-weight:700">SCHOOL VAN</text><circle cx="2" cy="21" r="2" fill="#fff7b0"/>' + wheel(18, 29, 6) + wheel(62, 29, 6))

# ---- illustrations kept as files in assets/ ------------------------------------
scene = read('assets/hero-scene.html')
classroom = read('assets/classroom.html')

# ============================== SECTIONS ====================================
def nav_html():
    out = []
    for label, slug, subs in NAV:
        href = '#page-' + slug
        sub = ''.join('<li><a href="#%s">%s</a></li>' % (s if s.startswith('branch-') else 'page-' + s, t) for s, t in subs)
        out.append('<li><a href="%s">%s</a>%s</li>' % (href, label, '<ul>%s</ul>' % sub if sub else ''))
    return '<ul>%s</ul>' % ''.join(out)

TICKER = ''.join(['<a href="#page-notice-admissions">Admissions open 2026–27: enroll for Nursery to Class 8</a>',
                  '<a href="#page-hifz">Scholars’ Hifz Academy: Hifz with ICSE education</a>',
                  '<a href="#campuses">Six campuses across Lucknow</a>', '<a href="#page-notices">View all notices</a>'])

def cards(items, tag='article'):
    return ''.join('<%s class="card reveal">%s<h3>%s</h3><p>%s</p></%s>' % (tag, icon(i[0]), i[1], i[2], tag) for i in items)

ACADEMICS = cards([(I['user'], 'Early years (ages 2–5)', 'A play-based, hands-on programme that builds problem-solving, communication and creativity.'),
                   (I['book'], 'Primary and middle school', 'English, Science and Social Studies taught with conceptual clarity, up to Class 8.'),
                   (I['screen'], 'LEAD smart classes', 'Digital tools and activity-based learning that help each child grow at their own pace.'),
                   (I['heart'], 'Value-based education', 'Ethics, compassion and respect build character and confidence alongside academics.'),
                   (I['home'], 'Hifz alongside school', 'Quran memorisation with Tajweed through <a href="#page-hifz">Scholars’ Hifz Academy</a>.'),
                   (I['clock'], 'Activities and events', 'Sports, arts, leadership and teamwork through activities across all campuses.')])
FACILITIES = cards([(I['screen'], 'Smart classrooms', 'LEAD smart classes in every campus.'),
                    (I['shield'], 'CCTV surveillance', 'A safe, hygienic environment for every child.'),
                    (I['people'], 'Low student-teacher ratio', 'Individual attention for each child.'),
                    (I['bus'], 'School transport', 'Bus and van service. See <a href="#page-transport">Transport</a>.')])
WHY = cards([(I['book'], 'ICSE English medium', 'Conceptual clarity in English, Science and Social Studies, building strong communication skills.'),
             (I['heart'], 'Value-based learning', 'Ethics, compassion and respect through a structured programme.'),
             (I['sprout'], 'Holistic growth', 'Leadership, teamwork, sports, arts and extracurriculars.')])
VENTURE_ICONS = dict(
    study='<path d="M12 6c-3-2-6-2-9-1v13c3-1 6-1 9 1 3-2 6-2 9-1V5c-3-1-6-1-9 1zM12 6v13"/>',
    neet='<circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/>',
    labs='<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3M8 15h8"/>',
    booster='<path d="M12 3c3 2 5 5 5 9l-2 3H9l-2-3c0-4 2-7 5-9z"/><circle cx="12" cy="10" r="1.6"/><path d="M9 15l-2 4M15 15l2 4"/>')
# (slug, title, text, logo file or None, icon key)
VENTURE_LIST = [('hifz', 'Scholars’ Hifz Academy', 'Quran memorisation with Tajweed alongside academics.', 'hifz-logo.webp', None),
                ('study-center', 'Study Center', 'Extra academic support.', None, 'study'),
                ('learning-labs', 'Learning Labs', 'Hands-on learning.', None, 'labs'),
                ('neet', 'NEET', 'Medical entrance preparation.', None, 'neet'),
                ('hive', 'Hive', 'Enrichment programme: towards transformation.', 'hive-logo.webp', None),
                ('booster', 'Booster', 'Revision and skills.', None, 'booster')]
def venture_card(slug, title, text, logo, ic):
    media = ('<img class="venture__logo" data-venture="%s" src="data:image/webp;base64,%s" alt="%s logo" width="76" height="76" loading="lazy">' % (slug, b64('assets/' + logo), title)
             if logo else icon(VENTURE_ICONS[ic], 'venture__icon'))
    return ('<a class="venture reveal" href="#page-%s"><span class="venture__media">%s</span><h3>%s</h3><p>%s</p><span class="venture__more">Learn more →</span></a>'
            % (slug, media, title, text))
VENTURES = ''.join(venture_card(*v) for v in VENTURE_LIST)
CONTACT = (
    '<a class="card card--link reveal" href="tel:%s">%s<h3>Call us</h3><p>%s</p></a>' % (PHONE_HREF, icon(I['phone']), PHONE) +
    '<a class="card card--link reveal" href="mailto:%s">%s<h3>Email</h3><p>%s</p></a>' % (EMAIL, icon(I['mail']), EMAIL) +
    '<a class="card card--link reveal" href="#campuses">%s<h3>Find a campus</h3><p>Six campuses across Lucknow</p></a>' % icon(I['pin']))
STATS = ''.join('<div class="stat reveal">%s<b class="stat__number" data-count="%s">0</b><span class="stat__label">%s</span></div>' % (icon(i, ''), n, l)
                for n, l, i in [(1000, 'Students', I['cap']), (100, 'Activities', I['play']), (3000, 'Online Classes', I['screen']), (200, 'Outdoor Events', I['tent'])])
CAMPUS_CARDS = ''.join('<a class="campus-card reveal" data-campus="%s" href="#branch-%s" aria-label="Open the %s campus page">%s<h3>%s</h3>'
                       '<span class="muted">Scholars’ Paradise International School</span><span class="go">View campus →</span></a>'
                       % (c[1], c[1], c[0], campus_building(c[2], c[0]), c[0]) for c in CAMPUSES)
PINS = ''.join('<g class="pin" data-campus="%s" tabindex="0" role="button" aria-label="%s campus"><title>%s campus</title><circle class="pulse" cx="%d" cy="%d" r="8"/>'
               '<circle class="dot" cx="%d" cy="%d" r="6"/><text x="%d" y="%d"%s>%s</text></g>'
               % (c[1], c[0], c[0], c[4][0], c[4][1], c[4][0], c[4][1], c[4][0] - 10 if c[4][0] > 330 else c[4][0] + 10, c[4][1] + 4,
                  ' text-anchor="end"' if c[4][0] > 330 else '', c[0]) for c in CAMPUSES)
AREA_OPTIONS = ''.join('<option>%s</option>' % a for c in CAMPUSES for a in c[3])
CLASS_OPTIONS = ''.join('<option>%s</option>' % c for c in CLASSES)
GALLERY = ''.join('<figure class="gallery__item reveal">%s<figcaption>%s</figcaption></figure>' % (f(), n) for n, _, f in scenes.GALLERY)
REELS = ''.join(
    '<article class="reel"><div class="reel__screen">%s<button class="reel__play" type="button" aria-label="Play or pause the preview: %s">▶</button><div class="reel__bar"><i></i></div></div>'
    '<h3>%s</h3><a href="%s" target="_blank" rel="noopener">Watch the full reel on Instagram ↗</a></article>' % (f(), t, t, u) for t, u, f in scenes.REELS)
TESTIMONIALS = ''.join('<blockquote%s>“%s”<footer>— %s</footer></blockquote>' % ('' if i == 0 else ' hidden', q, w) for i, (q, w) in enumerate([
    ("We chose Scholars’ Group for a strong English medium foundation. Our daughter is now fluent and confident.", "Parent of Grade 3 student"),
    ("The focus on spoken and written English, with smart classes, really helps kids grow.", "Parent of Class 5 student"),
    ("Dedicated teachers, modern classrooms and a focus on overall child development.", "Parent of Class 4 student")]))
BLOGS = ''.join('<article class="blog-card reveal"><div class="blog-card__image">%s<span class="blog-card__date"><b>30</b>Jul</span></div><h3>%s</h3>'
                '<a class="btn" href="%s%s/" target="_blank" rel="noopener">Read more</a></article>' % (icon(ic, ''), n, SITE, s) for n, s, ic in [
    ('Value-based moral education in Lucknow schools', 'value-based-moral-education-in-lucknow-schools', I['book']),
    ('Islamic studies with English medium curriculum', 'islamic-studies-with-english-medium-curriculum', I['cap']),
    ('Hifz e Quran with modern ICSE education in Lucknow', 'hifz-e-quran-with-modern-icse-education-in-lucknow', I['openbook'])])
FAQ_HTML = ''.join('<details class="reveal"><summary>%s</summary><p>%s</p></details>' % qa for qa in FAQ)
FOOTER_BRANCHES = ''.join('<div class="footer__branch"><a href="#branch-%s">%s<span>%s</span></a><small><a href="#branch-%s">Campus page</a> · '
                          '<a href="https://www.google.com/maps/search/Scholars+Paradise+International+School+%s+Lucknow" target="_blank" rel="noopener">Map</a> · '
                          '<a href="tel:%s">Call</a></small></div>' % (c[1], mini_building(c[2]), c[0], c[1], c[0].replace(' ', '+'), PHONE_HREF) for c in CAMPUSES)

# ============================== STRUCTURED DATA =============================
graph = [{"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Scholars’ Group of Institutions", "inLanguage": "en-IN"},
         {"@type": ["EducationalOrganization", "School"], "@id": SITE + "#school", "name": "Scholars’ Paradise International School",
          "alternateName": "Scholars’ Group of Institutions", "url": SITE, "description": DESC, "email": EMAIL, "telephone": PHONE,
          "address": {"@type": "PostalAddress", "addressLocality": "Lucknow", "addressRegion": "Uttar Pradesh", "addressCountry": "IN"},
          "areaServed": "Lucknow", "parentOrganization": {"@type": "Organization", "name": "Sir Syed Educational And Welfare Trust"},
          "knowsAbout": ["ICSE curriculum", "English medium education", "Hifz and Tajweed", "Smart classes"], "sameAs": [s[1] for s in SOCIAL]}]
for c in CAMPUSES:
    graph.append({"@type": "School", "@id": SITE + "#branch-" + c[1], "name": "Scholars’ Paradise International School – " + c[0],
                  "parentOrganization": {"@id": SITE + "#school"}, "telephone": PHONE,
                  "address": {"@type": "PostalAddress", "addressLocality": c[0] + ", Lucknow", "addressRegion": "Uttar Pradesh", "addressCountry": "IN"}})
graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]})
JSONLD = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)

# ============================== ASSEMBLY ====================================
css = read('src/style.css')
js = read('src/script.js')
js = js.replace('/*@BUS_SVG*/""', json.dumps(BUS)).replace('/*@VAN_SVG*/""', json.dumps(VAN))
page = read('src/page.html')
tokens = dict(TITLE=TITLE, DESC=DESC, JSONLD=JSONLD, CSS=css, JS=js, DOODLES=read('assets/doodles-pattern.txt'), LOGO=b64('assets/logo.webp'), ADMISSION_IMG=b64('assets/admission-open.webp'),
              NAV=nav_html(), TICKER=TICKER * 2, SOCIAL_TOP=social_links('social', 'Social media'), SOCIAL_FOOT=social_links('social footer__social', 'Social media links'),
              SCENE=scene, CLASSROOM=classroom, WHY=WHY, ACADEMICS=ACADEMICS, FACILITIES=FACILITIES, VENTURES=VENTURES, CONTACT=CONTACT, STATS=STATS,
              CAMPUS_CARDS=CAMPUS_CARDS, PINS=PINS, AREA_OPTIONS=AREA_OPTIONS, CLASS_OPTIONS=CLASS_OPTIONS, GALLERY=GALLERY, REELS=REELS,
              TESTIMONIALS=TESTIMONIALS, BLOGS=BLOGS, FAQ=FAQ_HTML, FOOTER_BRANCHES=FOOTER_BRANCHES, PHONE=PHONE, PHONE_HREF=PHONE_HREF, EMAIL=EMAIL)
for k, v in tokens.items():
    page = page.replace('@@%s@@' % k, v)
left = re.findall(r'@@[A-Z_]+@@', page)
assert not left, left
os.makedirs(os.path.join(HERE, 'dist'), exist_ok=True)
open(os.path.join(HERE, 'dist', 'index.html'), 'w', encoding='utf-8').write(page)
print('built', len(page), 'bytes')
