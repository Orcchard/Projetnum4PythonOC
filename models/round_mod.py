"""Initialisation d'un round"""


class Round:
    def __init__(
        self, round_number, round_name,
        start_time=None, end_time=None
    ):
        self.round_number = round_number
        self.round_name = round_name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = []

    def __str__(self):
        """Retourne une représentation lisible de l'objet Round"""
        return (
            f"Round({self.round_number} - {self.round_name}) - "
            f"{self.start_time} - {self.end_time} - {len(self.matches)} matchs"
        )

    def round_dict(self):
        """Sérialise le round en dictionnaire"""
        return {
            "round_number": self.round_number,
            "round_name": self.round_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.match_dict() for match in self.matches]
        }

    @staticmethod
    def recreate_round(round_data, all_players):
        """Reconstitue un round à partir des données sérialisées"""
        new_round = Round(
            round_number=round_data["round_number"],
            round_name=round_data["round_name"],
            start_time=round_data["start_time"],
            end_time=round_data["end_time"]
        )
        return new_round
