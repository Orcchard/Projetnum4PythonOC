"""Affichage lié aux tournois"""
import os
import sys
from tabulate import tabulate


class ViewTournament:
    """Gère l'affichage des informations liées aux tournois."""

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

    @staticmethod
    def no_file():
        "Affiche message erreur"
        print("Aucun fichier de tournois trouvé")

    @staticmethod
    def corrupted_file_jason():
        """Affiche message erreur fichier json corrompu"""
        print("Erreur lors de la lecture du fichier JSON. Il semble corrompu.")

    @staticmethod
    def back_to_menu():
        "Affiche message retour au menu principal"
        print("Retour au menu principal.")

    @staticmethod
    def all_rounds_played():
        """Message alerte tous les rounds joués"""
        print(" Tous les rounds ont déjà été joués.")

    @staticmethod
    def control_dates_tournament():
        "Message erreur date du tournois"
        print("Erreur: Les dates doivent être renseignées !")

    @staticmethod
    def create_new_tournament():
        """Affichage de création d'un nouveau tournois"""
        print("Création d'un nouveau tournoi...")

    @staticmethod
    def existing_name_tournament():
        """Message erreur si nom du tournois existe déjà"""
        print("Erreur: Un tournoi avec ce nom existe déjà.")

    @staticmethod
    def tournament_stopped():
        """Message d'erreur tournois interrompu """
        print("Tournoi interrompu. Sauvegarde en cours...")

    @staticmethod
    def nb_rounds_reached():
        """ Affiche que le maximum de 4 rounds est joué"""
        print("\n Tous les rounds sont terminés ! Tournoi finalisé !")
        print("Vous avez atteint le nombre de round maximum soit 4.")

    @staticmethod
    def no_players_in_tournament():
        """Message d'erreur aucun joueur dans le tournoi"""
        print("Erreur : Aucun joueur valide trouvé dans le tournoi.")

    @staticmethod
    def no_players_selected_tournament():
        """Message d'erreur aucun joueur selectionné pour ce tournoi"""
        print("Erreur : Aucun joueur séléctionné pour ce tournoi.")

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

    def display_title(self, tournament):
        """Affichage du Titre"""
        print("\n" + " o o o | TOURNOI : " + tournament.name.upper() + " | o o o\n")

    def display_round_header(self, header: str):
        """Affichage de l'en tête du round"""
        print(tabulate([[header]], headers=[""], tablefmt="fancy_grid", colalign=("center",)))

    def display_round_progress(self, current_round, total_rounds):
        """Affiche la progression des rounds"""
        print(f" -- {current_round} / {total_rounds} ")

    def display_tournament_tabulate(self, tournament_data_table, participants_table):
        """ Informations du tournoi et affichage sous forme de tableau"""
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
        # On trie les participants par score décroissant (meilleur score en premier)
        sorted_participants = sorted(participants_table, key=lambda x: x[3], reverse=True)

        # Définir les en-têtes de tableau pour les participants
        headers = ['Nom', 'Prénom', 'ID', 'Score', 'Adversaires IDs']
        # Afficher les participants sous forme de tableau
        print("\nPARTICIPANTS AU TOURNOI SELECTIONNÉ:")
        print(tabulate(sorted_participants, headers=headers, tablefmt="pretty"))

    def ask_start_round(self):
        """Création d'un round ou pas: choix de l'utilisateur"""
        response = input("Souhaitez-vous démarrer un round ? (O/N) ").strip().lower()
        if response in ["o", "n"]:
            """La vue renvoie la réponse au contrôleur."""
            return response
        print(" Entrée invalide. Veuillez répondre par 'O' ou 'N'.")

    @staticmethod
    def not_tournament():
        """ Affiche un message indiquant qu'aucun tournoi n'a été sélectionné."""
        print("\n Aucun tournois selectionné")

    @staticmethod
    def not_tournament_created():
        """ Affiche un message indiquant qu'aucun tournoi n'a été créé."""
        print("\n Aucun tournois créé")

    @staticmethod
    def yes_tournament_created():
        """ Affiche un message indiquant que le tournoi a été créé."""
        print(("Le tournoi a été créé avec succès."))

    def display_message(self, message):
        """Affiche un message générique (succès, erreur, info)."""
        print(f"\n {message}")

    def display_tournament_list(self, existing_tournaments):
        """Affiche la liste des tournois existants."""
        if not existing_tournaments:
            print("\n Aucun tournoi sélectionné")
            return
        print("\n Liste des tournois sauvegardés:")
        for index, existing_tournaments in enumerate(
            existing_tournaments, start=1
                ):
            rounds_count = len(existing_tournaments.get("rounds", []))
            print(
                f"{index}. {existing_tournaments['name']} "
                f" Se déroulant à {existing_tournaments['location']}"
                f" ({rounds_count} rounds)"
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
            print(f"\nMatch {i}: {match.player1.name}  vs {match.player2.name}")
            print("1. Victoire du joueur 1")
            print("2. Victoire du joueur 2")
            print("3. Match nul")
            while True:
                choice = input("Votre choix (1-3): ").strip()
                if choice == "1":
                    scores.append((1.0, 0.0))
                    break
                if choice == "2":
                    scores.append((0.0, 1.0))
                    break
                if choice == "3":
                    scores.append((0.5, 0.5))
                    break
                print("Erreur: choix invalide. Veuillez saisir 1, 2 ou 3.")
        return scores

    @staticmethod
    def display_matches(round_i):
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
        
        """
        # Affichage des informations du tournoi
        print(f"\nTournoi: {tournament['name']}")
        print(f"Date: {tournament['date_initial']}")
        print("------Participants----- :")
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

    @staticmethod
    def no_tournament_file_found():
        """Message erreur"""
        print("Aucun fichier de tournois trouvé.")

    @staticmethod
    def invalid_tournament_number():
        """Message erreur suite numéro de tournois sélectionné invalide"""
        print("Numéro de tournoi invalide.")

    @staticmethod
    def invalid_choice_entry():
        """Message erreur suite saisie invalide"""
        print("Saisie invalide.")

    @staticmethod
    def tournament_not_built():
        """Message d'erreur"""
        print("Erreur : le tournoi n'a pas pu être recréé.")

    @staticmethod
    def no_tournaments_in_json():
        """Message d'erreur"""
        print("Aucun tournoi trouvé dans le fichier.")

    def display_resume(self, tournament):
        """ Afficher le résumé du tournoi (par exemple le nom, la date, etc.)"""
        print(f"Résumé du tournoi {tournament.name}")

    def display_match_table(self, match_table):
        """Afficher le tableau des matchs"""
        print(
            tabulate(
                match_table, headers=["Joueur 1", "Score J1", "Joueur 2", "Score J2"],
                tablefmt="fancy_grid", colalign=("left", "center", "left", "center"))
            )

    def key_error_missing_field(self, field_name):
        """Message erreur """
        print(f"Erreur : clé manquante dans les données du tournoi ({field_name}).")

    def unexpected_error(self, error_message):
        """Message d'erreur"""
        print(f"Une erreur inattendue est survenue : {error_message}")

    def display_round_start(self, round_name, start_time):
        """Affichage des données du round"""
        print(f"\n Début du {round_name} à {start_time}\n")

    def display_round_object(self, round_i):
        """Affichage du round en cours"""
        print(f" {round_i}")

    def display_match_list_start(self, round_number):
        """Annonce les matchs du round"""
        print(f" Matchs de ce round numéro: {round_number} ")

    def display_match_vs(self, player1, player2):
        """Affiche match entre deux joueurs"""
        print(
            f"{player1.name} {player1.first_name} VS {player2.name} {player2.first_name}"
            )

    def ask_start_next_round(self):
        """Demande si l'utilisateur veut démarrer un nouveau round"""
        return input(
            "\n Souhaitez-vous démarrer le prochain round ? (o/n) : ").strip().lower()

    def ask_end_of_round(self):
        """Demande si les matchs sont terminés pour saisir les scores."""
        while True:
            response = input(
                "\n Si le match est terminé, saisir(o) pour entrer les scores ... : "
                ).strip().lower()
            if response in ["o", "n"]:
                return response
            print(" Entrée invalide. Veuillez répondre par 'O' ou 'N'.")

    def display_end_of_round(self, round_name, end_time):
        """Affiche la fin d'un round."""
        print(f"\n Fin du {round_name} à {end_time}\n")

    def error_saving(self, error_message):
        """Affichage erreur sauvegarde de fichier"""
        print(f"Erreur lors de la sauvegarde du fichier: {error_message}")

    def error_rebuilding_tournament(self, error, tournament_data):
        """Affiche une erreur lors de la reconstruction du tournoi."""
        print("\nErreur lors de la reconstruction du tournoi :", error)
        print("Données en échec :", tournament_data)

    def prompt_to_continue(self):
        """Invite l'utilisateur à appuyer sur Entrée pour continuer."""
        input("\nAppuyez sur Entrée pour continuer [ENTER]...")

    def display_loaded_rounds_info(self, tournament_name, number_of_rounds):
        """Affiche les informations sur les rounds chargés pour un tournoi."""
        print(f"Rounds chargés pour {tournament_name} : {number_of_rounds}")

    def player_added_to_tournament(self, name, first_name, current_count, max_players):
        """Affiche le message lorsqu'un joueur est ajouté au tournoi."""
        print(f"Joueur {name} {first_name} ajouté au tournoi !")
        print(f"{current_count} joueur(s) sélectionné(s) sur {max_players}.")

    def success_tournament_saved(self, tournament_name):
        """Affiche un message confirmant la sauvegarde d'un tournoi."""
        print(
            f"Le tournoi '{tournament_name}' et ses données ont été sauvegardés avec succès."
            )

    def show_created_tournament(self, tournament):
        """Affiche le tournoi créé."""
        print(f"\n{tournament}")

    def no_valid_pairs(self):
        print("Impossible de générer des matchs sans doublons. Tournoi bloqué.")
