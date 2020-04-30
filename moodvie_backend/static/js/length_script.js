window.addEventListener("load",function() { 
    let mood = document.getElementById("selectedMood");
    changeBackgroundBasedOnMood(mood);
 });

 function changeBackgroundBasedOnMood(mood) {
    if ("selectedMood" === "Inspiring") {
        document.body.style = hsl(186, 59% 47%);
    } else if ("selectedMood" === "Uplifting") {
        document.body.style = hsl(33, 78%, 65%);
    } else if ("selectedMood" === "Thought Provoking") {
        document.body.style = hsl(79, 54%, 65%);
    } else ("selectedMood" === "Love") {
        document.body.style = hsl(302, 62%, 47%);
    }
 };