import os
import sys
import json

#players_data_file = "data/players.json"
#tournaments_data_file = "data/tournaments.json"


class ViewTournament:
    
        

    @staticmethod
    def clear_screen():
        """Clear the display."""
        os.system("cls" if sys.platform == "win32" else "clear")

    @staticmethod
    def tournament_new_header():
        """Header before new tournament menu."""
        ViewTournament().clear_screen()
        print("\t**************************")
        print("\t* CREATION D'UN TOURNOI  *")
        print("\t************************\n")
        
    def prompt_for_new_tournament(self):
        """Collect data return as a dictionary."""
        print("Veuillez entrer les informations du tournois :")
        name = input("Nom tournois: ").capitalize()
        location = input("Lieu du tournois : ").capitalize()
        date_initial = input("Date de début du tournoi (format JJ/MM/AAAA) : ")
        date_end = input("Date de fin du tournoi (format JJ/MM/AAAA) : ")
        nb_round = input("Nombre de round : ")
        description = input("Description du tournoi : ")
        
        # Créer un dictionnaire contenant toutes les informations
        tournament_input_data = {
            "name": name,
            "location": location,
            "date_initial": date_initial,
            "date_end": date_end,
            "nb_round": nb_round,
            "description": description
        }
        return tournament_input_data
    