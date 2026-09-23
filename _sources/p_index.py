from partials import ico, page


LOGOS = [('logo-cesi.png', 'CESI'), ('logo-proform.png', 'Proform'), ('logo-aprentiv.jpg', 'Aprentiv'), ('logo-lide.jpg', 'Lide'), ('logo-leo.png', 'Léo'), ('logo-delville.png', 'Delville'), ('logo-client4.png', 'Client MAKE')]

def logos_band():
    imgs = ''.join(f'<img src="assets/clients/{f}" alt="{a}" loading="lazy">' for f, a in LOGOS)
    dup = ''.join(f'<img src="assets/clients/{f}" alt="" aria-hidden="true" loading="lazy">' for f, a in LOGOS)
    return f'''<section class="logos" aria-label="Ils me font confiance">
  <div class="wrap">
    <span class="logos-label">Ils me font confiance</span>
    <div class="marquee"><div class="marquee-track">{imgs}{dup}</div></div>
  </div>
</section>'''

def faq_item(q, a, open_=False):
    o = ' open' if open_ else ''
    return f'''<div class="faq-item{o}"><button class="faq-q" type="button" aria-expanded="{'true' if open_ else 'false'}">{q}<span class="pm">{ico('plus')}</span></button><div class="faq-a"><div><p>{a}</p></div></div></div>'''

def session(t, d):
    return f'<li>{ico("check")}<span><strong>{t}</strong> · {d}</span></li>'

BODY = f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-txt">
      <span class="eyebrow">Formation incendie · Paris &amp; Île-de-France</span>
      <h1 class="h-anim">Formez vos équipes au feu, <span class="accent">dans vos locaux.</span></h1>
      <p class="lead">Formations incendie, SST et réglementaires en intra-entreprise. Des exercices pratiques sur extincteurs, des attestations conformes, et un formateur qui connaît le terrain.</p>
      <div class="hero-btns">
        <a class="btn btn-primary" href="contact.html?univers=formation">Demander un devis {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-ghost" href="#formations">Voir les formations</a>
      </div>
      <div class="hero-proof">
        <span>{ico('flame')}SSIAP 1 &amp; 3</span>
        <span>{ico('heart')}Formateur SST agréé INRS</span>
        <span>{ico('shield')}Sapeur-pompier volontaire depuis 2012</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="hero-photo"><img src="assets/photo-formation.jpg" alt="Maxence Soileux prépare des extincteurs avant une formation incendie" width="1200" height="895" fetchpriority="high"></div>
      <div class="float-chip chip-a"><span class="ico-tile">{ico('shield')}</span><div><strong>IPRP déclaré</strong><span>Île-de-France</span></div></div>
      <div class="float-chip chip-b"><span class="ico-tile">{ico('users')}</span><div><strong>400+ stagiaires</strong><span>formés chaque année</span></div></div>
    </div>
  </div>
</section>

{logos_band()}

<section class="section" id="formations">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Catalogue</span>
      <h2>Trois domaines, toujours en intra-entreprise</h2>
      <p class="lead">Chaque session se déroule dans vos locaux, avec le matériel pédagogique fourni. Programmes adaptables à vos effectifs, vos horaires et votre DUERP.</p>
    </div>
    <div class="grid-3" data-stagger>
      <article class="card card--feature">
        <span class="ico-tile">{ico('flame')}</span>
        <h3>Sécurité incendie</h3>
        <p>Pour tous les établissements : ERP, IGH, industrie, tertiaire. Théorie courte, pratique longue.</p>
        <ul class="checks">
          {session('Sensibilisation incendie', '½ journée')}
          {session('Équipier de première intervention', '½ journée')}
          {session('Guide et serre-file', '½ journée')}
          {session('Module réalité mixte', 'en option')}
        </ul>
        <a class="link-arrow" href="formation-incendie.html">Voir les programmes {ico('arrow')}</a>
      </article>
      <article class="card">
        <span class="ico-tile">{ico('heart')}</span>
        <h3>SST &amp; secourisme</h3>
        <p>Selon le référentiel national INRS, avec certificat valable 24 mois.</p>
        <ul class="checks">
          {session('SST initial', '2 jours')}
          {session('Recyclage SST (MAC)', '1 jour')}
          {session('PSC', '1 jour')}
          {session('Gestes qui sauvent', '2 heures')}
        </ul>
        <a class="link-arrow" href="formation-sst.html">Voir les programmes {ico('arrow')}</a>
      </article>
      <article class="card">
        <span class="ico-tile">{ico('clipboard')}</span>
        <h3>Formations réglementaires</h3>
        <p>Construites à partir de vos risques réels et de votre document unique.</p>
        <ul class="checks">
          {session('Risques chimiques', '½ à 1 jour')}
          {session('Travail en hauteur', '1 jour')}
          {session('Prévention des RPS', '½ journée')}
          {session('Risque amiante SS4', 'sur devis')}
        </ul>
        <a class="link-arrow" href="formations-reglementaires.html">Voir les programmes {ico('arrow')}</a>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark" aria-label="Chiffres clés">
  <div class="wrap">
    <div class="stats" data-stagger>
      <div class="stat"><b data-count="400" data-suffix="+">400+</b><span>stagiaires formés chaque année</span></div>
      <div class="stat"><b>2019</b><span>formateur et consultant depuis</span></div>
      <div class="stat"><b data-count="5">5</b><span>certifications et habilitations</span></div>
      <div class="stat"><b data-count="8">8</b><span>secteurs d'activité accompagnés</span></div>
    </div>
  </div>
</section>

<section class="section" id="methode">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Déroulé</span>
      <h2>De la demande à l'attestation</h2>
    </div>
    <ol class="steps steps--4" data-stagger>
      <li><h4>Échange</h4><p>Vos effectifs, vos locaux, vos contraintes horaires. Un appel suffit.</p></li>
      <li><h4>Programme et devis</h4><p>Proposition détaillée avec contenu, durée et budget, envoyée sous 48 h.</p></li>
      <li><h4>Session sur site</h4><p>J'interviens chez vous avec extincteurs, supports et, si vous le souhaitez, les casques de réalité mixte.</p></li>
      <li><h4>Attestations et bilan</h4><p>Attestations individuelles, feuille d'émargement et bilan de session pour votre registre de sécurité.</p></li>
    </ol>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap split">
    <div class="media reveal">
      <img src="assets/firetraining-screenshot.jpg" alt="Vue de l'application FireTraining MS : un extincteur virtuel face à un départ de feu" width="1200" height="799" loading="lazy">
      <span class="media-tag">Capture de l'application FireTraining MS</span>
    </div>
    <div class="split-txt reveal">
      <span class="eyebrow">Option réalité mixte</span>
      <h2>Un module FireTraining MS, en complément du terrain</h2>
      <p class="lead">Avec le casque, vos stagiaires voient un départ de feu apparaître dans leur propre environnement de travail et s'exercent à le traiter. Le module s'ajoute aux exercices pratiques, il ne les remplace pas.</p>
      <ul class="checks">
        <li>{ico('check')}Casques fournis pour la session</li>
        <li>{ico('check')}Scénarios rejouables pour chaque stagiaire</li>
        <li>{ico('check')}Rapport individuel des réactions</li>
      </ul>
      <a class="link-arrow" href="firetraining-ms.html">Découvrir FireTraining MS {ico('arrow')}</a>
    </div>
  </div>
</section>

<section class="section" id="references">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Témoignages</span>
      <h2>Ce qu'en disent mes clients</h2>
    </div>
    <div class="grid-3" data-stagger>
      <figure class="quote"><blockquote>Une formation incendie sérieuse, accessible et parfaitement adaptée à nos 80 collaborateurs. M. Soileux a su capter l'attention du groupe du début à la fin.</blockquote><figcaption><strong>Responsable RH</strong>PME industrielle, Seine-Saint-Denis</figcaption></figure>
      <figure class="quote"><blockquote>La formation SST avec M. Soileux a été un vrai moment de montée en compétences pour nos équipes. Pédagogie claire, exercices pratiques, 100% de réussite.</blockquote><figcaption><strong>Coordinateur sécurité</strong>Établissement médico-social, Paris 15e</figcaption></figure>
      <figure class="quote"><blockquote>Le DUERP que Maxence a réalisé pour notre mairie est d'une qualité remarquable. Complet, opérationnel, et présenté de façon limpide au conseil municipal.</blockquote><figcaption><strong>Directrice générale des services</strong>Commune de 12 000 habitants, Val-de-Marne</figcaption></figure>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap split">
    <div class="split-txt reveal">
      <span class="eyebrow">Votre formateur</span>
      <h2>Maxence Soileux</h2>
      <p class="lead">Formateur et consultant depuis 2019, j'interviens auprès d'entreprises, de collectivités et d'organismes de formation en Île-de-France.</p>
      <p>Sapeur-pompier volontaire en Île-de-France depuis 2012, titulaire du SSIAP 3 et IPRP déclaré, je relie la formation à la réalité du feu et de vos risques : ce que vos équipes apprennent correspond à ce qu'elles rencontrent dans vos locaux.</p>
      <a class="link-arrow" href="conseil.html">Voir aussi mes missions de conseil {ico('arrow')}</a>
    </div>
    <div class="card cert-card reveal">
      <ul class="cert-list">
        <li><span class="ico-tile">{ico('shield')}</span><div><strong>Sapeur-pompier volontaire</strong><span>En Île-de-France depuis 2012</span></div></li>
        <li><span class="ico-tile">{ico('flame')}</span><div><strong>SSIAP 1 &amp; SSIAP 3</strong><span>Agent et chef de service sécurité incendie</span></div></li>
        <li><span class="ico-tile">{ico('heart')}</span><div><strong>Formateur SST agréé INRS</strong><span>Sauveteur secouriste du travail</span></div></li>
        <li><span class="ico-tile">{ico('grad')}</span><div><strong>Master MQSE</strong><span>Management qualité, sécurité, environnement</span></div></li>
        <li><span class="ico-tile">{ico('hardhat')}</span><div><strong>Encadrant technique amiante SS4</strong><span>Sous-section 4</span></div></li>
        <li><span class="ico-tile">{ico('scale')}</span><div><strong>IPRP déclaré</strong><span>Intervenant en prévention des risques professionnels</span></div></li>
      </ul>
    </div>
  </div>
</section>

%%ZONES%%

<section class="section" id="faq">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Questions fréquentes</span>
      <h2>Vos obligations, en clair</h2>
    </div>
    <div class="faq reveal">
      {faq_item("La formation incendie est-elle obligatoire en entreprise ?", "Oui. Le Code du travail (art. R.4227-28 et suivants) impose à tout employeur d'informer et de former ses salariés à la prévention incendie et aux consignes d'évacuation, quels que soient la taille et le secteur de l'établissement. Il prévoit aussi des exercices et essais périodiques.", True)}
      {faq_item("Combien de temps dure une formation incendie ?", "Une sensibilisation incendie dure une demi-journée, tout comme la formation d'équipier de première intervention, qui inclut la manipulation d'extincteurs. Les durées s'adaptent au nombre de participants et à la configuration de vos locaux.")}
      {faq_item("Combien de personnes par session ?", "Pour garder un vrai temps de pratique sur extincteurs, je recommande des groupes de 10 à 12 personnes. Pour des effectifs plus importants, j'organise plusieurs sessions sur la même journée.")}
      {faq_item("Quelle est la durée de validité du certificat SST ?", "Le certificat SST est valable 24 mois. Au-delà, un recyclage (MAC SST) d'une journée est nécessaire pour conserver le statut de sauveteur secouriste du travail.")}
      {faq_item("Intervenez-vous en dehors de Paris ?", "J'interviens dans toute l'Île-de-France, et partout en France selon les conditions de la mission (durée, nombre de sessions, frais de déplacement). <a class='link-arrow' href='#zones'>Voir les zones d'intervention</a>")}
    </div>
    <p style="text-align:center;margin-top:28px"><a class="link-arrow" href="faq.html">Toutes les questions {ico('arrow')}</a></p>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta-band reveal">
      <canvas data-embers="34" aria-hidden="true"></canvas>
      <div>
        <h2>Planifions votre prochaine session</h2>
        <p>Dites-moi combien de personnes former et où. Je vous envoie un programme et un devis sous 48 h.</p>
      </div>
      <div class="btns">
        <a class="btn btn-light" href="contact.html?univers=formation">Demander un devis {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a>
      </div>
    </div>
  </div>
</section>
'''

JSONLD = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"MAKE Consulting – Formation incendie Paris","url":"https://www.formation-incendie-paris.com","telephone":"+33684527858","email":"msoileux.make@gmail.com","image":"https://www.formation-incendie-paris.com/assets/photo-formation.jpg","address":{"@type":"PostalAddress","streetAddress":"2 rue Vandana Shiva","postalCode":"93450","addressLocality":"L'Île-Saint-Denis","addressCountry":"FR"},"areaServed":"Île-de-France","founder":{"@type":"Person","name":"Maxence Soileux","jobTitle":"Formateur SSIAP 3 et IPRP"}}</script>'''

def build():
    from p_local import zones_section
    return page('Formation incendie et SST à Paris | Maxence Soileux, SSIAP 3',
                'Formations incendie, SST et réglementaires dans vos locaux à Paris et en Île-de-France. Formateur SSIAP 3, IPRP déclaré, attestations conformes. Devis sous 48 h.',
                '', 'formation', BODY.replace('%%ZONES%%', zones_section()), JSONLD)
