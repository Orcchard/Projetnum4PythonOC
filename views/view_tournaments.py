"""Missing"""
import os
import sys
from tabulate import tabulate


class ViewTournament:
    """Missing"""

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

    def prompt_for_new_tournament(self):
        """Collect data return as a dictionary."""
        print("Veuillez entrer les informations du tournois:")
        name = input("Nom tournois: ").capitalize()
        location = input("Lieu du tournois: ").capitalize()
        date_initial = input("Date de début du tournoi (format JJ/MM/AAAA): ")
        date_end = input("Date de fin du tournoi (format JJ/MM/AAAA): ")
        nb_round = input("Nombre de rounds: ")
        description = input("Description du tournoi: ")
        # print(f"Infos saisies: {name}, {location}, {date_initial},")
        # print(f" {date_end}, {nb_round}, {description}")
        tournament_input_data = {
            "name": name,
            "location": location,
            "date_initial": date_initial,
            "date_end": date_end,
            "nb_round": nb_round,
            "description": description
        }
        """Crée un dictionnaire contenant toutes les informations"""
        return tournament_input_data

    def display_tournament_tabulate(self, tournament_data_table, participants_table):
        """ Informations du tournoi et affichage sous forme de tableau"""
        """Préparer les détails du tournoi sous forme de tableau"""
        tournament_info = [
            ["Nom", tournament_data_table['name']],
            ["Lieu", tournament_data_table['location']],
            ["Date de début", tournament_data_table['date_initial']],
            ["Date de fin", tournament_data_table['date_end']],
            ["Description", tournament_data_table['description']],
        ]
        """Afficher les détails du tournoi"""
        print("\nDétails du tournoi:")
        print(tabulate(tournament_info, tablefmt="pretty"))

        # Définir les en-têtes de tableau pour les participants
        headers = ['Nom', 'Prénom', 'ID', 'Score', 'Adversaires IDs']
        # Afficher les participants sous forme de tableau
        print("\nParticipants*****:")
        print(tabulate(participants_table, headers=headers, tablefmt="pretty"))

    def ask_start_round(self):
        """Missing"""
        response = input("Souhaitez-vous démarrer un round ? (O/N) ").strip().lower()
        if response in ["o", "n"]:
            """La vue renvoie la réponse au contrôleur."""
            return response
        print("❌ Entrée invalide. Veuillez répondre par 'O' ou 'N'.")

    @staticmethod
    def not_tournament():
        """Missing"""
        print("\n Aucun tournois selectionné")

    def display_message(self, message):
        """Affiche un message générique (succès, erreur, info)."""
        print(f"\n {message}")

    def display_alerte(self, message):
        """Affiche un message générique (Alerte)."""
        print(f"\n ❌ {message}")

    def display_tournament_list(self, existing_tournaments):
        """Affiche la liste des tournois existants."""
        if not existing_tournaments:
            print("\n❌ Aucun tournoi sélectionné")
            return
        print("\n Liste des tournois sauvegardés:")
        for index, existing_tournaments in enumerate(
            existing_tournaments, start=1
                ):
            print(
                f"{index}. {existing_tournaments['name']} "
                f"({existing_tournaments['location']})"
                )

    @staticmethod
    def get_scores_from_user(round_i):
        """Demande à l'utilisateur de saisir les scores du round terminé"""
        scores = []
        print(
            f"\nSaisie des scores pour {round_i.round_name} "
            f"(débuté à {round_i.start_time}):"
            )
        for i, match in enumerate(round_i.matches, start=1):
            print(f"\nMatch {i}: {match.player1.name} vs {match.player2.name}")
            while True:
                try:
                    score1 = float(input(f"Score de {match.player1.name}: "))
                    score2 = float(input(f"Score de {match.player2.name}: "))
                    scores.append((score1, score2))
                    break
                except ValueError:
                    print("Erreur: veuillez saisir un nombre valide pour le score.")
        return scores

    @staticmethod
    def display_matches(self, round_i):
        """Affiche la liste des matches pour le round donné."""
        print(f"\nMatches xxxxx du {round_i.round_name} (débuté à {round_i.start_time}):")
        for i, match in enumerate(round_i.matches, start=1):
            print(f"Match {i}: {match.player1.name} vs {match.player2.name}")
        print("Erreur")

    def get_user_choice(self):
        """Demande à l'utilisateur de choisir une action."""
        choice = input(
            "Tapez 'r' pour revenir à la liste des tournois, 'q' pour quitter "
            ).lower()
        return choice

    def display_tournament_info(self, tournament):
        """
        Affiche les informations détaillées du tournoi.
        :param tournament: L'objet Tournament contenant les informations du tournoi.
        """
        # Affichage des informations du tournoi
        print(f"\nTournoi: {tournament['name']}")
        print(f"Date: {tournament['date_initial']}")
        print("Participants:")
        for participant in tournament.get('players', []):
            print(f"- {participant}")

    def display_rounds(self, round_data):
        """
        Affiche les rounds du tournoi sous forme de tableau.
        :param round_data: Liste de dictionnaires contenant les informations des rounds.
        """
        headers = ["Round", "Match", "Joueur 1", "Joueur 2"]
        table = []
        for round_info in round_data:
            for match in round_info.get('matches', []):
                table.append([
                    f"Round {round_info['number']}",
                    f"Match {match['number']}",
                    match.get('player1', 'Inconnu'),
                    match.get('player2', 'Inconnu')
                ])
        print(tabulate(table, headers=headers, tablefmt="grid"))
