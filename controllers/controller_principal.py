"""Define the principal controller."""
import sys
import json
import os
import random
from datetime import datetime
from itertools import permutations


from controllers.controller_reports import ControllerReports
from views.view_reports import ViewReports
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
        self.view_reports = ViewReports()
        self.controller_reports = ControllerReports(self)
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
        self.view.loading_players_file()
        self.all_players = self.load_players_from_js_file()
        # Chargement de la liste de joueurs dans all_players """
        if not self.all_players:
            self.view.no_players_found()
        self.view.players_loaded_successfully(len(self.all_players))
        # AppeL le menu principal
        self.display_menu_principal()

    def load_players_from_js_file(self):
        """Charge les joueurs depuis le fichier JSON."""
        try:
            with open(self.players_file, "r", encoding="utf-8") as file:
                players_data = json.load(file)
                # Retourne les données  en instances"""
            return [Player.recreate_player(self, data)
                    for data in players_data
                    ]
        except FileNotFoundError:
            self.view.no_players_found()
            return []
        except Exception as e:
            self.view.no_succes_load(str(e))
            return []

    def display_menu_principal(self):
        """Méthode pour démarrer le programme.Affiche le menu"""
        while True:
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
                self.view_reports.reports_new_header()
                self.view_reports.display_menu_reports()
                self.controller_reports.display_report_choice()
            elif user_choice == "4":
                self.view.clear_screen()
                self.select_list_saved_tournaments(action_type="create_round")
            elif user_choice == "5":
                sys.exit()
            else:
                self.view_tournaments.invalid_choice_entry()
            self.view_tournaments.prompt_to_continue()
            # demander à appuyer sur entrée via la vue

    def player_add_input(self):
        """Adding a new player."""
        self.view.new_player_header()
        player_input_data = self.view.prompt_for_player()
        # Crée une instance de Player en utilisant recreate_player
        player = Player.recreate_player(self, player_input_data)
        self.view.display_player_created(player)
        # Sérialise les données du joueur
        player_data = player.player_dict()
        self.record_new_player(player_data)
        # Mise à jour de la liste en mémoire
        self.all_players.append(player)
        self.all_players.sort(key=lambda p: p.name.lower())

    def record_new_player(self, player_data):
        """Met à jour le fichier all_players en ajoutant un nouveau joueur."""
        try:
            players = []
            if os.path.exists(self.players_file):
                with open(self.players_file, "r", encoding="utf-8") as file:
                    players = json.load(file)
                    # Charge les données existantes du fichier JSON
            players.append(player_data)
            players.sort(key=lambda x: x["name"].lower())
            # Trie les joueurs par nom
            with open(self.players_file, "w", encoding="utf-8") as file:
                json.dump(players, file, ensure_ascii=False, indent=4)
        except Exception as e:
            self.view_tournaments.error_saving(str(e))
            return

    def new_tournament_input(self):
        """Recupère les données du tournois saisi par l'utilisateur"""
        self.view_tournaments.create_new_tournament()
        self.view_tournaments.tournament_new_header()
        tournament_input_data = (
            self.view_tournaments.prompt_for_new_tournament())
        # Validation des données ici (ex: dates non vides)"""
        if (not tournament_input_data["date_initial"] or not tournament_input_data["date_end"]):
            self.view_tournaments.control_dates_tournament()
            return
        # ✅ Vérifie si le nom du tournoi existe déjà
        existing_names = [t["name"] for t in self.load_tournaments_from_json()]
        if tournament_input_data["name"] in existing_names:
            self.view_tournaments.existing_name_tournament()
            return
        # Reconstruction de l'objet  Tournament
        # Intègre la liste self.all_players pour associer les joueurs existants au tournoi).
        tournament = Tournament.recreate_tournament(
            tournament_input_data, self.all_players
        )
        self.tournament = tournament
        self.view_tournaments.show_created_tournament(self.tournament)
        self.view_tournaments.yes_tournament_created()
        self.select_participants_tournament()

        # Sélectionne les participants immédiatement après la création du tournoi

    def select_participants_tournament(self):
        """
        Sélectionne 8 joueurs en saisissant
        les 3 premières lettres du nom.
        """
        if not self.tournament:
            self.view_tournaments.not_tournament_created()
            self.view_tournaments.display_loaded_rounds_info(
                self.tournament.name, len(self.tournament.rounds)
            )
        while len(self.tournament.participant_tournament) < MAX_PLAYERS:
            prefix = self.get_valid_prefix()
            matching_players = self.find_matching_players(prefix)
            if not matching_players:
                continue  # Redémarre la boucle si aucun joueur trouvé
            self.display_matching_players(matching_players)
            self.handle_player_selection(matching_players)
        self.display_selected_players()
        self.save_tournament_to_json(self.tournament)

    def get_valid_prefix(self):
        """Demande un préfixe valide (3 lettres min)."""
        while True:
            prefix = self.view.prompt_for_player_prefix().strip().lower()
            if len(prefix) >= 3:
                return prefix
            self.view.three_letters()

    def find_matching_players(self, prefix):
        """Retourne les joueurs correspondant au préfixe."""
        matching = [p for p in self.all_players if p.name.lower().startswith(prefix)]
        if not matching:
            self.view.not_any_players()
        return matching

    def display_matching_players(self, players):
        """Affiche la liste des joueurs avec des numéros."""
        self.view.display_players_list(
            players, title="Joueurs correspondants :"
        )

    def handle_player_selection(self, matching_players):
        """Gère la sélection des joueurs et les ajoute au tournoi"""
        try:
            selection = int(input(f"Choix (1-{len(matching_players)}): "))
            selected_player = matching_players[selection - 1]
            if self.is_player_already_selected(selected_player):
                self.view.player_already_selected()
            else:
                self.add_player_to_tournament(selected_player)
        except (ValueError, IndexError):
            self.view.invalid_entry()

    def display_selected_players(self):
        """Affichages des joueurs selectionnés"""
        if self.tournament is None:
            self.view_tournaments.not_tournament()
            return
        # Affiche les participants sélectionnés."""
        self.view.listing_selected_players()
        players_info = [
            (p["Player"].name, p["Player"].first_name, p["Player"].player_id)
            for p in self.tournament.participant_tournament
        ]
        self.view.display_selected_players_list(players_info)

    def is_player_already_selected(self, player):
        """Vérifie si le joueur est déjà dans le tournoi."""
        return any(p["Player"] == player for p in self.tournament.participant_tournament)

    def add_player_to_tournament(self, player):
        """Ajoute un joueur au tournoi."""
        self.tournament.participant_tournament.append({
            "Player": player,
            "Score": 0,
            "Adversaires": []
        })
        # Déléguer l'affichage à la vue
        self.view_tournaments.player_added_to_tournament(
            player.name,
            player.first_name,
            len(self.tournament.participant_tournament),
            MAX_PLAYERS)

    def save_tournament_to_json(self, tournament):
        """Enregiste ou met à jour un tournoi"""
        try:
            # Charge les tournois existants
            tournaments = self.load_tournaments_from_json()
            # Converti l'objet Tournament en dictionnaire avant de l'ajouter
            tournament_dict_data = tournament.tournament_dict()
            # Verifie si le tournois existe déjà dans la liste
            exist_tournament = next((
                t for t in tournaments if t["name"] == tournament.name), None)
            if exist_tournament:
                # Si le tournoi existe déjà, on met à jour les données
                tournaments.remove(exist_tournament)
            tournaments.append(tournament_dict_data)
            self.dump_tournaments(tournaments)
            self.view_tournaments.success_tournament_saved(tournament.name)
        except Exception as e:
            self.view_tournaments.error_saving(str(e))
            return

    def load_tournaments_from_json(self):
        """Charge les données du tournoi depuis un fichier JSON."""
        if os.path.exists(self.tournaments_file):
            with open(
                self.tournaments_file, "r", encoding="utf-8"
            ) as file:
                return json.load(file)
        return []

    def dump_tournaments(self, tournaments):
        """Sauvegarde la liste des tournois dans le fichier JSON."""
        with open(self.tournaments_file, "w", encoding="utf-8") as file:
            json.dump(tournaments, file, ensure_ascii=False, indent=4)

    def select_list_saved_tournaments(self, action_type="view"):
        """Sélectionne un tournoi sauvegardé parmi une liste."""
        if not os.path.exists(self.tournaments_file):
            self.view_tournaments.no_file()
            return None
        try:
            with open(self.tournaments_file, "r", encoding="utf-8") as file:
                existing_tournaments = json.load(file)
            if not existing_tournaments:
                self.view_tournaments.no_tournaments_in_json()
                return None
            # Affiche les tournois existants
            self.view_tournaments.display_tournament_list(existing_tournaments)
            # Boucle de sélection du tournoi
            while True:
                try:
                    tournament_index = int(
                        input("Entrez le numéro du tournoi à sélectionner: ")) - 1
                    if 0 <= tournament_index < len(existing_tournaments):
                        selected_tournament = existing_tournaments[tournament_index]
                        # Recrée l'objet Tournament
                        self.selected_tournament = self.recreate_tournament_controlleur(
                            selected_tournament, self.all_players
                        )
                        if not self.selected_tournament:
                            self.view_tournaments.tournament_not_built()
                            return None
                        # Affiche les informations du tournoi sélectionné
                        self.view_tournaments.display_tournament_info(selected_tournament)
                        if action_type == "view":
                            # Affichage des rounds et des matchs avec scores
                            self.display_tournament_rounds_and_matches(self.selected_tournament)
                            return None  # Quitte après avoir affiché les données
                        if action_type == "create_round":
                            # Propose de revenir à la liste des tournois  ou de créer un round
                            self.display_tournament_info(self.selected_tournament)
                            user_choice = self.view_tournaments.ask_start_round()
                            if user_choice == "o":
                                self.create_rounds(self.selected_tournament)
                                return  # Sort après avoir démarré le round
                            if user_choice == "n":
                                self.view_tournaments.back_to_menu()
                                return None  # Quitte la sélection
                    else:
                        self.view_tournaments.invalid_tournament_number()
                except ValueError:
                    self.view_tournaments.invalid_choice_entry()
        except FileNotFoundError:
            self.view_tournaments.no_file()
        except json.JSONDecodeError:
            self.view_tournaments.corrupted_file_jason()
        except KeyError as e:
            self.view_tournaments.key_error_missing_field(str(e))
        except Exception as e:
            self.view_tournaments.unexpected_error(str(e))
        return None

    def tournaments_file_exists(self):
        """message erreur vue"""
        if not os.path.exists(self.tournaments_file):
            self.view_tournaments.no_tournament_file_found()
            return False
        return True

    def display_tournament_info(self, selected_tournament):
        """
        Récupère les informations du tournoi et les envoie à la vue.
        """
        if not selected_tournament:
            self.view_tournaments.not_tournament()
            return
        # Prépare les participants pour l'affichage
        participants_table = []
        if selected_tournament.participant_tournament:
            for participant in selected_tournament.participant_tournament:
                player = participant["Player"]
                score = participant["Score"]
                # Récupére les player_id des adversaires
                adversaires_ids = []
                # Vérifie si c'est bien une liste
                if isinstance(participant.get("Adversaires"), list):
                    for adv in participant["Adversaires"]:
                        if isinstance(adv, int):  # Si c'est déjà un ID
                            adversaires_ids.append(adv)
                        elif hasattr(adv, 'player_id'):  # Si c'est un objet Player
                            adversaires_ids.append(adv.player_id)
                participants_table.append(
                    [player.name, player.first_name, player.player_id, score, adversaires_ids]
                )
            # Envoie les données à la vue"""
            tournament_data_table = selected_tournament.tournament_dict()
            self.view_tournaments.display_tournament_tabulate(
                tournament_data_table, participants_table
            )

    def create_rounds(self, selected_tournament):
        """Crée et démarre les rounds du tournoi"""
        if len(selected_tournament.rounds) >= int(selected_tournament.nb_round):
            self.view_tournaments.all_rounds_played()
            return  # On sort de la méthode immédiatement

        players = [
            p["Player"] for p in selected_tournament.participant_tournament
            if isinstance(p["Player"], Player)
        ]
        while len(selected_tournament.rounds) < int(selected_tournament.nb_round):
            round_number = len(selected_tournament.rounds) + 1
            self.view_tournaments.display_round_progress(
                len(selected_tournament.rounds), selected_tournament.nb_round
            )
            round_name = f"Round N°: {round_number}"
            round_i = Round(round_number, round_name)
            # Enregistre l'heure de début du round
            round_i.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.view_tournaments.display_round_start(round_name, round_i.start_time)
            if round_number == 1:
                random.shuffle(players)
            else:
                # Rounds suivants: Trie les joueurs par score décroissant
                players.sort(key=lambda p: next(
                    (entry["Score"] for entry in selected_tournament.participant_tournament
                        if entry["Player"] == p), 0), reverse=True
                )
                self.view_tournaments.display_round_object(round_i)
            round_i.matches = self.generate_matches(players, selected_tournament)
            # Ajoute le round au tournoi
            selected_tournament.rounds.append(round_i)
            if round_i.matches:
                self.view_tournaments.display_match_list_start(round_number)
                for match in round_i.matches:
                    p1 = match.player1
                    p2 = match.player2
                    p1_data = next(
                        p for p in selected_tournament.participant_tournament if
                        p["Player"].player_id == p1.player_id
                    )
                    p2_data = next(
                        p for p in selected_tournament.participant_tournament if
                        p["Player"].player_id == p2.player_id
                    )
                    if p2 not in p1_data["Adversaires"]:
                        p1_data["Adversaires"].append(p2)
                    if p1 not in p2_data["Adversaires"]:
                        p2_data["Adversaires"].append(p1)
                    self.view_tournaments.display_match_vs(p1, p2)
            # Attendre la confirmation de l'utilisateur pour terminer le round
            confirmation = self.view_tournaments.ask_end_of_round()
            if confirmation == "o":
                self.enter_scores(round_i, selected_tournament)
                self.display_tournament_info(selected_tournament)
            if round_number < int(selected_tournament.nb_round):
                continuer = self.view_tournaments.ask_start_next_round()
                if continuer != "o":
                    self.view_tournaments.tournament_stopped()
                    self.save_tournament_to_json(selected_tournament)
                    return
        self.view_tournaments.nb_rounds_reached()
        self.save_tournament_to_json(selected_tournament)
        return

    def enter_scores(self, round_i, selected_tournament):
        """Permet la saisie des scores d'un round et met à jour les joueurs."""
        # Vérifier que le tournoi existe
        if not selected_tournament:
            self.view_tournaments.not_tournament()
            return
        scores = self.view_tournaments.get_scores_from_user(round_i)
        for i, match in enumerate(round_i.matches):
            score1, score2 = scores[i]  # Récupérer les scores pour chaque match
            match.player1_score = score1
            match.player2_score = score2
            for participant in selected_tournament.participant_tournament:
                if participant["Player"].player_id == match.player1.player_id:
                    participant["Score"] += score1
                elif participant["Player"].player_id == match.player2.player_id:
                    participant["Score"] += score2
        round_i.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Affichage de fin de round via la vue
        self.view_tournaments.display_end_of_round(round_i.round_name, round_i.end_time)
        # Sauvegarde du tournoi après chaque round
        self.save_tournament_to_json(selected_tournament)

    def generate_matches(self, players, selected_tournament):
        """Genere les matchs controllant les paires de joeur unique pour un tournois """
        def can_pair(p1, p2):
            return not Match.already_played(p1, p2, selected_tournament.rounds)

        def valid_permutation(perm):
            tentative_matches = []
            for i in range(0, len(perm), 2):
                p1, p2 = perm[i], perm[i + 1]
                if can_pair(p1, p2):
                    tentative_matches.append(Match(p1, p2))
                else:
                    return None
            return tentative_matches

        for perm in permutations(players):
            matches = valid_permutation(perm)
            if matches:
                return matches

        # Si aucun appariement valide n'est trouvé
        self.view_tournaments.no_valid_pairs()
        return []

    def recreate_round(self, round_data, all_players):
        """Recrée un round à partir des données JSON."""
        round_i = Round(round_data["round_number"], round_data["round_name"])
        round_i.start_time = round_data["start_time"]
        round_i.end_time = round_data["end_time"]
        # Recréer les matchs à partir des données json"""
        for match_data in round_data["matches"]:
            match = self.recreate_match_controlleur(match_data, all_players)
            # Appel à la méthode du contrôleur
            round_i.matches.append(match)
        return round_i

    def recreate_match_controlleur(self, match_data, all_players):
        """Orchestre la reconstruction d'un match via la méthode statique de Match."""
        return Match.recreate_match(match_data, all_players)

    def recreate_tournament_controlleur(self, tournament_data, all_players):
        """Reconstitue un tournoi """
        try:
            tournament = Tournament.recreate_tournament(tournament_data, all_players)
            # Reconstruction des rounds via le contrôleur
            tournament.rounds = [
                self.recreate_round(round_data, all_players)
                for round_data in tournament_data.get("rounds", [])
            ]
            return tournament
        except (KeyError, TypeError, ValueError) as e:
            self.view_tournaments.error_rebuilding_tournament(e, tournament_data)
            return None

    def display_tournament_rounds_and_matches(self, tournament):
        """ Affichage des rounds et Matches pour un tournois.
        Args:
        tournament (Tournament): Le tournoi dont on veut afficher les informations
        """
        self.view_tournaments.display_title(tournament)
        for tourn_round in tournament.rounds:
            round_header = (
                f"Round {tourn_round.round_number}\n"
                f"DÉMARRÉ LE {tourn_round.start_time if tourn_round.start_time else 'Non démarré'}\n"
                f"TERMINÉ LE {tourn_round.end_time if tourn_round.end_time else 'En cours'}\n"
            )
            self.view_tournaments.display_round_header(round_header)
            # Construction du tableau des matchs
            match_table = []
            for match in tourn_round.matches:
                match_table.append([
                    f"{match.player1.name} {match.player1.first_name} {match.player1.player_id}",
                    match.player1_score,
                    f"{match.player2.name} {match.player2.first_name} {match.player2.player_id}",
                    match.player2_score
                ])
            self.view_tournaments.display_match_table(match_table)
