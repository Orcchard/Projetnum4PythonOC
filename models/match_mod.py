class Match:
    def __init__(self, player1, player2, player1_score=0, player2_score=0):
        # Initialisation des joueurs et des scores
        self.player1 = player1  # Premier joueur
        self.player2 = player2  # Deuxième joueur
        self.player1_score = player1_score  # Score du premier joueur
        self.player2_score = player2_score  # Score du deuxième joueur
        # constitution  d'un tuple pour stocker les informations du match

    def match_dict(self):
        return {
            "player1": self.player1.player_id,
            "player2": self.player2.player_id,
            "player1_score": self.player1_score,
            "player2_score": self.player2_score
            }
