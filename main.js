/* MAKE · v2 · interactions et animations (sans dépendance) */
(function () {
  'use strict';
  var GA_ID = 'G-N2FMZ4BVCC';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var doc = document.documentElement;

  /* ── Année automatique ─────────────────────────── */
  document.querySelectorAll('.year').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ── En-tête compact au défilement ─────────────── */
  var onScroll = function () { doc.classList.toggle('is-scrolled', window.scrollY > 24); };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ── Menu mobile ───────────────────────────────── */
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.main-nav');
  if (burger && nav) {
    var setOpen = function (open) {
      nav.classList.toggle('nav-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
    };
    burger.addEventListener('click', function () { setOpen(!nav.classList.contains('nav-open')); });
    nav.querySelectorAll('.nav-links a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  }

  /* ── Titre mot par mot ─────────────────────────── */
  document.querySelectorAll('.h-anim').forEach(function (h) {
    var i = 0, frag = document.createDocumentFragment();
    Array.prototype.slice.call(h.childNodes).forEach(function (node) {
      if (node.nodeType === 3) {
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
          var s = document.createElement('span');
          s.className = 'h-word'; s.textContent = part; s.style.animationDelay = (i++ * 70) + 'ms';
          frag.appendChild(s);
        });
      } else if (node.nodeName === 'BR') {
        frag.appendChild(node);
      } else {
        node.classList.add('h-word'); node.style.animationDelay = (i++ * 70) + 'ms';
        frag.appendChild(node);
      }
    });
    h.innerHTML = ''; h.appendChild(frag);
  });

  /* ── Apparitions au défilement ─────────────────── */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    document.querySelectorAll('[data-stagger]').forEach(function (parent) {
      Array.prototype.slice.call(parent.children).forEach(function (c, k) {
        c.classList.add('reveal'); c.style.transitionDelay = (k % 4) * 110 + 'ms';
      });
    });
    reveals = document.querySelectorAll('.reveal');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ── Compteurs ─────────────────────────────────── */
  var counters = document.querySelectorAll('[data-count]');
  var runCount = function (el) {
    var to = parseFloat(el.dataset.count), suffix = el.dataset.suffix || '', t0 = null;
    if (reduce) { el.textContent = to + suffix; return; }
    var step = function (t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / 1400, 1), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(to * eased).toLocaleString('fr-FR') + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { runCount(e.target); co.unobserve(e.target); } });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { co.observe(el); });
  }

  /* ── Halo des cartes ───────────────────────────── */
  document.querySelectorAll('.card').forEach(function (c) {
    c.addEventListener('pointermove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--x', (e.clientX - r.left) + 'px');
      c.style.setProperty('--y', (e.clientY - r.top) + 'px');
    });
  });

  /* ── FAQ ───────────────────────────────────────── */
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      var item = q.closest('.faq-item'), open = !item.classList.contains('open');
      item.classList.toggle('open', open);
      q.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ── Sous-navigation : section active ──────────── */
  var subLinks = document.querySelectorAll('.subnav a[href^="#"]');
  if (subLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    subLinks.forEach(function (a) { var t = document.getElementById(a.getAttribute('href').slice(1)); if (t) map[t.id] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        subLinks.forEach(function (a) { a.classList.remove('active'); a.removeAttribute('aria-current'); });
        var a = map[e.target.id]; a.classList.add('active'); a.setAttribute('aria-current', 'true');
        var w = a.parentElement; w.scrollTo({ left: a.offsetLeft - 16, behavior: reduce ? 'auto' : 'smooth' });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(map).forEach(function (id) { spy.observe(document.getElementById(id)); });
  }

  /* ── Onglets ───────────────────────────────────── */
  var tabs = document.querySelectorAll('[role="tab"]');
  if (tabs.length) {
    var select = function (tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
      if (focus) tab.focus();
    };
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t); history.replaceState(null, '', '#' + t.getAttribute('aria-controls')); });
      t.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        var n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length]; select(n, true);
      });
    });
    var h = location.hash.slice(1);
    tabs.forEach(function (t) {
      if (t.getAttribute('aria-controls') === h) {
        select(t);
        setTimeout(function () { document.getElementById('formules').scrollIntoView(); }, 50);
      }
    });
  }

  /* ── Vidéo : YouTube chargé au clic seulement ──── */
  document.querySelectorAll('[data-video]').forEach(function (box) {
    var btn = box.querySelector('.video-play');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + box.dataset.video + '?autoplay=1&rel=0&modestbranding=1';
      f.title = 'Démonstration de FireTraining MS';
      f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      box.appendChild(f); btn.remove();
      if (window.gtag) window.gtag('event', 'video_play', { video: 'firetraining-demo' });
    });
  });

  /* ── Braises (canvas) ──────────────────────────── */
  document.querySelectorAll('canvas[data-embers]').forEach(function (cv) {
    var host = cv.parentElement, ctx = cv.getContext('2d');
    var count = parseInt(cv.dataset.embers, 10) || 40;
    var dpr = Math.min(window.devicePixelRatio || 1, 2), W = 0, H = 0, P = [], running = false, raf;
    var size = function () { W = host.clientWidth; H = host.clientHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); };
    var spawn = function (y) {
      return { x: W * (0.25 + Math.random() * 0.75), y: y === undefined ? H + 10 : y, r: 0.7 + Math.random() * 1.8,
        vy: 0.2 + Math.random() * 0.5, vx: (Math.random() - 0.5) * 0.2, a: 0.25 + Math.random() * 0.6, ph: Math.random() * 6.28 };
    };
    var draw = function () {
      ctx.clearRect(0, 0, W, H);
      for (var k = 0; k < P.length; k++) {
        var p = P[k];
        p.y -= p.vy; p.ph += 0.02; p.x += p.vx + Math.sin(p.ph) * 0.18;
        var life = Math.max(0, p.y / H);
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.283);
        ctx.fillStyle = 'rgba(236,' + Math.round(105 + 70 * life) + ',60,' + (p.a * life).toFixed(3) + ')';
        ctx.shadowColor = 'rgba(224,102,44,.8)'; ctx.shadowBlur = 8; ctx.fill();
        if (p.y < -10) P[k] = spawn();
      }
      if (running) raf = requestAnimationFrame(draw);
    };
    size();
    for (var i = 0; i < count; i++) P.push(spawn(Math.random() * H));
    window.addEventListener('resize', size);
    if (reduce) { draw(); return; }
    new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && !running) { running = true; draw(); }
        else if (!e.isIntersecting) { running = false; cancelAnimationFrame(raf); }
      });
    }, { threshold: 0.05 }).observe(host);
  });

  /* ── Cookies : Google Analytics seulement après accord ── */
  var KEY = 'make-consent';
  var read = function () { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
  var write = function (v) { try { localStorage.setItem(KEY, v); } catch (e) {} };
  var loadGA = function () {
    if (window.__gaLoaded) return; window.__gaLoaded = true;
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date()); window.gtag('config', GA_ID, { anonymize_ip: true });
  };
  var banner = document.getElementById('cookie');
  var showBanner = function () { if (!banner) return; banner.hidden = false; requestAnimationFrame(function () { banner.classList.add('show'); }); };
  var hideBanner = function () { if (!banner) return; banner.classList.remove('show'); setTimeout(function () { banner.hidden = true; }, 400); };
  var choice = read();
  if (choice === 'accepted') loadGA(); else if (!choice) setTimeout(showBanner, 900);
  document.querySelectorAll('[data-consent]').forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.dataset.consent; write(v); hideBanner();
      if (v === 'accepted') loadGA();
    });
  });
  document.querySelectorAll('[data-cookie-settings]').forEach(function (b) { b.addEventListener('click', showBanner); });

  /* ── Formulaire de contact (Apps Script, JSONP) ── */
  var form = document.getElementById('contact-form');
  if (form) {
    var select = document.getElementById('objet');
    var sujets = {
      formation: ['Formation incendie / EPI', 'Formation SST / Secourisme', 'Formation réglementaire', 'Programme sur mesure'],
      firetraining: ['Démo FireTraining MS', 'Formation avec FireTraining MS (mes équipes)', 'Licence annuelle FireTraining MS (OF)', 'Achat FireTraining MS (formateur indépendant)'],
      conseil: ['Diagnostic initial offert (30 min)', 'DUERP clé en main', 'Prévention des RPS', 'Audit sécurité & incendie', 'Normes ISO (45001 / 9001 / 14001)', 'PCA ou PCS']
    };
    var fill = function (u, preset) {
      select.innerHTML = '<option value="">Choisir un sujet</option>';
      (sujets[u] || []).concat(['Autre demande']).forEach(function (s) {
        var o = document.createElement('option'); o.textContent = s; if (s === preset) o.selected = true; select.appendChild(o);
      });
      document.body.dataset.univers = u;
    };
    var params = new URLSearchParams(location.search);
    var u0 = params.get('univers'); if (!sujets[u0]) u0 = 'formation';
    var radio = form.querySelector('input[name="univers"][value="' + u0 + '"]'); if (radio) radio.checked = true;
    fill(u0, params.get('sujet'));
    form.querySelectorAll('input[name="univers"]').forEach(function (r) { r.addEventListener('change', function () { fill(r.value); }); });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var url = 'https://script.google.com/macros/s/AKfycbzcmJ85wr7qaQU-75tYN67jIIUaPOS5py2aJTYCp5-KAxZ_UILnc8EBDagtlojyWV6X/exec';
      var btn = document.getElementById('contact-submit'), err = document.getElementById('contact-error');
      var label = btn.innerHTML;
      btn.disabled = true; btn.textContent = 'Envoi en cours…'; err.hidden = true;
      var q = 'action=recevoir_lead_site&token=MAKE-SITE-2026';
      ['prenom', 'nom', 'organisation', 'email', 'telephone', 'objet', 'message'].forEach(function (n) {
        var el = form.querySelector('[name="' + n + '"]');
        var v = el ? el.value : '';
        if (n === 'objet') { var u = form.querySelector('input[name="univers"]:checked'); v = (u ? '[' + u.value + '] ' : '') + v; }
        q += '&' + encodeURIComponent(n) + '=' + encodeURIComponent(v);
      });
      var cb = 'jsonp_make_' + Date.now(), s = document.createElement('script'), timer;
      var cleanup = function () { delete window[cb]; if (s.parentNode) s.parentNode.removeChild(s); };
      var fail = function () { clearTimeout(timer); cleanup(); btn.disabled = false; btn.innerHTML = label; err.hidden = false; };
      window[cb] = function () {
        clearTimeout(timer); cleanup();
        document.getElementById('form-zone').innerHTML =
          '<div class="form-success"><div class="ico-tile"><svg class="ico" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></svg></div>' +
          '<h3>Message envoyé</h3><p class="lead">Merci. Je vous réponds sous 24 h ouvrées.</p></div>';
        if (window.gtag) window.gtag('event', 'generate_lead');
      };
      s.onerror = fail;
      timer = setTimeout(fail, 12000);
      s.src = url + '?' + q + '&callback=' + cb;
      document.body.appendChild(s);
    });
  }
})();
