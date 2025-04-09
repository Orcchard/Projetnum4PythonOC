"""Affichage des rapports"""
from tabulate import tabulate
from view_tournaments import ViewTournament


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
    def afficher_menu_rapports():
        """"""
        header = [["RAPPORTS DISPONIBLES"]]
        print(tabulate(header, tablefmt="grid"))
        rapports = [
            ["1", "Afficher les 8 joueurs enregistrés"],
            ["2", "Afficher la liste des tournois"],
            ["3", "Afficher les joueurs d'un tournoi"],
            ["4", "Afficher les rounds et matchs d'un tournoi"],
            ["0", "Retourner au menu principal"],
            ["10", "Quitter le programme"]
        ]
        print(tabulate(rapports, headers=["Option", "ÉDITION DE RAPPORT"], tablefmt="grid"))

    @staticmethod
    def afficher_choix_invalide():
        """Affichage choix erroné"""
        print("⛔ Choix invalide. Veuillez réessayer.\n")

    @staticmethod
    def saisir_choix(valeurs_autorisees):
        """ Affichage choix utilisateur"""
        while True:
            choix = input("Entrez votre choix : ").strip()
            if choix in valeurs_autorisees:
                return choix
            ViewTournament.afficher_choix_invalide()
