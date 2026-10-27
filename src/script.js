/* ==========================================================================
   SCHOLARS' PARADISE: website behaviour (plain JavaScript, no libraries)

   HOW THIS FILE IS ORGANISED
     1. DATA      campuses, classes, menu pages. Edit text here.
     2. HELPERS   small utilities used everywhere.
     3. MODULES   one function per feature, each starting with "init".
     4. START     the last lines call every init function.
   ========================================================================== */
(function () {
  'use strict';

  /* ======================================================================
     1. DATA
     ====================================================================== */
  const CAMPUSES = [
    { name: 'Vikas Nagar',   slug: 'vikas-nagar',   areas: ['Vikas Nagar', 'Jankipuram'] },
    { name: 'Gaurabagh',     slug: 'gaurabagh',     areas: ['Gaurabagh', 'Alambagh'] },
    { name: 'Muazzam Nagar', slug: 'muazzam-nagar', areas: ['Muazzam Nagar', 'Chowk'] },
    { name: 'Kursi',         slug: 'kursi',         areas: ['Kursi Road', 'Faizabad Road'] },
    { name: 'Kalyanpur',     slug: 'kalyanpur',     areas: ['Kalyanpur', 'Telibagh'] },
    { name: 'Ring Road',     slug: 'ring-road',     areas: ['Ring Road', 'Sitapur Road'] }
  ];
  const CLASSES = ['Nursery', 'LKG', 'UKG', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8'];
  const FACILITIES = ['LEAD smart classrooms', 'CCTV surveillance', 'Safe, hygienic environment', 'Low student-teacher ratio', 'Activity-based learning', 'Value-based education'];
  const PHONE = '+91-6393477299', PHONE_HREF = '+916393477299', EMAIL = 'info@scholarsgroup.in';
  const SCHOOL_TITLE = 'Scholars’ Paradise International School, Lucknow';
  const TBD = 'Details for this page will be provided by the school.';
  const BUS_SVG = /*@BUS_SVG*/"";   // filled in by build.py
  const VAN_SVG = /*@VAN_SVG*/"";   // filled in by build.py

  /* Icon paths used on the overlay pages (24 x 24 grid). */
  const ICONS = {
    book: '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5zM4 19.5V22h16"/>',
    cap: '<path d="M2 9l10-5 10 5-10 5zM6 11v5c3 3 9 3 12 0v-5"/>',
    heart: '<path d="M12 21s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/>',
    bell: '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4"/>',
    pin: '<path d="M12 22s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    bus: '<rect x="3" y="4" width="18" height="13" rx="3"/><path d="M3 11h18M7 20v-3M17 20v-3"/>',
    cal: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    star: '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
    mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    rupee: '<path d="M7 5h10M7 9h10M7 5c6 0 6 8 0 8l7 6"/>'
  };

  /* Menu pages. Key = URL hash (#page-<key>).  group = sidebar section.
     sections = [heading, text | list of strings].  cta = show "Apply" button. */
  const PAGES = {
    'about': { group: 'About', title: 'Our School', icon: 'book',
      lead: 'Scholars’ Group of Institutions is a trusted English medium school group in Lucknow, run by the Sir Syed Educational And Welfare Trust. Every child is guided to discover their full potential.',
      sections: [['Quick facts', ['ICSE curriculum, Nursery to Class 8', 'LEAD smart classes, digital tools and activity-based learning', 'Six campuses: Vikas Nagar, Gaurabagh, Muazzam Nagar, Kursi, Kalyanpur and Ring Road', 'Experienced faculty, moral education and real-world skills']],
                 ['Early years', 'A play-based, hands-on programme for children aged 2 to 5 builds problem-solving, communication and creativity.']] },
    'why-choose-us': { group: 'About', title: 'Why Choose Us', icon: 'star', lead: 'Three reasons parents choose Scholars’ Paradise.',
      sections: [['ICSE English medium', 'A recognised curriculum that builds strong academic and communication skills. English, Science and Social Studies are taught with conceptual clarity.'],
                 ['Value-based learning', 'Ethics, compassion and respect are taught through a structured programme, delivered in English.'],
                 ['Holistic growth', 'An English-speaking environment that builds leadership and teamwork, with sports, arts and extracurriculars.']] },
    'vision': { group: 'About', title: 'Vision & Mission', icon: 'heart',
      lead: 'Our motto: creating learned scholars with impeccable characters who can become great future leaders.',
      sections: [['Vision and mission statements', 'The school’s formal vision and mission text is to be added by the school.']] },
    'values': { group: 'About', title: 'Core Values', icon: 'heart',
      lead: 'A value-based approach that builds character and confidence alongside academic excellence.',
      sections: [['What we teach', ['Ethics', 'Compassion', 'Respect']]] },

    'admission-process': { group: 'Academic', title: 'Admission Process', icon: 'cap', cta: true, lead: 'Admissions are open for 2026–27, Nursery to Class 8.',
      sections: [['Proposed flow (school to confirm)', ['Submit the enquiry form with class and area', 'The nearest campus calls you back', 'Campus visit and documents (to be confirmed)']], ['Note', TBD]] },
    'fees': { group: 'Academic', title: 'Fees Structure', icon: 'rupee', cta: true, document: 'fees', lead: 'Class-wise and campus-wise fees will be shown here.', sections: [] },
    'transport': { group: 'Academic', title: 'Transport', icon: 'bus', document: 'transport', lead: 'School bus and van routes and timings for each campus.', sections: [] },
    'calendar': { group: 'Academic', title: 'Academic Calendar', icon: 'cal', document: 'calendar', lead: 'Term dates, holidays and events.', sections: [] },

    'campuses': { group: 'Campuses', title: 'Campuses', icon: 'pin', lead: 'Six campuses across Lucknow. Pick one to see its own page.',
      sections: [['Our campuses', CAMPUSES.map(c => '<a href="#branch-' + c.slug + '">' + c.name + '</a>')]] },

    'ventures': { group: 'Ventures', title: 'Our Ventures', icon: 'star', lead: 'Programmes that extend learning beyond the classroom.',
      sections: [['Programmes', ['Scholars’ Hifz Academy', 'Scholars’ Study Center', 'Scholars’ NEET', 'Scholars’ Learning Labs', 'Scholars’ Hive', 'Scholars’ Booster']]] },
    'hifz': { group: 'Ventures', title: 'Hifz Academy', icon: 'book', logo: 'hifz', cta: true, lead: 'Quran memorisation (Hifz) with proper Tajweed, alongside regular ICSE schooling.',
      sections: [['About', 'An ICSE Board Islamic school programme that blends Quranic memorisation with high-quality academic education.']] },
    'study-center': { group: 'Ventures', title: 'Study Center', icon: 'book', lead: 'Extra academic support outside school hours.', sections: [['Details', TBD]] },
    'neet': { group: 'Ventures', title: 'NEET', icon: 'cap', lead: 'Preparation for the NEET medical entrance examination.', sections: [['Details', TBD], ['Official site', 'exams.nta.ac.in/NEET']] },
    'learning-labs': { group: 'Ventures', title: 'Learning Labs', icon: 'star', lead: 'Hands-on learning spaces.', sections: [['Details', TBD]] },
    'hive': { group: 'Ventures', title: 'Hive', icon: 'star', logo: 'hive', lead: 'Scholars’ Hive: towards transformation.', sections: [['Details', TBD]] },
    'booster': { group: 'Ventures', title: 'Booster', icon: 'star', lead: 'Revision and skill-building.', sections: [['Details', TBD]] },

    'notices': { group: 'Notices', title: 'Notices', icon: 'bell', lead: 'Latest announcements from the school.',
      sections: [['All notices', [
        '<a href="#page-notice-admissions">Admissions Open 2026–27 (new)</a>', '<a href="#page-notice-annual">Annual Function Day 2024</a>',
        '<a href="#page-notice-leave">Leave After Annual Function 2024</a>', '<a href="#page-notice-winter">Winter Vacation Announcement</a>']]] },
    'notice-admissions': { group: 'Notices', title: 'Admissions Open 2026–27', icon: 'bell', cta: true,
      lead: 'Enroll your child in the best English Medium School in Lucknow and secure their future with a trusted institution.', sections: [['Classes', 'Nursery to Class 8, across six campuses.']] },
    'notice-annual': { group: 'Notices', title: 'Annual Function Day 2024', icon: 'bell', lead: 'Notice listed on the current website (2024).', sections: [['Details', 'Full notice text to be added by the school.']] },
    'notice-leave': { group: 'Notices', title: 'Leave After Annual Function 2024', icon: 'bell', lead: 'Notice listed on the current website (2024).', sections: [['Details', 'Full notice text to be added by the school.']] },
    'notice-winter': { group: 'Notices', title: 'Winter Vacation Announcement', icon: 'bell', lead: 'Notice listed on the current website.', sections: [['Details', 'Full notice text to be added by the school.']] },

    'blogs': { group: 'Blogs', title: 'Blogs', icon: 'book', lead: 'Guides for parents.',
      sections: [['Latest posts', [
        '<a href="https://scholarsgroup.in/value-based-moral-education-in-lucknow-schools/" target="_blank" rel="noopener">Value-based moral education in Lucknow schools</a>',
        '<a href="https://scholarsgroup.in/islamic-studies-with-english-medium-curriculum/" target="_blank" rel="noopener">Islamic studies with English medium curriculum</a>',
        '<a href="https://scholarsgroup.in/hifz-e-quran-with-modern-icse-education-in-lucknow/" target="_blank" rel="noopener">Hifz e Quran with modern ICSE education in Lucknow</a>']]] },
    'contact': { group: 'Contact Us', title: 'Contact Us', icon: 'mail', cta: true, lead: 'We would love to hear from you.',
      sections: [['Reach us', ['<a href="mailto:' + EMAIL + '">' + EMAIL + '</a>', '<a href="tel:' + PHONE_HREF + '">' + PHONE + '</a>', '<a href="https://wa.me/' + PHONE_HREF + '" target="_blank" rel="noopener">WhatsApp</a>']],
                 ['Campuses', CAMPUSES.map(c => '<a href="#branch-' + c.slug + '">' + c.name + '</a>')]] }
  };

  /* ======================================================================
     2. HELPERS
     ====================================================================== */
  const $  = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const escapeAmp = (text) => text.replace(/&/g, '&amp;');
  const stripTags = (html) => html.replace(/<[^>]+>/g, '');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const logoSrc = () => $('.brand img').src;
  const overlay = $('#overlay');

  /* ======================================================================
     3. MODULES
     ====================================================================== */

  /* --- 3.1 Logo images that reuse the header logo (keeps the file small) --- */
  function initLogos() {
    $$('img[data-logo]').forEach((img) => { img.src = logoSrc(); });
    document.documentElement.style.setProperty('--watermark', 'url(' + logoSrc() + ')');
  }

  /* --- 3.2 Mobile menu --- */
  function initNavigation() {
    const nav = $('#main-nav'), button = $('#menu-toggle');
    button.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      button.setAttribute('aria-expanded', String(open));
    });
    $$('a', nav).forEach((link) => link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      button.setAttribute('aria-expanded', 'false');
    }));
  }

  /* --- 3.3 Hero slider (auto-plays, words animate in) --- */
  function initHero() {
    const slides = $$('.hero__slide'), dotsBox = $('#hero-dots');
    let current = 0, timer;
    $$('.hero__slide h2').forEach((h) => {
      h.innerHTML = h.textContent.trim().split(' ')
        .map((word, i) => '<span class="hero__word" style="animation-delay:' + (i * 0.09) + 's">' + word + '&nbsp;</span>').join('');
    });
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.setAttribute('aria-label', 'Slide ' + (i + 1));
      dot.addEventListener('click', () => show(i));
      dotsBox.appendChild(dot);
    });
    function show(index) {
      current = index;
      slides.forEach((slide, i) => slide.classList.toggle('is-active', i === index));
      $$('button', dotsBox).forEach((dot, i) => dot.classList.toggle('is-active', i === index));
      clearInterval(timer);
      timer = setInterval(() => show((current + 1) % slides.length), 5500);
    }
    show(0);
  }

  /* --- 3.4 Scroll effects: progress bar, hero parallax, reveal, counters --- */
  function initScrollEffects() {
    const bar = $('#progress-bar'), scene = $('#hero-scene');
    const counters = $$('[data-count]');

    function animateCount(el) {
      if (el.dataset.started) return;
      el.dataset.started = '1';
      const target = Number(el.dataset.count), format = (n) => n.toLocaleString('en-US') + '+';
      if (reducedMotion) { el.textContent = format(target); return; }
      let start = null;
      requestAnimationFrame(function step(now) {
        if (!start) start = now;
        const progress = Math.min((now - start) / 2200, 1);
        el.textContent = format(Math.round(target * (1 - Math.pow(1 - progress, 3))));   // ease-out
        if (progress < 1) requestAnimationFrame(step); else el.classList.add('is-done');
      });
    }
    function onScroll() {
      const root = document.documentElement;
      bar.style.width = (root.scrollTop / (root.scrollHeight - root.clientHeight) * 100) + '%';
      if (scene && !reducedMotion) scene.style.transform = 'translateY(' + (-root.scrollTop * 0.06) + 'px)';
      counters.forEach((el) => {
        const box = el.getBoundingClientRect();
        if (box.top < innerHeight * 0.92 && box.bottom > 0) animateCount(el);
      });
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    setTimeout(onScroll, 500);

    /* Stagger: each .reveal gets an index among its .reveal siblings (CSS turns it into a delay). */
    $$('.reveal').forEach((el) => {
      const siblings = Array.from(el.parentElement.children).filter((child) => child.classList.contains('reveal'));
      el.style.setProperty('--i', siblings.indexOf(el));
    });
    const reveal = new IntersectionObserver((entries) => entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      setTimeout(() => entry.target.classList.add('is-settled'), 1800);   // after the entrance, hover is quick again
      reveal.unobserve(entry.target);
    }), { threshold: 0.15 });
    $$('.reveal').forEach((el) => reveal.observe(el));
  }

  /* --- 3.5 Button ripple + card tilt --- */
  function initInteractions() {
    document.addEventListener('click', (event) => {
      const button = event.target.closest('.btn');
      if (!button || reducedMotion) return;
      const box = button.getBoundingClientRect(), ripple = document.createElement('span');
      ripple.className = 'ripple';
      ripple.style.left = (event.clientX - box.left - 10) + 'px';
      ripple.style.top = (event.clientY - box.top - 10) + 'px';
      button.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
    if (reducedMotion || !window.matchMedia('(pointer: fine)').matches) return;
    $$('.card').forEach((card) => {
      card.addEventListener('mousemove', (e) => {
        const box = card.getBoundingClientRect();
        const x = (e.clientX - box.left) / box.width - 0.5, y = (e.clientY - box.top) / box.height - 0.5;
        card.style.transform = 'perspective(700px) rotateY(' + x * 8 + 'deg) rotateX(' + (-y * 8) + 'deg)';
      });
      card.addEventListener('mouseleave', () => { card.style.transform = ''; });
    });
  }

  /* --- 3.6 Campus finder (select box + map pins) --- */
  function initCampusFinder() {
    const select = $('#finder-area'), result = $('#finder-result');
    const campusByArea = {};
    CAMPUSES.forEach((c) => c.areas.forEach((area) => { campusByArea[area] = c; }));

    function show(campus, area) {
      $$('.pin').forEach((pin) => pin.classList.toggle('is-active', !!campus && pin.dataset.campus === campus.slug));
      result.innerHTML = campus
        ? '<h3>' + campus.name + ' campus</h3><p>' + (area ? 'Nearest to ' + area + '. ' : '') + 'Address and phone to be added by the school.</p>' +
          '<a class="btn btn--green" target="_blank" rel="noopener" href="https://www.google.com/maps/search/Scholars+Paradise+International+School+' + encodeURIComponent(campus.name) + '+Lucknow">Open in Google Maps</a> ' +
          '<a class="btn" href="#branch-' + campus.slug + '">View campus page</a>'
        : '<p>Choose an area or tap a pin.</p>';
    }
    select.addEventListener('change', () => show(campusByArea[select.value], select.value));
    $$('.pin').forEach((pin) => {
      const activate = () => show(CAMPUSES.find((c) => c.slug === pin.dataset.campus));
      pin.addEventListener('click', activate);
      pin.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); } });
    });
    show(null);
  }

  /* --- 3.7 Parent testimonials (rotating) --- */
  function initTestimonials() {
    const quotes = $$('#testimonial blockquote'), dotsBox = $('#testimonial-dots');
    let current = 0;
    quotes.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.type = 'button'; dot.setAttribute('aria-label', 'Review ' + (i + 1));
      dot.addEventListener('click', () => show(i));
      dotsBox.appendChild(dot);
    });
    function show(index) {
      current = index;
      quotes.forEach((q, i) => { q.hidden = i !== index; });
      $$('button', dotsBox).forEach((d, i) => d.classList.toggle('is-active', i === index));
    }
    show(0);
    setInterval(() => show((current + 1) % quotes.length), 6000);
  }

  /* --- 3.8 Social reels: preview plays when visible; click to pause/play --- */
  function initReels() {
    const reels = $$('.reel');
    const visible = new IntersectionObserver((entries) => entries.forEach((entry) => {
      const reel = entry.target;
      if (reel.dataset.manual) return;                    // the visitor chose; leave it alone
      reel.classList.toggle('is-playing', entry.isIntersecting && !reducedMotion);
    }), { threshold: 0.6 });
    reels.forEach((reel) => {
      visible.observe(reel);
      $('.reel__play', reel).addEventListener('click', () => {
        reel.dataset.manual = '1';
        reel.classList.toggle('is-playing');
      });
    });
  }

  /* --- 3.9 Enquiry forms (inline form + pop-up share the same checks) --- */
  const isValidMobile = (value) => value.replace(/\D/g, '').slice(-10).length === 10;
  const campusForArea = (area) => (CAMPUSES.find((c) => c.areas.includes(area)) || CAMPUSES[0]).name;

  function initInlineForm() {
    const form = $('#enquiry-form'), steps = $$('.form-step', form), bars = $$('.form-steps span', form), message = $('#enq-message');
    const goTo = (n) => {
      steps.forEach((s, i) => s.classList.toggle('is-active', i === n));
      bars.forEach((b, i) => b.classList.toggle('is-active', i <= n));
    };
    $('#enq-next').addEventListener('click', () => {
      if (!$('#enq-name').value.trim() || !isValidMobile($('#enq-mobile').value)) {
        message.style.display = 'block'; message.textContent = 'Enter the parent name and a 10-digit mobile number.'; return;
      }
      message.style.display = 'none'; goTo(1);
    });
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      message.style.display = 'block';
      message.textContent = 'Thank you, ' + $('#enq-name').value.trim() + '. The ' + campusForArea($('#enq-area').value) + ' campus will call you about ' + $('#enq-class').value + '. (Demo: nothing was sent.)';
      form.reset(); goTo(0);
    });
  }

  function initAdmissionModal() {
    const modal = $('#admission-modal'), form = $('#modal-form'), message = $('#m-message');
    const FLAG = 'sp_admission_seen';

    function open(area) {
      if (!overlay.hidden) return;                         // do not cover a campus/menu page
      if (area) $('#m-area').value = area;
      message.style.display = 'none';
      modal.classList.add('is-open');
      setTimeout(() => $('#m-name').focus(), 60);
    }
    function close() {
      modal.classList.remove('is-open');
      try { sessionStorage.setItem(FLAG, '1'); } catch (e) { /* storage may be blocked */ }
    }
    window.openAdmission = open;                           // used by the overlay pages

    $$('[data-open-admission]').forEach((el) => el.addEventListener('click', (e) => { e.preventDefault(); open(); }));
    $('#modal-close').addEventListener('click', close);
    modal.addEventListener('click', (e) => { if (e.target === modal) close(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      message.style.display = 'block';
      if (!$('#m-name').value.trim() || !isValidMobile($('#m-mobile').value)) { message.textContent = 'Enter the parent name and a 10-digit mobile number.'; return; }
      message.textContent = 'Thank you, ' + $('#m-name').value.trim() + '. The ' + campusForArea($('#m-area').value) + ' campus will call you about ' + $('#m-class').value + '. (Demo: nothing was sent.)';
      form.reset();
      setTimeout(close, 3200);
    });
    /* open automatically once per visit */
    setTimeout(() => {
      let seen = false;
      try { seen = !!sessionStorage.getItem(FLAG); } catch (e) { /* ignore */ }
      if (!seen) open();
    }, 1200);
  }

  /* --- 3.10 Search-engine data that changes with the page being viewed --- */
  const seoDefaults = { title: document.title, description: ($('meta[name=description]') || {}).content };
  function setSeo(title, description, crumbs) {
    document.title = title;
    const meta = $('meta[name=description]');
    if (meta) meta.setAttribute('content', description);
    let script = $('#ld-breadcrumb');
    if (!script) { script = document.createElement('script'); script.type = 'application/ld+json'; script.id = 'ld-breadcrumb'; document.head.appendChild(script); }
    script.textContent = crumbs ? JSON.stringify({ '@context': 'https://schema.org', '@type': 'BreadcrumbList',
      itemListElement: crumbs.map((name, i) => ({ '@type': 'ListItem', position: i + 1, name: name })) }) : '';
  }

  /* --- 3.11 Overlay pages (menu pages and campus pages) --- */
  const HOME_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11l9-8 9 8M5 10v10h5v-6h4v6h5V10"/></svg>';

  /* Builds the common frame: top bar, banner, sidebar and main column. */
  function renderOverlay(o) {
    const sidebar = o.side.map((item, i) => '<a href="' + item.href + '"' + (item.current ? ' class="is-current"' : '') +
      ' style="animation:fade-up .4s ' + (i * 0.04) + 's backwards">' + item.label + '</a>').join('');
    overlay.innerHTML =
      '<div class="overlay__bar"><div class="container"><a class="overlay__brand" href="#" data-close><img src="' + logoSrc() + '" alt="" width="46">' +
        '<span><b>Scholars’ Group of Institutions</b><small>Scholars’ Paradise International School · Lucknow</small></span></a>' +
        '<button class="back-btn" type="button" data-close><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>Back to Home</button></div></div>' +
      '<div class="overlay__banner"><div class="container"><div>' +
        '<p class="breadcrumb"><a href="#" data-close>' + HOME_ICON + 'Home</a> › ' + o.section + ' › ' + escapeAmp(o.title) + '</p>' +
        '<h2>' + escapeAmp(o.title) + '</h2><p class="overlay__lead">' + o.lead + '</p>' +
        (o.cta ? '<p><button class="btn btn--green" type="button" data-apply>Apply / enquire now</button></p>' : '') +
      '</div>' + (o.logo ? '<img class="overlay__logo" src="' + o.logo + '" alt="">' : '<svg class="overlay__icon" viewBox="0 0 24 24" aria-hidden="true">' + o.icon + '</svg>') + '</div></div>' +
      '<div class="container overlay__layout"><aside class="overlay__side" aria-label="' + o.section + '"><h4>' + o.section + '</h4>' + sidebar + '</aside>' +
        '<div class="overlay__main">' + o.main + '</div></div>';
    overlay.hidden = false;
    overlay.scrollTop = 0;
    document.body.style.overflow = 'hidden';
    $$('[data-close]', overlay).forEach((el) => el.addEventListener('click', (e) => { e.preventDefault(); closeOverlay(); }));
    const apply = $('[data-apply]', overlay);
    if (apply) apply.addEventListener('click', () => { closeOverlay(); setTimeout(() => window.openAdmission(o.area), 150); });
    overlay.setAttribute('aria-label', stripTags(o.title));
    setSeo(o.seoTitle || stripTags(o.title) + ' | ' + SCHOOL_TITLE, o.seoDescription || stripTags(o.lead), ['Home', o.section, stripTags(o.title)]);
    $('.back-btn', overlay).focus();
  }

  function closeOverlay() {
    if (overlay.hidden) return;
    overlay.hidden = true;
    document.body.style.overflow = '';
    setSeo(seoDefaults.title, seoDefaults.description, null);
    if (/^#(branch|page)-/.test(location.hash)) location.hash = '';
  }

  /* Documents: letterhead + table, used by Fees, Transport and Calendar. */
  const letterhead = (title) =>
    '<div class="letterhead"><img src="' + logoSrc() + '" alt="School logo"><div><h3>SCHOLARS’ GROUP OF INSTITUTIONS</h3>' +
    '<p>Unit of Sir Syed Educational And Welfare Trust</p><p>' + SCHOOL_TITLE + ' · ' + EMAIL + ' · ' + PHONE + '</p></div></div>' +
    '<div class="document-title"><b>' + title + '</b></div>';
  const vehicleIcon = (kind) => kind === 'bus'
    ? '<svg class="vehicle" viewBox="0 0 34 22" aria-label="Bus"><rect x="1" y="2" width="32" height="15" rx="4" fill="#f2b705"/><path d="M5 6h5M12 6h5M19 6h5" stroke="#8fd3ff" stroke-width="3"/><circle cx="9" cy="18" r="3" fill="#222"/><circle cx="25" cy="18" r="3" fill="#222"/></svg>'
    : '<svg class="vehicle" viewBox="0 0 34 22" aria-label="Van"><rect x="1" y="4" width="32" height="13" rx="4" fill="#fff" stroke="#9fb0d8"/><path d="M4 7h8l3 4H4z" fill="#8fd3ff"/><rect x="1" y="12" width="32" height="2.5" fill="#029547"/><circle cx="9" cy="18" r="3" fill="#222"/><circle cx="25" cy="18" r="3" fill="#222"/></svg>';

  const DOCUMENTS = {
    fees() {
      const rows = CLASSES.map((c) => '<tr><td><b>' + c + '</b></td><td>—</td><td>—</td><td>—</td><td>—</td></tr>').join('');
      return '<div class="document">' + letterhead('Fee Structure · Academic Session 2026–27') +
        '<div class="table-wrap"><table class="data-table"><thead><tr><th>Class</th><th>Admission fee</th><th>Tuition fee (monthly)</th><th>Annual charges</th><th>Transport (optional)</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
        '<p class="document-note">Layout preview. Amounts are to be provided by the school and may differ by campus. Payment schedule and concessions: to be confirmed.</p></div>';
    },
    transport() {
      const rows = CAMPUSES.map((c) => '<tr><td><b>' + c.name + '</b></td><td>' + vehicleIcon('bus') + vehicleIcon('van') + 'Bus · Van</td><td>' + c.areas.join(', ') + '</td><td>—</td><td>—</td></tr>').join('');
      const road = '<div class="road-scene"><svg viewBox="0 0 520 150" role="img" aria-label="A school bus and a school van on the road">' +
        '<rect width="520" height="150" fill="#eaf3ff"/><circle class="sun-pulse" cx="470" cy="30" r="16" fill="#ff9f1c"/><g class="cloud-a" fill="#fff"><ellipse cx="90" cy="30" rx="30" ry="11"/><ellipse cx="110" cy="23" rx="18" ry="10"/></g>' +
        '<rect y="66" width="520" height="84" fill="#cfe8cf"/><rect y="82" width="520" height="58" fill="#2a2f2c"/><path d="M0 111h520" stroke="#fff" stroke-dasharray="16 12" stroke-width="2"/>' +
        '<rect x="40" y="36" width="8" height="40" fill="#6b4226"/><circle cx="44" cy="32" r="20" fill="#2e9d54"/><rect x="420" y="46" width="6" height="30" fill="#888"/>' +
        '<polygon points="423,22 441,40 423,58 405,40" fill="#fef100" stroke="#123075" stroke-width="2"/><text x="423" y="43" text-anchor="middle" style="font-size:7px;font-weight:700">SCHOOL</text>' +
        '<g transform="translate(0,80)"><g class="road-van">' + VAN_SVG + '</g></g><g transform="translate(0,99)"><g class="road-bus">' + BUS_SVG + '</g></g></svg></div>';
      return road + '<div class="document">' + letterhead('School Transport · Academic Session 2026–27') +
        '<div class="table-wrap"><table class="data-table"><thead><tr><th>Campus</th><th>Vehicle</th><th>Areas covered (demo)</th><th>Pick-up window</th><th>Monthly charge</th></tr></thead><tbody>' + rows + '</tbody></table></div>' +
        '<p class="document-note">Layout preview. Routes, timings and charges are to be provided by the school. Area mapping is a demo.</p></div>';
    },
    calendar() {
      const months = ['April 2026', 'May 2026', 'June 2026', 'July 2026', 'August 2026', 'September 2026', 'October 2026', 'November 2026', 'December 2026', 'January 2027', 'February 2027', 'March 2027'];
      const now = new Date(), thisMonth = now.toLocaleString('en-US', { month: 'long' }) + ' ' + now.getFullYear();
      const cards = months.map((m, i) => '<div class="month' + (m === thisMonth ? ' is-now' : '') + '" style="animation-delay:' + (i * 0.04) + 's"><b>' + m + '</b><span>Dates to be announced</span>' +
        (m === thisMonth ? '<em>This month · Admissions open 2026–27</em>' : '') + '</div>').join('');
      return '<div class="document">' + letterhead('Academic Calendar · Session 2026–27') + '<div class="month-grid">' + cards + '</div>' +
        '<p class="document-note">Layout preview. Term dates, holidays and events are to be provided by the school. Current announcements are listed under <a href="#page-notices">Notices</a>.</p></div>';
    }
  };

  function openPage(key) {
    const page = PAGES[key];
    if (!page) return;
    const siblings = Object.keys(PAGES).filter((k) => PAGES[k].group === page.group);
    const sectionsHtml = page.sections.map((s, i) => {
      const body = Array.isArray(s[1]) ? '<div class="check-list">' + s[1].map((item) => '<div>' + item + '</div>').join('') + '</div>' : '<p style="max-width:70ch">' + s[1] + '</p>';
      return '<div style="animation:fade-up .5s ' + (0.1 + i * 0.08) + 's backwards"><h3>' + s[0] + '</h3>' + body + '</div>';
    }).join('');
    renderOverlay({
      section: page.group, title: page.title, lead: page.lead, icon: ICONS[page.icon], cta: page.cta,
      logo: page.logo ? $('.venture__logo[data-venture="' + page.logo + '"]').src : '',
      side: siblings.map((k) => ({ href: '#page-' + k, label: escapeAmp(PAGES[k].title), current: k === key })),
      main: page.document ? DOCUMENTS[page.document]() : sectionsHtml
    });
  }

  function openCampus(slug) {
    const campus = CAMPUSES.find((c) => c.slug === slug);
    if (!campus) return;
    const art = $('.campus-card[data-campus="' + slug + '"] svg');            // reuse the card illustration
    const main = '<div class="campus-hero">' + (art ? art.outerHTML : '') + '</div>' +
      '<p><button class="btn btn--green" type="button" data-apply>Apply at this campus</button> ' +
      '<a class="btn" target="_blank" rel="noopener" href="https://www.google.com/maps/search/Scholars+Paradise+International+School+' + encodeURIComponent(campus.name) + '+Lucknow">Open in Google Maps</a></p>' +
      '<h3>Facilities</h3><div class="check-list">' + FACILITIES.map((f, i) => '<div style="animation:fade-up .5s ' + (i * 0.07) + 's backwards">' + f + '</div>').join('') + '</div>' +
      '<h3>Classes</h3><div class="chip-list">' + CLASSES.map((c, i) => '<span style="animation-delay:' + (i * 0.05) + 's">' + c + '</span>').join('') + '</div>' +
      '<p class="muted">Branch-wise class availability is to be confirmed by the school.</p>' +
      '<h3>Areas this campus serves</h3><div class="chip-list">' + campus.areas.map((a) => '<span>' + a + '</span>').join('') + '</div><p class="muted">Demo mapping.</p>' +
      '<h3>Contact</h3><p>' + PHONE + ' · ' + EMAIL + '</p>';
    renderOverlay({
      section: 'Campuses', title: campus.name + ' Campus', icon: ICONS.pin, area: campus.areas[0], main: main,
      lead: 'ICSE English medium school in ' + campus.name + ', Lucknow · Nursery to Class 8 · LEAD smart classes',
      seoTitle: campus.name + ' Campus | ICSE English Medium School in ' + campus.name + ', Lucknow | Scholars’ Paradise',
      seoDescription: 'Scholars’ Paradise ' + campus.name + ' campus: ICSE English medium school in ' + campus.name + ', Lucknow. Nursery to Class 8, LEAD smart classes, safe CCTV-monitored campus. Admissions open 2026–27.',
      side: CAMPUSES.map((c) => ({ href: '#branch-' + c.slug, label: c.name + ' Campus', current: c.slug === slug }))
    });
  }

  /* --- 3.12 Router: the URL hash decides which overlay is shown --- */
  function route() {
    const hash = location.hash;
    if (hash.indexOf('#page-') === 0) openPage(hash.slice(6));
    else if (hash.indexOf('#branch-') === 0) openCampus(hash.slice(8));
    else if (!overlay.hidden) { overlay.hidden = true; document.body.style.overflow = ''; setSeo(seoDefaults.title, seoDefaults.description, null); }
  }
  function initRouter() {
    window.addEventListener('hashchange', route);
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeOverlay(); });
    route();
  }

  /* --- 3.13 "Show my changes" (presentation helper, remove on the live site) --- */
  function initPresentationToggle() {
    const button = $('#toggle-changes');
    button.addEventListener('click', () => {
      const on = document.body.classList.toggle('show-changes');
      button.setAttribute('aria-pressed', String(on));
      button.textContent = on ? 'Hide my changes' : 'Show my changes';
    });
  }

  /* ======================================================================
     4. START
     ====================================================================== */
  initLogos();
  initNavigation();
  initHero();
  initScrollEffects();
  initInteractions();
  initCampusFinder();
  initTestimonials();
  initReels();
  initInlineForm();
  initAdmissionModal();
  initPresentationToggle();
  initRouter();
}());
