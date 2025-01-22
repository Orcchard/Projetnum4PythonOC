import os
from os import path
import json
import sys
class View:
    
    
    @staticmethod
    def clear_screen():
        """Clear the display."""
        os.system("cls" if sys.platform == "win32" else "clear")
    
    def main_header(self):
        #Header before the main menu
        #self.clear_screen()
        print("\t**********************************************")
        print("\t* Bienvenue dans le gestionnaire de tournoi  *")
        print("\t********************************************\n")
        
    
    def menu(self):
        #Display the main menu with some data info
        #num_of_players = self.number_of_player()
        print("\nMENU PRINCIPAL")
        print("1. Créer un joueur")
        print("2. Créer un tournoi")
        print("3. Editer un rapport")
        print("4. Supprimer un joueur ")
        print("\n5. Quitter le programme")
        print()
    #si option 2 faire appel au controlleur qui fera appel a la vue player_input_tournois etc...
    #def number_of_players(self, all_players):
        """Récupère le nombre de joueurs"""
        #return len(all_players)
        
    
    
    @staticmethod
    def first_prompt():
        """Proposal to the user to make a choice."""
        print("\nFaites votre choix et pressez la touche [ENTREE] : ")
        
        
        
        
    @staticmethod
    def new_player_header():
        """Header to add a New Player'."""
        View().clear_screen()
        
        
        print("\t**********************************************")
        print("\t*AJOUT D'UN NOUVEAU JOUEUR")
        print("\t********************************************\n")
    
    def prompt_for_player(self):
        """Collect all necessary player data and return as a dictionary."""
        print("Veuillez entrer les informations du joueur :")
        name = input("Nom du joueur : ").capitalize()
        first_name = input("Prénom du joueur : ").capitalize()
        player_id = input("\nIdentifiant du joueur (2 Lettres majuscules et 5 nombres) : ").upper()
        birth_date = input("Date de naissance du joueur (format JJ/MM/AAAA) : ")
        # Créer un dictionnaire contenant toutes les informations
        player_input_data = {
            "name": name,
            "first_name": first_name,
            "player_id": player_id,
            "birth_date": birth_date,
        }
        return player_input_data
        
    