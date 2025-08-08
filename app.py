from flask import Flask, jsonify, request
from scraping import scrape_mobile_legends, scrape_free_fire, scrape_pubg
from utils import merge_results

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Game Recharge Price API Running"})

@app.route("/prices", methods=["GET"])
def get_prices():
    game = request.args.get("game", "").lower()

    if game == "mobile_legends":
        data = scrape_mobile_legends()
    elif game == "free_fire":
        data = scrape_free_fire()
    elif game == "pubg":
        data = scrape_pubg()
    else:
        return jsonify({"error": "Game not supported"}), 400

    return jsonify(data)

@app.route("/all", methods=["GET"])
def get_all_prices():
    data = merge_results(
        scrape_mobile_legends(),
        scrape_free_fire(),
        scrape_pubg()
    )
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
