from flask import Flask, request, render_template_string

app = Flask(__name__)

# Serve the HTML file
@app.route("/")
def home():
    return open("index.html").read()

# Handle the conversion
@app.route("/convert", methods=["POST"])
def convert():
    try:
        temperature = float(request.form["temperature"])
        unit = request.form["unit"]

        if unit == "c_to_f":
            converted = (temperature * 9/5) + 32
            result = f"{temperature}°C is equal to {converted:.2f}°F"
        elif unit == "f_to_c":
            converted = (temperature - 32) * 5/9
            result = f"{temperature}°F is equal to {converted:.2f}°C"
        else:
            result = "Invalid conversion type selected."

        return render_template_string(f"""
            <h1>Temperature Converter</h1>
            <p>{result}</p>
            <a href="/">Back to Converter</a>
        """)
    except ValueError:
        return "Invalid temperature input!"

if __name__ == "__main__":
    app.run(debug=True)
