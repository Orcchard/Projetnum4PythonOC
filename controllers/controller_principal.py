"""Define the principal controller."""
import json
import os
import random
from views.view_users import View
from views.view_tournaments import ViewTournament
from models.player_mod import Player
from models.tournament_mod import Tournament
from models.round_mod import Round
from models.match_mod import Match

MAX_PLAYERS = 8


class ControllerPrincipal:
    """Principal controller."""

    def __init__(self):
        """Initialise le controler avec une vue et ses attributs ."""
        self.view = View()
        self.view_tournaments = ViewTournament()
        self.all_players = []
        self.tournament = None
        self.participant_tournament = []

        """Le tournoi courant"""
        self.players_file = "all_players_data.json"
        self.tournaments_file = "tournaments_data.json"

    def run(self):
        """Run the main program"""
        print("Chargement des joueurs...")
        self.all_players = self.load_players_from_js_file()
        """Chargement de la liste de joueurs dans all_players"""
        if not self.all_players:
            print(
                "Aucun joueur trouvé"
                "Veuillez vérifier le fichier des joueurs"
            )
            print(f"{len(self.all_players)} joueurs chargés avec succès.")
        """ Charge les tournois existants"""
        self.load_tournaments_from_json()
        """Charge les tournois stockés dans fichier json"""
        self.display_menu_principal()
        """Appele le menu principal"""

    def load_players_from_js_file(self):
        """Charge les joueurs depuis le fichier JSON."""
        try:
            with open(self.players_file, "r", encoding="utf-8") as file:
                players_data = json.load(file)
                """ Retourne les données  en instances"""
                return [Player.recreate_player(data)
                        for data in players_data
                        ]
        except FileNotFoundError:
            print("Erreur : fichier de données des joueurs introuvable.")
            return []
        except Exception as e:
            print(f"Erreur lors du chargement des joueurs : {e}")
            return []

    def display_menu_principal(self):
        """
        Méthode pour démarrer le programme.
        Affiche le menu principal
        """
        """while True:"""
        self.view.clear_screen()
        self.view.main_header()
        self.view.menu()
        self.view.first_prompt()
        user_choice = input()
        if user_choice == "1":
            self.player_add_input()
        elif user_choice == "2":
            self.new_tournament_input()
        elif user_choice == "3":
            pass
        elif user_choice == "4":
            pass
        elif user_choice == "5":
            self.select_list_saved_tournaments()
        elif user_choice == "6":
            print("à completer")
        else:
            print("Mauvaise saisie")

    def player_add_input(self):
        """Adding a new player."""
        self.view.new_player_header()
        player_input_data = self.view.prompt_for_player()
        """ Crée une instance de Player en utilisant recreate_player"""
        player = Player.recreate_player(player_input_data)
        print(f"========{player}")
        print("Le joueur a été ajouté avec succès.")
        """ Sérialise les données du joueur"""
        player_data = player.player_dict()
        self.record_new_player(player_data)

    def record_new_player(self, player_data):
        """Met à jour le fichier all_players en ajoutant un nouveau joueur."""
        try:
            players = []
            if os.path.exists(self.players_file):
                with open(self.players_file, "r", encoding="utf-8") as file:
                    players = json.load(file)
                    """Charge les données existantes du fichier JSON"""
            players.append(player_data)
            players.sort(key=lambda x: x["name"].lower())
            """Trie les joueurs par nom"""
            with open(self.players_file, "w", encoding="utf-8") as file:
                json.dump(players, file, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier: {e}")

    def new_tournament_input(self):
        """Create a new tournament."""
        self.view_tournaments.tournament_new_header()
        tournament_input_data = (
            self.view_tournaments.prompt_for_new_tournament()
            )
        """Crée une instance de Tournament"""
        self.tournament = Tournament.recreate_tournament(
            tournament_input_data, self.all_players)
        print(self.tournament)
        print(f"========{self.tournament}")
        print("Le tournoi a été créé avec succès.")
        print()
        """Sauvegarder tous les tournois, y compris le nouveau"""
        self.select_participants_tournament()
        """Sélectionne les participants immédiatement
        après la création du tournoi
        """

    def save_tournaments_to_json(self):
        try:
            tournaments = []
            """stock les anciens tournois"""
            if os.path.exists(self.tournaments_file):
                with open(
                    self.tournaments_file, "r", encoding="utf-8"
                        ) as file:
                    tournaments = json.load(file)
                    """ajoute le tournoi actuel à la liste"""
            """
            Converti l'objet Tournament
            en dictionnaire avant de l'ajouter
            """
            tournament_dict = self.tournament.tournament_dict()
            tournaments.append(tournament_dict)
            with open(
                self.tournaments_file, "w", encoding="utf-8"
                    ) as file:
                json.dump(tournaments, file, ensure_ascii=False, indent=4)
                """ Sauvegarde les tournois (anciens + nouveau)."""
            print(
                f"Le tournois {self.tournament.name} et les participants "
                f"sauvegardés avec succès"
                )
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier : {e}")

    def load_tournaments_from_json(self):
        """
        Charge les données du tournoi depuis un fichier JSON.
        Utilise la méthode recreate_tournament de la classe Tournament.
        """
        try:
            if os.path.exists(self.tournaments_file):
                with open(
                    self.tournaments_file, "r", encoding="utf-8"
                        ) as file:
                    data = json.load(file)
                self.tournaments = [Tournament.recreate_tournament(
                    t, self.all_players) for t in data]
                """recrée les joueurs associés au tournois"""
                if self.tournaments:
                    self.tournament = self.tournaments[-1]
                """ Prend le dernier tournoi chargé"""
                print(
                    f"{len(self.tournaments)}"
                    "tournois chargés depuis {self.tournaments_file}."
                )
        except FileNotFoundError:
            print(f"Erreur : le fichier {self.tournaments_file} introuvable.")
        except Exception as e:
            print(f"Erreur lors du chargement du fichier : {e}")

    def select_participants_tournament(self):
        """
        Sélectionne 8 joueurs en saisissant
        les 3 premières lettres du nom.
        """
        if not self.tournament:
            print("Aucun tournoi n'a été créé.")
            return

        while len(self.tournament.participant_tournament) < MAX_PLAYERS:
            """Demande les 3 premières lettres du nom du participant"""
            prefix = self. view.prompt_for_player_prefix()
            """
            Appel à la méthode prompt_for_player_prefix pour
            obtenir les joueurs correspondants
            """
            matching_players = [
                player for player in self.all_players
                if player.name.lower().startswith(prefix)
                ]
            """ Si aucun joueur n'est trouvé, on recommence"""
            if not matching_players:
                print(
                    "Aucun joueur trouvé avec ce préfixe."
                    "Veuillez réessayer."
                    )
                continue
            """Affiche les joueurs correspondants avec un numéro incrémenté"""
            print("\nJoueurs correspondants :")
            for index, player in enumerate(matching_players, start=1):
                print(f"{index}. {player}")

            """Demander à l'utilisateur de choisir un joueur selon numéro"""
            try:
                selection = int(
                    input(
                        f"Choisissez un joueur (1 à {len(matching_players)}),"
                        f"saisis : {
                            len(self.tournament.participant_tournament)}/8 : "
                        )
                    )
                if 1 <= selection <= len(matching_players):
                    selected_player = matching_players[selection - 1]
                    """Les listes en Python sont indexées à partir de 0"""
                    if selected_player not in [
                        p["Player"] for p in
                        self.tournament.participant_tournament
                    ]:
                        self.tournament.participant_tournament.append(
                            {
                                "Player": selected_player,
                                "Score": 0,
                                "Adversaires": []
                                }
                            )
                        print(
                            f"Joueur ({selected_player.name}) "
                            f"({selected_player.first_name}) sélectionné."
                        )
                    else:
                        print("Ce joueur a déjà été sélectionné.")
                else:
                    print("Sélection invalide.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        """Affiche les joueurs sélectionnés"""
        print("\nJoueurs sélectionnés :")
        for participant in self.tournament.participant_tournament:
            player = participant["Player"]
            print(
                f"({player.name} {player.first_name})"
                f"(ID : {player.player_id})"
                )
        """Sauvegarde le tournoi avec les participants"""
        self.save_tournaments_to_json()

    def select_list_saved_tournaments(self):
        try:
            if os.path.exists(self.tournaments_file):
                with open(
                    self.tournaments_file, "r", encoding="utf-8"
                            )as file:
                    existing_tournaments = json.load(file)
            else:
                print("Aucun fichier de tournois trouvé.")
                return None
            if not existing_tournaments:
                print("Aucun tournoi trouvé dans le fichier.")
                return None
            """ Affiche les tournois existants"""
            print("\nTournois existants :")
            for index, tournament in enumerate(existing_tournaments, start=1):
                print(f"{index}. {tournament['name']}")
            """Demande à l'utilisateur de sélectionner un tournoi"""
            try:
                tournament_index = int(
                    input("Entrez le numéro du tournoi à sélectionner : ")
                ) - 1
                if 0 <= tournament_index < len(existing_tournaments):
                    selected_tournament = existing_tournaments[
                        tournament_index
                        ]
                    print(
                        f"Tournoi {selected_tournament['name']} "
                        f"sélectionné avec succès."
                    )
                    """Converti le dictionnaire en instance de Tournament"""
                    self.tournament = Tournament.recreate_tournament(
                        selected_tournament, self.all_players
                    )
                    """Affiche les informations du tournoi sélectionné"""
                    self.display_tournament_info()
                    return selected_tournament
                else:
                    print("Numéro de tournoi invalide.")
                    return None
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                return None
        except Exception as e:
            print(f"Erreur lors de la sélection du tournoi : {e}")

    def display_tournament_info(self):
        """
        Affiche les informations du tournoi sélectionné et propose d'ajouter un round selon les scores.
        """
        self.view_tournaments.display_tournament_tabulate()
        print("\nInformations du tournoi sélectionné :")
        print(f"Nom du tournoi : {self.tournament.name}")
        print(f"Lieu : {self.tournament.location}")
        print(f"Date de début : {self.tournament.date_initial}")
        print(f"Date de fin : {self.tournament.date_end}")
        print(f"Description : {self.tournament.description}")
        if self.tournament.participant_tournament:
            print("\nParticipants :")
            """
            Affiche les participants du tournoi
            """
            for participant in self.tournament.participant_tournament:
                player = participant["Player"]
                score = participant["Score"]
                print(
                    f"- {player.name} {player.first_name} "
                    f"(ID : {player.player_id}) : {score} points"
                    )
        else:
            print("\nAucun participant n'a été ajouté")
        if hasattr(self.tournament, "rounds") and self.tournament.rounds:
            print("\nRounds :")
            for round_index, round_data in enumerate(
                self.tournament.rounds, start=1
                    ):
                print(f"Round {round_index} :")
                for match in round_data["matches"]:
                    player1 = match["player1"]
                    player2 = match["player2"]
                    print(f"  {player1.name} vs {player2.name} - ")
                    print(
                        f" Scores : {match.player1_score} - "
                        f"{match.player2_score}")

    def next_round(self):
        if not self.tournament:
            print("Aucun tournois selectionné")
            return
        current_round_number = len(self.tournament.rounds) + 1
        """Vérification du nombre maximal de rounds"""
        if current_round_number > int(self.tournament.nb_round):
            print("Tous les rounds ont déjà été joués !")
            return
        """Création du round"""
        round_name = f"Round {current_round_number}"
        new_round = Round(
            round_number=current_round_number,
            name=round_name,
            start_time=None,
            end_time=None
            )
        if current_round_number == 1:
            random.shuffle(self.tournament.participant_tournament)
            print(f" le round en cours est le numéro: {current_round_number}")
        else:
            """Trie joueurs par ordre décroissant des scores"""
            self.tournament.participant_tournament = sorted(
                self.tournament.participant_tournament,
                key=lambda x: x["Score"],
                reverse=True
            )
