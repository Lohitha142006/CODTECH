from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {
        "id": 1,
        "title": "Python Basics",
        "content": "Learn variables, loops, functions",
        "topics": [
            {"name": "Variables", "link": "https://www.w3schools.com/python/python_variables.asp"},
            {"name": "Loops", "link": "https://www.w3schools.com/python/python_for_loops.asp"},
            {"name": "functions", "link": "https://www.w3schools.com/python/python_functions.asp"}
        ]
    },
    {
        "id": 2,
        "title": "Web Development",
        "content": "HTML, CSS, JavaScript basics",
        "topics": [
            {"name": "HTML", "link": "https://www.w3schools.com/html/"},
            {"name": "CSS", "link": "https://www.w3schools.com/css/"},
            {"name": "JAVASCRIPT", "link": "https://www.w3schools.com/javascript/"}
        ]
    },
    {
        "id": 3,
        "title": "Data Structures",
        "content": "Arrays, stacks, queues",
        "topics": [
           {"name": "Arrays", "link": "https://www.geeksforgeeks.org/introduction-to-arrays/"},
            {"name": "Stacks", "link": "https://www.geeksforgeeks.org/stack-data-structure/"},
            {"name": "Queues", "link": "https://www.geeksforgeeks.org/queue-data-structure/"}
        ]
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def course_list():
    return render_template("courses.html", courses=courses)

@app.route("/course/<int:id>")
def course_detail(id):
    course = None
    for c in courses:
        if c["id"] == id:
            course = c
    return render_template("course_detail.html", course=course)

if __name__ == "__main__":
    app.run(debug=True)

    
