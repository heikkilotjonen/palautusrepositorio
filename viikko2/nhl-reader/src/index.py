"""NHL player statistics reader and formatter.

This module provides functionality to fetch and display NHL player statistics
by nationality and season using the NHL stats API.
"""

import requests
from rich.console import Console
from rich.table import Table
from player import Player


class PlayerReader:
    """A class to read player data from NHL stats API."""

    def __init__(self, url):
        """Initialize PlayerReader with API URL.

        Args:
            url (str): The NHL stats API URL
        """
        self.url = url

    def get_players(self):
        """Fetch and parse player data from the API.

        Returns:
            list: List of Player objects
        """
        response = requests.get(self.url, timeout=10).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:
    """A class to analyze and filter player statistics."""

    def __init__(self, player_reader):
        """Initialize PlayerStats with a player reader.

        Args:
            player_reader (PlayerReader): The reader to fetch player data
        """
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        """Get top scorers filtered by nationality.

        Args:
            nationality (str): The nationality to filter by

        Returns:
            list: List of players sorted by points (goals + assists)
        """
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
    if not players:
        print(f"No players from {country} found in season {season}.")
        return

    table = Table(title=f"Season {season} players from {country}", show_header=True)
    for col in [("Name", "cyan", True), ("Teams", "magenta", False),
                ("Goals", "right", False), ("Assists", "right", False), ("Points", "right", False)]:
        table.add_column(col[0], style=col[1], no_wrap=col[2] if len(col) > 2 else False)

    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.goals + p.assists))

    Console().print(table)

def main():
    season = choose_season()
    country = choose_country()
    players = get_players(country, season)
    print_table(players, season, country)


if __name__ == "__main__":
    main()
