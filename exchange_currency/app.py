from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Set up the API URL and your API key
API_KEY = " 4778c323062ca9538527adb5" 
API_URL = "https://v6.exchangerate-api.com/v6/{}/latest/USD".format(API_KEY)

def get_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data['conversion_rates']

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    converted_amount = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            
            # Fetch conversion rates from the API
            rates = get_exchange_rates()
            if from_currency != 'USD':
                amount_in_usd = amount / rates[from_currency]
            else:
                amount_in_usd = amount

            converted_amount = amount_in_usd * rates[to_currency]

            message = f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}."
        except ValueError:
            message = "Please enter a valid amount."
    return render_template('index.html', message=message, converted_amount=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)
