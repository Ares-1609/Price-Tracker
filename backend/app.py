from flask import Flask, request, jsonify
from flask_cors import CORS 
from scraper import get_price
from emailer import send_email

app = Flask(__name__)
CORS(app)      

@app.route("/track", methods=["POST"])
def track():
    data = request.get_json()
    name = data["name"]
    url = data["url"]
    target = int(data["target_price"])
    email = data["email"]

    price = get_price(url)
    if price and price <= target:
        send_email(name, url, price, email)
        return jsonify({"message": f"✅ Deal found! Email sent to {email}"})
    elif price:
        return jsonify({"message": f"ℹ️ Current price is ₹{price}. No deal yet."})
    else:
        return jsonify({"message": "❌ Failed to fetch price. Check URL."})

if __name__ == "__main__":
    app.run(debug=True)
