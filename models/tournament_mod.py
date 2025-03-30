class Tournament:
    """ Definition de la classe tournament"""
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
        """Sérialise le tournoi en dictionnaire"""
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
                        participant["Adversaires"]]
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
        # Optimisation: création d'un dictionnaire {player_id: Player}
        players_dict = {p.player_id: p for p in all_players}    
        """Reconstitution des participants"""
        tournament.participant_tournament = []
        for participant_data in tournament_data.get("participant_tournament", []):
            try:
                # Récupération du joueur principal
                player = players_dict[participant_data["player"]]            
                # Récupération des adversaires
                adversaires = [
                    players_dict[adv_id]
                    for adv_id in participant_data["adversaires"]
                ]
                # Ajout du participant avec son score et ses adversaires
                tournament.participant_tournament.append({
                    "Player": player,  # Objet Player
                    "Score": participant_data["score"],  # Désérialisation du score
                    "Adversaires": adversaires  # Liste d'objets Player
                })
            except KeyError as e:
                raise ValueError(f"Joueur ID {e.args[0]} introuvable.") from None
        # Vérifie le type avant de retourner
        print(f"Type de tournament recréé: {type(tournament)}")  
        return tournament
