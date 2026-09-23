# Gabarits du site make-consulting.fr (même système que formation-incendie-paris.com)
import json
from icons_src import ICONS

ICONS = dict(ICONS)
ICONS.update({
 'external': '<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 'briefcase': '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 'radio': '<path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5M19.1 4.9C23 8.8 23 15.1 19.1 19"/><circle cx="12" cy="12" r="2"/>',
 'leaf': '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
})

BASE = 'https://make-consulting.fr/'
FORMATION = 'https://www.formation-incendie-paris.com/'
EMAIL = 'maxence@make-consulting.fr'

def ico(name, cls='ico', extra=''):
    return f'<svg class="{cls}{extra}" viewBox="0 0 24 24" aria-hidden="true"><use href="#i-{name}"/></svg>'

def sprite():
    return '<svg width="0" height="0" style="position:absolute" aria-hidden="true">' + ''.join(
        f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + '</svg>'

def ext(href, label, cls='link-arrow'):
    return f'<a class="{cls}" href="{href}" target="_blank" rel="noopener">{label} {ico("external")}<span class="sr-only"> (nouvel onglet)</span></a>'

def head(title, desc, canonical, extra=''):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}{canonical}">
<meta property="og:image" content="{BASE}assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1A2548">
<link rel="icon" href="assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/favicon-180.png">
<link rel="manifest" href="assets/site.webmanifest">
<link rel="preload" href="assets/fonts/manrope.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css">
<script>document.documentElement.classList.add('js');</script>
{extra}
</head>'''

NAV = [('DUERP', 'duerp.html'), ('Audit et ISO', 'audit-qse.html'), ('Incendie et SSIAP', 'securite-incendie.html'),
       ('Références', 'references.html'), ('À propos', 'a-propos.html')]
DIAG = 'contact.html?sujet=Diagnostic%20initial%20offert%20(30%20min)'

def header(current=''):
    links = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == current else '') + f'>{l}</a></li>' for l, h in NAV)
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="univers-bar">
    <div class="wrap">
      <p class="topline"><span class="dot-or" aria-hidden="true"></span>Cabinet conseil QSE et prévention · IPRP déclaré</p>
      <div class="topright">
        <a class="toplink" href="{FORMATION}" target="_blank" rel="noopener">Formation incendie et FireTraining MS {ico('external')}<span class="sr-only"> (autre site, nouvel onglet)</span></a>
        <a class="tel" href="tel:+33684527858">{ico('phone')}<span>06 84 52 78 58</span></a>
      </div>
    </div>
  </div>
  <div class="main-nav">
    <div class="wrap">
      <a class="brand" href="index.html" aria-label="MAKE Consulting, accueil">
        <img src="assets/logo.png" alt="" width="200" height="262">
        <span class="brand-txt"><strong>MAKE Consulting</strong><span>Conseil QSE · Prévention · IPRP</span></span>
      </a>
      <nav aria-label="Navigation principale">
        <ul class="nav-links" id="nav-links">
          {links}
          <li><a class="btn btn-primary btn-sm" href="{DIAG}">Diagnostic offert {ico('arrow', extra=' ico-arrow')}</a></li>
        </ul>
      </nav>
      <button class="burger" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img class="logo-chip" src="assets/logo.png" alt="MAKE Consulting" width="200" height="262" loading="lazy">
        <p>MAKE Consulting, cabinet conseil en qualité, sécurité et environnement. Maxence Soileux, IPRP déclaré et sapeur-pompier volontaire depuis 2012. Île-de-France et France entière.</p>
      </div>
      <div>
        <h3 class="h4">Missions</h3>
        <ul>
          <li><a href="duerp.html">DUERP clé en main</a></li>
          <li><a href="audit-qse.html">Audit QSE et ISO</a></li>
          <li><a href="prevention-rps.html">Prévention des RPS</a></li>
          <li><a href="securite-incendie.html">Sécurité incendie</a></li>
          <li><a href="diagnostic-ssiap.html">Diagnostic SSIAP</a></li>
          <li><a href="continuite-activite.html">PCA et PCS</a></li>
          <li><a href="iprp-externalise.html">IPRP externalisé</a></li>
        </ul>
      </div>
      <div>
        <h3 class="h4">Formation</h3>
        <ul>
          <li><a href="{FORMATION}formation-incendie.html" target="_blank" rel="noopener">Formation incendie</a></li>
          <li><a href="{FORMATION}formation-sst.html" target="_blank" rel="noopener">SST et secourisme</a></li>
          <li><a href="{FORMATION}firetraining-ms.html" target="_blank" rel="noopener">FireTraining MS</a></li>
          <li><a href="{FORMATION}" target="_blank" rel="noopener">formation-incendie-paris.com</a></li>
        </ul>
      </div>
      <div>
        <h3 class="h4">Contact</h3>
        <ul>
          <li><a href="tel:+33684527858">06 84 52 78 58</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{DIAG}">Diagnostic offert (30 min)</a></li>
          <li><a href="faq.html">Questions fréquentes</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© <span class="year">2026</span> MAKE Consulting · Maxence Soileux · L'Île-Saint-Denis</span>
      <span><a href="mentions-legales.html">Mentions légales</a> · <button type="button" data-cookie-settings>Gérer les cookies</button></span>
    </div>
  </div>
</footer>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookies" hidden>
  <p>J'utilise Google Analytics pour mesurer la fréquentation du site, uniquement avec votre accord. <a href="mentions-legales.html#cookies">En savoir plus</a></p>
  <div class="cookie-btns">
    <button class="btn btn-ghost btn-sm" type="button" data-consent="refused">Refuser</button>
    <button class="btn btn-primary btn-sm" type="button" data-consent="accepted">Accepter</button>
  </div>
</div>
<script src="main.js" defer></script>
</body>
</html>'''

def page(title, desc, canonical, body, extra_head='', current=''):
    return (head(title, desc, canonical, extra_head) + '\n<body data-univers="conseil">\n' + sprite() + '\n'
            + header(current) + '\n<main id="contenu">\n' + body + '\n</main>\n' + footer())

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

# ── composants ────────────────────────────────────────
def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{ico("check")}{i}</li>' for i in items) + '</ul>'

def faq_item(q, a, open_=False):
    o = ' open' if open_ else ''
    return f'<div class="faq-item{o}"><button class="faq-q" type="button" aria-expanded="{"true" if open_ else "false"}">{q}<span class="pm">{ico("plus")}</span></button><div class="faq-a"><div><p>{a}</p></div></div></div>'

def faq_block(titre, items, eyebrow='Questions fréquentes', tint=True):
    fq = ''.join(faq_item(q, a, k == 0) for k, (q, a) in enumerate(items))
    return f'''<section class="section{' section--tint' if tint else ''}" id="faq">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal"><span class="eyebrow">{eyebrow}</span><h2>{titre}</h2></div>
    <div class="faq reveal">{fq}</div>
    <p style="text-align:center;margin-top:28px"><a class="link-arrow" href="faq.html">Toutes les questions {ico('arrow')}</a></p>
  </div>
</section>'''

def cta(titre, texte, sujet='Diagnostic%20initial%20offert%20(30%20min)', label='Réserver le diagnostic offert'):
    return f'''<section class="section">
  <div class="wrap">
    <div class="cta-band reveal">
      <div><h2>{titre}</h2><p>{texte}</p></div>
      <div class="btns"><a class="btn btn-light" href="contact.html?sujet={sujet}">{label} {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a></div>
    </div>
  </div>
</section>'''

def page_hero(crumb, h1, lead, facts=None, btns=True, sujet='Diagnostic%20initial%20offert%20(30%20min)'):
    kf = ''.join(f'<span class="pill">{ico(i)}{t}</span>' for i, t in (facts or []))
    b = f'<div class="hero-btns"><a class="btn btn-primary" href="contact.html?sujet={sujet}">Demander un devis {ico("arrow", extra=" ico-arrow")}</a><a class="btn btn-ghost" href="{DIAG}">Diagnostic offert (30 min)</a></div>' if btns else ''
    return f'''<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
    <h1 class="h-anim">{h1}</h1>
    <p class="lead">{lead}</p>
    {f'<div class="keyfacts">{kf}</div>' if kf else ''}
    {b}
  </div>
</section>'''

def case(tag, year, titre, contexte, fait, quote=None, lieu=''):
    items = checks(fait) if fait else ''
    q = f'<figure class="case-quote"><blockquote>{quote[0]}</blockquote><figcaption>{quote[1]}</figcaption></figure>' if quote else ''
    meta = ' · '.join(x for x in [lieu, year] if x)
    return f'''<article class="card case" data-tag="{tag}"><div class="case-head"><span class="pill pill--acc">{tag}</span><span class="case-year">{meta}</span></div><h3>{titre}</h3><p>{contexte}</p>{items}{q}</article>'''

def steps(items, four=False):
    return f'<ol class="steps{" steps--4" if four else ""}" data-stagger>' + ''.join(f'<li><h3 class="h4">{t}</h3><p>{d}</p></li>' for t, d in items) + '</ol>'

def formation_band():
    return f'''<section class="section section--dark">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Formation</span>
      <h2>Former vos équipes après le diagnostic</h2>
      <p class="lead">Formation incendie, SST, risques chimiques, prévention des RPS : les formations sont présentées sur un site dédié, avec les programmes détaillés et le module de réalité mixte FireTraining MS.</p>
      <div class="hero-btns">{ext(FORMATION, 'Voir formation-incendie-paris.com', 'btn btn-light')}{ext(FORMATION + 'firetraining-ms.html', 'FireTraining MS', 'btn btn-outline-light')}</div>
    </div>
    <div class="media reveal"><img src="assets/firetraining-screenshot.jpg" alt="Vue de l'application FireTraining MS : extincteur virtuel face à un départ de feu" width="1200" height="799" loading="lazy"></div>
  </div>
</section>'''
