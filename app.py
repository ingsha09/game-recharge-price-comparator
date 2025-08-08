from flask import Flask, jsonify, request
from scraping import (
    scrape_mobile_legends_codashop,
    scrape_free_fire_seagm,
    scrape_pubg_uc_seagm
)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Game Recharge Price API Live"})

@app.route("/prices", methods=["GET"])
def get_prices():
    game = request.args.get("game", "").lower()
    if game == "mobile_legends":
        return jsonify(scrape_mobile_legends_codashop())
    elif game == "free_fire":
        return jsonify(scrape_free_fire_seagm())
    elif game == "pubg_mobile":
        return jsonify(scrape_pubg_uc_seagm())
    else:
        return jsonify({"error": "Game not supported"}), 400

@app.route("/all", methods=["GET"])
def get_all():
    data = []
    data += scrape_mobile_legends_codashop()
    data += scrape_free_fire_seagm()
    data += scrape_pubg_uc_seagm()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
