const analyzeBtn = document.getElementById("analyzeBtn");
const textInput = document.getElementById("textInput");
const resultDiv = document.getElementById("result");

analyzeBtn.addEventListener("click", async () => {
    const text = textInput.value.trim();
    if (!text) return alert("Please enter how you feel!");

    resultDiv.innerHTML = `<p class="loading">Analyzing your mood... 🎵</p>`;
    analyzeBtn.disabled = true;

    try {
        const response = await fetch("http://127.0.0.1:8000/emotion/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        if (data.song && data.song.track_id) {
            resultDiv.innerHTML = `
                <span class="emotion-badge ${data.emotion.toLowerCase()}">
                    ${getEmotionEmoji(data.emotion)} ${data.emotion}
                </span>
                <div class="player-wrapper">
                    <iframe
                        src="https://open.spotify.com/embed/track/${data.song.track_id}"
                        width="100%"
                        height="152"
                        frameBorder="0"
                        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                        loading="lazy">
                    </iframe>
                </div>
            `;
        } else {
            resultDiv.innerHTML = `<p class="error">No song found for this emotion. Try again!</p>`;
        }
    } catch (err) {
        resultDiv.innerHTML = `<p class="error">Error connecting to backend. Make sure the server is running!</p>`;
        console.error(err);
    } finally {
        analyzeBtn.disabled = false;
    }
});

function getEmotionEmoji(emotion) {
    const emojis = {
        happy: "😊",
        sad: "😢",
        angry: "😠",
        relaxed: "😌",
        neutral: "😐"
    };
    return emojis[emotion.toLowerCase()] || "🎵";
}