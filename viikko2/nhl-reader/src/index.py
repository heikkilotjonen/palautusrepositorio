import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader
    
    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()
        players = [p for p in players if p.nationality == nationality]
        players.sort(key=lambda p: p.goals + p.assists, reverse=True)  
        return players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()