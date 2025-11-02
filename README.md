# 🤖 AI Portfolio | Ravi Singh

An **AI-powered interactive portfolio** built using **Flask, MySQL, HTML, CSS, and JavaScript** — allowing users to ask natural language questions like *“Show me Ravi’s projects”* or *“Tell me about the Car Rental System”*.  
The AI dynamically filters and displays relevant details from the portfolio database.

---

## 🌟 Features

- 💬 **Interactive Chat UI** — users can ask queries about projects, skills, or GitHub links.  
- 🧠 **Intelligent Filtering** — backend matches keywords from prompts to show correct info.  
- 🗄️ **Dynamic Database** — project data stored and fetched from MySQL.  
- ⚡ **Real-Time Response** — instant communication between Flask and frontend.  
- 🎨 **Minimal UI Design** — responsive and easy to navigate.

---

## 🧰 Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask) |
| **Database** | MySQL |
| **Version Control** | Git / GitHub |
| **IDE** | Visual Studio Code |

---

## 🧱 Project Structure

AI_Portfolio/
│
├── app.py # Main Flask application
├── db_config.py # MySQL connection setup
├── requirements.txt # Dependencies
│
├── templates/
│ └── index.html # Frontend HTML
│
├── static/
│ ├── style.css # Styling
│ └── script.js # Frontend logic (chat functionality)
│
└── database/
└── portfolio.sql # Project data for MySQL
