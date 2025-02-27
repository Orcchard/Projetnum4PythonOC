from datetime import datetime, timedelta


class Round:
    def __init__(
        self, round_number, round_name,
        start_time=None, end_time=None
    ):
        """Initialisation d'un round"""
        self.round_number = round_number
        self.round_name = round_name
        self.start_time = start_time
        self.end_time = end_time
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
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.match_dict() for match in self.matches]
        }

    def recreate_round(round_data, all_players):
        return Round(
            round_number=round_data["round_number"],
            round_name=round_data["round_name"],
            start_time=round_data["start_time"],
            end_time=round_data["end_time"],
        )
        """Reconstituer les matches"""
        matches = [
            recreate_match(match_data, all_players)
            for match_data in round_data["matches"]
            ]
        matches = matches

    def add_match(self, match):
        """Ajouter un match au round"""
        self.matches.append(match)
