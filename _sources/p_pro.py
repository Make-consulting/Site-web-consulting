from partials import ico, page
from p_index import faq_item

def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{ico("check")}{i}</li>' for i in items) + '</ul>'

def steps(items):
    return '<ol class="steps steps--4">' + ''.join(f'<li><h4>{t}</h4><p>{d}</p></li>' for t, d in items) + '</ol>'

LIC = 'contact.html?univers=firetraining&amp;sujet=Licence%20annuelle%20FireTraining%20MS%20(OF)'
ACH = 'contact.html?univers=firetraining&amp;sujet=Achat%20FireTraining%20MS%20(formateur%20ind%C3%A9pendant)'
DEMO = 'contact.html?univers=firetraining&amp;sujet=D%C3%A9mo%20FireTraining%20MS'

BODY = f'''
<section class="hero hero--night">
  <canvas data-embers="50" aria-hidden="true"></canvas>
  <div class="wrap hero-grid">
    <div class="hero-txt">
      <span class="eyebrow">FireTraining MS · Professionnels de la formation</span>
      <h1 class="h-anim">Ajoutez la réalité mixte <span class="accent">à vos formations incendie.</span></h1>
      <p class="lead">Organisme de formation ou formateur indépendant, utilisez FireTraining MS dans vos propres sessions. Deux formules, pensées pour deux façons de travailler.</p>
      <div class="hero-btns">
        <a class="btn btn-primary" href="{DEMO}">Demander une démo {ico('arrow', extra=' ico-arrow')}</a>
        <a class="btn btn-outline-light" href="#formules">Choisir ma formule</a>
      </div>
      <div class="hero-proof">
        <span>{ico('headset')}Meta Quest</span>
        <span>{ico('flame')}Conçue par un formateur SSIAP 3</span>
        <span>{ico('shield')}Et sapeur-pompier volontaire</span>
      </div>
    </div>
    <div class="hero-visual">
      <div class="media"><img src="assets/firetraining-screenshot.jpg" alt="Extincteur virtuel dirigé vers un départ de feu dans FireTraining MS" width="1200" height="799" fetchpriority="high"></div>
    </div>
  </div>
</section>

<section class="section" id="formules">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal">
      <span class="eyebrow">Formules</span>
      <h2>Vous êtes…</h2>
    </div>
    <div class="tabs" role="tablist" aria-label="Choisir votre profil">
      <button class="tab" role="tab" id="tab-of" aria-controls="of" aria-selected="true" type="button">{ico('building')}<span><b>Un organisme de formation</b><small>Licence annuelle</small></span></button>
      <button class="tab" role="tab" id="tab-formateur" aria-controls="formateur" aria-selected="false" type="button" tabindex="-1">{ico('usercheck')}<span><b>Un formateur indépendant</b><small>Achat unique</small></span></button>
    </div>

    <div class="tab-panel" role="tabpanel" id="of" aria-labelledby="tab-of">
      <div class="split" style="align-items:start">
        <div class="split-txt">
          <h3 class="panel-title">Licence annuelle pour organismes de formation</h3>
          <p class="lead">Intégrez FireTraining MS à votre catalogue et équipez vos formateurs. La licence comprend l&#39;accompagnement, le support et l&#39;évolution de l&#39;application.</p>
          {checks(['Accès complet à l&#39;application', 'Prise en main de vos formateurs (2 h)', 'Support technique inclus', 'Mises à jour et nouveaux scénarios inclus', 'Tableau de bord formateur'])}
          <div class="hero-btns"><a class="btn btn-primary" href="{LIC}">Parler de la licence {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-ghost" href="{DEMO}">Voir une démo</a></div>
          <p class="price-note">Tarif annuel sur devis, selon le nombre de formateurs et de casques.</p>
        </div>
        <div class="card why">
          <h4>Ce que la licence apporte à votre organisme</h4>
          <ul class="why-list">
            <li><span class="ico-tile">{ico('award')}</span><div><strong>Une offre qui se distingue</strong><span>Un module réalité mixte à présenter dans vos propositions et votre catalogue.</span></div></li>
            <li><span class="ico-tile">{ico('users')}</span><div><strong>Des sessions plus interactives</strong><span>Chaque stagiaire passe à l&#39;action, même quand l&#39;exercice sur feu réel est limité.</span></div></li>
            <li><span class="ico-tile">{ico('chart')}</span><div><strong>Un suivi des stagiaires</strong><span>Réactions et temps mesurés pendant l&#39;exercice, pour un débriefing précis.</span></div></li>
            <li><span class="ico-tile">{ico('refresh')}</span><div><strong>Une application qui évolue</strong><span>Nouveaux scénarios inclus pendant toute la durée de la licence.</span></div></li>
          </ul>
        </div>
      </div>
      <div class="panel-steps">
        <h4 class="steps-title">Le déploiement</h4>
        {steps([('Démo', 'Présentation dans vos locaux ou à Paris, avec vos formateurs.'), ('Devis', 'Selon le nombre de formateurs, de casques et de sites.'), ('Prise en main', 'Deux heures avec vos formateurs pour animer un exercice.'), ('En session', 'Vos formateurs utilisent l&#39;application, le support reste disponible.')])}
      </div>
    </div>

    <div class="tab-panel" role="tabpanel" id="formateur" aria-labelledby="tab-formateur" hidden>
      <div class="split" style="align-items:start">
        <div class="split-txt">
          <h3 class="panel-title">Achat de l&#39;application pour formateurs indépendants</h3>
          <p class="lead">Un achat unique, sans abonnement. Vous installez l&#39;application sur votre casque et vous l&#39;utilisez en toute autonomie dans vos sessions.</p>
          {checks(['Fichier d&#39;installation livré', 'Scénario tronc commun inclus', 'Sans abonnement annuel', 'Scénarios additionnels à l&#39;unité', 'Utilisation en autonomie'])}
          <div class="hero-btns"><a class="btn btn-primary" href="{ACH}">Obtenir un devis {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-ghost" href="{DEMO}">Voir une démo</a></div>
          <p class="price-note">Tarif sur demande.</p>
        </div>
        <div class="card why">
          <h4>Pourquoi l&#39;achat convient aux indépendants</h4>
          <ul class="why-list">
            <li><span class="ico-tile">{ico('target')}</span><div><strong>Un coût maîtrisé</strong><span>Vous payez une fois, sans engagement annuel.</span></div></li>
            <li><span class="ico-tile">{ico('layers')}</span><div><strong>Vous choisissez vos scénarios</strong><span>Ajoutez des scénarios à l&#39;unité, selon vos clients et vos sessions.</span></div></li>
            <li><span class="ico-tile">{ico('headset')}</span><div><strong>Un matériel léger</strong><span>Un casque Meta Quest se transporte facilement d&#39;une session à l&#39;autre.</span></div></li>
            <li><span class="ico-tile">{ico('award')}</span><div><strong>Un argument face à vos clients</strong><span>Proposez un module réalité mixte en complément de vos exercices pratiques.</span></div></li>
          </ul>
        </div>
      </div>
      <div class="panel-steps">
        <h4 class="steps-title">Comment ça se passe</h4>
        {steps([('Démo', 'Vous testez l&#39;application avant de décider.'), ('Achat', 'Devis puis achat unique, sans abonnement.'), ('Installation', 'Le fichier est livré et installé sur votre casque.'), ('Scénarios', 'Vous ajoutez des scénarios quand vous en avez besoin.')])}
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">En pratique</span><h2>Ce qu&#39;il faut pour animer un exercice</h2></div>
    <div class="modal-grid" data-stagger>
      <div class="modal-item"><span class="ico-tile">{ico('headset')}</span><h4>Un casque Meta Quest</h4><p>Je vous conseille sur les modèles compatibles avant l&#39;achat.</p></div>
      <div class="modal-item"><span class="ico-tile">{ico('building')}</span><h4>Une salle de formation</h4><p>Le stagiaire voit la salle grâce à la vidéo en transparence : pas besoin d&#39;espace dédié.</p></div>
      <div class="modal-item"><span class="ico-tile">{ico('users')}</span><h4>Des stagiaires à tour de rôle</h4><p>Chacun traite son départ de feu pendant que le groupe observe et commente.</p></div>
      <div class="modal-item"><span class="ico-tile">{ico('flame')}</span><h4>La pratique réelle à côté</h4><p>L&#39;application complète la manipulation d&#39;extincteurs, elle ne la remplace pas.</p></div>
    </div>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap">
    <div class="sec-head sec-head--center reveal"><span class="eyebrow">Questions fréquentes</span><h2>Avant de vous équiper</h2></div>
    <div class="faq reveal">
      {faq_item("Quelle différence entre la licence et l&#39;achat ?", "La licence annuelle s&#39;adresse aux organismes de formation : elle inclut la prise en main des formateurs, le support, les mises à jour et les nouveaux scénarios. L&#39;achat s&#39;adresse aux formateurs indépendants : un paiement unique, un scénario tronc commun, et des scénarios additionnels à l&#39;unité.", True)}
      {faq_item("Quel casque faut-il ?", "L&#39;application fonctionne sur casques Meta Quest. Je vous indique les modèles compatibles avant tout achat de matériel.")}
      {faq_item("Mes stagiaires doivent-ils connaître la réalité virtuelle ?", "Non. Le stagiaire continue de voir la salle et ses collègues. La mise en casque prend quelques instants et le formateur guide chaque exercice.")}
      {faq_item("L&#39;application remplace-t-elle la formation pratique ?", "Non. C&#39;est un complément pédagogique. Les formations doivent conserver leurs éléments pratiques obligatoires, dont la manipulation réelle d&#39;extincteurs.")}
      {faq_item("Puis-je tester avant de m&#39;engager ?", "Oui. Je propose une démonstration à Paris ou dans vos locaux en Île-de-France. Ailleurs en France, contactez-moi pour organiser une présentation.")}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="cta-band reveal" style="background:var(--night)">
      <canvas data-embers="40" aria-hidden="true"></canvas>
      <div><h2>Voyez l&#39;application avec vos formateurs</h2><p>Une démonstration de 30 minutes pour juger si FireTraining MS a sa place dans vos sessions.</p></div>
      <div class="btns"><a class="btn btn-primary" href="{DEMO}">Demander une démo {ico('arrow', extra=' ico-arrow')}</a><a class="btn btn-outline-light" href="tel:+33684527858">{ico('phone')} 06 84 52 78 58</a></div>
    </div>
  </div>
</section>
'''

def build():
    return page('FireTraining MS pour organismes de formation et formateurs | Licence et achat',
                "Intégrez la réalité mixte à vos formations incendie : licence annuelle FireTraining MS pour organismes de formation, achat unique pour formateurs indépendants. Démonstration sur demande.",
                'firetraining-pro.html', 'firetraining', BODY, current='firetraining-pro.html')
