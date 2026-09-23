import json
from partials import ico, page
from p_index import faq_item

BASE = 'https://www.formation-incendie-paris.com/'

def case(tag, year, titre, contexte, fait, quote=None):
    items = ''.join(f'<li>{ico("check")}{x}</li>' for x in fait)
    items = f'<ul class="checks">{items}</ul>' if fait else ''
    q = ''
    if quote:
        q = f'<figure class="case-quote"><blockquote>{quote[0]}</blockquote><figcaption>{quote[1]}</figcaption></figure>'
    return f'''<article class="card case"><div class="case-head"><span class="pill pill--acc">{tag}</span><span class="case-year">{year}</span></div>
<h3>{titre}</h3><p>{contexte}</p>{items}{q}</article>'''

DEPTS = {
 'seine-saint-denis': dict(
   nom='Seine-Saint-Denis', code='93', slug='formation-incendie-seine-saint-denis.html',
   h1='Formation incendie et SST <span class="accent">en Seine-Saint-Denis</span>',
   lead="Mon activité est basée à L'Île-Saint-Denis. J'interviens dans tout le département, sur des sites industriels, logistiques, tertiaires et des établissements recevant du public.",
   facts=[('pin', 'Basé dans le 93'), ('flame', 'Formateur SSIAP 3'), ('shield', 'Sapeur-pompier volontaire'), ('clock', 'Devis sous 48 h')],
   cases=[
     case('Conseil IPRP', '2026', "Prévention des risques pour une entreprise de chargement et déchargement",
          "Mission IPRP de trois mois pour une entreprise de l'est du département, dont l'activité comprend du chargement et du déchargement sur deux sites.",
          ["Refonte complète du document unique : 9 unités de travail, 57 risques cotés sur une échelle de 6 niveaux de priorité",
           "Protocoles de chargement et déchargement : version interne, version pour les clients, fiche pour les particuliers et affiche A4",
           "Audit de conformité santé-sécurité en 26 thèmes",
           "Points critiques signalés par écrit à la direction, avec les mesures à prendre"]),
     case('Formation incendie', '', "Formation incendie pour 80 collaborateurs d'une PME industrielle",
          "Formation incendie de l'ensemble du personnel d'une PME industrielle du département.",
          [],
          ("Une formation incendie sérieuse, accessible et parfaitement adaptée à nos 80 collaborateurs. M. Soileux a su capter l'attention du groupe du début à la fin.", 'Responsable RH, PME industrielle')),
   ],
   faq=[("Intervenez-vous dans toute la Seine-Saint-Denis ?", "Oui, de Saint-Denis à Montreuil, de Bobigny à Tremblay-en-France. Mon activité est basée à L'Île-Saint-Denis, ce qui me permet de caler une session rapidement."),
        ("Pouvez-vous former des équipes postées ?", "Oui. Je peux organiser plusieurs sessions dans la journée, tôt le matin ou en fin de journée, pour couvrir les différentes équipes sans arrêter l'activité."),
        ("Faites-vous aussi le document unique ?", "Oui. En tant qu'IPRP déclaré, je réalise ou mets à jour votre DUERP, et je construis le plan de formation qui en découle.")],
 ),
 'paris': dict(
   nom='Paris', code='75', slug='formation-incendie-paris.html',
   h1='Formation incendie et SST <span class="accent">à Paris</span>',
   lead="Bureaux, établissements médico-sociaux, commerces, organismes de formation : j'interviens dans tous les arrondissements, dans vos locaux et à vos horaires.",
   facts=[('pin', 'Tous arrondissements'), ('heart', 'Formateur SST agréé INRS'), ('shield', 'Sapeur-pompier volontaire'), ('clock', 'Devis sous 48 h')],
   cases=[
     case('Formation SST', '', "Formation SST pour un établissement médico-social du 15e arrondissement",
          "Formation de sauveteurs secouristes du travail pour les équipes d'un établissement médico-social parisien.",
          ["Formation selon le référentiel national de l'INRS", "Mises en situation pratiques", "Évaluation certificative en fin de session"],
          ("La formation SST avec M. Soileux a été un vrai moment de montée en compétences pour nos équipes. Pédagogie claire, exercices pratiques, 100% de réussite.", 'Coordinateur sécurité, établissement médico-social')),
     case('Formation SSIAP', '2026', "Parcours SSIAP 3 pour un organisme de formation parisien",
          "Conception de supports et de programmes SSIAP 3 pour un organisme de formation parisien.",
          ["Cahiers de formation SSIAP 3, initial et recyclage", "Programme d'introduction de trois jours, centré sur la posture managériale du chef de service"]),
   ],
   faq=[("Intervenez-vous dans les immeubles de bureaux ?", "Oui. La formation se déroule dans une salle de réunion pour la partie théorique. Pour la manipulation d'extincteurs, nous définissons ensemble un espace adapté : cour, parking ou toit-terrasse."),
        ("Formez-vous des agents SSIAP ?", "Je conçois et j'anime des formations SSIAP, notamment pour des organismes de formation. Pour un besoin SSIAP, contactez-moi pour en parler."),
        ("Combien de temps à l'avance faut-il réserver ?", "Comptez en général deux à trois semaines. Pour une urgence (visite de la commission de sécurité, nouvel arrivant), contactez-moi : je fais au mieux.")],
 ),
 'val-de-marne': dict(
   nom='Val-de-Marne', code='94', slug='formation-incendie-val-de-marne.html',
   h1='Formation et prévention <span class="accent">dans le Val-de-Marne</span>',
   lead="Collectivités, services techniques, entreprises : j'accompagne les organisations du Val-de-Marne sur la formation incendie et SST, le document unique et l'organisation de la prévention.",
   facts=[('landmark', 'Collectivités et entreprises'), ('scale', 'IPRP déclaré'), ('shield', 'Sapeur-pompier volontaire'), ('clock', 'Devis sous 48 h')],
   cases=[
     case('Conseil IPRP', '', "Document unique d'une commune de 12 000 habitants",
          "Réalisation du document unique d'une commune du département, jusqu'à sa présentation au conseil municipal.",
          ["Visites de terrain et entretiens", "Évaluation et cotation des risques par unité de travail", "Plan d'action priorisé", "Présentation au conseil municipal"],
          ("Le DUERP que Maxence a réalisé pour notre mairie est d'une qualité remarquable. Complet, opérationnel, et présenté de façon limpide au conseil municipal.", 'Directrice générale des services, commune de 12 000 habitants')),
     case('Diagnostic', '2026', "Diagnostic organisationnel de services généraux multisites",
          "Diagnostic pour une structure d'environ 400 salariés répartis sur 12 sites, dont des services techniques implantés dans le Val-de-Marne.",
          ["Diagnostic des services techniques et de trois fonctions support", "Cinq causes racines identifiées", "Plan d'action en six objectifs", "Alerte santé-sécurité transmise à la direction générale"]),
   ],
   faq=[("Travaillez-vous avec les collectivités ?", "Oui : document unique, formation incendie et SST des agents, plan communal de sauvegarde. Les collectivités ont les mêmes obligations que les entreprises en santé et sécurité au travail."),
        ("Pouvez-vous intervenir sur plusieurs sites ?", "Oui. J'organise les sessions et les visites site par site, avec un planning commun et un interlocuteur unique."),
        ("Proposez-vous la formation incendie aux agents ?", "Oui, avec les mêmes programmes que pour les entreprises : sensibilisation, équipier de première intervention, guide et serre-file.")],
 ),
}

def build_dept(key):
    d = DEPTS[key]
    kf = ''.join(f'<span class="pill">{ico(i)}{t}</span>' for i, t in d['facts'])
    fq = ''.join(faq_item(q, a, k == 0) for k, (q, a) in enumerate(d['faq']))
    others = ''.join(f'<a class="link-arrow" href="{v["slug"]}">{v["nom"]} ({v["code"]}) {ico("arrow")}</a>' for k, v in DEPTS.items() if k != key)
    body = f'''
<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a><span aria-hidden="true">/</span><a href="index.html#zones">Zones d'intervention</a><span aria-hidden="true">/</span><span>{d['nom']}</span></nav>
    <h1 class="h-anim">{d['h1']}</h1>
    <p class="lead">{d['lead']}</p>
    <div class="keyfacts">{kf}</div>
    <div class="hero-btns"><a class="btn btn-primary" href="contact.html?univers=formation">Demander un devis {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-ghost" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Interventions dans le {d['code']}</span><h2>Ce que j'ai réalisé dans le département</h2><p class="lead">Des missions réelles, décrites sans nommer les clients.</p></div>
    <div class="grid-2" data-stagger>{''.join(d['cases'])}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Formations</span><h2>Ce que je propose en {d['nom']}</h2></div>
    <div class="grid-3" data-stagger>
      <a class="card cat-card" href="formation-incendie.html"><span class="ico-tile">{ico('flame')}</span><h3>Formation incendie</h3><p>Sensibilisation, équipier de première intervention, guide et serre-file. Une demi-journée par session.</p><span class="link-arrow">Voir les programmes {ico('arrow')}</span></a>
      <a class="card cat-card" href="formation-sst.html"><span class="ico-tile">{ico('heart')}</span><h3>SST et secourisme</h3><p>SST initial, recyclage, PSC et gestes qui sauvent, selon le référentiel INRS.</p><span class="link-arrow">Voir les programmes {ico('arrow')}</span></a>
      <a class="card cat-card" href="conseil.html"><span class="ico-tile">{ico('clipboard')}</span><h3>Conseil et DUERP</h3><p>Document unique, prévention des RPS, audits, avec un IPRP déclaré.</p><span class="link-arrow">Voir les missions {ico('arrow')}</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Pourquoi moi</span>
      <h2>Un formateur qui connaît le feu de l'intérieur</h2>
      <p class="lead">Sapeur-pompier volontaire en Île-de-France depuis 2012, je forme vos équipes avec ce que j'observe en intervention : les erreurs qui coûtent du temps, les réflexes qui sauvent.</p>
      <ul class="checks">
        <li>{ico('check')}SSIAP 1 et SSIAP 3, formateur SST agréé INRS</li>
        <li>{ico('check')}IPRP déclaré : la formation s'appuie sur vos risques réels</li>
        <li>{ico('check')}Matériel fourni, attestations individuelles</li>
      </ul>
    </div>
    <div class="media reveal"><img src="assets/photo-formation.jpg" alt="Maxence Soileux prépare des extincteurs avant une formation incendie" width="1200" height="895" loading="lazy"></div>
  </div>
</section>

<section class="section section--tint" id="faq">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal"><span class="eyebrow">Questions fréquentes</span><h2>Intervenir en {d['nom']}</h2></div>
    <div class="faq reveal">{fq}</div>
    <div class="other-zones">J'interviens aussi en {others}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band reveal">
      <canvas data-embers="30" aria-hidden="true"></canvas>
      <div><h2>Une session à organiser en {d['nom']} ?</h2><p>Indiquez le nombre de personnes, le lieu et la période. Programme et devis sous 48 h.</p></div>
      <div class="btns"><a class="btn btn-light" href="contact.html?univers=formation">Demander un devis {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a></div>
    </div>
  </div>
</section>'''
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": f"Formation incendie et SST – {d['nom']}", "serviceType": "Formation sécurité incendie et secourisme",
         "provider": {"@type": "LocalBusiness", "name": "MAKE Consulting", "url": BASE, "telephone": "+33684527858"},
         "areaServed": {"@type": "AdministrativeArea", "name": d['nom']}, "url": BASE + d['slug']},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": d['nom'], "item": BASE + d['slug']}]}]}
    title = f"Formation incendie et SST {'à' if key == 'paris' else 'en' if key != 'val-de-marne' else 'dans le'} {d['nom']} ({d['code']}) | Maxence Soileux"
    desc = f"Formation incendie, SST et prévention en {d['nom']} ({d['code']}) : interventions dans vos locaux, formateur SSIAP 3, IPRP déclaré et sapeur-pompier volontaire. Exemples de missions réalisées dans le département."
    return page(title, desc, d['slug'], 'formation', body, '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>')

def zones_section():
    cards = ''.join(f'''<a class="card cat-card zone" href="{d['slug']}"><span class="zone-code">{d['code']}</span><h3>{d['nom']}</h3><p>{len(d['cases'])} missions décrites</p><span class="link-arrow">Voir {ico('arrow')}</span></a>''' for d in DEPTS.values())
    return f'''<section class="section section--tint" id="zones">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Zones d'intervention</span>
      <h2>En Île-de-France, et partout en France selon la mission</h2>
      <p class="lead">J'interviens dans toute l'Île-de-France. Ailleurs en France, selon la durée de la mission, le nombre de sessions et les frais de déplacement.</p>
    </div>
    <div class="zones-grid" data-stagger>
      {cards}
      <div class="card zone zone--fr"><span class="zone-code">FR</span><h3>Hors Île-de-France</h3><ul class="checks"><li>{ico('check')}Audit interne ISO 9001 de deux jours, association d'aide à domicile, Vendée</li><li>{ico('check')}Plan de continuité d'activité, site de valorisation de déchets, Alpes-Maritimes</li></ul></div>
    </div>
  </div>
</section>'''
