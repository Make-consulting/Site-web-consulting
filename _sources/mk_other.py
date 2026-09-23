import re
from mk import *
from mk_pages import ALL_CASES, METHODE

# ─── RÉFÉRENCES ─────────────────────────────────────────
def build_refs():
    tags = []
    for c in ALL_CASES:
        t = re.search(r'data-tag="([^"]+)"', c).group(1)
        if t not in tags: tags.append(t)
    btns = '<button type="button" data-filter="all" aria-pressed="true">Toutes</button>' + ''.join(f'<button type="button" data-filter="{t}" aria-pressed="false">{t}</button>' for t in tags)
    body = f'''
{page_hero('Références', 'Missions <span class="accent">réalisées</span>',
  "Des missions réelles, en Île-de-France et ailleurs en France. Les clients ne sont pas nommés : c'est un engagement de confidentialité que je tiens pour chacun.", btns=False)}
<section class="section">
  <div class="wrap">
    <div class="cases-filter" role="group" aria-label="Filtrer par type de mission">{btns}</div>
    <div class="grid-2" id="cases" data-stagger>{''.join(ALL_CASES)}</div>
  </div>
</section>
<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Formation</span><h2>Et côté formation</h2><p class="lead">Formations incendie et SST pour une PME industrielle de 80 salariés, un établissement médico-social, des organismes de formation : les références formation sont sur le site dédié.</p></div>
    {ext(FORMATION + '#references', 'Voir les références formation')}
  </div>
</section>
{cta('Votre situation ressemble à l’une de ces missions ?', "Parlons-en : le premier échange de 30 minutes est offert.")}
'''
    return page("Références et missions réalisées | MAKE Consulting",
        "Missions de conseil réalisées par MAKE Consulting : DUERP, audit ISO 9001, triple certification, diagnostic organisationnel, plan de continuité d'activité. Clients anonymisés.",
        'references.html', body, current='references.html')

# ─── À PROPOS ───────────────────────────────────────────
def build_about():
    body = f'''
{page_hero('À propos', 'Maxence Soileux, <span class="accent">fondateur de MAKE Consulting</span>',
  "Consultant QSE indépendant, IPRP déclaré et sapeur-pompier volontaire depuis 2012. Une structure sans intermédiaire : la personne qui vous répond est celle qui vient sur votre site.", btns=False)}

<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="split-txt reveal">
      <span class="eyebrow">Parcours</span>
      <h2>Pourquoi MAKE Consulting</h2>
      <p>En intervenant sur des sites industriels, des établissements médico-sociaux, des bureaux et des entrepôts, j'ai fait le même constat : les dirigeants veulent bien faire, mais personne ne leur explique concrètement quoi faire, ni comment le prouver.</p>
      <p>MAKE Consulting est né de ce constat, en 2019. Une structure agile, où vous avez directement en ligne la personne qui évaluera vos risques et rédigera vos documents. Pas une équipe anonyme, pas un sous-traitant.</p>
      <p>Sapeur-pompier volontaire en Île-de-France depuis 2012, je ne parle pas de sécurité depuis un bureau. Intervenir dans un environnement dégradé, gérer l'urgence, communiquer avec des équipes sous pression : cette expérience nourrit chacune de mes recommandations.</p>
      <p>J'enseigne aussi en école d'ingénieurs et en IUT, du Bac+3 au Master, sur l'AMDEC, les risques psychosociaux, la sécurité incendie et le management QSE.</p>
    </div>
    <div class="card cert-card reveal">
      <ul class="cert-list">
        <li><span class="ico-tile">{ico('scale')}</span><div><strong>IPRP déclaré</strong><span>Intervenant en prévention des risques professionnels, Île-de-France</span></div></li>
        <li><span class="ico-tile">{ico('shield')}</span><div><strong>Sapeur-pompier volontaire</strong><span>En Île-de-France depuis 2012</span></div></li>
        <li><span class="ico-tile">{ico('grad')}</span><div><strong>Master MQSE</strong><span>Management qualité, sécurité, environnement</span></div></li>
        <li><span class="ico-tile">{ico('flame')}</span><div><strong>SSIAP 1 et SSIAP 3</strong><span>Agent et chef de service sécurité incendie</span></div></li>
        <li><span class="ico-tile">{ico('heart')}</span><div><strong>Formateur SST agréé INRS</strong><span>Sauveteur secouriste du travail</span></div></li>
        <li><span class="ico-tile">{ico('hardhat')}</span><div><strong>Encadrant technique amiante SS4</strong><span>Sous-section 4</span></div></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Valeurs</span><h2>Trois engagements vérifiables</h2></div>
    <div class="pillars" data-stagger>
      <div class="pillar"><span class="ico-tile">{ico('target')}</span><h3>Rigueur</h3><p>Un document unique ou un rapport d'audit n'a de valeur que s'il est exact, complet et défendable. Chaque évaluation suit une méthode structurée, tracée et reproductible.</p></div>
      <div class="pillar"><span class="ico-tile">{ico('eye')}</span><h3>Terrain</h3><p>Les risques se voient sur le poste de travail, s'entendent dans les pratiques quotidiennes, se lisent dans les accidents passés. Le travail commence toujours là.</p></div>
      <div class="pillar"><span class="ico-tile">{ico('scale')}</span><h3>Indépendance</h3><p>Pas d'actionnaire à satisfaire, pas de produit à vendre en complément. Les recommandations servent votre intérêt, pas un catalogue.</p></div>
    </div>
  </div>
</section>

{formation_band()}

{cta('Travaillons ensemble', "Le premier échange de 30 minutes est offert, sans engagement.")}
'''
    return page("À propos | Maxence Soileux, consultant QSE et IPRP | MAKE Consulting",
        "Maxence Soileux, fondateur de MAKE Consulting : consultant QSE indépendant depuis 2019, IPRP déclaré, sapeur-pompier volontaire depuis 2012, Master MQSE.",
        'a-propos.html', body, current='a-propos.html')

# ─── FAQ ────────────────────────────────────────────────
GROUPS = [
 ('faq-duerp', 'clipboard', 'Document unique', [
   ("Qui doit réaliser un DUERP ?", "Tout employeur, dès le premier salarié (Code du travail, art. R.4121-1)."),
   ("À quelle fréquence le mettre à jour ?", "Au moins une fois par an dans les entreprises de 11 salariés et plus. Dans toutes les entreprises, à chaque décision d'aménagement important modifiant les conditions de travail et quand une information nouvelle sur un risque est connue (art. R.4121-2)."),
   ("Que risque une entreprise sans DUERP ?", "Une amende de 1 500 €, portée à 3 000 € en cas de récidive (art. R.4741-1). En cas d'accident, l'absence d'évaluation des risques pèse lourdement dans la reconnaissance d'une faute inexcusable."),
   ("Combien coûte un DUERP clé en main ?", "À partir de 2 400 € HT pour une TPE de moins de 10 salariés. Au-delà, sur devis selon l'effectif, le nombre de sites et les activités."),
 ]),
 ('faq-iprp', 'scale', 'IPRP et prévention', [
   ("Qu'est-ce qu'un IPRP ?", "Un intervenant en prévention des risques professionnels, reconnu par le Code du travail (art. L.4644-1) et enregistré auprès de l'administration, qui accompagne les employeurs dans leur démarche de prévention."),
   ("Quand lancer une analyse des RPS ?", "En cas de réorganisation, de turn-over ou d'absentéisme élevé, de signalements de mal-être ou à la demande du CSE. Les RPS doivent de toute façon figurer dans le document unique."),
   ("Les collectivités ont-elles les mêmes obligations ?", "Oui : DUERP, prévention des RPS, sécurité incendie. Les communes exposées à des risques majeurs identifiés doivent en plus disposer d'un plan communal de sauvegarde."),
 ]),
 ('faq-audit', 'award', 'Audit et ISO', [
   ("Pouvez-vous nous certifier ISO ?", "Non : la certification est délivrée par un organisme accrédité. Je vous prépare à l'audit et je peux conduire vos audits internes."),
   ("Quelle différence entre audit QSE et DUERP ?", "Le DUERP porte sur les risques pour les personnes. L'audit QSE examine l'ensemble du système de management : organisation, processus, documentation, environnement."),
 ]),
 ('faq-incendie', 'flame', 'Incendie et SSIAP', [
   ("Qu'est-ce qu'un plan de défense incendie ?", "Un document qui décrit, pour une installation classée, les scénarios d'incendie, les moyens de lutte, l'alerte et l'organisation de l'intervention. Il peut être exigé par la réglementation ICPE ou une prescription préfectorale."),
   ("À qui s'adresse le diagnostic SSIAP ?", "Aux exploitants d'ERP et d'IGH qui veulent vérifier le niveau réel de leur service de sécurité, et aux sociétés de sécurité privée qui veulent objectiver celui de leurs équipes."),
 ]),
 ('faq-pratique', 'briefcase', 'En pratique', [
   ("Intervenez-vous hors d'Île-de-France ?", "Oui, selon les conditions de la mission : durée, nombre de jours sur site et frais de déplacement."),
   ("Le diagnostic initial est-il vraiment gratuit ?", "Oui. C'est un échange de 30 minutes, par téléphone ou en visio, pour comprendre votre situation et vous orienter. Il n'engage à rien."),
   ("Proposez-vous des formations ?", f"Oui, présentées sur <a href='{FORMATION}' target='_blank' rel='noopener'>formation-incendie-paris.com</a> : incendie, SST, formations réglementaires et réalité mixte FireTraining MS."),
 ]),
]

def strip(t): return re.sub('<[^>]+>', '', t)

def build_faq():
    blocks = ''.join(f'<div class="faq-group" id="{gid}"><h2><span class="ico-tile">{ico(i)}</span>{t}</h2><div class="faq">{"".join(faq_item(q, a) for q, a in items)}</div></div>' for gid, i, t, items in GROUPS)
    nav = ''.join(f'<a href="#{g[0]}">{g[2]}</a>' for g in GROUPS)
    body = f'''
{page_hero('Questions fréquentes', 'Questions <span class="accent">fréquentes</span>', "Document unique, IPRP, audits, sécurité incendie : les réponses aux questions que l'on me pose le plus souvent.", btns=False)}
<nav class="subnav" aria-label="Thèmes"><div class="wrap">{nav}</div></nav>
<section class="section"><div class="wrap">{blocks}</div></section>
{cta("Votre question n'y est pas ?", "Posez-la directement : je réponds sous 48 h, et le premier échange est offert.")}
'''
    faq_ld = ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for g in GROUPS for q, a in g[3]]})
    return page("Questions fréquentes | DUERP, IPRP, audit QSE, sécurité incendie | MAKE Consulting",
        "Réponses sur le DUERP (obligations, mise à jour, sanctions), le rôle d'un IPRP, les audits QSE et ISO, les plans de défense incendie et le diagnostic SSIAP.",
        'faq.html', body, faq_ld)

# ─── CONTACT ────────────────────────────────────────────
BESOINS = ['Diagnostic initial offert (30 min)', 'DUERP clé en main', 'Audit QSE / normes ISO', 'Prévention des RPS', 'Audit sécurité & incendie', 'Diagnostic SSIAP', 'PCA ou PCS', 'IPRP externalisé', 'Autre demande']
def build_contact():
    opts = ''.join(f'<option>{b}</option>' for b in BESOINS)
    body = f'''
<section class="hero" style="padding-bottom:40px">
  <div class="wrap"><div class="sec-head" style="margin-bottom:0">
    <span class="eyebrow">Contact</span>
    <h1 class="h-anim">Parlons de votre projet</h1>
    <p class="lead">Décrivez votre situation en quelques lignes. Je vous réponds sous 48 h, et le premier échange de 30 minutes est offert.</p>
  </div></div>
</section>
<section class="section" style="padding-top:0">
  <h2 class="sr-only">Coordonnées et formulaire</h2>
  <div class="wrap split contact-grid">
    <div class="split-txt">
      <ul class="contact-list">
        <li><span class="ico-tile">{ico('phone')}</span><div><small>Téléphone</small><a href="tel:+33684527858">06 84 52 78 58</a></div></li>
        <li><span class="ico-tile">{ico('mail')}</span><div><small>E-mail</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
        <li><span class="ico-tile">{ico('pin')}</span><div><small>Zone d'intervention</small><span class="v">Île-de-France et France entière</span><p style="color:var(--ink-3);font-size:.9rem">Hors Île-de-France, selon les conditions de la mission</p></div></li>
      </ul>
      <div class="legal-note">{ico('grad')}<p><strong>Une demande de formation ?</strong> Les formations incendie, SST et FireTraining MS ont leur propre site : <a href="{FORMATION}contact.html" target="_blank" rel="noopener">formation-incendie-paris.com</a>.</p></div>
    </div>
    <div class="form-card" id="form-zone">
      <form class="form" id="contact-form" novalidate data-source="make-consulting">
        <div class="field"><label for="prenom">Prénom *</label><input id="prenom" name="prenom" autocomplete="given-name" required></div>
        <div class="field"><label for="nom">Nom *</label><input id="nom" name="nom" autocomplete="family-name" required></div>
        <div class="field field--full"><label for="organisation">Entreprise ou collectivité *</label><input id="organisation" name="organisation" autocomplete="organization" required></div>
        <div class="field"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="telephone">Téléphone</label><input id="telephone" name="telephone" type="tel" autocomplete="tel"></div>
        <div class="field"><label for="secteur">Secteur d'activité</label><select id="secteur" name="secteur"><option value="">Choisir</option><option>Industrie / logistique</option><option>BTP</option><option>Tertiaire</option><option>Commerce</option><option>Médico-social</option><option>Collectivité</option><option>Sécurité privée</option><option>Autre</option></select></div>
        <div class="field"><label for="effectif">Effectif</label><select id="effectif" name="effectif"><option value="">Choisir</option><option>1 à 9 salariés</option><option>10 à 49 salariés</option><option>50 à 249 salariés</option><option>250 et plus</option></select></div>
        <div class="field field--full"><label for="objet">Votre besoin *</label><select id="objet" name="objet" required><option value="">Choisir</option>{opts}</select></div>
        <div class="field field--full"><label for="message">Votre message *</label><textarea id="message" name="message" required placeholder="Contexte, échéance, sites concernés"></textarea></div>
        <div class="field--full" style="display:flex;flex-direction:column;gap:12px">
          <button class="btn btn-primary" type="submit" id="contact-submit" style="align-self:flex-start">Envoyer ma demande {ico('arrow', extra=' ico-arrow')}</button>
          <p class="form-error" id="contact-error" hidden>L'envoi n'a pas abouti. Écrivez-moi directement à {EMAIL} ou appelez le 06 84 52 78 58.</p>
          <p class="form-note">* Champs obligatoires. Vos données servent uniquement à répondre à votre demande (voir les <a href="mentions-legales.html#confidentialite">mentions légales</a>).</p>
        </div>
      </form>
    </div>
  </div>
</section>'''
    return page("Contact | Diagnostic QSE offert | MAKE Consulting",
        "Contactez MAKE Consulting pour un DUERP, un audit QSE, une mission de prévention ou un diagnostic SSIAP. Premier échange de 30 minutes offert, réponse sous 48 h.",
        'contact.html', body)

# ─── MENTIONS LÉGALES ───────────────────────────────────
def build_mentions():
    body = f'''
{page_hero('Mentions légales', 'Mentions légales <span class="accent">et confidentialité</span>', "Dernière mise à jour : septembre 2026.", btns=False)}
<section class="section legal">
  <div class="wrap">
    <h2 id="mentions">Éditeur du site</h2>
    <ul>
      <li>Maxence Soileux, entrepreneur individuel (MAKE Consulting), consultant en qualité, sécurité et environnement</li>
      <li>2 rue Vandana Shiva, 93450 L'Île-Saint-Denis</li>
      <li>Téléphone : 06 84 52 78 58 · E-mail : {EMAIL}</li>
      <li>SIRET : 879 519 221 00022 · TVA intracommunautaire : FR50879519221</li>
      <li>Responsable de la publication : Maxence Soileux</li>
    </ul>
    <h2>Hébergeur</h2>
    <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
    <h2>Propriété intellectuelle</h2>
    <p>Les contenus de ce site appartiennent à Maxence Soileux, sauf mention contraire. Toute reproduction sans autorisation écrite est interdite.</p>
    <h2 id="confidentialite">Données personnelles</h2>
    <p>Conformément au RGPD (UE 2016/679) et à la loi Informatique et Libertés. Responsable du traitement : Maxence Soileux, à l'adresse ci-dessus.</p>
    <div class="table-wrap"><table>
      <thead><tr><th>Données</th><th>Finalité</th><th>Base légale</th><th>Conservation</th></tr></thead>
      <tbody>
        <tr><td>Nom, prénom, e-mail, téléphone, organisation, secteur, effectif, message</td><td>Répondre aux demandes de contact et de devis</td><td>Mesures précontractuelles, intérêt légitime</td><td>3 ans après le dernier contact</td></tr>
        <tr><td>Mesure d'audience (Google Analytics)</td><td>Comprendre la fréquentation du site</td><td>Consentement</td><td>13 mois maximum</td></tr>
      </tbody>
    </table></div>
    <p>Le formulaire est traité via Google Apps Script et stocké dans un tableur Google (Google LLC). Les transferts hors Union européenne sont encadrés par les clauses contractuelles types de la Commission européenne. Vos données ne sont jamais vendues.</p>
    <h2 id="cookies">Cookies</h2>
    <p>Google Analytics n'est chargé qu'après votre accord, donné via le bandeau. Sans accord, aucun cookie de mesure n'est déposé. Vous pouvez changer d'avis à tout moment avec le lien « Gérer les cookies » en bas de page. Les polices de caractères sont hébergées sur ce site.</p>
    <h2 id="droits">Vos droits</h2>
    <p>Droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité : écrivez à {EMAIL}. Réponse sous un mois. Vous pouvez aussi saisir la CNIL (www.cnil.fr, 3 place de Fontenoy, 75007 Paris).</p>
  </div>
</section>'''
    return page("Mentions légales | MAKE Consulting", "Mentions légales, politique de confidentialité et gestion des cookies du site make-consulting.fr.", 'mentions-legales.html', body)

def build_404():
    body = f'''<section class="hero"><div class="wrap" style="text-align:center;display:flex;flex-direction:column;align-items:center;gap:20px;padding-block:40px">
  <span class="zone-code" style="font-size:5rem">404</span>
  <h1 class="h-anim">Cette page <span class="accent" style="color:var(--acc);font-style:italic;font-weight:500">n'existe pas</span></h1>
  <p class="lead">Elle a peut-être changé d'adresse lors de la refonte du site.</p>
  <div class="hero-btns" style="justify-content:center"><a class="btn btn-primary" href="index.html">Retour à l'accueil {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-ghost" href="contact.html">Me contacter</a></div>
</div></section>'''
    h = page('Page introuvable | MAKE Consulting', "Cette page n'existe pas ou a changé d'adresse.", '404.html', body)
    h = h.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<base href="/">', 1)
    return h.replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"', 1)

def build_blog_redirect():
    return '''<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8"><title>Ressources | MAKE Consulting</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://make-consulting.fr/faq.html">
<meta http-equiv="refresh" content="0; url=faq.html">
<script>location.replace('faq.html');</script>
</head><body><p>Cette page a déménagé : <a href="faq.html">voir les questions fréquentes</a>.</p></body></html>'''
