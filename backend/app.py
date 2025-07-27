from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_price
from emailer import send_email

app = Flask(__name__)
CORS(app)

@app.route("/track", methods=["POST"])
def track():
    try:
        data = request.get_json()
        name = data["name"]
        url = data["url"]
        target = int(data["target_price"])
        email = data["email"]

        result = get_price(url)

        if not result:
            return jsonify({"message": "❌ Failed to fetch price. Check URL."})

        price = result["price"]
        title = result["title"]
        image = result["image"]

        if price is not None:
            if price <= target:
                send_email(name, url, price, email)
                return jsonify({
                    "message": f"✅ Deal found! Email sent to {email}",
                    "title": title,
                    "image": image,
                    "price": price
                })
            else:
                return jsonify({
                    "message": f"ℹ️ Current price is ₹{price}. No deal yet.",
                    "title": title,
                    "image": image,
                    "price": price
                })
        else:
            return jsonify({"message": "❌ Could not extract price."})

    except Exception as e:
        print("Server error:", e)
        return jsonify({"message": "❌ Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
