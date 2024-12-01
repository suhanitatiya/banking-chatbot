import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState(""); // User query
  const [response, setResponse] = useState(""); // Chatbot response

  const sendMessage = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:8000/chat/", { message }); // API call
      setResponse(res.data.response); // Update response
    } catch (err) {
      console.error("Error fetching response:", err);
      setResponse("Error: Unable to get a response."); // Handle errors
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Banking Chatbot</h1>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your query..."
        style={{ width: "300px", marginRight: "10px" }}
      />
      <button onClick={sendMessage}>Send</button>
      <div style={{ marginTop: "20px" }}>
        <strong>Response:</strong> {response}
      </div>
    </div>
  );
}

export default App;
