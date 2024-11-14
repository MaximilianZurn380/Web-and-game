let score = 0;

document.getElementById("buttonPress").addEventListener("click", () => {
    score++;
    document.getElementById("score").innerText = score;
});