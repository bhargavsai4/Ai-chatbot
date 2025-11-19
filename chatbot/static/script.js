async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;
  
    appendMessage("user", message);
    input.value = "";
  
    appendMessage("bot", "Typing...", true); // show typing...
  
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: message })
    });
  
    const data = await response.json();
    removeTypingIndicator();
    appendMessage("bot", data.answer);
  }
  
  function appendMessage(sender, text, isTyping = false) {
    const chatbox = document.getElementById("chatbox");
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}`;
    msgDiv.innerText = text;
    msgDiv.dataset.typing = isTyping;
    chatbox.appendChild(msgDiv);
    chatbox.scrollTop = chatbox.scrollHeight;
  }
  
  function removeTypingIndicator() {
    const chatbox = document.getElementById("chatbox");
    const nodes = chatbox.querySelectorAll('[data-typing="true"]');
    nodes.forEach(node => node.remove());
  }
  