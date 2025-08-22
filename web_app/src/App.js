import React, { useState } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([]);
  const [listening, setListening] = useState(false);

  const handleListen = () => {
    if (!window.SpeechRecognition && !window.webkitSpeechRecognition) {
      alert("Your browser does not support Speech Recognition.");
      return;
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    recognition.onstart = () => setListening(true);
    recognition.onend = () => setListening(false);

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      addMessage("You: " + transcript);
      sendToFlask(transcript);
    };

    recognition.start();
  };

  const addMessage = (text) => {
    setMessages((prev) => [...prev, text]);
  };

  const sendToFlask = async (text) => {
    try {
      const res = await axios.post("/api/voice", { text });
      const responseText = res.data.response.join(" ");
      addMessage("Assistant: " + responseText);
    } catch (err) {
      addMessage("Assistant: Error connecting to server.");
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>AIVA – AI Voice Assistant</h2>
      <button onClick={handleListen} disabled={listening}>
        {listening ? "Listening..." : "Talk to Assistant"}
      </button>

      <div
        style={{
          marginTop: "20px",
          padding: "10px",
          border: "1px solid #ccc",
          height: "300px",
          overflowY: "auto",
        }}
      >
        {messages.map((msg, i) => (
          <div key={i}>{msg}</div>
        ))}
      </div>

      <div style={{ marginTop: "20px" }}>
        <strong>Suggestions:</strong>
        <ul>
          <li>Hi / Hello</li>
          <li>What time is it?</li>
          <li>What’s today’s date?</li>
          <li>Play [song name]</li>
          <li>Stop / Exit</li>
        </ul>
      </div>
    </div>
  );
}

export default App;
