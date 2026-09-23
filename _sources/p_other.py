from partials import ico, page

CONTACT = f'''
<section class="hero" style="padding-bottom:40px">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">Contact</span>
      <h1 class="h-anim">Parlons de votre projet</h1>
      <p class="lead">Formation, démonstration FireTraining MS ou mission de conseil : je vous réponds sous 24 h ouvrées.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <h2 class="sr-only">Coordonnées et formulaire</h2>
  <div class="wrap split contact-grid">
    <div class="split-txt">
      <ul class="contact-list">
        <li><span class="ico-tile">{ico('phone')}</span><div><small>Téléphone</small><a href="tel:+33684527858">06 84 52 78 58</a></div></li>
        <li><span class="ico-tile">{ico('mail')}</span><div><small>E-mail</small><a href="mailto:msoileux.make@gmail.com">msoileux.make@gmail.com</a></div></li>
        <li><span class="ico-tile">{ico('pin')}</span><div><small>Zone d'intervention</small><span class="v">Île-de-France et France entière</span><p style="color:var(--ink-3);font-size:.9rem">Hors Île-de-France, selon les conditions de la mission</p></div></li>
      </ul>
      <div class="legal-note">{ico('headset')}<p><strong>Envie de tester FireTraining MS ?</strong> Choisissez l'univers FireTraining MS dans le formulaire : je vous propose une démonstration sans engagement.</p></div>
    </div>
    <div class="form-card" id="form-zone">
      <form class="form" id="contact-form" novalidate>
        <fieldset class="univers-pick" style="border:0;padding:0;margin:0">
          <legend class="sr-only">Votre demande concerne</legend>
          <label><input type="radio" name="univers" id="u-formation" value="formation" checked><span>Formation<small>Incendie, SST, réglementaire</small></span></label>
          <label><input type="radio" name="univers" id="u-firetraining" value="firetraining"><span>FireTraining MS<small>Démo, licence, achat</small></span></label>
          <label><input type="radio" name="univers" id="u-conseil" value="conseil"><span>Conseil<small>DUERP, RPS, audit, ISO</small></span></label>
        </fieldset>
        <div class="field"><label for="prenom">Prénom *</label><input id="prenom" name="prenom" autocomplete="given-name" required></div>
        <div class="field"><label for="nom">Nom *</label><input id="nom" name="nom" autocomplete="family-name" required></div>
        <div class="field field--full"><label for="organisation">Organisation</label><input id="organisation" name="organisation" autocomplete="organization" placeholder="Entreprise, mairie, organisme de formation"></div>
        <div class="field"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="telephone">Téléphone</label><input id="telephone" name="telephone" type="tel" autocomplete="tel"></div>
        <div class="field field--full"><label for="objet">Sujet *</label><select id="objet" name="objet" required><option value="">Choisir un sujet</option></select></div>
        <div class="field field--full"><label for="message">Votre message *</label><textarea id="message" name="message" required placeholder="Effectifs, lieu, période souhaitée, contexte"></textarea></div>
        <div class="field--full" style="display:flex;flex-direction:column;gap:12px">
          <button class="btn btn-primary" type="submit" id="contact-submit" style="align-self:flex-start">Envoyer ma demande {ico('arrow', extra=' ico-arrow')}</button>
          <p class="form-error" id="contact-error" hidden>L'envoi n'a pas abouti. Écrivez-moi directement à msoileux.make@gmail.com ou appelez le 06 84 52 78 58.</p>
          <p class="form-note">* Champs obligatoires. Vos données servent uniquement à répondre à votre demande (voir les <a href="mentions-legales.html#confidentialite">mentions légales</a>).</p>
        </div>
      </form>
    </div>
  </div>
</section>
'''

MENTIONS = '''
<section class="hero" style="padding-bottom:32px">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:0">
      <span class="eyebrow">Informations légales</span>
      <h1>Mentions légales et confidentialité</h1>
      <p class="lead">Dernière mise à jour : septembre 2026.</p>
    </div>
  </div>
</section>
<section class="section legal" style="padding-top:0">
  <div class="wrap">
    <h2 id="mentions">Éditeur du site</h2>
    <ul>
      <li>Maxence Soileux, entrepreneur individuel (MAKE Consulting), formateur et consultant en prévention des risques professionnels</li>
      <li>2 rue Vandana Shiva, 93450 L'Île-Saint-Denis</li>
      <li>Téléphone : 06 84 52 78 58 · E-mail : msoileux.make@gmail.com</li>
      <li>SIRET : 879 519 221 00022 · TVA intracommunautaire : FR50879519221</li>
      <li>Responsable de la publication : Maxence Soileux</li>
    </ul>
    <h2>Hébergeur</h2>
    <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
    <h2>Propriété intellectuelle</h2>
    <p>Les contenus de ce site (textes, images, logo, captures de l'application FireTraining MS) appartiennent à Maxence Soileux, sauf mention contraire. Toute reproduction sans autorisation écrite est interdite.</p>

    <h2 id="confidentialite">Données personnelles</h2>
    <p>Conformément au RGPD (UE 2016/679) et à la loi Informatique et Libertés, voici comment vos données sont traitées. Responsable du traitement : Maxence Soileux, à l'adresse ci-dessus.</p>
    <div class="table-wrap"><table>
      <thead><tr><th>Données</th><th>Finalité</th><th>Base légale</th><th>Conservation</th></tr></thead>
      <tbody>
        <tr><td>Nom, prénom, e-mail, téléphone, organisation, message</td><td>Répondre aux demandes de contact et de devis</td><td>Mesures précontractuelles, intérêt légitime</td><td>3 ans après le dernier contact</td></tr>
        <tr><td>Mesure d'audience (Google Analytics)</td><td>Comprendre la fréquentation du site</td><td>Consentement</td><td>13 mois maximum</td></tr>
      </tbody>
    </table></div>
    <p>Le formulaire de contact est traité via Google Apps Script et stocké dans un tableur Google (Google LLC). Les transferts hors Union européenne sont encadrés par les clauses contractuelles types de la Commission européenne. Vos données ne sont jamais vendues.</p>

    <h2 id="cookies">Cookies</h2>
    <p>Google Analytics n'est chargé qu'après votre accord, donné via le bandeau. Sans accord, aucun cookie de mesure n'est déposé. Vous pouvez modifier votre choix à tout moment avec le lien « Gérer les cookies » en bas de chaque page. La vidéo de démonstration de FireTraining MS n'est chargée depuis YouTube (Google, domaine youtube-nocookie.com) que si vous cliquez sur « Lire ». Les polices de caractères sont hébergées sur ce site : leur affichage ne fait appel à aucun service tiers.</p>

    <h2 id="droits">Vos droits</h2>
    <p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité. Pour les exercer : msoileux.make@gmail.com. Réponse sous un mois. Vous pouvez également saisir la CNIL (www.cnil.fr, 3 place de Fontenoy, 75007 Paris).</p>
  </div>
</section>
'''

def build_contact():
    return page('Contact | Formation, FireTraining MS et conseil QSE',
                'Demande de devis formation incendie et SST, démonstration FireTraining MS ou mission de conseil QSE en Île-de-France. Réponse sous 24 h ouvrées.',
                'contact.html', 'formation', CONTACT)

def build_mentions():
    return page('Mentions légales | MAKE Consulting', 'Mentions légales, politique de confidentialité et gestion des cookies du site formation-incendie-paris.com.',
                'mentions-legales.html', 'formation', MENTIONS)


NOTFOUND = f'''
<section class="hero">
  <div class="wrap" style="text-align:center;display:flex;flex-direction:column;align-items:center;gap:20px;padding-block:40px">
    <span class="zone-code" style="font-size:5rem">404</span>
    <h1 class="h-anim">Cette page <span class="accent" style="color:var(--acc);font-style:italic;font-weight:500">n'existe pas</span></h1>
    <p class="lead">Elle a peut-être changé d'adresse lors de la refonte du site. Voici les pages les plus consultées.</p>
    <div class="hero-btns" style="justify-content:center">
      <a class="btn btn-primary" href="index.html">Retour à l'accueil {ico('arrow', extra=' ico-arrow')}</a>
      <a class="btn btn-ghost" href="formations.html">Voir les formations</a>
    </div>
    <div class="other-zones" style="margin-top:12px"><a class="link-arrow" href="firetraining-ms.html">FireTraining MS {ico('arrow')}</a><a class="link-arrow" href="conseil.html">Conseil {ico('arrow')}</a><a class="link-arrow" href="contact.html">Contact {ico('arrow')}</a></div>
  </div>
</section>'''

def build_404():
    h = page('Page introuvable | MAKE Consulting', "Cette page n'existe pas ou a changé d'adresse.", '404.html', 'formation', NOTFOUND)
    h = h.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<base href="/">', 1)
    return h.replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"', 1)
