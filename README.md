# MAKE Consulting — Site web make-consulting.fr

Site statique HTML/CSS pour MAKE Consulting, cabinet QSE (Qualité, Sécurité, Environnement).

---

## Structure des fichiers

```
make-consulting.fr/
├── index.html          → Accueil
├── duerp.html          → Offre DUERP clé en main
├── audit-qse.html      → Offre Audit QSE
├── a-propos.html       → Présentation / Maxence Soileux
├── blog.html           → Articles SEO (placeholder)
├── contact.html        → Formulaire qualifiant
├── style.css           → Feuille de style unique (mobile-first)
└── assets/
    └── logo.png        ← À placer manuellement
```

---

## Déploiement sur GitHub Pages

### Étape 1 — Créer le dépôt GitHub

1. Connectez-vous sur [github.com](https://github.com)
2. Créez un nouveau dépôt public nommé `make-consulting.fr` (ou `website`)
3. **Ne pas** initialiser avec README (vous allez pousser des fichiers existants)

### Étape 2 — Uploader les fichiers

**Via l'interface GitHub (sans ligne de commande) :**

1. Dans votre dépôt vide, cliquez **Add file → Upload files**
2. Glissez-déposez tous les fichiers du dossier `make-consulting.fr/`
3. Créez le dossier `assets/` en uploadant `logo.png` avec le chemin `assets/logo.png`
4. Cliquez **Commit changes**

**Via Git (si vous utilisez le terminal) :**

```bash
cd make-consulting.fr
git init
git add .
git commit -m "init: site make-consulting.fr"
git remote add origin https://github.com/VOTRE-COMPTE/make-consulting.fr.git
git push -u origin main
```

### Étape 3 — Activer GitHub Pages

1. Dans votre dépôt, allez dans **Settings → Pages**
2. Source : **Deploy from a branch**
3. Branch : **main** / **/ (root)**
4. Cliquez **Save**

Votre site sera accessible en quelques minutes à l'adresse :
`https://VOTRE-COMPTE.github.io/make-consulting.fr/`

### Étape 4 — Connecter votre nom de domaine make-consulting.fr

1. Dans **Settings → Pages → Custom domain**, entrez `make-consulting.fr`
2. Chez votre registrar (OVH, Namecheap, Gandi…), créez les enregistrements DNS suivants :

```
Type A     @    185.199.108.153
Type A     @    185.199.109.153
Type A     @    185.199.110.153
Type A     @    185.199.111.153
Type CNAME www  VOTRE-COMPTE.github.io.
```

3. Attendez la propagation DNS (15 min à 48h selon le registrar)
4. Activez **Enforce HTTPS** dans GitHub Pages une fois le domaine validé

---

## Éléments à personnaliser avant la mise en ligne

### Obligatoires

| Élément | Fichier(s) | Action |
|---|---|---|
| **Logo** | `assets/logo.png` | Copier votre fichier logo ici |
| **SIRET** | Tous les footers | Remplacer "SIRET : à compléter" |
| **Témoignages** | `index.html` | Remplacer les 3 placeholders par de vraies citations |
| **Photo Maxence** | `a-propos.html` | Remplacer le placeholder `<div class="profile-placeholder">` par `<img src="assets/maxence-soileux.jpg" alt="Maxence Soileux, fondateur de MAKE Consulting">` |
| **Page mentions légales** | `mentions-legales.html` | Créer cette page (éditeur, hébergeur, RGPD) |

### Recommandés

| Élément | Fichier(s) | Action |
|---|---|---|
| Formulaire → Make.com | `contact.html`, `duerp.html`, `audit-qse.html` | Voir section ci-dessous |
| Articles de blog | `blog.html` | Rédiger et publier les 3 articles SEO |
| Google Analytics / Search Console | Tous les `<head>` | Ajouter le tag GA4 et vérifier la propriété |
| Favicon | Tous les `<head>` | Ajouter `<link rel="icon" href="assets/favicon.ico">` |

---

## Connexion des formulaires à Make.com

Les trois formulaires (contact.html, duerp.html, audit-qse.html) sont actuellement en HTML statique. Pour recevoir les soumissions par email ou les enregistrer dans un CRM :

### Option 1 — Formspree (le plus simple, gratuit jusqu'à 50 soumissions/mois)

1. Créez un compte sur [formspree.io](https://formspree.io)
2. Créez un nouveau formulaire et copiez l'endpoint fourni (ex: `https://formspree.io/f/XXXXXXXX`)
3. Dans chaque fichier HTML, remplacez `action="#"` (ou `action="contact.html"`) par l'endpoint Formspree
4. Remplacez `method="POST"` par `method="POST"` (inchangé)

### Option 2 — Make.com (webhook) — Recommandé

1. Dans Make.com, créez un scénario avec un déclencheur **Webhooks → Custom webhook**
2. Copiez l'URL du webhook générée
3. Dans chaque formulaire HTML, remplacez l'attribut `action` par l'URL webhook
4. Ajoutez dans le scénario Make un module Email ou Slack pour être notifié à chaque soumission
5. Optionnel : ajouter un module Google Sheets pour centraliser les leads

```html
<!-- Exemple de modification dans contact.html -->
<form name="contact-principal" method="POST" action="https://hook.eu1.make.com/VOTRE_WEBHOOK_ID" ...>
```

> Note : les formulaires en `method="POST"` vers Make.com nécessitent que Make accepte les données `application/x-www-form-urlencoded`. Configurez le module webhook en conséquence ou utilisez un script JS fetch() si nécessaire.

---

## SEO — Checklist post-lancement

- [ ] Créer un compte Google Search Console et vérifier le domaine
- [ ] Soumettre le sitemap (à créer : `sitemap.xml`)
- [ ] Vérifier l'indexation des 6 pages principales
- [ ] Rédiger et publier les 3 articles de blog (priorité SEO locale : "DUERP Île-de-France", "consultant QSE TPE", etc.)
- [ ] Créer une fiche Google My Business pour MAKE Consulting
- [ ] Obtenir les premiers backlinks (annuaires QSE, pages IPRP, réseaux professionnels)

---

## Support technique

Le site est en HTML/CSS pur, sans dépendance externe ni framework. Toute modification peut être faite directement dans les fichiers. Pour toute question technique sur le déploiement GitHub Pages, la documentation officielle est disponible sur [docs.github.com/pages](https://docs.github.com/pages).
