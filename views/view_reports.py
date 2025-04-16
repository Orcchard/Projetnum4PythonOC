"""Affichage des rapports"""
from tabulate import tabulate
from views.view_tournaments import ViewTournament


class ViewReports:
    """Gère l'affichage des rapports"""

    @staticmethod
    def reports_new_header():
        """En tête de l'affichage des tournois."""
        ViewTournament().clear_screen()
        # Créer un tableau avec une seule ligne pour le titre
        title_table = [["EDITION DES RAPPORTS DES TOURNOIS"]]
        print(tabulate(title_table, tablefmt="grid"))

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
        """ Affichage choix utilisateur"""
        while True:
            choix = input("Entrez votre choix : ").strip()
            if choix in valeurs_autorisees:
                return choix
            ViewReports.display_invalid_choice()
