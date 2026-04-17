<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>INSANE DODGE</title>

<style>
body{
    margin:0;
    background:black;
    color:white;
    text-align:center;
    font-family:Arial;
    overflow:hidden;
}

canvas{
    display:block;
    margin:auto;
    background:#0d0d0d;
    border:2px solid #222;
}

h2,p{
    margin:8px;
}
</style>
</head>
<body>

<h2>🔥 INSANE DODGE 🔥</h2>
<p id="score">Score: 0 | Recorde: 0</p>

<canvas id="game" width="320" height="500"></canvas>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let score = 0;
let record = localStorage.getItem("record") || 0;
let gameOver = false;

let player = {
    x: 140,
    y: 450,
    w: 40,
    h: 40
};

let obstacles = [];
let particles = [];

let speed = 4;
let spawnTimer = 0;

// swipe mobile
let touchStartX = 0;

canvas.addEventListener("touchstart", e => {
    touchStartX = e.touches[0].clientX;
});

canvas.addEventListener("touchmove", e => {
    let currentX = e.touches[0].clientX;

    if(currentX < touchStartX - 20){
        moveLeft();
        touchStartX = currentX;
    }

    if(currentX > touchStartX + 20){
        moveRight();
        touchStartX = currentX;
    }
});

// teclado pc
document.addEventListener("keydown", e => {
    if(e.key === "ArrowLeft") moveLeft();
    if(e.key === "ArrowRight") moveRight();
});

function moveLeft(){
    if(player.x > 0) player.x -= 40;
}

function moveRight(){
    if(player.x < canvas.width - player.w) player.x += 40;
}

// desenhar jogador
function drawPlayer(){
    ctx.fillStyle = "lime";
    ctx.fillRect(player.x, player.y, player.w, player.h);
}

// desenhar obstáculos
function drawObstacles(){
    ctx.fillStyle = "red";

    obstacles.forEach(obs => {
        ctx.fillRect(obs.x, obs.y, obs.w, obs.h);
    });
}

// criar obstáculo
function spawnObstacle(){
    let cols = canvas.width / 40;
    let x = Math.floor(Math.random() * cols) * 40;

    obstacles.push({
        x:x,
        y:0,
        w:40,
        h:40
    });
}

// mover obstáculos
function updateObstacles(){
    obstacles.forEach(obs => obs.y += speed);

    obstacles = obstacles.filter(obs => obs.y < canvas.height);
}

// partículas
function createParticles(x,y){
    for(let i=0;i<20;i++){
        particles.push({
            x:x,
            y:y,
            dx:(Math.random()-0.5)*6,
            dy:(Math.random()-0.5)*6,
            life:30
        });
    }
}

function drawParticles(){
    ctx.fillStyle = "orange";

    particles.forEach(p => {
        ctx.fillRect(p.x,p.y,4,4);
        p.x += p.dx;
        p.y += p.dy;
        p.life--;
    });

    particles = particles.filter(p => p.life > 0);
}

// colisão
function checkCollision(){
    for(let obs of obstacles){
        if(
            player.x < obs.x + obs.w &&
            player.x + player.w > obs.x &&
            player.y < obs.y + obs.h &&
            player.y + player.h > obs.y
        ){
            createParticles(player.x + 20, player.y + 20);
            endGame();
        }
    }
}

function endGame(){
    gameOver = true;

    if(score > record){
        record = score;
        localStorage.setItem("record", record);
    }

    setTimeout(() => {
        alert("💀 Game Over\nScore: " + score);
        resetGame();
    }, 200);
}

function resetGame(){
    score = 0;
    speed = 4;
    obstacles = [];
    particles = [];
    player.x = 140;
    gameOver = false;
    loop();
}

// loop
function loop(){
    if(gameOver) return;

    ctx.clearRect(0,0,canvas.width,canvas.height);

    drawPlayer();
    drawObstacles();
    drawParticles();

    updateObstacles();
    checkCollision();

    spawnTimer++;

    if(spawnTimer > 30){
        spawnObstacle();
        spawnTimer = 0;
    }

    score++;

    // dificuldade progressiva
    if(score % 200 === 0){
        speed += 0.5;
    }

    document.getElementById("score").innerText =
        "Score: " + score + " | Recorde: " + record;

    requestAnimationFrame(loop);
}

loop();
</script>

</body>
</html>
