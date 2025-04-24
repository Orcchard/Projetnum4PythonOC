"""Affichage des rapports"""
from tabulate import tabulate
from views.view_tournaments import ViewTournament
from views.view_users import View


class ViewReports:
    """Gère l'affichage des rapports"""

    def __init__(self):
        self.view = View()
        self.view_tournaments = ViewTournament()

    @staticmethod
    def no_round_played():
        """Message d'erreur"""
        print("Aucun round joué dans ce tournoi.")

    @staticmethod
    def reports_new_header():
        """En tête de l'affichage des tournois."""
        ViewTournament().clear_screen()
        # Créer un tableau avec une seule ligne pour le titre
        title_table = [["EDITION DES RAPPORTS DES TOURNOIS"]]
        print(tabulate(title_table, tablefmt="grid"))

    @staticmethod
    def good_by():
        """Sortie du menu"""
        print("👋 Au revoir !")

    @staticmethod
    def display_menu_reports():
        """ Affiche le menu rapports"""
        header = [["RAPPORTS DISPONIBLES"]]
        print(tabulate(header, tablefmt="grid"))
        rapports = [
            ["1", "Afficher les joueurs enregistrés dans la base de donnée"],
            ["2", "Afficher la liste des tournois"],
            ["3", "Afficher les joueurs d'un tournoi"],
            ["4", "Afficher les rounds et matchs d'un tournoi"],
            ["0", "Retourner au menu principal"],
            ["10", "Quitter le programme"]
        ]
        print(tabulate(rapports, headers=["Option", "ÉDITION DE RAPPORT"], tablefmt="grid"))

    @staticmethod
    def display_invalid_choice():
        """Affichage choix erroné"""
        print("⛔ Choix invalide. Veuillez réessayer.\n")

    @staticmethod
    def prompt_choice_report(valeurs_autorisees):
        """ Demande un choixà l'utilisateur"""
        while True:
            choix = input("Entrez votre choix : ").strip()
            if choix in valeurs_autorisees:
                return choix
            print("choix invalide")

    @staticmethod
    def error_loading_tournament():
        """Affichage d'erreur"""
        print("erreur probable au chargement du tournois")

    @staticmethod
    def error_construction():
        """Affichage d'erreur"""
        print("Erreur lors de la reconstruction du tournoi")

    @staticmethod
    def no_tournament_to_display():
        """Affichage erreur"""
        print("Aucun tournoi trouvé à afficher.")

    @staticmethod
    def display_tournament_list(tournaments):
        """Affiche la liste des tournois sous forme de tableau."""
        table = []
        for index, tournament in enumerate(tournaments, start=1):
            rounds_played = len(tournament.get("rounds", []))  # Nombre de rounds joués
            table.append([
                index,
                tournament.get("name", "N/A"),
                tournament.get("location", "N/A"),
                tournament.get("date_initial", "N/A"),
                tournament.get("date_end", "N/A"),
                f"{rounds_played} rounds"
            ])
        headers = ["#", "Nom", "Lieu", "Début", "Fin", "Rounds joués"]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    @staticmethod
    def wait_for_user():
        """ Mise en attente de l'utilisateur afin de visualiser la liste des tournois"""
        input("\nAppuyez sur Entrée pour revenir au menu des rapports...")

    @staticmethod
    def no_players_found():
        """Messge d'erreur"""
        print("aucun joueur chargés verifier votre fichier de sauvegarde")

    @staticmethod
    def display_all_players(players_table):
        """Affichage detous les joueurs d'echec stockés dans la base de donnée"""
        headers = ['Nom', 'Prénom', 'ID', 'Date de naissance']
        print(f"\nNombre total de joueurs enregistrés : {len(players_table)}")
        print(tabulate(players_table, headers=headers, tablefmt="pretty"))

    def prompt_for_tournament_index(self, max_index):
        """l'utilisateur sélectionne un tournoi,
            message d'erreur saisie erronée """
        while True:
            choix = input("Sélectionnez le numéro du tournoi : ").strip()
            if not choix:
                return None
            if not choix.isdigit():
                print("Veuillez entrer un nombre valide.")
                continue
            index = int(choix) - 1
            if 0 <= index < max_index:
                return index
            print("Numéro invalide. Réessayez.")
