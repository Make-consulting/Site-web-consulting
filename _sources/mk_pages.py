from mk import *

# ─── Cas réels anonymisés ───────────────────────────────
C_DUERP_93 = case('DUERP', '2026', "Refonte complète de la prévention d'une entreprise de manutention",
    "Mission IPRP de trois mois pour une entreprise dont l'activité comprend du chargement et du déchargement sur deux sites.",
    ["Document unique réécrit : 9 unités de travail, 57 risques cotés sur 6 niveaux de priorité",
     "Protocoles de chargement et déchargement : version interne, version clients, fiche particuliers, affiche A4",
     "Audit de conformité santé-sécurité en 26 thèmes",
     "Points critiques signalés par écrit à la direction"], lieu='Seine-Saint-Denis')
C_DUERP_COMMUNE = case('DUERP', '', "Document unique d'une commune de 12 000 habitants",
    "Réalisation du document unique d'une commune, jusqu'à sa présentation au conseil municipal.",
    ["Visites de terrain et entretiens", "Cotation des risques par unité de travail", "Plan d'action priorisé", "Présentation aux élus"],
    ("Le DUERP que Maxence a réalisé pour notre mairie est d'une qualité remarquable. Complet, opérationnel, et présenté de façon limpide au conseil municipal.", 'Directrice générale des services'), lieu='Val-de-Marne')
C_DIAG = case('Diagnostic', '2026', "Diagnostic organisationnel de services généraux multisites",
    "Structure d'environ 400 salariés répartis sur 12 sites : services techniques et trois fonctions support.",
    ["Cinq causes racines identifiées", "Plan d'action en six objectifs", "Alerte santé-sécurité transmise à la direction générale"], lieu='Île-de-France')
C_ISO9001 = case('Audit ISO', '2026', "Audit interne ISO 9001 d'une association d'aide à domicile",
    "Audit interne de deux jours, conduit selon la norme ISO 9001, pour une structure du secteur médico-social.",
    ["Guide d'entretien et grille d'audit multi-onglets", "Distinction rigoureuse entre non-conformités avérées et potentielles", "Rapport formel remis à la direction"], lieu='Vendée')
C_ISO3 = case('ISO 9001 · 14001 · 45001', '', "Accompagnement pluriannuel vers la triple certification",
    "Accompagnement d'une entreprise vers la certification qualité, environnement et santé-sécurité, sur plusieurs années.",
    ["Analyse des écarts sur les trois normes", "Structuration du système de management intégré", "Préparation des audits de certification"])
C_PCA = case('Continuité', '', "Plan de continuité d'activité d'un site de valorisation de déchets",
    "Élaboration du PCA d'un site industriel de valorisation de déchets.",
    ["Analyse des activités critiques", "Scénarios de crise propres au site", "Procédures de reprise"], lieu='Alpes-Maritimes')

ALL_CASES = [C_DUERP_93, C_DUERP_COMMUNE, C_DIAG, C_ISO9001, C_ISO3, C_PCA]

MISSIONS = [
 ('clipboard', 'Obligation légale', 'DUERP clé en main', "Votre document unique réalisé de A à Z, avec un plan d'action priorisé.", 'duerp.html'),
 ('award', 'Management QSE', 'Audit QSE et normes ISO', "Audit de conformité, audit interne, accompagnement vers ISO 9001, 14001 et 45001.", 'audit-qse.html'),
 ('activity', 'Risques psychosociaux', 'Prévention des RPS', "Diagnostic des facteurs de risque, restitution anonymisée et plan d'action.", 'prevention-rps.html'),
 ('flame', 'Incendie', 'Sécurité incendie', "Audit de conformité, consignes, plans de défense incendie pour les sites ICPE.", 'securite-incendie.html'),
 ('radio', 'ERP et IGH', 'Diagnostic des services SSIAP', "Évaluation en situation des agents de sécurité incendie de vos sites.", 'diagnostic-ssiap.html'),
 ('refresh', 'Crise', 'PCA et PCS', "Plan de continuité d'activité pour les entreprises, plan communal de sauvegarde pour les communes.", 'continuite-activite.html'),
 ('briefcase', 'Suivi', 'IPRP externalisé', "Un préventeur quelques jours par an, pour les structures sans service HSE.", 'iprp-externalise.html'),
]

def mission_cards():
    cards = ''.join(f'<a class="card cat-card mission-card" href="{h}"><span class="ico-tile">{ico(i)}</span><span class="pill">{tag}</span><h3>{t}</h3><p>{d}</p><span class="link-arrow">Découvrir {ico("arrow")}</span></a>' for i, tag, t, d, h in MISSIONS)
    cards += f'<a class="card cat-card mission-card card--feature" href="{FORMATION}" target="_blank" rel="noopener"><span class="ico-tile">{ico("grad")}</span><span class="pill">Autre site</span><h3>Formation</h3><p>Incendie, SST, formations réglementaires et réalité mixte FireTraining MS.</p><span class="link-arrow">formation-incendie-paris.com {ico("external")}</span></a>'
    return f'<div class="grid-4" data-stagger>{cards}</div>'

METHODE = [('Diagnostic', 'Votre situation réglementaire, votre secteur, vos obligations. Échange initial offert.'),
           ('Proposition', 'Périmètre, livrables, délais et budget. Devis sous 48 h.'),
           ('Terrain', 'Visites, entretiens, analyse documentaire. Je viens sur site.'),
           ('Livrables', 'Documents finalisés, présentés à la direction, au CSE ou à la CSSCT.'),
           ('Suivi', "Accompagnement dans la mise en œuvre du plan d'action.")]

ORG = {"@context": "https://schema.org", "@type": "ProfessionalService", "name": "MAKE Consulting", "url": BASE,
       "description": "Cabinet conseil en qualité, sécurité et environnement : DUERP, audit QSE, ISO, prévention des RPS, sécurité incendie.",
       "telephone": "+33684527858", "email": EMAIL, "image": BASE + "assets/og-image.jpg",
       "address": {"@type": "PostalAddress", "streetAddress": "2 rue Vandana Shiva", "postalCode": "93450", "addressLocality": "L'Île-Saint-Denis", "addressCountry": "FR"},
       "areaServed": ["Île-de-France", "France"], "founder": {"@type": "Person", "name": "Maxence Soileux", "jobTitle": "Consultant QSE, IPRP"},
       "sameAs": [FORMATION]}

# ─── ACCUEIL ────────────────────────────────────────────
def build_index():
    body = f'''
<section class="hero hero--conseil">
  <div class="wrap hero-grid">
    <div class="hero-txt">
      <span class="eyebrow">Cabinet conseil QSE · IPRP déclaré</span>
      <h1 class="h-anim">Vos obligations santé-sécurité, <span class="accent">traduites en plan d'action.</span></h1>
      <p class="lead">DUERP, audits QSE et ISO, prévention des RPS, sécurité incendie. Un consultant qui vient sur le terrain, pour les entreprises et les collectivités, en Île-de-France et partout en France.</p>
      <div class="hero-btns">
        <a class="btn btn-primary" href="{DIAG}">Réserver le diagnostic offert {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-ghost" href="#missions">Voir les missions</a>
      </div>
      <div class="hero-proof">
        <span>{ico('scale')}IPRP déclaré</span>
        <span>{ico('shield')}Sapeur-pompier volontaire depuis 2012</span>
        <span>{ico('grad')}Master MQSE</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="diag-card">
        <span class="eyebrow">Premier échange</span>
        <div class="big">30 min</div>
        <p style="color:var(--ink-2)">Un diagnostic initial offert pour faire le point sur votre situation et savoir par quoi commencer.</p>
        {checks(['Vos obligations selon votre effectif et votre secteur', "L'état de votre document unique", 'Les actions à mener en premier'])}
        <a class="btn btn-primary" href="{DIAG}">Choisir un créneau {ico('arrow', extra=' ico-arrow')}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-block:40px" aria-label="Secteurs accompagnés">
  <div class="wrap">
    <div class="sectors" data-stagger>
      <span class="pill">{ico('building')}Industrie et logistique</span>
      <span class="pill">{ico('landmark')}Collectivités</span>
      <span class="pill">{ico('heart')}Médico-social et aide à domicile</span>
      <span class="pill">{ico('leaf')}Valorisation des déchets</span>
      <span class="pill">{ico('hardhat')}BTP</span>
      <span class="pill">{ico('users')}Tertiaire</span>
    </div>
  </div>
</section>

<section class="section section--tint" id="missions">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Missions</span><h2>Sept missions, un point de départ commun : le diagnostic</h2><p class="lead">Chaque mission commence par un état des lieux de votre situation réglementaire et organisationnelle.</p></div>
    {mission_cards()}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Pourquoi MAKE Consulting</span><h2>Un consultant de terrain, pas un rapport générique</h2></div>
    <div class="pillars" data-stagger>
      <div class="pillar"><span class="ico-tile">{ico('eye')}</span><h3>Terrain</h3><p>Les risques se voient sur le poste de travail, pas dans les documents. Chaque mission commence sur site, avec les équipes.</p></div>
      <div class="pillar"><span class="ico-tile">{ico('target')}</span><h3>Rigueur</h3><p>Une méthode structurée, tracée et reproductible. Un document unique ou un rapport d'audit doit être exact, complet et défendable.</p></div>
      <div class="pillar"><span class="ico-tile">{ico('scale')}</span><h3>Indépendance</h3><p>Pas de produit à vendre en complément, pas d'intermédiaire : vous échangez directement avec la personne qui intervient.</p></div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Références</span><h2>Missions récentes</h2><p class="lead">Des missions réelles, décrites sans nommer les clients.</p></div>
    <div class="grid-3" data-stagger>{C_DUERP_93}{C_DUERP_COMMUNE}{C_ISO9001}</div>
    <p style="margin-top:28px"><a class="link-arrow" href="references.html">Toutes les références {ico('arrow')}</a></p>
  </div>
</section>

<section class="section" id="methode">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Méthode</span><h2>Comment j'interviens</h2></div>
    {steps(METHODE)}
  </div>
</section>

{formation_band()}

{faq_block("Ce qu'on me demande le plus", [
  ("Qui doit réaliser un DUERP ?", "Tout employeur, dès le premier salarié (Code du travail, art. R.4121-1). La mise à jour est au moins annuelle dans les entreprises de 11 salariés et plus, et obligatoire à chaque changement important : nouvel équipement, réorganisation, accident du travail."),
  ("Qu'est-ce qu'un IPRP ?", "L'intervenant en prévention des risques professionnels est reconnu par le Code du travail (art. L.4644-1) pour accompagner les employeurs dans leur démarche de prévention. Faire appel à un IPRP valorise votre démarche auprès de votre CSE ou de votre CSSCT."),
  ("Intervenez-vous hors d'Île-de-France ?", "Oui, selon les conditions de la mission : durée, nombre de jours sur site et frais de déplacement. J'ai par exemple conduit un audit ISO 9001 en Vendée et un plan de continuité d'activité dans les Alpes-Maritimes."),
  ("Proposez-vous aussi des formations ?", f"Oui. Les formations incendie, SST et réglementaires sont présentées sur <a href='{FORMATION}' target='_blank' rel='noopener'>formation-incendie-paris.com</a>. Elles complètent souvent un DUERP ou un audit."),
])}

{cta('Faisons le point en 30 minutes', "Un échange offert, sans engagement, pour savoir où vous en êtes et par quoi commencer.")}
'''
    return page("MAKE Consulting | Cabinet conseil QSE, DUERP et prévention en Île-de-France",
        "Cabinet conseil QSE : DUERP clé en main, audit QSE et ISO, prévention des RPS, sécurité incendie, diagnostic SSIAP. Maxence Soileux, IPRP déclaré. Diagnostic initial offert.",
        '', body, ld(ORG))

# ─── DUERP ──────────────────────────────────────────────
def service_ld(name, slug, desc):
    return ld({"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": name, "description": desc, "url": BASE + slug, "provider": {"@type": "ProfessionalService", "name": "MAKE Consulting", "url": BASE}, "areaServed": ["Île-de-France", "France"]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE}, {"@type": "ListItem", "position": 2, "name": name, "item": BASE + slug}]}]})

def build_duerp():
    body = f'''
{page_hero('DUERP clé en main', 'DUERP <span class="accent">clé en main</span>',
  "Votre document unique d'évaluation des risques professionnels, réalisé sur le terrain, avec un plan d'action priorisé que vos équipes peuvent réellement suivre.",
  [('scale', 'Obligatoire dès le 1er salarié'), ('eye', 'Visite terrain incluse'), ('users', 'Présentation au CSE'), ('file', 'À partir de 2 400 € HT')],
  sujet='DUERP%20cl%C3%A9%20en%20main')}

<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="split-txt reveal">
      <span class="eyebrow">L'obligation</span>
      <h2>Ce que la loi impose</h2>
      <p class="lead">Tout employeur doit évaluer les risques auxquels ses salariés sont exposés et consigner le résultat dans un document unique, dès le premier salarié.</p>
      {checks(["<strong>Mise à jour</strong> au moins une fois par an à partir de 11 salariés, et dans tous les cas à chaque changement important des conditions de travail",
               "<strong>Plan d'action</strong> : programme annuel de prévention (PAPRIPACT) à partir de 50 salariés, liste d'actions de prévention en dessous",
               "<strong>Conservation</strong> des versions successives pendant 40 ans",
               "<strong>Sanction</strong> : amende de 1 500 €, 3 000 € en cas de récidive (art. R.4741-1), et risque de faute inexcusable en cas d'accident"])}
    </div>
    <div class="card reveal" style="gap:16px">
      <h3>Ce qui est inclus</h3>
      {checks(["Visite de terrain et définition des unités de travail", "Identification et cotation des risques selon une grille reproductible", "Document unique conforme, en version numérique et imprimable", "Plan d'action priorisé, avec délais recommandés", "Restitution à la direction et au CSE", "En option : formation d'un référent pour la mise à jour interne"])}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Tarifs</span><h2>Des forfaits annoncés à l'avance</h2><p class="lead">Le devis définitif est établi après un échange de 30 minutes sur votre contexte : secteur, organisation, risques spécifiques.</p></div>
    <div class="table-wrap reveal" style="border:0">
      <table class="price-table">
        <thead><tr><th>Taille de l'entreprise</th><th>Délai indicatif</th><th>Tarif HT</th></tr></thead>
        <tbody>
          <tr><td>TPE, jusqu'à 9 salariés</td><td>5 à 10 jours</td><td>À partir de 2 400 €</td></tr>
          <tr><td>PME, 10 à 49 salariés</td><td>10 à 20 jours</td><td>Sur devis</td></tr>
          <tr><td>PME, 50 à 99 salariés</td><td>3 à 5 semaines</td><td>Sur devis</td></tr>
          <tr><td>Mise à jour annuelle (client existant)</td><td>2 à 5 jours</td><td>Forfait réduit</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Déroulé</span><h2>De la visite au document final</h2></div>
    {steps([('Échange', 'Effectif, activités, sites, documents existants.'), ('Terrain', 'Observation des postes et entretiens avec les équipes.'), ('Rédaction', 'Cotation des risques et plan d&#39;action priorisé.'), ('Restitution', 'Présentation à la direction et au CSE.')], True)}
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Références</span><h2>Documents uniques réalisés</h2></div>
    <div class="grid-2" data-stagger>{C_DUERP_93}{C_DUERP_COMMUNE}</div>
  </div>
</section>

{faq_block('DUERP : vos questions', [
  ("Mon DUERP date de plusieurs années, faut-il tout refaire ?", "Pas forcément. Je commence par relire le document existant. S'il est structuré, une mise à jour suffit. S'il ne correspond plus à la réalité des postes, une refonte coûte souvent moins cher qu'une succession de corrections."),
  ("Combien de temps faut-il prévoir de votre côté ?", "Une demi-journée à une journée de disponibilité pour la visite et les entretiens selon la taille du site, puis une heure pour la restitution."),
  ("Le DUERP doit-il inclure les risques psychosociaux ?", "Oui. Les RPS font partie des risques à évaluer. Pour aller plus loin qu'une première évaluation, voir la <a href='prevention-rps.html'>mission de prévention des RPS</a>."),
  ("Qui doit être associé à la démarche ?", "Le CSE, s'il existe, est consulté sur le document unique et ses mises à jour. Le référent sécurité et le service de prévention et de santé au travail peuvent aussi y contribuer."),
], tint=False)}

{cta('Votre document unique est-il à jour ?', "Faisons le point en 30 minutes, gratuitement, avant de parler devis.")}
'''
    return page("DUERP clé en main | Document unique d'évaluation des risques | MAKE Consulting",
        "DUERP clé en main réalisé par un IPRP : visite terrain, cotation des risques, plan d'action, présentation au CSE. À partir de 2 400 € HT pour une TPE. Île-de-France et France entière.",
        'duerp.html', body, service_ld('DUERP clé en main', 'duerp.html', "Réalisation du document unique d'évaluation des risques professionnels."), current='duerp.html')

# ─── AUDIT QSE / ISO ────────────────────────────────────
def build_audit():
    body = f'''
{page_hero('Audit QSE et ISO', 'Audit QSE <span class="accent">et normes ISO</span>',
  "Mesurer l'écart entre votre organisation et les exigences qui s'appliquent à vous, puis le réduire : audit de conformité, audit interne, accompagnement vers ISO 9001, 14001 et 45001.",
  [('award', 'ISO 9001 · 14001 · 45001'), ('search', 'Audit interne'), ('grad', 'Master MQSE'), ('clock', 'Devis sous 48 h')], sujet='Normes%20ISO%20(45001%20%2F%209001%20%2F%2014001)')}

<section class="section">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Trois façons d'intervenir</span><h2>Selon où vous en êtes</h2></div>
    <div class="grid-3" data-stagger>
      <article class="card"><span class="ico-tile">{ico('search')}</span><h3>Audit QSE</h3><p>Une photographie objective de votre organisation : réglementation, documentation, pratiques terrain, culture sécurité.</p>{checks(['Cadrage et collecte documentaire', 'Visite terrain et entretiens', 'Écarts classés par criticité', "Plan d'actions priorisé"])}</article>
      <article class="card card--feature"><span class="ico-tile">{ico('award')}</span><h3>Accompagnement ISO</h3><p>De l'état des lieux à l'audit de certification, pour une norme ou un système intégré.</p>{checks(['Analyse des écarts', 'Structuration du système de management', 'Formation des équipes', "Préparation à l'audit de certification"])}</article>
      <article class="card"><span class="ico-tile">{ico('clipboard')}</span><h3>Audit interne</h3><p>L'audit interne exigé par les normes ISO, conduit par un auditeur extérieur à vos équipes.</p>{checks(["Guide d'entretien et grille d'audit", 'Non-conformités avérées et potentielles bien distinguées', 'Rapport formel, sans jugement de valeur'])}</article>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Déroulé d'un audit</span><h2>Du cadrage à la restitution</h2></div>
    {steps([('Cadrage', 'Périmètre, référentiels applicables, documents existants.'), ('Analyse documentaire', 'Conformité réglementaire et normative.'), ('Terrain', 'Observations et entretiens, de la direction aux opérateurs.'), ('Rapport', 'Écarts majeurs, mineurs et pistes de progrès.'), ('Plan d&#39;actions', 'Responsable, délai et indicateur pour chaque action.')])}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Références</span><h2>Audits et accompagnements réalisés</h2></div>
    <div class="grid-3" data-stagger>{C_ISO9001}{C_ISO3}{C_DIAG}</div>
  </div>
</section>

{faq_block('Audit et ISO : vos questions', [
  ("Quelle différence entre un audit QSE et un DUERP ?", "Le DUERP porte sur les risques pour les personnes. L'audit QSE examine l'ensemble du système : organisation, processus, documentation, environnement, satisfaction client."),
  ("Pouvez-vous nous certifier ?", "Non : la certification est délivrée par un organisme certificateur accrédité. Mon rôle est de vous y préparer et, si besoin, de conduire vos audits internes."),
  ("Combien de temps pour obtenir une certification ?", "Cela dépend de votre point de départ et du nombre de normes visées. Une triple certification se prépare généralement sur plusieurs mois, parfois plusieurs années pour un système intégré complet."),
])}

{cta("Vous préparez une certification ?", "Parlons de votre point de départ et de votre calendrier.", sujet='Normes%20ISO%20(45001%20%2F%209001%20%2F%2014001)', label='En parler')}
'''
    return page("Audit QSE et accompagnement ISO 9001, 14001, 45001 | MAKE Consulting",
        "Audit QSE, audit interne et accompagnement vers la certification ISO 9001, ISO 14001 et ISO 45001, par un consultant titulaire d'un Master MQSE. Île-de-France et France entière.",
        'audit-qse.html', body, service_ld('Audit QSE et accompagnement ISO', 'audit-qse.html', "Audit QSE, audit interne et accompagnement à la certification ISO."), current='audit-qse.html')

# ─── RPS ────────────────────────────────────────────────
def build_rps():
    body = f'''
{page_hero('Prévention des RPS', 'Prévention des <span class="accent">risques psychosociaux</span>',
  "Un diagnostic pour comprendre ce qui pèse sur vos équipes, une restitution anonymisée, et un plan d'action concret que la direction et le CSE peuvent porter ensemble.",
  [('activity', 'Modèle de Karasek'), ('users', 'Questionnaire anonyme'), ('clipboard', 'Plan budgété'), ('refresh', 'Suivi à 6 mois')], sujet='Pr%C3%A9vention%20des%20RPS')}

<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="split-txt reveal">
      <span class="eyebrow">Quand agir</span>
      <h2>Les signaux qui justifient un diagnostic</h2>
      <p class="lead">Les risques psychosociaux doivent figurer dans le document unique. Une analyse approfondie devient nécessaire quand les signaux s'accumulent.</p>
      {checks(['Réorganisation ou changement de direction', 'Turn-over ou absentéisme en hausse', 'Signalements de mal-être ou de conflits', 'Demande du CSE ou alerte du médecin du travail'])}
    </div>
    <div class="card reveal" style="gap:16px">
      <h3>Ce que comprend la mission</h3>
      {checks(['Questionnaire anonyme et entretiens individuels ou collectifs', 'Analyse des facteurs de risque selon le modèle de Karasek', 'Restitution chiffrée et anonymisée à la direction et au CSE', "Plan d'action priorisé et budgété", 'Point de suivi à 6 mois inclus'])}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Méthode</span><h2>Comprendre, repérer, agir</h2></div>
    {steps([('Cadrage', 'Périmètre, calendrier, communication aux équipes.'), ('Recueil', 'Questionnaire anonyme et entretiens.'), ('Analyse', 'Facteurs de risque par service ou métier.'), ('Plan d&#39;action', 'Mesures priorisées, restitution et suivi.')], True)}
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Former les managers</span>
      <h2>Compléter le diagnostic par la formation</h2>
      <p class="lead">Une demi-journée de formation à la prévention des RPS aide managers, RH et élus du CSE à repérer les signaux et à agir au quotidien.</p>
      {ext(FORMATION + 'formations-reglementaires.html#rps', 'Voir la formation RPS')}
    </div>
    {C_DIAG}
  </div>
</section>

{faq_block('RPS : vos questions', [
  ("Les réponses sont-elles vraiment anonymes ?", "Oui. Les résultats sont restitués par groupes suffisamment larges pour qu'aucune réponse individuelle ne soit identifiable."),
  ("Le CSE doit-il être associé ?", "Il est fortement recommandé de l'associer dès le cadrage : la démarche gagne en légitimité et le plan d'action est mieux porté."),
  ("Combien de temps dure un diagnostic ?", "De quelques semaines à deux ou trois mois selon l'effectif, le nombre de sites et le taux de réponse au questionnaire."),
])}

{cta("Des signaux vous inquiètent ?", "Un premier échange confidentiel pour décider de la bonne démarche.", sujet='Pr%C3%A9vention%20des%20RPS', label='En parler')}
'''
    return page("Prévention des risques psychosociaux (RPS) | Diagnostic et plan d'action | MAKE Consulting",
        "Diagnostic des risques psychosociaux : questionnaire anonyme, entretiens, analyse selon le modèle de Karasek, restitution et plan d'action. Suivi à 6 mois inclus.",
        'prevention-rps.html', body, service_ld('Prévention des risques psychosociaux', 'prevention-rps.html', "Diagnostic RPS et plan d'action."))

# ─── SÉCURITÉ INCENDIE ──────────────────────────────────
def build_incendie():
    body = f'''
{page_hero('Sécurité incendie', 'Sécurité incendie : <span class="accent">conformité et défense</span>',
  "Audit de conformité, consignes, organisation de l'évacuation, plans de défense incendie pour les sites classés. Par un consultant SSIAP 3 et sapeur-pompier volontaire depuis 2012.",
  [('flame', 'SSIAP 3'), ('shield', 'Sapeur-pompier volontaire'), ('building', 'ERP, IGH, industrie'), ('leaf', 'Sites ICPE')], sujet='Audit%20s%C3%A9curit%C3%A9%20%26%20incendie')}

<section class="section">
  <div class="wrap">
    <h2 class="sr-only">Les prestations</h2>
    <div class="grid-3" data-stagger>
      <article class="card"><span class="ico-tile">{ico('search')}</span><h3>Audit de conformité incendie</h3><p>Vos obligations, vos installations, vos documents : un état des lieux et des préconisations classées par priorité.</p>{checks(['Revue des obligations réglementaires', 'Inspection terrain des moyens de secours', 'Consignes, registre, exercices', 'Rapport et plan de mise en conformité'])}</article>
      <article class="card card--feature"><span class="ico-tile">{ico('leaf')}</span><h3>Plan de défense incendie</h3><p>Pour les installations classées (ICPE) soumises à cette exigence, notamment après une prescription préfectorale ou une inspection.</p>{checks(['Analyse des scénarios et des stockages', "Moyens de lutte et d'alerte", 'Consignes et organisation', 'Options : formation, exercice, suivi des stocks'])}</article>
      <article class="card"><span class="ico-tile">{ico('exit')}</span><h3>Organisation de l'évacuation</h3><p>Guides, serre-files, points de rassemblement, personnes à mobilité réduite : une organisation qui fonctionne le jour J.</p>{checks(["Désignation et rôle des équipiers", 'Consignes adaptées au bâtiment', "Exercice et retour d'expérience"])}</article>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Services de sécurité</span>
      <h2>Vos agents SSIAP sont-ils prêts ?</h2>
      <p class="lead">Pour les exploitants d'ERP et d'IGH et les sociétés de sécurité privée : une évaluation en situation des agents de sécurité incendie.</p>
      <a class="btn btn-primary" style="align-self:flex-start" href="diagnostic-ssiap.html">Découvrir le diagnostic SSIAP {ico('arrow', extra=' ico-arrow')}</a>
    </div>
    <div class="split-txt reveal">
      <span class="eyebrow">Former</span>
      <h2>Et former vos équipes</h2>
      <p class="lead">Sensibilisation, équipiers de première intervention, guides et serre-files, avec l'option réalité mixte FireTraining MS.</p>
      {ext(FORMATION + 'formation-incendie.html', 'Voir les formations incendie')}
    </div>
  </div>
</section>

{faq_block('Sécurité incendie : vos questions', [
  ("Quelles sont les obligations incendie d'un employeur ?", "Le Code du travail (art. R.4227-28 et suivants) impose notamment des moyens d'extinction adaptés, une consigne de sécurité incendie, l'information et la formation du personnel, et des exercices et essais périodiques. Les ERP et IGH ont des règles complémentaires."),
  ("Qu'est-ce qu'un plan de défense incendie ?", "Un document qui décrit, pour une installation classée, les scénarios d'incendie, les moyens de lutte, l'organisation de l'alerte et l'intervention. Il peut être exigé par la réglementation ICPE ou par une prescription préfectorale."),
  ("Pouvez-vous organiser un exercice d'évacuation ?", "Oui, avec préparation, observation pendant l'exercice et retour d'expérience écrit pour votre registre de sécurité."),
])}

{cta("Un audit ou une prescription à traiter ?", "Décrivez votre site et votre échéance : je vous propose une démarche et un devis sous 48 h.", sujet='Audit%20s%C3%A9curit%C3%A9%20%26%20incendie', label='Demander un devis')}
'''
    return page("Audit sécurité incendie et plan de défense incendie (ICPE) | MAKE Consulting",
        "Audit de conformité incendie, plan de défense incendie pour sites ICPE, organisation de l'évacuation. Consultant SSIAP 3 et sapeur-pompier volontaire. Île-de-France et France entière.",
        'securite-incendie.html', body, service_ld('Sécurité incendie', 'securite-incendie.html', "Audit de conformité incendie et plans de défense incendie."), current='securite-incendie.html')

# ─── DIAGNOSTIC SSIAP ───────────────────────────────────
def build_ssiap():
    body = f'''
{page_hero('Diagnostic SSIAP', 'Diagnostic des services <span class="accent">de sécurité incendie</span>',
  "Vos agents SSIAP savent-ils réagir à une alarme réelle ? Une évaluation en situation, sur votre site, avec un rapport par agent et un plan de montée en compétences.",
  [('building', 'ERP et IGH'), ('radio', 'Mises en situation'), ('shield', 'Sapeur-pompier volontaire'), ('flame', 'SSIAP 3')], sujet='Diagnostic%20SSIAP')}

<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="split-txt reveal">
      <span class="eyebrow">Pour qui</span>
      <h2>Deux publics, une même question</h2>
      {checks(["<strong>Exploitants d'ERP et d'IGH</strong> (hôtels, cliniques, lieux de loisirs, immeubles de bureaux) : vérifier le niveau réel du service de sécurité que vous payez",
               "<strong>Sociétés de sécurité privée</strong> : objectiver le niveau de vos équipes, préparer un appel d'offres, cibler la formation"])}
      <p class="lead" style="margin-top:8px">Le diplôme SSIAP atteste qu'un agent a été formé. Il ne dit pas comment il réagira, sur votre site, à 3 heures du matin.</p>
    </div>
    <div class="card reveal" style="gap:16px">
      <h3>Ce qui est évalué</h3>
      {checks(["Connaissance du site, des risques et des moyens de secours", "Exploitation du système de sécurité incendie et levée de doute", "Rondes et main courante", "Conduite à tenir en cas d'alarme et d'évacuation", "Accueil et guidage des sapeurs-pompiers", "Coordination au sein de l'équipe"])}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Déroulé</span><h2>De l'observation au plan de progrès</h2></div>
    {steps([('Cadrage', 'Site, effectif, horaires, attentes de l&#39;exploitant.'), ('Observation', 'Rondes, postes et documents du service.'), ('Mises en situation', 'Scénarios réalistes adaptés au site.'), ('Rapport', 'Niveau par agent et par équipe, plan de montée en compétences.')], True)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Pourquoi moi</span><h2>Le regard de celui qui arrive en intervention</h2></div>
    <div class="pillars" data-stagger>
      <div class="pillar"><span class="ico-tile">{ico('shield')}</span><h3>Sapeur-pompier volontaire</h3><p>Depuis 2012, je vois ce qui se passe quand les secours arrivent sur un site : ce qui fait gagner du temps, et ce qui en fait perdre.</p></div>
      <div class="pillar"><span class="ico-tile">{ico('flame')}</span><h3>SSIAP 3</h3><p>Je connais le métier de l'intérieur : les attendus réglementaires, la posture du chef de service, la réalité des postes de sécurité.</p></div>
      <div class="pillar"><span class="ico-tile">{ico('scale')}</span><h3>IPRP déclaré</h3><p>Le diagnostic s'inscrit dans une démarche de prévention plus large, reliée à votre document unique.</p></div>
    </div>
  </div>
</section>

{faq_block('Diagnostic SSIAP : vos questions', [
  ("Les mises en situation perturbent-elles l'exploitation ?", "Non. Les scénarios sont préparés avec l'exploitant et programmés à des moments choisis, sans déclenchement réel de l'alarme générale sauf si vous le souhaitez."),
  ("Qui reçoit le rapport ?", "Le commanditaire : l'exploitant du site ou la société de sécurité. Le contenu par agent est discuté en amont pour que la démarche reste constructive."),
  ("Proposez-vous la formation qui suit ?", "Oui. Le plan de montée en compétences peut déboucher sur des sessions ciblées, construites à partir des écarts observés."),
])}

{cta("Faites le point sur votre service de sécurité", "Parlons de votre site et de vos équipes.", sujet='Diagnostic%20SSIAP', label='En parler')}
'''
    return page("Diagnostic des services de sécurité incendie (SSIAP) en ERP et IGH | MAKE Consulting",
        "Évaluation en situation des agents SSIAP pour les exploitants d'ERP et d'IGH et les sociétés de sécurité privée : mises en situation, rapport par agent, plan de montée en compétences.",
        'diagnostic-ssiap.html', body, service_ld('Diagnostic des services de sécurité incendie', 'diagnostic-ssiap.html', "Évaluation en situation des agents SSIAP."))

# ─── PCA / PCS ──────────────────────────────────────────
def build_pca():
    body = f'''
{page_hero('PCA et PCS', 'Continuité d&#39;activité <span class="accent">et gestion de crise</span>',
  "Préparer votre organisation à un sinistre, une cyberattaque ou la défaillance d'un fournisseur. Et pour les communes, un plan communal de sauvegarde opérationnel.",
  [('refresh', 'PCA entreprises'), ('landmark', 'PCS communes'), ('users', 'Exercice de crise'), ('shield', 'Expérience opérationnelle')], sujet='PCA%20ou%20PCS')}

<section class="section">
  <div class="wrap">
    <h2 class="sr-only">Les prestations</h2>
    <div class="grid-2" data-stagger>
      <article class="card"><span class="ico-tile">{ico('refresh')}</span><h3>Plan de continuité d'activité</h3><p>Identifier ce qui ne doit pas s'arrêter, et comment le maintenir ou le redémarrer.</p>{checks(["Analyse d'impact sur l'activité (BIA)", 'Identification des ressources critiques', 'Procédures de secours et de reprise', 'Test et exercice de crise'])}</article>
      <article class="card card--feature"><span class="ico-tile">{ico('landmark')}</span><h3>Plan communal de sauvegarde</h3><p>Rédaction ou révision du PCS, selon les obligations issues de la loi du 13 août 2004, élargies en 2021.</p>{checks(['Diagnostic des risques communaux', 'Organisation de la cellule de crise', 'Fiches réflexes par scénario', 'Annuaire de crise et exercice'])}</article>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Référence</span>
      <h2>Un PCA pour un site industriel</h2>
      <p class="lead">Les plans de continuité les plus utiles sont ceux qui partent des scénarios propres au site, pas d'un modèle générique.</p>
    </div>
    {C_PCA}
  </div>
</section>

{faq_block('PCA et PCS : vos questions', [
  ("Quelle différence entre PCA et plan de gestion de crise ?", "Le plan de gestion de crise organise la réponse immédiate. Le PCA garantit que les activités essentielles continuent ou redémarrent dans un délai acceptable. Les deux se complètent."),
  ("Quelles communes doivent avoir un PCS ?", "Les communes exposées à certains risques majeurs, notamment celles couvertes par un plan de prévention des risques naturels ou technologiques ou par un plan particulier d'intervention. Le périmètre a été élargi en 2021."),
  ("Faut-il tester le plan ?", "Oui. Un plan jamais exercé révèle ses failles le jour de la crise. Je propose un exercice sur table ou en conditions réelles, suivi d'un retour d'expérience."),
])}

{cta("Votre organisation est-elle prête ?", "Échangeons sur vos activités critiques et vos scénarios.", sujet='PCA%20ou%20PCS', label='En parler')}
'''
    return page("Plan de continuité d'activité (PCA) et plan communal de sauvegarde (PCS) | MAKE Consulting",
        "Élaboration de plans de continuité d'activité pour les entreprises et de plans communaux de sauvegarde pour les communes : analyse d'impact, procédures, exercice de crise.",
        'continuite-activite.html', body, service_ld('PCA et PCS', 'continuite-activite.html', "Plans de continuité d'activité et plans communaux de sauvegarde."))

# ─── IPRP EXTERNALISÉ ───────────────────────────────────
def build_iprp():
    body = f'''
{page_hero('IPRP externalisé', 'Un préventeur, <span class="accent">sans l&#39;embaucher</span>',
  "Pour les PME et les collectivités sans service HSE : quelques jours par an d'un IPRP qui connaît votre entreprise, tient votre prévention à jour et vous alerte quand il le faut.",
  [('briefcase', 'Quelques jours par an'), ('refresh', 'DUERP tenu à jour'), ('users', 'Présence au CSE'), ('scale', 'IPRP déclaré')], sujet='IPRP%20externalis%C3%A9')}

<section class="section">
  <div class="wrap split" style="align-items:start">
    <div class="split-txt reveal">
      <span class="eyebrow">Le principe</span>
      <h2>Un volume de jours fixé ensemble</h2>
      <p class="lead">Nous définissons un nombre de jours sur la période et un programme. Je viens sur site aux moments utiles et reste joignable entre deux visites.</p>
      {checks(['Mise à jour du document unique et suivi du plan d&#39;action', 'Visites de terrain et analyse des accidents', 'Participation aux réunions du CSE ou de la CSSCT', 'Veille réglementaire appliquée à votre activité', 'Alertes écrites sur les situations à risque'])}
    </div>
    <div class="card reveal" style="gap:16px">
      <h3>Pour qui</h3>
      {checks(['PME de 20 à 250 salariés sans préventeur interne', 'Collectivités et établissements publics', 'Entreprises qui sortent d&#39;un DUERP ou d&#39;un audit et veulent tenir le cap'])}
      <p style="color:var(--ink-2)">Le Code du travail impose à l'employeur de désigner un ou plusieurs salariés compétents pour s'occuper de la prévention. À défaut de compétences internes, il peut faire appel à un IPRP (art. L.4644-1).</p>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Référence</span>
      <h2>Du diagnostic au suivi</h2>
      <p class="lead">Une mission ponctuelle révèle souvent le besoin d'un suivi : c'est le cas de cette entreprise, où le document unique et les protocoles ont posé les bases d'un accompagnement dans la durée.</p>
    </div>
    {C_DUERP_93}
  </div>
</section>

{cta("Parlons d'un accompagnement dans la durée", "Nous définissons ensemble le volume de jours et les priorités.", sujet='IPRP%20externalis%C3%A9', label='En parler')}
'''
    return page("IPRP externalisé | Préventeur à temps partagé pour PME et collectivités | MAKE Consulting",
        "Accompagnement en prévention quelques jours par an : mise à jour du DUERP, suivi du plan d'action, présence au CSE, veille réglementaire. Pour PME et collectivités sans service HSE.",
        'iprp-externalise.html', body, service_ld('IPRP externalisé', 'iprp-externalise.html', "Accompagnement récurrent en prévention des risques professionnels."))
