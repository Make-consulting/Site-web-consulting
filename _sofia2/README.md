# Sofia2 — visuels LinkedIn

- `visuel.py` génère le visuel du post (1080 × 1350, JPG) aux couleurs de MAKE Consulting, avec le vrai logo (`assets/logo.png`) et les polices du site. Aucun quota d'IA.
- Les images publiées sont déposées dans `medias/linkedin/AAAA-MM-JJ-slug.jpg` et servies par
  `https://raw.githubusercontent.com/Make-consulting/Site-web-consulting/main/medias/linkedin/<fichier>`.
- Les images de plus de 7 jours sont supprimées par la tâche planifiée (elles restent dans l'historique git).
- Ces dossiers ne sont pas mis en ligne sur make-consulting.fr (site hébergé chez OVH, déployé à la main).
