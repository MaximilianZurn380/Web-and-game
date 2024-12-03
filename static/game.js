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


    fetch("/save-score", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            player_name: playerName,
            score: score
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error("Error", error);
    });
});
document.getElementById("saveScore").addEventListener("click", function ()
{
    console.log("eghejghjkgfh");
    
});