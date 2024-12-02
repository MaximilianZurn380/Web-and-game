let score = 0;

document.getElementById("buttonPress").addEventListener("click", function ()
{
    score++;
    document.getElementById("score").innerText = score;
});

document.getElementById("saveScore").addEventListener("click", function () {
    const playerName = document.getElementById("playerName").value;

    if (!playerName)
    {
        alert("Please enter your name");
        return;
    }
})
document.getElementById("saveScore").addEventListener("click", function ()
{
    console.log("eghejghjkgfh");
    
});