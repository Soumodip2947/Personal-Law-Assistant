# 📚 Personal Law Assistant (India) 🇮🇳

A modern, dynamic, and fully offline desktop-based legal reference tool that helps users search and interact with Indian laws including the Constitution of India, Indian Penal Code (IPC), and Code of Criminal Procedure (CrPC). This application is equipped with advanced features like PDF export, text-to-speech, animated GUI, and keyword-based legal search integrated with Indian Kanoon for case references.

---

## 🧠 Features

- 🔍 **Smart Search**: Search by section number or keywords across Constitution, IPC, and CrPC.
- 📜 **Full Constitution of India**: Stored in JSON, fully indexed and searchable.
- ⚖️ **IPC and CrPC**: Complete sections stored in a local SQLite database.
- 📁 **PDF Export**: Save search results or any article/section to a professionally formatted PDF.
- 🔊 **Text-to-Speech**: Read aloud any legal content using offline TTS (Text-to-Speech).
- 🌐 **Indian Kanoon Integration**: Search for relevant case law via Indian Kanoon in one click.
- 🎨 **Dynamic GUI**: Built with ttkbootstrap and `tkinter`, includes animated background and stylish UI.
- ⌨️ **Keyboard Shortcut**: Press `Enter` to perform a search instantly.
- 💡 **Fully Offline**: All primary features work without the internet.

---

## 📦 Tech Stack

| Component        | Technology Used         |
|------------------|--------------------------|
| GUI Framework     | `tkinter`, `ttkbootstrap` |
| Database          | SQLite (`law_data.db`)    |
| Constitution Data | JSON (`constitution.json`)|
| PDF Export        | `reportlab`              |
| Text-to-Speech    | `pyttsx3`                |
| Web Search        | `webbrowser` (Indian Kanoon) |
| OS Compatibility  | Windows, Linux           |

---

## 🏁 Getting Started

### 🔧 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/yourname/personal-law-assistant.git
cd personal-law-assistant
```

2. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
python main.py
```

---

### 📁 Folder Structure

```
personal-law-assistant/
├── constitution.json         # Constitution of India (JSON)
├── law_data.db               # IPC and CrPC sections (SQLite DB)
├── main.py                   # Application entry point
├── utils/
│   ├── pdf_exporter.py       # PDF generation logic
│   ├── tts_engine.py         # Text-to-speech utility
│   └── data_handler.py       # Database and JSON logic
├── assets/
│   ├── icons/                # Icons for buttons (search, PDF, TTS)
│   └── background/           # Optional animated background
└── requirements.txt
```

---

## 📝 Requirements

```
ttkbootstrap
pyttsx3
reportlab
Pillow
```

Install them via:

```bash
pip install -r requirements.txt
```

---

## 🔐 Data Sources

- ✅ Constitution of India: Local `constitution.json`
- ✅ Indian Penal Code: Local SQLite table `ipc_sections`
- ✅ Code of Criminal Procedure: Local SQLite table `crpc_sections`
- ✅ Indian Kanoon: Case search using `https://indiankanoon.org/search/?formInput=`

---

## 💡 How It Works

- User selects the law domain (IPC, CrPC, Constitution)
- Inputs either a section number or keyword
- Hits "Search" or presses `Enter`
- Result is shown in styled output box with options to:
  - Export as PDF
  - Read aloud
  - Search related cases on Indian Kanoon

---

## 🎯 Use Cases

- ⚖️ Law students preparing for exams
- 📚 Researchers studying the Indian legal system
- 👨‍💼 Lawyers needing offline legal reference
- 🇮🇳 Citizens seeking rights or code clarity

---

## 🧪 Testing & Compatibility

- Tested on: `Windows 10`, `Windows 11`, and `Ubuntu 22.04`
- Python version: `3.10+` recommended

---

## 🚀 Future Enhancements

- 🏛️ Landmark case crawler with Indian Kanoon scraper
- 🗂️ Section bookmarks and history
- 📱 Mobile app or web-based version
- 🎙️ Audio summary or chatbot assistant

---

## 📜 License

MIT License

---

## 🙏 Acknowledgments

- [Indian Kanoon](https://indiankanoon.org)
- Government of India legal datasets
- Python developers & open-source community

---

## 📸 Screenshots

*(You can insert GUI screenshots here with `![Screenshot](./assets/screenshot1.png)` if available)*

---

## 👤 Author

**Soumodip Sanyal**  
*Python Enthusiast | LegalTech Developer | GUI Designer*

Connect: [GitHub](https://github.com/) | [LinkedIn](https://linkedin.com/)
