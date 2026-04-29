# 🚀 Jarvis V3 — Local AI Assistant (Phi + Voice + GUI)

A minimal AI assistant built using **Python + Local AI (Phi)**  
Works offline, no API limits, clean UI.

---

## ⚡ Features
- 🎤 Voice commands (YouTube, Time, Music)
- 🧠 Local AI (Phi via Ollama)
- 🖥️ Streamlit GUI (Siri-style UI)
- 🌐 Works offline (after setup)
- ⚡ Fast + lightweight

---

## 🧠 Tech Stack
- Python
- Streamlit
- SpeechRecognition
- pyttsx3
- Requests
- Ollama (Phi model)

---

## ⚙️ Setup

### 1. Install dependencies
```bash
pip install streamlit speechrecognition pyttsx3 requests
```

### 2. Install Ollama & run Phi
```bash
ollama run phi
```

### 3. Run project
``` bash
streamlit run main.py
```

---

📂 How It Works
Voice Input → Command Check → 
    ├── If match → Run action (YouTube, Time, Music)
    └── Else → Send to Phi (Local AI)

---

### 🔥 Future Improvements
- Memory (chat history)
- Wake word ("Hey Jarvis")
- Better UI/UX
- More commands

---

### 🧠 Learnings
- Real projects = system design, not just code
- Always build fallback (AI can fail)
- Keep it simple, focus on high-impact features

---

### 📌 Author

Built by Nishant Chauhan

---

### ⭐ Support

If you found this useful:

- Star the repo
- Share with others
