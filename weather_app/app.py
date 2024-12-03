from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your OpenWeatherMap API Key
API_KEY = "your_openweathermap_api_key"  # Replace with your API key

@app.route("/")
def home():
    return render_template("index.html", weather=None)

@app.route("/weather", methods=["POST"])
def get_weather():
    city = request.form["city"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"],
        }
        return render_template("index.html", weather=weather)
    else:
        return render_template("index.html", weather={"city": city, "temp": "N/A", "condition": "City not found", "humidity": "N/A"})

if __name__ == "__main__":
    app.run(debug=True)
