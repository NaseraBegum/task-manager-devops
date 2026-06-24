from flask import Flask, request

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    html = """
    <h1>Task Manager</h1>

    <form action="/add" method="post">
        <input type="text" name="task" placeholder="Enter task">
        <button type="submit">Add Task</button>
    </form>

    <h3>Tasks:</h3>
    <ul>
    """

    for task in tasks:
        html += f"<li>{task}</li>"

    html += "</ul>"

    return html


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task:
        tasks.append(task)

    return home()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
