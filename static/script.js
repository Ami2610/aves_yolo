let running = false;

function toggleVideo() {
    const video = document.getElementById("video");
    const box = document.getElementById("videoBox");

    if (!running) {
        // START
        video.src = "/video";  // endpoint Flask
        video.classList.add("active");

        box.classList.remove("stop");
        box.classList.add("active");
    } else {
        // STOP
        video.src = "";
        video.classList.remove("active");

        box.classList.remove("active");
        box.classList.add("stop");
    }

    running = !running;
}
