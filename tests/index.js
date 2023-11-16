document.addEventListener("DOMContentLoaded", function () {
  const canvas = document.getElementById("gameCanvas");
  const ctx = canvas.getContext("2d");
  const sizeOfCell = 10;
  let matrices = [];
  let isRunning = false;
  let step = 100;
  let socket;

  canvas.width = 500;
  canvas.height = 500;

  function initiateWebSocket() {
    socket = new WebSocket("ws://localhost:8000");
    socket.onmessage = function (event) {
      updateGrid(JSON.parse(event.data));
    };

    socket.onclose = function (event) {
      console.log("Connection closed");
    };
    socket.onerror = function (event) {
      console.log("Error: " + event.data);
    };
  }

  function updateGrid(newState) {
    matrices = newState;
    drawMatricesGrid();
  }

  function drawMatricesGrid() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let y = 0; y < matrices.length; y++) {
      for (let x = 0; x < matrices[y].length; x++) {
        ctx.fillStyle = matrices[y][x] ? "black" : "white";
        ctx.fillRect(x * sizeOfCell, y * sizeOfCell, sizeOfCell, sizeOfCell);
      }
    }

    // les quadrillages
    ctx.strokeStyle = "#000";
    // les lignes verticales
    for (let i = 0; i <= canvas.width; i += sizeOfCell) {
      ctx.beginPath();
      ctx.moveTo(i, 0);
      ctx.lineTo(i, canvas.height);
      ctx.stroke();
    }
    // les lignes horizontales
    for (let j = 0; j <= canvas.height; j += sizeOfCell) {
      ctx.beginPath();
      ctx.moveTo(0, j);
      ctx.lineTo(canvas.width, j);
      ctx.stroke();
    }
  }

  canvas.addEventListener("click", function (event) {
    if (!isRunning) {
      const rect = canvas.getBoundingClientRect();
      const x = Math.floor((event.clientX - rect.left) / sizeOfCell);
      const y = Math.floor((event.clientY - rect.top) / sizeOfCell);
      matrices[y][x] = matrices[y][x] ? 0 : 1;
      drawMatricesGrid();
    }
  });

  document.getElementById("startBtn").addEventListener("click", function () {
    if (!isRunning) {
      isRunning = true;
      if (socket.readyState === WebSocket.CLOSED) {
        initiateWebSocket();
      }

      if (socket.readyState === WebSocket.OPEN) {
        socket.send(
          JSON.stringify({ initial_state: matrices, steps: step, delay: 0 })
        );
      } else {
        setTimeout(() => {
          socket.send(
            JSON.stringify({ initial_state: matrices, steps: step, delay: 0 })
          );
        }, 1000);
      }
    }
  });

  document.getElementById("pauseBtn").addEventListener("click", function () {
    isRunning = false;
    socket.close();
  });

  document.getElementById("resetBtn").addEventListener("click", function () {
    matrices = Array(50)
      .fill() // 50 lignes vides
      .map(() => Array(50).fill(0)); // 50 colonnes de 0 par ligne
    drawMatricesGrid(); // dessine la grille
    isRunning = false;
  });

  document
    .getElementById("randomStateBtn")
    .addEventListener("click", function () {
      if (!isRunning) {
        matrices = Array(50)
          .fill()
          .map(() =>
            Array(50)
              .fill()
              .map(() => Math.round(Math.random()))
          );
        drawMatricesGrid();
      }
    });

  // update du nombre d'etapes
  document.getElementById("numSteps").addEventListener("change", function () {
    step = parseInt(numSteps.value);
  });

  initiateWebSocket();
  resetBtn.click();
});
