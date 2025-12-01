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
            raise ValueError("Invalid player")

    def get_player1_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        if 0 <= self.player1_score < 4:
            return score_names[self.player1_score]
                
                
    def get_player2_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        if 0 <= self.player2_score < 4:
            return score_names[self.player2_score]
                
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
            player1_score = self.get_player1_score()
            player2_score = self.get_player2_score()
            score = player1_score + "-" + player2_score


        return score

