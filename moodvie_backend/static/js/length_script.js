window.addEventListener("load",function() { 
    console.log('loaded');
    let mood = document.getElementById("selectedMood").innerHTML;
        console.log(mood);
        changeBackgroundBasedOnMood(mood);
 });

function changeBackgroundBasedOnMood(mood) {
    if (mood == "inspiring") {
        document.body.style.backgroundColor = 'rgb(' + [217, 107, 107].join(',') + ')';
        // document.body.style= hsl(186, 59%, 47%);
    } else if (mood == "uplifting") {
        document.body.style.backgroundColor = 'rgb(' + [235, 173, 90].join(',') + ')';
        // document.body.style = hsl(33, 78% 65%);
    } else if (mood == "thought-provoking") {
        document.body.style.backgroundColor = 'rgb(' + [184, 214, 117].join(',') + ')';
        // document.body.style = hsl(79, 54% 65%);
    } else {
        document.body.style.backgroundColor = 'rgb(' + [107, 217, 149].join(',') + ')';
        }
}
