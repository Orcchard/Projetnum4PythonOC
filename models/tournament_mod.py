class Tournament:
    def __init__(
        self, name, location, date_initial,
        date_end, nb_round=4, description=""
    ):
        """
        Initialise un tournoi avec ses details et une liste vide de joueurs.
        """
        self.name = name
        self.location = location
        self.date_initial = date_initial
        self.date_end = date_end
        self.nb_round = nb_round
        self.description = description
        self.participant_tournament = []
        self.adversaires = []
        self.rounds = []

    def __str__(self):
        """Renvoie une representation textuelle du tournoi."""
        return (f"Tournoi: {self.name}, Lieu: {self.location}, "
                f"Debut: {self.date_initial}, Fin: {self.date_end}, "
                f"Description: {self.description}")

    def tournament_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "date_initial": self.date_initial,
            "date_end": self.date_end,
            "nb_round": self.nb_round,
            "description": self.description,
            "participant_tournament": [
                {
                    "player": participant["Player"].player_id,
                    "score": participant["Score"],
                    "adversaires": [
                        adversary.player_id for adversary in
                        participant["Adversaires"]
                    ],
                }
                for participant in self.participant_tournament
            ],
            "rounds": [round.round_dict() for round in self.rounds]
        }

    @staticmethod
    def recreate_tournament(tournament_data, all_players):
        """Reconstitution du tournois"""
        tournament = Tournament(
            name=tournament_data["name"],
            location=tournament_data["location"],
            date_initial=tournament_data["date_initial"],
            date_end=tournament_data["date_end"],
            nb_round=tournament_data["nb_round"],
            description=tournament_data["description"]
        )
        """Reconstitution des participants"""
        tournament.participant_tournament = [
            {
                "Player": next(
                    (player for player in all_players
                        if player.player_id == participant["player"]), None),
                "Score": participant["score"],
                "Adversaires": [
                    next(
                        (player for player in all_players if
                            player.player_id == adv_id), None
                    ) for adv_id in participant["adversaires"]
                ]
            }
            for participant in tournament_data.get(
                "participant_tournament", []
                )
        ]
        return tournament
