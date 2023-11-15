const socket = new WebSocket("ws://127.0.0.1:8000/ws/game-of-life");


socket.onopen = function (e) {
    console.log("here we go!");
    // on envoi l'etat initial au serveur
    // TODO: remplacer par un etat aléatoire OU un etat choisi par l'utilisateur
    socket.send(JSON.stringify({
        initial_state: [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        // TODO: remplacer par un nombre choisi par l'utilisateur
        steps: 10,
        // TODO: remplacer par un nombre choisi par l'utilisateur (par defaut 1s)
        delay: 1
    }));
};

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log("state :", data.current_state);
    displayGameState(data.current_state);
};

socket.onerror = function(error) {
    console.log(`erreur: ${error.message}`);
};

// afficher l'etat du jeu: la matrice bi-dimensionnelle
function displayGameState(state) {

    matrices.innerHTML = '';


    state.forEach(row => {
        const rowDiv = document.createElement('div');
        row.forEach(cell => {
            const cellDiv = document.createElement('div');
            cellDiv.style.width = '20px';
            cellDiv.style.height = '20px';
            cellDiv.style.display = 'inline-block';
            cellDiv.style.border = '1px solid black';
            cellDiv.style.backgroundColor = cell ? 'black' : 'white';
            rowDiv.appendChild(cellDiv);
        });
        matrices.appendChild(rowDiv);
    });
}