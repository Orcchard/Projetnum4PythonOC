import random
from player_mod import Player
from match_mod import Match
from round_mod import Round


class Tournament:
    def __init__(self, name, location, date_initial, date_end, nb_round=4, description=""):
        """
        Initialise un tournois avec ses details et une liste vide de joueurs.
        """
        self.name = name
        self.location = location
        self.date_initial = date_initial
        self.date_end = date_end
        self.nb_round = nb_round
        self.description = description
        self.participant_tournois = []  # Liste pour stocker les 8 joueurs ajoutes au tournois
        self.adversaires = [] # quels sont les adversaires que le joueur a rencontré pendant un tournois.
        self.rounds = [] # 1 round contient 4 matches
        
    def __str__(self):
        """
        Renvoie une representation textuelle du tournois.
        """
        
        return (f"Tournois: {self.name}, Lieu: {self.location}, "
                f"Debut: {self.date_initial}, Fin: {self.date_end}, "
                f"Description: {self.description}")
        
        
    def tournament_dict(self):
        return {
            "name":self.name,
            "location" :self.location,
            "date_initial":self.date_initial,
            "date_end":self.date_end, 
            "nb_round":self.nb_round,
            "description":self.description,
            "participant_tournois":[
                {"player":participant["Player"].player_id,
                 "score":participant["Score"],
                 "adversaires":[adversary.player_id for adversary in participant["Adversaires"]]
                    
                }
                for participant in self.participant_tournois
            ],
            "rounds": [round.round_dict() for round in self.rounds],
            
                }
            
            
            
            
        