import sys
import os
from tabulate import tabulate
MAX_PLAYERS = 8


class View:

    @staticmethod
    def clear_screen():
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

    def main_header(self):
        title_table = [["Bienvenue dans le gestionnaire de tournoi"]]
        print(tabulate(title_table, tablefmt="grid"))

    def menu(self):
        """Affiche le menu principal"""
        header = ["MENU PRINCIPAL"]
        options = [
            ["1", "Créer un joueur"],
            ["2", "Créer un tournoi"],
            ["3", "Éditer un rapport"],
            ["4", "Supprimer un joueur"],
            ["5", "Reprendre un tournoi"],
            ["6", "Quitter le programme"],
        ]
        print("\n" + tabulate([], headers=header, tablefmt="grid"))
        """Affiche le titre encadré"""
        print(tabulate(options, tablefmt="plain"))
        """Afficher le menu sans bordures pour plus de clarté"""

    @staticmethod
    def first_prompt():
        """Proposal to the user to make a choice."""
        print("\nFaites votre choix et pressez la touche [ENTREE] : ")

    def prompt_for_player_prefix(self):
        """
        Demande à l'utilisateur d'entrer les 3
        premières lettres du nom du participant.
        """
        return input(
            "Entrez les 3 premières lettres du nom du participant "
            "puis pressez la touche [ENTER]: "
        ).strip().lower()

    @staticmethod
    def new_player_header():
        """Header to add a New Player'."""
        View().clear_screen()
        print("\t**********************************************")
        print("\t*      AJOUT D'UN NOUVEAU JOUEUR             *")
        print("\t*********************************************\n")

    def prompt_for_player(self):
        """Collect all necessary player data and return as a dictionary."""
        print("Veuillez entrer les informations du joueur :")
        name = input("Nom du joueur : ").capitalize()
        first_name = input("Prénom du joueur : ").capitalize()
        player_id = input(
            "\nIdentifiant du joueur (2 Lettres majuscules et 5 nombres) : "
            ).upper()
        date_of_birth = input(
            "Date de naissance du joueur (format JJ/MM/AAAA) : "
            )
        # Créer un dictionnaire contenant toutes les informations
        player_input_data = {
            "name": name,
            "first_name": first_name,
            "player_id": player_id,
            "date_of_birth": date_of_birth,
        }
        return player_input_data

    def not_enough_players(self):
        """Check the number of players."""
        self.clear_screen()
        num_of_players = self.number_of_player()
        if num_of_players < MAX_PLAYERS:
            print(
                f"\nIl y a {num_of_players} joueurs disponibles. "
                f"Veuillez en ajouter de nouveaux.\n"
            )
