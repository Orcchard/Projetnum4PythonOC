import os
import sys
from tabulate import tabulate


class ViewTournament:
    @staticmethod
    def get_scores_from_user(round_instance):
        """
        Demande à l'utilisateur de saisir les 
        scores pour chaque match du round.
        Retourne une liste de tuples (score1, score2).
        """
        scores = []
        print(
            f"\nSaisie des scores pour {round_instance.round_name} "
            f"(débuté à {round_instance.start_time}) :"
            )
        for i, match in enumerate(round_instance.matches, start=1):
            print(f"\nMatch {i} : {match.player1.name} vs {match.player2.name}")
            while True:
                try:
                    score1 = float(input(f"Score de {match.player1.name} : "))
                    score2 = float(input(f"Score de {match.player2.name} : "))
                    scores.append((score1, score2))
                    break
                except ValueError:
                    print("Erreur : veuillez saisir un nombre valide pour le score.")
            return scores

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

    def ask_start_round(self):
        response = input("Souhaitez-vous démarrer un round ? (O/N) ").strip().lower()
        if response in ["o", "n"]:
            """La vue renvoie la réponse au contrôleur."""
            return response
        print("❌ Entrée invalide. Veuillez répondre par 'O' ou 'N'.")

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
        for index, existing_tournaments in enumerate(
            existing_tournaments, start=1
                ):
            print(
                f"{index}. {existing_tournaments['name']} "
                f"({existing_tournaments['location']})"
                )

    def display_matches(self, round_instance):
        """
        Affiche la liste des matches pour le round donné.
        """
        print(f"\nMatches du {round_instance.round_name} (débuté à {round_instance.start_time}) :")
        for i, match in enumerate(round_instance.matches, start=1):
            print(f"Match {i} : {match.player1.name} vs {match.player2.name}")
        else:
            print("Erreur")

    def display_round_matches(self, matches):
        """
        Affiche les matchs du round sous forme de tableau.
        :param matches: Liste des matchs contenant les joueurs.
        """
        headers = ["Match", "Joueur 1", "Joueur 2"]
        table = [[i + 1, match.player1.name, match.player2.name] for i, match in enumerate(matches)]
        print(f"Matches reçus : {matches}")  
        """Debugging"""
        print("\n Liste des matchs du round :")
        print(tabulate(table, headers=headers, tablefmt="pretty"))
