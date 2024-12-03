from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    if task:
        tasks.append(task)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete_task():
    task = request.form["task"]
    if task in tasks:
        tasks.remove(task)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
