# PyKnowledgeDesk

PyKnowledgeDesk is a Python GUI-based desktop application built with Tkinter that works as a mini offline knowledge library.  
Users can search programming topics, read explanations, and listen to them using text-to-speech.

---

## 🚀 Features

- 🔍 Search topics from a JSON-based knowledge database
- 🖥️ Clean and simple Tkinter graphical interface
- 🔊 Text-to-speech support using `pyttsx3`
- 📁 Offline usage (no internet required)
- 🧠 Beginner-friendly educational tool

---

## 🛠️ Requirements

- Python 3.8+
- Modules:
  - `tkinter` (built-in with Python)
  - `json` (built-in)
  - `pyttsx3`

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/samglobalsolutionsofficial-del/PyKnowledgeDesk.git
Navigate to the project folder:

bash
Copy code
cd PyKnowledgeDesk
Install required dependencies:

bash
Copy code
pip install pyttsx3
▶️ Usage
Run the application using:

bash
Copy code
python app/main.py
How it works:
Enter a topic name in the input field

Click Search to view the explanation

Click Play Audio to hear the explanation

Results are loaded from data/data.json

📁 Project Structure
css
Copy code
PyKnowledgeDesk/
├── app/
│   ├── main.py
│   └── icon/
│       └── library_ico.png
├── data/
│   └── data.json
├── README.md
├── requirements.txt
└── .gitignore
🔮 Future Improvements
Add more programming topics

Improve UI design

Add category-based search

Export explanations as text or audio

Package as a standalone executable

👨‍💻 Author
Sameer Khan
GitHub: https://github.com/samglobalsolutionsofficial-del

📄 License
This project is open-source and available under the MIT License.

yaml
Copy code

---

# 🧪 STEP 5: Commit README to GitHub

After saving the file:

```bash
git add README.md
git commit -m "Add professional README for PyKnowledgeDesk"
git push