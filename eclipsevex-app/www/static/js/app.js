let chatHistory = [];

async function sendMessage() {

    let input = document.getElementById("msg");
    let text = input.value;
    input.value = "";
    if (!text.trim()) return;

    addMessage("user", text);
    chatHistory.push({ role: "user", text: text });

    // Placeholder bubble that will hold the live status line, then the answer
    let aiDiv = addMessage("ai", "");
    let statusSpan = document.createElement("span");
    statusSpan.className = "status-line";
    aiDiv.appendChild(statusSpan);

    let answerStarted = false;
    let fullAnswer = "";

    try {
        let res = await fetch("/api/chat/stream", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text, history: chatHistory })
        });

        let reader = res.body.getReader();
        let decoder = new TextDecoder();
        let buffer = "";

        while (true) {
            let { value, done } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, { stream: true });

            let parts = buffer.split("\n\n");
            buffer = parts.pop(); // keep the last (possibly incomplete) chunk

            for (let part of parts) {
                if (!part.startsWith("data: ")) continue;
                let payload;
                try {
                    payload = JSON.parse(part.slice(6));
                } catch (e) {
                    continue;
                }

                if (payload.status) {
                    statusSpan.innerText = payload.status;
                    statusSpan.style.display = "inline";
                } else if (payload.t) {
                    if (!answerStarted) {
                        answerStarted = true;
                        statusSpan.style.display = "none";
                    }
                    fullAnswer += payload.t;
                    aiDiv.innerText = fullAnswer;
                } else if (payload.done) {
                    statusSpan.style.display = "none";
                }
            }

            let box = document.getElementById("chatbox");
            box.scrollTop = box.scrollHeight;
        }

        chatHistory.push({ role: "ai", text: fullAnswer });

    } catch (e) {
        statusSpan.style.display = "none";
        aiDiv.innerText = "Error. Please try again.";
    }
}

function addMessage(role, text) {

    let box = document.getElementById("chatbox");

    let div = document.createElement("div");
    div.className = "msg " + role;
    div.innerText = text;

    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
    return div;
}
