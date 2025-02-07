from datetime import datetime, timedelta


class Round:
    def __init__(
        self, round_number, round_name,
        start_time=None, end_time=None
    ):
        """Initialisation d'un round"""
        self.round_number = round_number
        self.round_name = round_name
        self.start_time = datetime.now()
        self.end_time = (self.start_time + timedelta(hours=4))
        self.matches = []

    def __str__(self):
        """Retourner une représentation lisible de l'objet Round"""
        return (
            f"Round({self.round_number} - {self.round_name}) - "
            f"{self.start_time} - {self.end_time} - {len(self.matches)} matchs"
            )

    def round_dict(self):
        return {
            "round_number": self.round_number,
            "round_name": self.round_name,
            "matches": [match.match_dict() for match in self.matches]
        }
