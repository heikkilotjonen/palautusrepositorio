class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        elif player_name == self.player2_name:
            self.player2_score = self.player2_score + 1
        else:
            print("Invalid player")

    def get_player1_score(self):
        for i in range(0, 4):
            if i == self.player1_score:
                if i == 0:
                    return "Love"
                elif i == 1:
                    return "Fifteen"
                elif i == 2:
                    return "Thirty"
                elif i == 3:
                    return "Forty"
                
                
    def get_player2_score(self):
        for i in range(0, 4):
            if i == self.player2_score:
                if i == 0:
                    return "Love"
                if i == 1:
                    return "Fifteen"
                elif i == 2:
                    return "Thirty"
                elif i == 3:
                    return "Forty"
                
    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                score = "Love-All"
            elif self.player1_score == 1:
                score = "Fifteen-All"
            elif self.player1_score == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score_difference = self.player1_score - self.player2_score

            if score_difference == 1:
                score = f"Advantage {self.player1_name}"
            elif score_difference == -1:
                score = f"Advantage {self.player2_name}"
            elif score_difference >= 2:
                score = f"Win for {self.player1_name}"
            else:
                score = f"Win for {self.player2_name}"

        else:
            player_1_score = self.get_player1_score()
            player_2_score = self.get_player2_score()
            score = player_1_score +"-"+ player_2_score


        return score

