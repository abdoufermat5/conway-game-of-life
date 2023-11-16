# Jeu de la vie Conway

### Description
Le jeu de la vie (ou game of life) est un automate cellulaire évoluant sur une grille (de taille théoriquement infinie)
composée de cases carrées appelées cellules qui ont un état binaire (1 pour vivante et 0 pour morte). Les cellules
évoluent dans le temps en fonction de leur voisinage (chaque cellule a 8 cellules voisines)., ce qui modifie la grille
à chaque étape d'évolution (appelée génération).

### Règles
- Une cellule morte possédant exactement 3 voisines vivantes devient vivante (elle naît).
- Une cellule vivante possédant 2 ou 3 voisines vivantes le reste, sinon elle meurt.
- Les autres cellules (mortes ou vivantes) restent dans leur état actuel.

### Implémentation
- Le jeu de la vie est implémenté en python sous forme de package: `game_of_life`
- A COMPLETER AU FIL DU TEMPS 

### Utilisation

On a mis en place un websocket pour pouvoir communiquer avec le jeu de la vie.
Pour lancer le serveur websocket, on a utiliser fastapi (peut etre pas necessaire mais on veut faire d'autres trucs openAPI)
Pour lancer le serveur websocket, il faut lancer le script `main_server.py` dans le dossier `api/` avec uvicorn:
```bash
uvicorn main_server:app --reload
```
Le serveur websocket est alors accessible sur `ws://localhost:8000/ws`

Ensuite on a mis en place un client javascript pour pouvoir communiquer avec le serveur websocket.
Il suffit juste d'ouvrir le fichier `index.html` dans un navigateur web pour pouvoir jouer au jeu de la vie.

### TODO Ameliorations de l'algo et du package
- [ ] Decoupler le code: possibilité POO
- [ ] Revoir la complexité de l'algo pour le moment enorme!!

### TODO Ameliorations de l'UI et l'UX
- [ ] Ajouter une grille infinie (illusion d'infini) zoomable
- [ ] Ajouter un bouton pour lancer le jeu
- [ ] Ajouter un bouton pour arreter le jeu
- [ ] Ajouter un bouton pour faire une etape
- [ ] Ajouter un bouton pour effacer la grille
- [ ] Ajouter un bouton pour generer un etat aleatoire