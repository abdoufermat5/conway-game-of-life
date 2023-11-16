# Jeu de la vie Conway

### Description
Le jeu de la vie (ou game of life) est un automate cellulaire évoluant sur une grille (de taille théoriquement infinie)
composée de cases carrées appelées cellules qui ont un état binaire (1 pour vivante et 0 pour morte). Les cellules
évoluent dans le temps en fonction de leur voisinage (chaque cellule a 8 cellules voisines)., ce qui modifie la grille
à chaque étape d'évolution (appelée génération).

![illustration](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

### Règles
- Une cellule morte possédant exactement 3 voisines vivantes devient vivante (elle naît).
- Une cellule vivante possédant 2 ou 3 voisines vivantes le reste, sinon elle meurt.
- Les autres cellules (mortes ou vivantes) restent dans leur état actuel.

### Implémentation
- Le jeu de la vie est implémenté en python sous forme de package: `galsen_game_of_life`
- Le package est publie sur PyPi: https://pypi.org/project/galsen-game-of-life/

```python
def game_of_life(matrices):
    n_col = len(matrices[0])
    n_row = len(matrices)
    # on initialize un etat vide
    next_Matrices = [[0 for _ in range(n_col)] for _ in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            num_neighbors = 0
            # print("ij: ", i, j, "mat:", matrices[i][j], end="\t")
            # check des 8 voisins
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < len(matrices) and 0 <= y < len(matrices[0]):
                        if matrices[x][y] == 1:
                            num_neighbors += 1

            num_neighbors = num_neighbors - matrices[i][j]
            # print("neighbors: ",num_neighbors, end="\t")
            if num_neighbors in [0, 1] or num_neighbors > 3:
                    # print("die")
                    next_Matrices[i][j] = 0
            else:

                if matrices[i][j] == 0:
                    if num_neighbors == 3:
                        # print("survival")
                        next_Matrices[i][j] = 1
                    else:
                        pass
                        # print("died")
                if matrices[i][j] == 1:
                    next_Matrices[i][j] = 1
                    # print("survival")

    return next_Matrices
```

Dans ce code on crée la fonction game_of_life qui permet de calculer l'etat suivant a partir d'un etat actuel. Il prend en parametres l'etat actuel qui est une matrices bidimensionnelle (n*m) et retourne l'etat suivant de meme type.
Le fonctionnement est assez simple on regarde les 8 voisins de chaque cellule et en fonction des criteres de bases, on met a jour la cellule dans la matrice representant l'etat suivant.

### Utilisation
Vu qu'on a mis notre solution sous forme de package donc pour l'utiliser indépendemment du test qu'on propose dans ce projet vous devez creer un projet python et installer le package.

Donc on commence par installer le package:

```bash
pip3 install galsen-game-of-life
```
Pour tester notre implementation du jeu de la vie on a plusieurs options:

#### 1. application client/serveur

Pour notre part on a mis en place un [websocket](https://fr.wikipedia.org/wiki/Websocket) client/serveur.

![illustration](https://upload.wikimedia.org/wikipedia/commons/1/10/Websocket_connection.png)

```python
import asyncio
import websockets
import json
from galsen_game_of_life import game_of_life  


async def game_of_life_server(websocket, path):
    try:
        initial_message = await websocket.recv()
        data = json.loads(initial_message)
        initial_state = data["initial_state"]
        print("Initial state: ", initial_state, sep="\n")
        steps = data["steps"]
        delay = data["delay"]

        current_state = initial_state

        for _ in range(steps):
            current_state = game_of_life(current_state)

            await websocket.send(json.dumps(current_state))

            await asyncio.sleep(delay)
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally")
    except websockets.exceptions.ConnectionClosedError as e:
        print("Connection closed with error:", e)



if __name__ == "__main__":

    start_server = websockets.serve(game_of_life_server, "localhost", 8000)
    print("Server started at localhost:8000")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

```
Dans ce code on ouvre un socket sur 8000 pour interagir avec un client. A la reception d'un etat et les params associés, le serveur renvoie en streaming tous les etats (generations) jusqu'a atteindre un certains nombre `steps` spécifié
par le client.
Puis il se remet a l'ecoute jusqu'a ce que la connection soit fermé par le client.

Pour lancer le serveur websocket, il faut lancer le script `main_server.py` dans le dossier `api/`:

```bash
python3 api/main_server.py
```

Le serveur websocket est alors accessible sur `ws://localhost:8000`

Ensuite on a mis en place un client javascript pour pouvoir communiquer avec le serveur websocket.
Il suffit juste d'ouvrir le fichier `index.html` (dans le dossier `client-app/`) dans un navigateur web pour pouvoir jouer au jeu de la vie.

<b>Spoiler Alert:</b> On est pas trop bon en html/css par ici!! 

![gol](./assets/gme-of-life.gif)

#### 2. application console
Une autre option c'est de tester sur des fichiers en console.

On peut jouer au jeu de la vie en ligne de commande!. Pour cela il vous faudra un fichier de depart contenant un etat initial
Exemple de fichier de depart:
```bash title="test-data.txt"
0 1 1 1 1 0 1 1 0 1
0 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 0 0 1 0
0 1 1 0 1 1 0 1 0 1
0 0 0 0 0 1 1 1 0 0
0 0 0 1 0 0 1 0 1 0
1 0 1 1 1 0 0 1 0 1
1 1 0 0 0 0 0 0 1 1
1 0 1 0 1 1 0 1 1 1
1 0 0 0 0 0 1 0 0 0
```
Pour lancer le jeu de la vie en ligne de commande, il faut ensuite installer le package `galsen-game-of-life`:

```bash
pip3 install galsen-game-of-life
```

ensuite on peut lancer en ligne de commande:
```bash
galsen-game-of-life --input test-data.txt --num-steps 10 --output-file test-data-out.txt
```

> `--num-steps` : pour le nombre d'iterations
> `--input` : le path du fichier en entrée
> `--output-file` : le fichier en sortie (optionnel)

Si on veut voir les etapes intermediaires, on peut ajouter l'option `--verbose`:
```bash
galsen-game-of-life --input test-data.txt --num-steps 10 --output-file test-data-out.txt --verbose 1
```

