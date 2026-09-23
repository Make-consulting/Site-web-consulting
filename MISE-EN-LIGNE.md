# Mise en ligne de make-consulting.fr

Nouveau site du cabinet MAKE Consulting : 14 pages, construites sur la même base que formation-incendie-paris.com.

## 1. Avant de publier : relire

- [ ] **Tarifs DUERP** : repris de l'ancien site (à partir de 2 400 € HT pour une TPE, délais de 5 à 10 jours). À confirmer.
- [ ] **Références** : six missions anonymisées. En particulier l'accompagnement triple certification (pas de secteur ni d'année indiqués) et le PCA dans les Alpes-Maritimes.
- [ ] **À propos** : la mention « +10 ans d'expérience » de l'ancien site a été retirée, faute de pouvoir la vérifier (activité indépendante depuis 2019). Même chose pour « SASU » : vous êtes aujourd'hui entrepreneur individuel.
- [ ] **Diagnostic SSIAP** : relire le contenu de l'offre et les publics visés.
- [ ] **Adresse e-mail** : le site affiche maxence@make-consulting.fr.

## 2. Publier sur GitHub

Dépôt : `Make-consulting/Site-web-consulting`

1. **Conserver** le fichier `CNAME` (make-consulting.fr).
2. **Supprimer** les anciens fichiers : `index.html`, `a-propos.html`, `audit-qse.html`, `duerp.html`, `blog.html`, `contact.html`, `style.css`, `README.md` et le dossier `assets`.
3. **Déposer** tout le contenu de ce dossier à la racine du dépôt.

Les anciennes adresses restent valables : `duerp.html`, `audit-qse.html`, `a-propos.html` et `contact.html` gardent leur nom. `blog.html` redirige vers la FAQ.

⚠️ Vérifiez bien le nom du dépôt avant de déposer : **Site-web-consulting**, et non Site-web-Formation.

## 3. Après la mise en ligne

- [ ] **Formulaire** : envoyer une demande test. L'ancien formulaire ne fonctionnait pas (il n'envoyait rien). Le nouveau utilise le même Apps Script que le site formation. Le sujet arrive préfixé `[make-consulting]`, et le secteur et l'effectif sont ajoutés en tête du message.
- [ ] **Google Search Console** : ajouter la propriété `make-consulting.fr` (validation par DNS chez OVH), puis soumettre `sitemap.xml`.
- [ ] **Google Analytics** : le site utilise le même identifiant que le site formation. Les statistiques des deux sites sont donc regroupées, mais vous pouvez les séparer avec le filtre « Nom d'hôte ». Si vous préférez des statistiques distinctes, créez un second flux de données et envoyez-moi son identifiant.
- [ ] **Aperçu LinkedIn** : tester l'adresse dans le Post Inspector (image `assets/og-image.jpg`).

## 4. Liens entre les deux sites

- make-consulting.fr renvoie vers formation-incendie-paris.com : dans la barre du haut, sur une carte « Formation » parmi les missions, dans un bandeau « Former vos équipes », dans le pied de page, sur la page Contact et dans les FAQ.
- formation-incendie-paris.com renvoie vers make-consulting.fr : la page Conseil devient une page passerelle, et le pied de page ainsi que les pages locales pointent vers les missions de conseil.

## 5. Modifier le site plus tard

Même principe que pour le site formation : le dossier `_sources` contient le générateur (`python3 build.py`). GitHub Pages ne publie pas ce dossier.
