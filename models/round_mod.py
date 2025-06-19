"""Module de gestion des rounds de tournoi d'échecs.
Ce module définit la classe Round qui représente une étape d'un tournoi,
contenant plusieurs matchs entre joueurs avec gestion des horaires.
"""


class Round:
    """Représente un round dans un tournoi d'échecs, contenant plusieurs matchs.

    Attributes:
        round_number (int): Numéro séquentiel du round dans le tournoi.
        round_name (str): Nom du round (ex: "Round 1", "Finale").
        start_time (date): Date et heure de début.
        end_time (date): Date et heure de fin.
        matches (date): Liste des matchs du round.
    """

    def __init__(
        self, round_number, round_name,
        start_time=None, end_time=None
    ):
        """Initialise un round de tournoi"""
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

    def add_match(self, match):
        """Ajoute un match à la liste des matchs du round."""
        self.matches.append(match)
