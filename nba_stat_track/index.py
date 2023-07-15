import requests
from flask import Flask, jsonify
from nba_stat_track.models import SeasonDataSchema, Player, PlayerSchema


from marshmallow import ValidationError


from marshmallow import ValidationError

app = Flask(__name__)

def handle_validation_error(error):
    response = jsonify(error.messages)
    response.status_code = 400
    return response

@app.route('/player/<player_name>')
def get_player(player_name):
    response = requests.get(f"https://www.balldontlie.io/api/v1/players?search={player_name}")
    data = response.json()

    if 'data' in data and data['data']:
        player_id = data['data'][0]['id']
        season_averages_url = f'https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}'
        season_averages_response = requests.get(season_averages_url)

        if season_averages_response.status_code == 200:
            season_averages_data = season_averages_response.json()
            if season_averages_data['data']:
                player_data = {
                    'first_name': data['data'][0]['first_name'],
                    'last_name': data['data'][0]['last_name'],
                    'position': data['data'][0]['position'],
                    'team': data['data'][0]['team']['full_name'],
                    'season_data': []
                }
                for season_average in season_averages_data['data']:
                    season_data = {
                        'season': season_average['season'],
                        'games_played': season_average['games_played'],
                        'min': season_average['min'],
                        'fg_pct': season_average['fg_pct'],
                        'fg3_pct': season_average['fg3_pct'],
                        'ft_pct': season_average['ft_pct'],
                        'pts': season_average['pts']
                    }
                    player_data['season_data'].append(season_data)

                # Create a Player object
                player = Player(
                    first_name=data['data'][0]['first_name'],
                    last_name=data['data'][0]['last_name'],
                    position=data['data'][0]['position'],
                    team=data['data'][0]['team']['full_name'],
                    season_data=player_data['season_data']
                )

                # Serialize the Player object
                player_schema = PlayerSchema()
                serialized_player = player_schema.dump(player)

                return jsonify(serialized_player)

            else:
                return jsonify({"error": "No 2022 season average data available for this player."}), 404
        else:
            return jsonify({"error": "Error occurred while fetching season average data."}), 404

    return jsonify({"error": "No player found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
