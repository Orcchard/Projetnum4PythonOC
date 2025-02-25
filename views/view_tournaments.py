import os
import sys
from tabulate import tabulate


class ViewTournament:
    @staticmethod
    def clear_screen():
        """Clear the display."""
        os.system("cls" if sys.platform == "win32" else "clear")

    @staticmethod
    def tournament_new_header():
        """Header before new tournament menu."""
        ViewTournament().clear_screen()
        # Créer un tableau avec une seule ligne pour le titre
        title_table = [["CREATION D'UN TOURNOIS"]]
        print(tabulate(title_table, tablefmt="grid"))

    def prompt_to_user_select_tournament(self):
        """
        Demande à l'utilisateur de sélectionner
        un tournoi voir controleur
        """
        pass

    def prompt_for_new_tournament(self):
        """Collect data return as a dictionary."""
        print("Veuillez entrer les informations du tournois :")
        name = input("Nom tournois: ").capitalize()
        location = input("Lieu du tournois : ").capitalize()
        date_initial = input("Date de début du tournoi (format JJ/MM/AAAA) : ")
        date_end = input("Date de fin du tournoi (format JJ/MM/AAAA) : ")
        nb_round = input("Nombre de rounds : ")
        print(f"Nombre de rounds saisi : {nb_round}")  # Vérifie la saisie
        description = input("Description du tournoi : ")
        print(f"Infos saisies : {name}, {location}, {date_initial},")
        print(f" {date_end}, {nb_round}, {description}")

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

    def display_tournament_tabulate(self, tournament_data, participants_table):
        """ Informations du tournoi et affichage sous forme de tableau"""
        """Préparer les détails du tournoi sous forme de tableau"""
        tournament_info = [
            ["Nom", tournament_data['name']],
            ["Lieu", tournament_data['location']],
            ["Date de début", tournament_data['date_initial']],
            ["Date de fin", tournament_data['date_end']],
            ["Description", tournament_data['description']],
        ]
    
        """Afficher les détails du tournoi"""
        print("\nDétails du tournoi :")
        print(tabulate(tournament_info, tablefmt="pretty"))

        # Définir les en-têtes de tableau pour les participants
        headers = ['Nom', 'Prénom', 'ID', 'Score', 'Adversaires IDs']
        # Afficher les participants sous forme de tableau
        print("\nParticipants :")
        print(tabulate(participants_table, headers=headers, tablefmt="pretty"))

    @staticmethod
    def not_tournament():
        print("\nAucun tournois selectionné")

    def display_message(self, message):
        """Affiche un message générique (succès, erreur, info)."""
        print(f"\n🔹 {message}")
    
    def display_alerte(self, message):
        """Affiche un message générique (Alerte)."""
        print(f"\n ❌ {message}")

    def display_tournament_list(self, existing_tournaments):
        """Affiche la liste des tournois existants."""
        if not existing_tournaments:
            print("\n❌ Aucun tournoi sélectionné")
            return
        print("\n Liste des tournois sauvegardés :")
        for index, existing_tournaments in enumerate(existing_tournaments, start=1):
            print(f"{index}. {existing_tournaments['name']} ({existing_tournaments['location']})")
