"""Affichages liés aux joueurs"""
import sys
import os
from datetime import datetime
from tabulate import tabulate
MAX_PLAYERS = 8


class View:
    """gère l'affichage lié aux joueurs"""

    @staticmethod
    def clear_screen():
        """Efface l'affichage à l'écran en cours pour passer à une autre mire"""
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

    def main_header(self):
        """Affiche le titre principal du gestionnaire de tournoi dans un tableau formaté"""
        title_table = [["Bienvenue dans le gestionnaire de tournoi"]]
        print(tabulate(title_table, tablefmt="grid"))

    def menu(self):
        """Affiche le menu principal"""
        header = ["MENU PRINCIPAL"]
        options = [
            ["1", "Créer un joueur"],
            ["2", "Créer un tournoi"],
            ["3", "Éditer un tournois complet"],
            ["4", "Afficher les rapports "],
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
        print("\nFaites votre choix et pressez la touche [ENTREE]: ")

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
    def loading_players_file():
        """Message de chargement des joueurs"""
        print("Chargement des joueurs...")

    @staticmethod
    def no_players_found():
        """Message d'erreur"""
        print("Erreur: fichier de données des joueurs introuvable.")

    def players_loaded_successfully(self, count):
        """Message affiché si chargement des joueurs ok affichage du nombre de joueurs"""
        message = f"{count} joueurs chargés avec succès."
        print(message)

    def no_succes_load(self, error_message):
        """Message d'erreur de chargement des joueurs"""
        print(f"Erreur lors du chargement des joueurs : {error_message}")

    def display_player_created(self, player):
        """Message affichant les données du joueur crée et sauvegardé en json"""
        print(
            f"Joueur ajouté avec succès : {player.first_name} "
            f"{player.name} (ID: {player.player_id})"
            )

    @staticmethod
    def new_player_header():
        """Header to add a New Player'."""
        View().clear_screen()
        print("\t**********************************************")
        print("\t*      AJOUT D'UN NOUVEAU JOUEUR             *")
        print("\t*********************************************\n")

    def prompt_for_player(self):
        """Collect all necessary player data and return as a dictionary."""
        print("Veuillez entrer les informations du joueur:")
        name = input("Nom du joueur: ").capitalize()
        first_name = input("Prénom du joueur: ").capitalize()
        player_id = input(
            "\nIdentifiant du joueur (2 lettres majuscules suivies de 5 chiffres (ex: AB12345): "
            ).upper()
        # Validation de la date de naissance
        while True:
            date_of_birth = input("Date de naissance du joueur (format JJ/MM/AAAA): ")
            try:
                # Essaye de parser la date, si erreur → format invalide
                datetime.strptime(date_of_birth, "%d/%m/%Y")
                break
            except ValueError:
                print("Format invalide. Veuillez entrer la date au format JJ/MM/AAAA.")
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

    def display_players_list(self, players, title=""):
        """Affiche une liste de joueurs formatée avec des numéros."""
        message = f"\n{title}\n" if title else "\n"
        for idx, player in enumerate(players, start=1):
            message += f"{idx}. {player.name} {player.first_name}\n"
        self.display_message(message)

    def display_message(self, message):
        """Affiche un message générique (succès, erreur, info)."""
        print(f"\n🔹 {message}")

    @staticmethod
    def three_letters():
        """Message afin d'imposer au moins les 3 premières lettres du nom"""
        print("Erreur : 3 lettres minimum !")

    @staticmethod
    def not_any_players():
        """Alerte qu'aucun joueur avec ce prefix n'est connu de la base des players"""
        print("Aucun joueur trouvé. Réessayez.")

    @staticmethod
    def player_already_selected():
        """Alerte que le  joueur est déjà séléctionné"""
        print("Joueur déjà sélectionné.")

    @staticmethod
    def invalid_entry():
        "Message d'erreur pour saisie invalide"
        print("Entrée invalide")

    @staticmethod
    def listing_selected_players():
        """Affichage des joueurs sélectionnés pour un tournoi"""
        print("\nListe des joueurs sélectionnés:")

    def display_selected_players_list(self, players_info):
        """Affiche la liste des joueurs sélectionnés."""
        for name, first_name, player_id in players_info:
            print(f"{name} {first_name} (ID: {player_id})")
