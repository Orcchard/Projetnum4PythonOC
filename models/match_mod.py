"""
Module de gestion des matchs d'échecs.
Ce module définit la classe Match qui représente un affrontement entre deux joueurs
dans le cadre d'un tournoi, avec le score et les méthodes de sérialisation associées.
"""


class Match:
    """
    Représente un match entre deux joueurs dans un tournoi d'échecs
        Attributes:
            player1 (Player): Premier joueur du match.
            player2 (Player): Deuxième joueur du match.
            player1_score : Score du premier joueur (0, 0.5 ou 1).
            player2_score : Score du deuxième joueur (0, 0.5 ou 1).
            """

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

    @staticmethod
    def already_played(player1, player2, rounds):
        """Vérifie si deux joueurs se sont déjà affrontés dans les rounds précédents."""
        pair = tuple(sorted((player1.player_id, player2.player_id)))
        return any(
            pair == tuple(sorted((match.player1.player_id, match.player2.player_id)))
            for rnd in rounds
            for match in rnd.matches
        )
