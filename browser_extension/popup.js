const playPauseButton = document.getElementById("playPause");
const playPauseIcon = document.getElementById("playPauseIcon");
const extractButton = document.getElementById("extract");

const updateUI = (state) => {
    if (state === "loading") {
        extractButton.hidden = true;
        playPauseButton.hidden = false;
        playPauseButton.disabled = true;
        playPauseButton.style.backgroundColor = "#d3d3d3";
        playPauseButton.innerHTML = `<i id="playPauseIcon" class="fas fa-pause icon"></i> Wait`;
    } else if (state === "playing") {
        playPauseButton.disabled = false;
        playPauseButton.style.backgroundColor = "#28a745";
        playPauseButton.innerHTML = `<i id="playPauseIcon" class="fas fa-pause icon"></i> Pause`;
        extractButton.hidden = true;
        playPauseButton.hidden = false;
    } else if (state === "paused") {
        playPauseButton.disabled = false;
        playPauseButton.style.backgroundColor = "#007bff";
        playPauseButton.innerHTML = `<i id="playPauseIcon" class="fas fa-play icon"></i> Play`;
        extractButton.hidden = true;
        playPauseButton.hidden = false;
    } else {
        extractButton.hidden = false;
        playPauseButton.hidden = true;
    }
};

// Check the state when the popup is opened
chrome.storage.local.get(["isPlaying", "isLoading", "activeTabId"], (result) => {
    const isPlaying = result.isPlaying || false;
    const isLoading = result.isLoading || false;

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const currentTabId = tabs[0].id;
        const isActiveTab = currentTabId === result.activeTabId;

        if (isLoading && isActiveTab) {
            updateUI("loading");
        } else if (isPlaying && isActiveTab) {
            updateUI("playing");
        } else {
            updateUI();
        }
    });
});

// Handle "Hear Summary" button click
extractButton.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const activeTabId = tabs[0].id;

        chrome.storage.local.set({ activeTabId, isLoading: true });
        updateUI("loading");

        chrome.scripting.executeScript({
            target: { tabId: activeTabId },
            files: ["content.js"],
        });
    });
});

// Handle "Play/Pause" button click
playPauseButton.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.tabs.sendMessage(tabs[0].id, { action: "toggleAudio" }, (response) => {
            const isPlaying = response?.isPlaying || false;
            chrome.storage.local.set({ isPlaying, isLoading: false });
            updateUI(isPlaying ? "playing" : "paused");
        });
    });
});

// Listener for messages from the content script
chrome.runtime.onMessage.addListener((message) => {
    if (message.action === "audioStarted") {
        chrome.storage.local.set({ isPlaying: true, isLoading: false });
        updateUI("playing");
    } else if (message.action === "audioCompleted") {
        chrome.storage.local.set({ isPlaying: false, isLoading: false });
        updateUI("paused");
    }
});
