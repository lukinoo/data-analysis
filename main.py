from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
from flask_cors import CORS, cross_origin

# import utils
from utils.handle_key_values import handle_key_values
from utils.uuid import get_a_uuid


app = Flask(__name__)

CORS(app)

API_URL = "https://www.scrapethissite.com/pages/forms/?per_page=100"


@app.route('/scrape-hockey')
def scrape_hockey():
    response = requests.get(API_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    teams = soup.find_all('tr', class_='team')

    hockey_data = []

    for team in teams:
        team_info = {
            "_id": get_a_uuid(),
            "name": handle_key_values(team, "td", "name"),
            "year": handle_key_values(team, "td", "year"),
            "wins": handle_key_values(team, "td", "wins"),
            "losses": handle_key_values(team, "td", "losses"),
            "gf": handle_key_values(team, "td", "gf"),
            "ga": handle_key_values(team, "td", "ga")
        }

        hockey_data.append(team_info)

    return jsonify(hockey_data)


if __name__ == '__main__':
    app.run(debug=True)
