import requests
from player import Player
from rich.console import Console
from rich.table import Table
import rich


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

def choose_country():
    countries = ["FIN", "SWE", "CAN", "USA", "CZE", "RUS",
                 "SLO", "FRA", "GBR", "SVK", "DEN", "NED",
                 "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]
    while True:
        country = str(input("Nationality [[USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]] "))
        if country not in countries:
            print("not a valid country")
        else:
            return country

def choose_season():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"]
    while True:
        season = str(input("Season [2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26] "))
        if season not in seasons:
            print("not a valid season")
        else:
            return season

def get_players(country, season):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality(country)

def print_table(players, season, country):
    if len(players) == 0:
        print(f"No players from {country} found in season {season}.")
        return
    
    console = Console()
    table = Table(title=f"Season {season} players from {country}")

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")
    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists)
        )
    console.print(table)

def main():
    season = choose_season()
    country = choose_country()
    players = get_players(country, season)
    print_table(players, season, country)


if __name__ == "__main__":
    main()