chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
console.log("message received: ",message)
  if (message.action === "sendToAPI") {
    console.log("received: ", message.data)
    const apiUrl = "https://your-api-endpoint.com/data"; // Replace with your API endpoint

    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(message.data)
    })
    .then(response => response.json())
    .then(data => console.log("API response:", data))
    .catch(error => console.error("API error:", error));
  }
});
