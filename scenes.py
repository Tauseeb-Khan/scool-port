"""Hand-drawn SVG illustrations used by the gallery ("Life at Scholars'") and the social reels."""

def kid(x, y, body, skin='#f5c9a0', cls='', hair='#2b1b12', arm=''):
    """A simple child figure: head, hair, body, legs. (x, y) is the centre of the head."""
    return ('<g class="%s"><circle cx="%d" cy="%d" r="9" fill="%s"/>'
            '<path d="M%d %da9 9 0 0 1 18 0z" fill="%s"/>'
            '<rect x="%d" y="%d" width="16" height="22" rx="7" fill="%s"/>'
            '<rect x="%d" y="%d" width="5" height="11" rx="2" fill="#2d3142"/>'
            '<rect x="%d" y="%d" width="5" height="11" rx="2" fill="#2d3142"/>%s</g>'
            % (cls, x, y, skin, x - 9, y - 1, hair, x - 8, y + 10, body, x - 6, y + 30, x + 1, y + 30, arm))

def svg(label, inner, vb='0 0 300 225'):
    return '<svg viewBox="%s" role="img" aria-label="%s" preserveAspectRatio="xMidYMid slice">%s</svg>' % (vb, label, inner)

def grad(gid, top, bottom):
    return ('<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/>'
            '<stop offset="1" stop-color="%s"/></linearGradient></defs><rect width="300" height="225" fill="url(#%s)"/>'
            % (gid, top, bottom, gid))

# ---- Gallery scenes --------------------------------------------------------
def sports():
    return svg('Children running on a school sports day track', grad('g-sports', '#6ec6ff', '#e3f6ff') +
        '<circle cx="250" cy="38" r="16" fill="#ffd23f"/>'
        '<path d="M0 16h300" stroke="#123075" stroke-width="2"/>'
        + ''.join('<polygon class="a-blink" style="animation-delay:%.1fs" points="%d,16 %d,16 %d,34" fill="%s"/>' % (i * .2, 10 + i * 30, 30 + i * 30, 20 + i * 30, c)
                  for i, c in enumerate(['#f74c3a', '#fef100', '#029547', '#2575fc'] * 3))
        + '<rect y="130" width="300" height="95" fill="#4cb35f"/><rect y="160" width="300" height="52" fill="#d9663d"/>'
        '<path d="M0 186h300" stroke="#fff" stroke-width="2" stroke-dasharray="14 10"/>'
        '<path d="M262 132v-42h30v42" fill="none" stroke="#fff" stroke-width="4"/>'
        + kid(40, 142, '#f74c3a', cls='a-run') + kid(40, 170, '#2575fc', skin='#e3b48a', cls='a-run" style="animation-delay:-1.6s')
        + '<g class="a-bounce"><circle cx="165" cy="118" r="10" fill="#fff" stroke="#222" stroke-width="1.5"/><path d="M157 118h16M165 110v16" stroke="#222"/></g>')

def art():
    return svg('Children painting at an easel in an art class', grad('g-art', '#fff3d9', '#ffe7b8') +
        '<rect y="170" width="300" height="55" fill="#e9d3a5"/>'
        '<path d="M120 110l-14 62M180 110l14 62M150 110v62" stroke="#8a5a2b" stroke-width="5"/>'
        '<rect x="105" y="38" width="90" height="72" fill="#fff" stroke="#8a5a2b" stroke-width="4"/>'
        '<circle cx="132" cy="58" r="9" fill="#ffd23f"/><path d="M105 106q22-30 45-8t45-22v32z" fill="#4cb35f"/>'
        + kid(70, 112, '#2575fc') +
        '<g class="a-paint"><line x1="80" y1="130" x2="112" y2="96" stroke="#f5c9a0" stroke-width="6" stroke-linecap="round"/><circle cx="114" cy="94" r="4" fill="#f74c3a"/></g>'
        '<rect x="215" y="128" width="72" height="8" fill="#8a5a2b"/><rect x="222" y="136" width="5" height="34" fill="#8a5a2b"/><rect x="275" y="136" width="5" height="34" fill="#8a5a2b"/>'
        '<ellipse cx="250" cy="122" rx="26" ry="9" fill="#fff" stroke="#c9b48a"/><circle cx="238" cy="120" r="4" fill="#f74c3a"/><circle cx="250" cy="118" r="4" fill="#2575fc"/><circle cx="262" cy="121" r="4" fill="#029547"/>'
        '<circle class="a-fall" cx="160" cy="40" r="3" fill="#f74c3a"/><circle class="a-fall" style="animation-delay:-1.3s" cx="190" cy="30" r="3" fill="#2575fc"/><circle class="a-fall" style="animation-delay:-2.2s" cx="230" cy="40" r="3" fill="#fef100"/>')

def science():
    return svg('A child in safety goggles doing a science experiment', grad('g-sci', '#d8f3f0', '#b7e4de') +
        '<rect y="148" width="300" height="77" fill="#8a5a2b"/><rect y="148" width="300" height="8" fill="#a8743b"/>'
        '<path d="M130 52h30v38l32 54q6 14-10 14h-74q-16 0-10-14l32-54z" fill="#fff" fill-opacity=".85" stroke="#7aa" stroke-width="2"/>'
        '<path d="M112 128l12-22h42l12 22q6 14-10 14h-48q-16 0-8-14z" fill="#4cc27a"><animate attributeName="fill" values="#4cc27a;#2575fc;#f74c3a;#4cc27a" dur="6s" repeatCount="indefinite"/></path>'
        '<circle class="a-rise" cx="140" cy="120" r="4" fill="#fff"/><circle class="a-rise" style="animation-delay:-1s" cx="152" cy="124" r="3" fill="#fff"/><circle class="a-rise" style="animation-delay:-1.8s" cx="146" cy="116" r="5" fill="#fff"/>'
        '<rect x="30" y="132" width="44" height="12" rx="3" fill="#444"/><rect x="48" y="86" width="10" height="46" fill="#666"/><path d="M52 90l34 14" stroke="#777" stroke-width="8" stroke-linecap="round"/><circle cx="90" cy="108" r="6" fill="#aaa"/>'
        + kid(240, 112, '#ffffff', cls='a-sway') +
        '<rect x="229" y="107" width="22" height="7" rx="3" fill="#2575fc" fill-opacity=".8"/>')

def hifz():
    return svg('A child reading a book on a wooden stand in the Hifz Academy', grad('g-hifz', '#e4f5e9', '#cbead6') +
        '<path d="M205 190V70a35 35 0 0 1 70 0v120z" fill="#ffe9a8" stroke="#8a5a2b" stroke-width="4"/>'
        '<circle class="a-blink" cx="228" cy="62" r="2.5" fill="#fff"/><circle class="a-blink" style="animation-delay:.6s" cx="252" cy="82" r="2" fill="#fff"/><circle class="a-blink" style="animation-delay:1.1s" cx="240" cy="108" r="2.5" fill="#fff"/>'
        '<line x1="70" y1="0" x2="70" y2="40" stroke="#8a5a2b"/><g class="a-sway"><rect x="60" y="40" width="20" height="26" rx="4" fill="#c9922c"/><rect class="a-blink" x="64" y="46" width="12" height="14" fill="#ffd27a"/></g>'
        '<rect y="178" width="300" height="47" fill="#7ec8a0"/><path d="M0 200h300" stroke="#5fae88" stroke-width="3" stroke-dasharray="8 8"/>'
        '<path d="M96 168l30-30M156 168l-30-30" stroke="#8a5a2b" stroke-width="6"/>'
        '<path d="M126 118q-26-10-44-4v38q18-6 44 4z" fill="#fff" stroke="#c9b48a"/><g class="a-flip"><path d="M126 118q26-10 44-4v38q-18-6-44 4z" fill="#fffbe8" stroke="#c9b48a"/></g>'
        + kid(60, 130, '#ffffff', cls='a-sway'))

def annual():
    return svg('Children performing on stage at the annual function', grad('g-annual', '#3b2a73', '#1e1440') +
        '<g class="a-beam" fill="#fff" fill-opacity=".14"><polygon points="70,0 40,150 130,150"/></g><g class="a-beam" style="animation-delay:-1.5s" fill="#fff" fill-opacity=".14"><polygon points="230,0 200,150 290,150"/></g>'
        '<rect y="158" width="300" height="67" fill="#8a5a2b"/><rect y="158" width="300" height="7" fill="#a8743b"/>'
        '<path d="M0 0h50q-10 70 4 160H0z" fill="#c4322f"/><path d="M300 0h-50q10 70-4 160h54z" fill="#c4322f"/>'
        '<text x="150" y="30" text-anchor="middle" style="font:700 14px Poppins,sans-serif;fill:#fef100;letter-spacing:2px">ANNUAL DAY</text>'
        + kid(105, 112, '#ffd23f', cls='a-bounce') + kid(150, 108, '#ff7fa0', skin='#e3b48a', cls='a-bounce" style="animation-delay:-.3s') + kid(195, 112, '#4cc27a', cls='a-bounce" style="animation-delay:-.6s')
        + ''.join('<polygon class="a-fall" style="animation-delay:-%.1fs" points="%d,10 %d,16 %d,16 %d,20 %d,26 %d,22 %d,26 %d,20 %d,16 %d,16" fill="%s"/>'
                  % (i * .7, x, x + 2, x + 6, x + 3, x + 4, x, x - 4, x - 3, x - 6, x - 2, c)
                  for i, (x, c) in enumerate([(70, '#fef100'), (120, '#f74c3a'), (180, '#4cc27a'), (230, '#2575fc'), (150, '#ff7fa0')])))

def smartclass():
    return svg('Children learning in front of a LEAD smart board', grad('g-smart', '#fff4dc', '#ffe9bd') +
        '<rect y="176" width="300" height="49" fill="#e9d3a5"/>'
        '<rect x="40" y="26" width="170" height="100" rx="6" fill="#12332a" stroke="#8a5a2b" stroke-width="5"/>'
        '<text x="52" y="46" style="font:700 10px Poppins,sans-serif;fill:#fff">LEAD Smart Class</text>'
        '<g class="chart-bars"><rect x="58" y="86" width="20" height="30" fill="#f2b705"/><rect x="86" y="66" width="20" height="50" fill="#4cc27a"/><rect x="114" y="96" width="20" height="20" fill="#4aa3ff"/><rect x="142" y="74" width="20" height="42" fill="#ff7fa0"/><rect x="170" y="60" width="20" height="56" fill="#f2b705"/></g>'
        '<rect x="228" y="30" width="56" height="66" fill="#bfe8ff" stroke="#8a5a2b" stroke-width="4"/><path d="M256 30v66M228 63h56" stroke="#8a5a2b" stroke-width="2"/>'
        + kid(70, 150, '#4aa3ff') + kid(150, 152, '#ff7fa0', skin='#e3b48a') +
        '<g class="a-wave"><line x1="236" y1="182" x2="246" y2="150" stroke="#f5c9a0" stroke-width="5" stroke-linecap="round"/></g>'
        + kid(230, 150, '#ffa33a') +
        '<g fill="#8a5a2b"><rect x="40" y="188" width="64" height="8" rx="2"/><rect x="120" y="188" width="64" height="8" rx="2"/><rect x="200" y="188" width="64" height="8" rx="2"/></g>')

GALLERY = [
    ('Sports Day', 'Sports day', sports),
    ('Art Class', 'Art class', art),
    ('Science Lab', 'Science lab', science),
    ('Hifz Academy', 'Hifz Academy', hifz),
    ('Annual Function', 'Annual function', annual),
    ('Smart Class', 'Smart class', smartclass),
]

# ---- Reel preview scenes (vertical, 9:13) ----------------------------------------
def reel_svg(label, bg, inner):
    return '<svg viewBox="0 0 180 260" role="img" aria-label="%s" preserveAspectRatio="xMidYMid slice"><rect width="180" height="260" fill="%s"/>%s</svg>' % (label, bg, inner)

def reel_sandwich():
    layers = [('<rect x="40" y="168" width="100" height="16" rx="8" fill="#e8b36b"/>', 0),
              ('<ellipse cx="90" cy="162" rx="46" ry="7" fill="#e8402f"/>', .5),
              ('<path d="M42 158q8-9 16 0t16 0 16 0 16 0 16 0 8-3 0 6H42z" fill="#4cb35f"/>', 1.0),
              ('<polygon points="44,150 136,150 136,156 44,156" fill="#ffd23f"/>', 1.5),
              ('<path d="M40 148q0-22 50-22t50 22z" fill="#e8b36b"/>', 2.0)]
    s = '<ellipse cx="90" cy="190" rx="66" ry="12" fill="#fff" stroke="#d9c9a6"/>'
    s += ''.join('<g class="a-drop" style="animation-delay:%.1fs">%s</g>' % (d, p) for p, d in layers)
    s += ('<g><ellipse cx="90" cy="50" rx="30" ry="22" fill="#fff"/><ellipse cx="66" cy="62" rx="18" ry="14" fill="#fff"/><ellipse cx="114" cy="62" rx="18" ry="14" fill="#fff"/>'
          '<rect x="62" y="64" width="56" height="16" fill="#fff" stroke="#ddd"/></g>'
          '<circle cx="90" cy="100" r="16" fill="#f5c9a0"/><circle cx="84" cy="98" r="2" fill="#222"/><circle cx="96" cy="98" r="2" fill="#222"/><path d="M83 106q7 6 14 0" stroke="#222" fill="none" stroke-width="1.5"/>'
          '<text x="90" y="236" text-anchor="middle" style="font:700 13px Poppins,sans-serif;fill:#123075">Little chefs</text>')
    return reel_svg('Animated preview: little chefs making a sandwich', '#ffe9c2', s)

def reel_puppy():
    s = ('<g class="a-sway" style="transform-origin:90px 130px"><path d="M52 84q-22 10-12 52q20-6 26-26z" fill="#7a4a2b" class="a-wave"/><path d="M128 84q22 10 12 52q-20-6-26-26z" fill="#7a4a2b" class="a-wave"/>'
         '<circle cx="90" cy="118" r="42" fill="#f3d9b1"/><ellipse cx="90" cy="130" rx="20" ry="15" fill="#fff"/><ellipse cx="90" cy="122" rx="7" ry="5" fill="#222"/>'
         '<circle cx="74" cy="106" r="5" fill="#222"/><circle cx="106" cy="106" r="5" fill="#222"/><path d="M82 134q8 8 16 0" stroke="#222" fill="none" stroke-width="2"/><path class="a-blink" d="M88 136q2 14 4 0" fill="#f74c3a"/></g>'
         '<g class="a-fold"><rect x="62" y="186" width="56" height="40" fill="#ff9f1c"/></g>'
         '<polygon class="a-fall" points="30,10 46,10 38,26" fill="#2575fc"/><polygon class="a-fall" style="animation-delay:-1.4s" points="130,0 148,0 140,18" fill="#f74c3a"/><rect class="a-fall" style="animation-delay:-2.3s" x="100" y="0" width="14" height="14" fill="#fef100"/>'
         '<text x="90" y="250" text-anchor="middle" style="font:700 13px Poppins,sans-serif;fill:#123075">Paper to puppy</text>')
    return reel_svg('Animated preview: paper folded into a puppy', '#cdeccf', s)

def reel_penstand():
    pens = ['#f74c3a', '#2575fc', '#029547', '#f2b705', '#ff7fa0']
    s = ''.join('<rect class="a-pen" style="animation-delay:%.1fs" x="%d" y="%d" width="9" height="62" rx="3" fill="%s" transform="rotate(%d %d 150)"/>'
                % (i * .35, 52 + i * 18, 92, c, (i - 2) * 8, 56 + i * 18) for i, c in enumerate(pens))
    s += ('<rect x="40" y="140" width="100" height="70" rx="10" fill="#f2b705"/><rect x="40" y="160" width="100" height="10" fill="#d89b00"/><rect x="40" y="184" width="100" height="10" fill="#d89b00"/>'
          '<circle class="a-blink" cx="30" cy="60" r="3" fill="#fff"/><circle class="a-blink" style="animation-delay:.7s" cx="150" cy="80" r="3" fill="#fff"/>'
          '<text x="90" y="240" text-anchor="middle" style="font:700 13px Poppins,sans-serif;fill:#123075">Pen stand making</text>')
    return reel_svg('Animated preview: making a pen stand', '#d7e8ff', s)

REELS = [
    ('Little chefs making sandwiches', 'https://www.instagram.com/reel/DemDmediURp/', reel_sandwich),
    ('From paper to puppy', 'https://www.instagram.com/reel/DemByZ2lAtR/', reel_puppy),
    ('Pen stand making', 'https://www.instagram.com/reel/DedvdV9kvoy/', reel_penstand),
]
