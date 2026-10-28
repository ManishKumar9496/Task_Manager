from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    items = ""

    for i, task in enumerate(tasks):
        items += f"<li>{task} <a href='/delete/{i}'>Delete</a></li>"

    return f"""
    <html>
    <head><title>My Task Manager</title></head>
    <body style="font-family:Arial; margin:50px">
        <h1>My Task Manager</h1>
        <form method="POST" action="/add">
            <input name="task" placeholder="Enter a task" required>
            <button type="submit">Add Task</button>
        </form>
        <h2>My Tasks</h2>
        <ul>{items}</ul>
    </body>
    </html>
    """

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task", "").strip()
    if task:
        tasks.append(task)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)	


# Task Manager - practicing Git branches
