from datetime import datetime, timedelta
from match_mod import Match
class Round:
    def __init__(self, round_number, round_name):
        # Initialisation d'un round avec le numéro, le nom, et les dates de début et de fin
        self.round_number = round_number  # Numéro du round
        self.round_name = round_name  # Nom du round (ex: "Premier round", "Finale", etc.)
        self.start_time = datetime.now() - timedelta(hours=2)  # Date et heure de début définies automatiquement
        self.end_time = datetime.now()  # Date et heure de fin (à définir plus tard)
        self.matches = []  # Liste des matchs (chaque match est une liste de 2 joueurs)

    def __str__(self):
        # Retourner une représentation lisible de l'objet Round
        return f"Round {self.round_number} - {self.round_name} - {len(self.matches)} matchs"
        
    