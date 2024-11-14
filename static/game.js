const clicker = document.getElementById("PressableButton")
let score = document.getElementById("score")

clicker.addEventListener("click", function () {
    score += 1
});