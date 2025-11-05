class Player:
    def __init__(self, data):
        self.name = data['name']

        self.nationality = data['nationality']

        self.assists = data['assists']

        self.goals = data['goals']

        self.team = data['team']

        self.games = data['games']

    def __str__(self):
        return self.name + "  " + self.team + "  " + str(self.goals) + " + " + str(self.assists) + " = " + str(self.goals + self.assists)
