window.addEventListener("load",function() { 
    let mood = document.getElementById("selectedMood");
    changeBackgroundBasedOnMood(mood);
 });

 function changeBackgroundBasedOnMood(mood) {
    if ("selectedMood" === "Inspiring") {
        document.body.style = rgb(50, 177, 192);
    } else if ("selectedMood" === "Uplifting") {
        document.body.style = rgb(235, 173, 90);
    } else if ("selectedMood" === "Thought Provoking") {
        document.body.style = rgb(184, 214, 117);
    } else {
        document.body.style = rgb(193, 46, 188);
    }
 };