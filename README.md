
# VoicePrint ID 🔊🛡️

**VoicePrint ID** is a secure voice-biometric authentication system with a simple web interface. Built using Python (Flask), it captures and verifies user identity using unique vocal signatures.

---

## 🌐 Features

- 🎤 Web-based voice registration and login
- 🔐 Voice biometric authentication using MFCC + cosine similarity
- 🧠 Simple front-end using HTML + CSS
- 📦 Dependency management via Poetry or pip

---

## 📂 Project Structure

```
voiceprint-id/
├── static/
│   └── style.css               # Basic styling for UI
├── templates/
│   └── index.html              # Web interface
├── main.py                     # Flask server + voice logic
├── voice_db.json               # Stores user voiceprints (ensure privacy!)
├── requirements.txt            # Pip dependencies
├── pyproject.toml              # Poetry config
├── .gitignore
└── README.md                   # This file
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-117ABHISHEK/voiceprint-id.git
cd voiceprint-id
```

### 2. Install Dependencies

Using **Poetry**:
```bash
poetry install
```

Or using **pip**:
```bash
pip install -r requirements.txt
```

### 3. Start the Web App

```bash
python main.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## ⚠️ Notes

- The `voice_db.json` file may contain personal data. Replace it with a dummy or exclude it from GitHub if needed.
- This project is intended for learning/demo purposes only.

---

## 🙌 Made By

Developed with ❤️ by Abhishek  
Built using Python, Flask, and Web Audio API.

---

## 📜 License

MIT License — free to use, share, and modify.
