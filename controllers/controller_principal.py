"""Define the principal controller."""
import json
import os
import random
from datetime import datetime

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
        self.selected_tournament = None
        self.rounds = []

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
            self.view_tournaments.display_message("à completer")
            return None
        else:
            self.view_tournaments.display_message("Mauvaise saisie")
            return None

    def player_add_input(self):
        """Adding a new player."""
        self.view.new_player_header()
        player_input_data = self.view.prompt_for_player()
        """ Crée une instance de Player en utilisant recreate_player"""
        player = Player.recreate_player(player_input_data)
        print(f"========{player}")
        self.view_tournaments.display_message(
            "Le joueur a été ajouté avec succès."
            )
        """ Sérialise les données du joueur"""
        player_data = player.player_dict()
        self.record_new_player(player_data)
        return None

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
        self.view_tournaments.display_message(
            "Création d'un nouveau tournoi..."
            )

        self.view_tournaments.tournament_new_header()
        tournament_input_data = (
            self.view_tournaments.prompt_for_new_tournament()
            )
        """Validation des données ici (ex: dates non vides)"""
        if (
            not tournament_input_data["date_initial"]
            or not tournament_input_data["date_end"]
        ):
            self.view_tournaments.display_message(
                "Erreur : Les dates doivent être renseignées !"
            )
            return
        print(f"Données reçues pour le tournoi : {tournament_input_data}")
        """Crée une instance de Tournament"""
        tournament = Tournament.recreate_tournament(
            tournament_input_data, self.all_players
            )
        print(f"Nombre de joueurs chargés : {len(self.all_players)}")
        for player in self.all_players:
            print(player)
        self.tournament = tournament
        print(f"========{self.tournament} ")
        self.view_tournaments.display_message(
            "Le tournoi a été créé avec succès."
            )

        self.select_participants_tournament()
        """
        Sélectionne les participants immédiatement
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
                f"Le tournois {self.tournament.name} et ses "
                f"8 participants sauvegardés avec succès"
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
            self.view_tournaments.display_alerte("Aucun tournoi n'a été créé.")
            return

        while len(self.tournament.participant_tournament) < MAX_PLAYERS:
            """Demande les 3 premières lettres du nom du participant"""
            prefix = self.view.prompt_for_player_prefix()
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
                self.view_tournaments.display_message(
                    "Aucun joueur trouvé avec ce préfixe.Veuillez réessayer.")
                continue
            """Affiche les joueurs correspondants avec un numéro incrémenté"""
            self.view_tournaments.display_message("nJoueurs correspondants :")
            for index, player in enumerate(matching_players, start=1):
                print(f"{index}. {player}")

            """Demande à l'utilisateur de choisir un joueur selon numéro"""
            try:
                selection = int(
                    input(
                        f"Choisissez un joueur de (1 à {len(matching_players)}),"
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
                        self.view_tournaments.display_message(
                            "Ce joueur a déjà été sélectionné"
                            )
                else:
                    self.view_tournaments.display_message(
                        "Sélection invalide"
                        )
            except ValueError:
                self.view_tournaments.display_message(
                    "Veuillez entrer un nombre valide+++"
                    )
                return None
        """Affiche les joueurs sélectionnés"""
        self.view_tournaments.display_message("\nJoueurs sélectionnés :")
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
                self.view_tournaments.display_message(
                    "Aucun fichier de tournois trouvé"
                    )
                return None
            if not existing_tournaments:
                self.view_tournaments.display_message(
                    "Aucun tournoi trouvé dans le fichier."
                    )
                return None
            """ Affiche les tournois existants"""
            self.view_tournaments.display_tournament_list(existing_tournaments)
            """Demande à l'utilisateur de sélectionner un tournoi"""
            try:
                tournament_index = int(
                    input("Entrez le numéro du tournoi à sélectionner : ")
                ) - 1
                if 0 <= tournament_index < len(existing_tournaments):
                    selected_tournament = existing_tournaments[
                        tournament_index]
                    print(
                        f"Tournoi {selected_tournament['name']} "
                        f"sélectionné avec succès."
                    )
                    """Converti le dictionnaire en instance de Tournament"""
                    self.selected_tournament = Tournament.recreate_tournament(
                        selected_tournament, self.all_players
                    )
                    """Affiche les informations du tournoi sélectionné"""
                    self.display_tournament_info(self.selected_tournament)
                    return self.selected_tournament

                else:
                    self.view_tournaments.display_message(
                        "Numéro de tournoi invalide."
                        )
                    return None
            except ValueError:
                self.view_tournaments.display_message(
                    "Veuillez entrer un nombre valide."
                    )
                return None
        except Exception as e:
            self.view_tournaments.display_message(
                f"Erreur lors de la sélection du tournoi : {e}"
                )

    def display_tournament_info(self, selected_tournament):
        """
        Récupère les informations du
        tournoi et les envoie à la vue.
        """
        if not self.selected_tournament:
            self.view_tournaments.not_tournament()
            return
        """Prépare les participants pour l'affichage"""
        participants_table = []
        if self.selected_tournament.participant_tournament:
            for participant in self.selected_tournament.participant_tournament:
                player = participant["Player"]
                score = participant["Score"]
                """Récupére uniquement les player_id des adversaires"""
                adversaires_ids = [
                    adv.player_id for adv in participant["Adversaires"]]
                participants_table.append([
                    player.name, player.first_name,
                    player.player_id, score, adversaires_ids
                ])
            """Envoie les données à la vue"""
            tournament_data = self.selected_tournament.tournament_dict()
            self.view_tournaments.display_tournament_tabulate(
                tournament_data, participants_table
                )
            """
            La vue Demande à l'utilisateur
            s'il souhaite démarrer un round
            """
            response = self.view_tournaments.ask_start_round()
            if response == "o":
                self.create_rounds(selected_tournament)
                #scores = self.view_tournaments.get_scores_from_user(new_round)
                #self.enter_scores(new_round, scores)
        else:
            print("Démarrage de round annulé.")

    def start_new_round(self, round_number, round_name):
        """Crée un nouveau round, ajoute heure debut au tournois"""
        new_round = Round(round_number=round_number, round_name=round_name)
        new_round.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tournament.rounds.append(new_round)
        return new_round

    def create_rounds(self, tournament):
        players = [p["Player"] for p in tournament.participant_tournament]
        """
        Crée tous les rounds du tournoi.
        tournament.participant_tournament est une
        liste de dictionnaires, où chaque dictionnaire
        représente un participant du tournoi avec :
        Player → l'objet joueur (Player)
        Score → son score actuel
        Adversaires → la liste de ses adversaires passés
        """
        """Stocke les adversaires des rounds précédents"""
        adversaires = {p.player_id: set() for p in players}
        """
        Nom du dictionnaire : adversaires
        Clés : les player_id des joueurs
        Valeurs : des ensembles vides
        """
        for round_number in range(1, int(self.tournament.nb_round) + 1):
            round_name = f"==== Round numéro: {round_number} ===="
            round_i = Round(round_number, round_name)
            """Ajoute le round au tournoi"""
            """ Premier round : Mélange des joueurs"""
            if round_number == 1:
                random.shuffle(players)
            else:
                """Rounds suivants : Trie les joueurs par score décroissant"""
                players.sort(key=lambda p: next(
                    (entry["Score"] for entry in self.tournament.participant_tournament
                        if entry["Player"] == p), 0), reverse=True
                    )
            new_matches = []
            available_players = players.copy()
            while available_players:
                player1 = available_players.pop(0)
                """Cherche un adversaire qui n'a pas encore joué contre player1"""
                for i, player2 in enumerate(available_players):
                    if player2.player_id not in adversaires[player1.player_id]:
                        match = Match(player1, player2)
                        new_matches.append(match)
                        """Mettre à jour l'historique des adversaires"""
                        adversaires[player1.player_id].add(player2.player_id)
                        adversaires[player2.player_id].add(player1.player_id)
                        available_players.pop(i)
                        break
            round_i.matches = new_matches
            tournament.rounds.append(round_i)
        self.view_tournaments.display_round_matches(round_i.matches)
        self.save_tournaments_to_json()
        self.enter_scores()
        print(f"Rounds sauvegardés: {[round.round_name for round in self.tournament.rounds]}")
        print(f"Nombre de rounds créés: {len(self.tournament.rounds)}")

    def enter_scores(self, round_instance, scores):
        """permet la saisie de score d'un round et valide l'heure de fin"""
        for match, (score1, score2) in zip(round_instance.matches, scores):
            match.player1_score = score1
            match.player2_score = score2
            # Mise à jour des points des joueurs
            if score1 > score2:
                match.player1.points += 1
            elif score1 < score2:
                match.player2.points += 1
            else:
                match.player1.points += 0.5
                match.player2.points += 0.5
        round_instance.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
