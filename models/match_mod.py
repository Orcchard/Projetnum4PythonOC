class Match:
    """Définition de la classe tournament"""
    def __init__(self, player1, player2, player1_score=0, player2_score=0):
        """Initialisation des joueurs et des scores"""
        self.player1 = player1
        self.player2 = player2
        self.player1_score = player1_score
        self.player2_score = player2_score

    def match_dict(self):
        """retourne les données sous forme de dictionnaire"""
        return {
            "player1": self.player1.player_id,
            "player2": self.player2.player_id,
            "player1_score": self.player1_score,
            "player2_score": self.player2_score
            }

    @staticmethod
    def recreate_match(match_data, all_players):
        """Recrée un objet Match à partir d'un dictionnaire"""
        player1 = next(
            (
                player for player in all_players
                if player.player_id == match_data["player1"]
                ), None
        )
        player2 = next(
            (
                player for player in all_players
                if player.player_id == match_data["player2"]
                ), None
        )
        if player1 is None or player2 is None:
            raise ValueError(
                "Un ou plusieurs joueurs du match sont introuvables."
                )
        return Match(
            player1=player1,
            player2=player2,
            player1_score=match_data["player1_score"],
            player2_score=match_data["player2_score"],
        )
