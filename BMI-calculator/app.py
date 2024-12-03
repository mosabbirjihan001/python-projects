from flask import Flask, request, render_template_string

app = Flask(__name__)

# Serve the HTML file
@app.route("/")
def home():
    return open("index.html").read()

# Handle BMI calculation
@app.route("/calculate", methods=["POST"])
def calculate_bmi():
    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Classify BMI
        if bmi < 18.5:
            classification = "Underweight"
        elif 18.5 <= bmi < 24.9:
            classification = "Normal weight"
        elif 25 <= bmi < 29.9:
            classification = "Overweight"
        else:
            classification = "Obese"

        result = f"Your BMI is {bmi:.2f}. Classification: {classification}"

        return render_template_string(f"""
            <h1>BMI Calculator</h1>
            <p>{result}</p>
            <a href="/">Back to Calculator</a>
        """)
    except ValueError:
        return "Invalid input. Please enter numbers for weight and height."

if __name__ == "__main__":
    app.run(debug=True)
