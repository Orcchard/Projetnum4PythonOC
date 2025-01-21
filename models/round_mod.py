from datetime import datetime, timedelta
from models.match_mod import Match
#from player_mod import Player
class Round:
    def __init__(self, round_number, round_name, start_time=None, end_time=None):
        # Initialisation d'un round avec le numéro, le nom, et les dates de début et de fin
        self.round_number = round_number  # Numéro du round
        self.round_name = round_name  # Nom du round (ex: "Premier round", "Finale", etc.)
        self.start_time = datetime.now()  # Date et heure de début définies automatiquement
        self.end_time = (self.start_time + timedelta(hours=4))# 4 heures plus tard)
        self.matches = []  # Liste des matchs (chaque match est une liste de 2 joueurs)
        

    def __str__(self):
        # Retourner une représentation lisible de l'objet Round
        return f"Round {self.round_number} - {self.round_name} - {self.start_time} - {self.end_time} {len(self.matches)} matchs"
        
    def round_dict(self):
        return {
            "round_number": self.round_number,
            "round_name": self.round_name,
            "matches": [match.match_dict() for match in self.matches],
        }