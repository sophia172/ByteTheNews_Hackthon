(() => {

    let audio = null; 

    const playAudio = (audioBlob) => {      
        const audioUrl = URL.createObjectURL(audioBlob);
        if (audio) {
            audio.pause();
            audio.currentTime = 0;
            audio.src = ""; 
            audio = null;
        }
        audio = new Audio(audioUrl);
        audio.addEventListener("ended", () => {
            console.log("Audio playback completed.");
            isAudioPlaying = false; 
            chrome.runtime.sendMessage({ action: "audioCompleted" });
        });
        audio.addEventListener("play", () => {
            console.log("Audio playback started.");
            isAudioPlaying = true; 
            chrome.runtime.sendMessage({ action: "audioStarted" });
        });
        audio.play();
        isAudioPlaying = true;
    };

    const toggleAudioPlayback = () => {
        if (audio) {
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
        } else {
            console.log("No audio loaded yet.");
        }
    };

    const pageUrl = window.location.href;

    const extractedData = {
        url: pageUrl
    };

    fetch('http://localhost:8000/api/data', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(extractedData)
    })
    .then(async (response) => {
        if (!response.ok) {
            throw new Error(`API error: ${response.statusText}`);
        }
        
        audioBlob = await response.blob();
        playAudio(audioBlob); 
    })
    .catch(error => console.error("API error:", error));

    chrome.runtime.onMessage.addListener((message) => {
        if (message.action === "toggleAudio") {
            toggleAudioPlayback();
        }
    });
})();
