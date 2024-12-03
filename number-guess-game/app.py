from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Generate a random number at the start
target_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def guess():
    global target_number
    message = ""
    
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            if guess < target_number:
                message = "Too low! Try again."
            elif guess > target_number:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You've guessed the number {target_number}."
                target_number = random.randint(1, 100)  # Reset the number after guessing correctly
        except ValueError:
            message = "Please enter a valid number."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
