from flask import Flask, render_template, request, jsonify
from db_config import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    response = generate_response(user_input)
    return jsonify({"response": response})

def generate_response(user_input):
    conn = get_db_connection()
    cursor = conn.cursor()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 I'm Ravi Singh’s AI Portfolio Assistant. You can ask about my projects, skills, or GitHub."

    elif "skills" in user_input:
        return """
        <b>Technical Skills:</b><br>
        Languages: Java, Python, C++, JavaScript (ES6+)<br>
        Web & Application: HTML, CSS, React.js, RESTful APIs<br>
        Databases: MySQL, MongoDB<br>
        Data & Analytics: NumPy, Pandas, Matplotlib, Seaborn, Tableau, Excel, RStudio<br>
        Version Control: Git/GitHub<br>
        Soft Skills: Problem-Solving, Team Player, Leadership, Adaptability, Agile Collaboration
        """

    elif "github" in user_input:
        cursor.execute("SELECT title, github_link FROM projects")
        data = cursor.fetchall()
        if data:
            response = "Here are my GitHub projects:<br>"
            for d in data:
                response += f"• <b>{d['title']}</b>: <a href='{d['github_link']}' target='_blank'>{d['github_link']}</a><br>"
            return response
        else:
            return "I don’t have GitHub projects listed yet."

    elif "project" in user_input or "work" in user_input:
        cursor.execute("SELECT title, description, tech_stack FROM projects")
        projects = cursor.fetchall()
        if projects:
            response = "Here are some of my key projects:<br><br>"
            for p in projects:
                response += f"<b>{p['title']}</b><br>{p['description']}<br><i>Tech Used:</i> {p['tech_stack']}<br><br>"
            return response
        else:
            return "I don't have any projects listed right now."

    else:
        return "I'm not sure about that. Try asking about my 'skills', 'projects', or 'GitHub'."

if __name__ == "__main__":
    app.run(debug=True)
