# 📘 Personal Law Assistant

A Python-based legal reference desktop application that allows users to search and view Indian laws offline with a modern GUI, export sections to PDF, and fetch case summaries from Indian Kanoon.

---

## 🖼️ Screenshot

![Personal Law Assistant Screenshot](./📘%20Personal%20Law%20Assistant%2017_06_2025%204_50_23%20AM.png)

---

## 💡 Features

- Search sections from IPC, CrPC, and the Constitution
- Export results as a PDF
- View landmark cases via Indian Kanoon
- Read aloud functionality
- Offline access to all datasets

---

## 📁 Project Structure

/PersonalLawAssistant/
│
├── main.py
├── search.py
├── pdf_export.py
├── indian_kanoon.py
├── utils.py
├── data/
│ ├── ipc.json
│ ├── crpc.json
│ └── constitution.json
└── requirements.txt

yaml
Copy
Edit

---

> 📸 If you're uploading to GitHub, make sure the image is saved in the same directory as your README file or update the path accordingly.

Let me know if you’d like a full `README.md` file generated!







You said:
give me complete readme


ChatGPT said:
Sure! Below is a complete and professional README.md file for your Personal Law Assistant project, including the screenshot, project description, features, setup instructions, usage, and contribution notes.

markdown
Copy
Edit
# ⚖️ Personal Law Assistant

**Personal Law Assistant** is a fully offline desktop application built in Python that enables users to search through and explore major Indian laws like the Constitution of India, Indian Penal Code (IPC), and Criminal Procedure Code (CrPC). It also integrates Indian Kanoon web results and provides PDF export and text-to-speech functionalities — all in a dynamic, modern GUI.

---

## 🖼️ Screenshot

![Personal Law Assistant Screenshot](./📘%20Personal%20Law%20Assistant%2017_06_2025%204_50_23%20AM.png)

---

## ✨ Features

- ✅ Offline search for **IPC**, **CrPC**, and **Indian Constitution**  
- ✅ Smart **section-based** and **keyword-based** search  
- ✅ View results in a clean, readable GUI  
- ✅ Export results as **PDF**  
- ✅ Integrate with **Indian Kanoon** to fetch landmark case summaries  
- ✅ **Text-to-speech** feature for reading law aloud  
- ✅ Sleek dark theme GUI using `ttkbootstrap`

---

## 🛠️ Built With

- 🐍 **Python 3.10+**
- 🖼️ `tkinter` & `ttkbootstrap` — for building the GUI
- 📁 `json` — for storing legal data locally
- 📄 `fpdf` — for PDF export
- 🌐 `webbrowser` — for Indian Kanoon integration
- 🔊 `pyttsx3` — for Text-to-Speech

---

## 📁 Folder Structure

/PersonalLawAssistant/
│
├── main.py # GUI application entry point
├── search.py # Contains section and keyword search logic
├── pdf_export.py # Code to export content as PDF
├── indian_kanoon.py # Indian Kanoon web integration
├── utils.py # Optional utilities and text formatting
├── requirements.txt # Python package dependencies
├── data/
│ ├── ipc.json # IPC Sections
│ ├── crpc.json # CrPC Sections
│ └── constitution.json # Constitution Articles
└── README.md

yaml
Copy
Edit

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/PersonalLawAssistant.git
cd PersonalLawAssistant
2. Create virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate.bat     # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
📂 Requirements
ini
Copy
Edit
ttkbootstrap==1.10.1
fpdf==1.7.2
pyttsx3==2.90
🚀 Usage
Run the application
bash
Copy
Edit
python main.py
Functionalities
Select law type from dropdown (ipc, crpc, constitution)

Enter section number or keyword

Click 🔍 Search to view results

Click 🖨 Export PDF to save the displayed result as a PDF

Click 📜 Indian Kanoon to fetch related online cases

Click 🗣 Read Aloud to enable Text-to-Speech

📘 Datasets Used
All JSON datasets were manually created from publicly available government resources.

Datasets include:

All sections of IPC and CrPC

Full Constitution of India with articles and schedules

🧪 Future Improvements
 Add voice search via speech_recognition

 Add bookmark/save feature for sections and cases

 Add multi-language support (Hindi, Bengali, etc.)

 Connect to a remote server for real-time law updates

🤝 Contribution
Have suggestions or want to contribute?

Fork this repository

Create your feature branch (git checkout -b feature/NewFeature)

Commit your changes (git commit -m 'Add NewFeature')

Push to the branch (git push origin feature/NewFeature)

Open a Pull Request

📜 License
This project is open-source and free to use under the MIT License.

👨‍💻 Author
Soumodip Sanyal
Crafted with ❤️ and justice for the Indian legal tech community.
