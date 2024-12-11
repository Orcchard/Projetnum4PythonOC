import datetime
import random
from player_mod import Player


class Match:
    def __init__(self, player1, player2, player1_score=0, player2_score=0):
        # Initialisation des joueurs et des scores
        self.player1 = player1  # Premier joueur
        self.player2 = player2  # Deuxième joueur
        self.player1_score = player1_score  # Score du premier joueur
        self.player2_score = player2_score  # Score du deuxième joueur
                # constitution  d'un tuple pour stocker les informations du match
        self.match_tuple = ([self.player1, self.player1_score], [self.player2, self.player2_score])
    
    def display_match(self):
        # Affiche les binomes
        # return f"{self.player1.first_name} {self.player1.name} (ID: {self.player1.player_id}) VS {self.player2.first_name} {self.player2.name} (ID: {self.player2.player_id})"
        pass
    def enter_scores(self):
        #Affiche le match
        # print(self.display_match())
        # Mise à jour des scores via la méthode enter_scores
        pass


