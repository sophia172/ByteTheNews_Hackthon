(() => {
    let audio = null;
    let isPlaying = false;

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
            isPlaying = false;
            chrome.runtime.sendMessage({ action: "audioCompleted" });
        });
        audio.addEventListener("play", () => {
            isPlaying = true;
            chrome.runtime.sendMessage({ action: "audioStarted" });
        });
        audio.play();
    };

    const toggleAudioPlayback = () => {
        if (audio) {
            if (audio.paused) {
                audio.play();
                isPlaying = true;
            } else {
                audio.pause();
                isPlaying = false;
            }
        } else {
            console.log("No audio loaded yet.");
        }
        return isPlaying;
    };

    const pageUrl = window.location.href;

    fetch("https://bytethenews.yingliu.site/api/data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: pageUrl }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`API error: ${response.statusText}`);
            }
            return response.blob();
        })
        .then((audioBlob) => {
            playAudio(audioBlob);
        })
        .catch((error) => console.error("API error:", error));

    chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
        if (message.action === "toggleAudio") {
            const currentPlayingState = toggleAudioPlayback();
            sendResponse({ isPlaying: currentPlayingState });
        }
    });
})();
