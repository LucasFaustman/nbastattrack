import requests
from tabulate import tabulate

player_name = input("Enter the name of the player you want 2022 season averages for: ")
query_url = f'https://www.balldontlie.io/api/v1/players?search={player_name}'

response = requests.get(query_url)

if response.status_code == 200:
    data = response.json()
    if data['data']:
        player_id = data['data'][0]['id']
        season_averages_url = f'https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}'
        season_averages_response = requests.get(season_averages_url)
        
        if season_averages_response.status_code == 200:
            season_averages_data = season_averages_response.json()
            if season_averages_data['data']:
                player_stats = []
                for season_average in season_averages_data['data']:
                    player_stats.append([
                        data['data'][0]['first_name'],
                        data['data'][0]['last_name'],
                        data['data'][0]['position'],
                        data['data'][0]['team']['full_name'],
                        season_average['season'],
                        season_average['games_played'],
                        season_average['min'],
                        season_average['fg_pct'],
                        season_average['fg3_pct'],
                        season_average['ft_pct'],
                        season_average['pts']
                    ])
                
                headers = ["First Name", "Last Name", "Position", "Team", "Season", "Games Played", "Minutes", "FG%", "3P%", "FT%", "PTS"]
                print(tabulate(player_stats, headers=headers, tablefmt="grid"))
            else:
                print("No 2022 season average data available for the player.")
        else:
            print("Error occurred while fetching season average data.")
    else:
        print("Player not found.")
else:
    print("Error occurred while fetching player data. Please try again.")
