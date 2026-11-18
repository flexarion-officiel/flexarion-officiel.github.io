# Compte rendu de la première version

## Appréciation sur la forme

### Commun à toutes les pages
- Lorsque le scroll n'est pas tout en haut de la page, proposer un bouton pour retourner tout en haut, de manière smooth

### Header
- (Mobile) : Ajouter un menu burger pour afficher les différentes sections du menu

### Footer
- Aligner les textes au centre
- Supprimer le lien « En savoir plus »
- Ajouter le logo de flexarion
- Ajouter les liens **externes** suivants :
    - Organisation GitHub : https://github.com/flexarion-officiel
    - amU IUT : https://iut.univ-amu.fr/fr
- Meilleur responsive pour mobile (surtout pour le texte)

### Page d'accueil
- L'image est beaucoup trop grande et ne laisse pas apparaitre le titre, les boutons et autre

### Page studio
- Supprimer la mention « Flexarion est un studio fictif... »

### Page Below Zero
- Créer une section pour expliquer l'origine du nom Sextia, et faire un lien vers cette section dès que le mot Sextia est mentionné dans la page. Bien choisir l'emplacement de la section

### Page Contact & Presse
- Supprimer la mention « Cette adresse fait partie de la fiction... »
- Supprimer la mention « fictif » pour le responsable communication
- Supprimer la section de la charte graphique

### Page Mentions légales
- Supprimer cette page de l'indexation (donc du sitemap.xml et autres)

## Appréciation globale

Mentionner que le projet est fictif ne te pénalise pas en soi : Google ne baisse pas le classement d'une page parce qu'elle contient « fictif ». Ce qui compte, c'est l'endroit où tu le dis. Garde-le dans les mentions légales et en pied de page, et sors-le du titre, de la meta description et du début du balisage Organization, là où ces mots prennent la place de tes mots-clés. En ce moment, la description de ton balisage commence par « studio indépendant (fictif) ». Mets la mention à la fin de la phrase, ou retire-la du JSON-LD (les données structurées que lisent les moteurs) et garde-la dans le texte visible du pied de page.

Ton balisage déclare un LocalBusiness avec une adresse, des coordonnées GPS et 8 salariés, alors que le studio n'existe pas. Google considère des données structurées trompeuses comme du spam et peut les ignorer, voire sanctionner le site. Passe plutôt en simple Organization, sans adresse ni géolocalisation. C'est là que les concurrents qui ne disent rien prennent un vrai risque, et pas toi.

La page d'accueil centrée sur le nom. Ton titre commence déjà par « Flexarion », c'est parfait. Ajoute alternateName (« Flexarion Studio », « Studio Flexarion ») dans le balisage Organization, et un logo déclaré dans logo.
De la fraîcheur.