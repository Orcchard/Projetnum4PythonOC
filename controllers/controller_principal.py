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
        self.display_menu_principal()
        """AppeL le le menu principal"""

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
            print("Erreur: fichier de données des joueurs introuvable.")
            return []
        except Exception as e:
            print(f"Erreur lors du chargement des joueurs: {e}")
            return []

    def display_menu_principal(self):
        """
        Méthode pour démarrer le programme.Affiche le menu"""
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
                pass
            elif user_choice == "4":
                pass
            elif user_choice == "5":
                self.view.clear_screen()
                self.select_list_saved_tournaments()
            elif user_choice == "6":
                self.view_tournaments.display_message("à completer")
            else:
                self.view_tournaments.display_message("Mauvaise saisie")
            input("\nAppuyez sur Entrée pour continuer...")

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
        """Recupère la création du tournois saisi par l'utilisateur"""
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
                "Erreur: Les dates doivent être renseignées !"
            )
            return
        """Crée une instance de Tournament"""
        tournament = Tournament.recreate_tournament(
            tournament_input_data, self.all_players
            )
        """Affiche les informations après la création du tournoi."""
        self.view_tournaments.display_message(f"Nombre de joueurs chargés: {len(self.all_players)}")
        self.tournament = tournament
        self.view_tournaments.display_message(f"\n========{self.tournament}")
        self.view_tournaments.display_message("Le tournoi a été créé avec succès.")
        self.select_participants_tournament()
        """
        Sélectionne les participants immédiatement
        après la création du tournoi
        """

    def select_participants_tournament(self):
        """
        Sélectionne 8 joueurs en saisissant
        les 3 premières lettres du nom.
        """
        if not self.tournament:
            self.view_tournaments.display_alerte("Aucun tournoi n'a été créé.")
            return
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
            self.view_tournaments.display_message("Erreur : 3 lettres minimum !")

    def find_matching_players(self, prefix):
        """Retourne les joueurs correspondant au préfixe."""
        matching = [p for p in self.all_players if p.name.lower().startswith(prefix)]
        if not matching:
            self.view_tournaments.display_message("Aucun joueur trouvé. Réessayez.")
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
                self.view_tournaments.display_message("Joueur déjà sélectionné.")
            else:
                self.add_player_to_tournament(selected_player)
        except (ValueError, IndexError):
            self.view_tournaments.display_message("Entrée invalide.")

    def display_selected_players(self):
        """Affiche les participants sélectionnés."""
        self.view_tournaments.display_message("\nJoueurs sélectionnés:")
        for p in self.tournament.participant_tournament:
            player = p["Player"]
            print(f"{player.name} {player.first_name} (ID: {player.player_id})")

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
        print(f"Joueur {player.name} {player.first_name} ajouté !")
        print(
            f"{len(self.tournament.participant_tournament)} "
            f"joueurs sélectionné(s) sur {MAX_PLAYERS}"
            )

    def save_tournament_to_json(self, tournament):
        """Enregiste ou met à jour un tournoi"""
        try:
            """Charge les tournois existants"""
            tournaments = self.load_tournaments_from_json()
            """Converti l'objet Tournament en dictionnaire avant de l'ajouter"""
            tournament_dict_data = tournament.tournament_dict()
            """Ajout du nouveau tournoi à la liste"""
            tournaments.append(tournament_dict_data)
            # Sauvegarder les tournois mis à jour
            self.dump_tournaments(tournaments)
            self.view_tournaments.display_message(
                f"Le tournoi {tournament.name} et ses données ont été sauvegardés avec succès."
                )
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier : {e}")
            self.display_menu_principal()  # Retour au menu principal en cas d'erreur

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

    def select_list_saved_tournaments(self):
        """Sélectionne un tournoi sauvegardé parmi une liste."""
        if not os.path.exists(self.tournaments_file):
            self.view_tournaments.display_message("Aucun fichier de tournois trouvé")
            return None
        try:
            with open(self.tournaments_file, "r", encoding="utf-8") as file:
                existing_tournaments = json.load(file)
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
                    input("Entrez le numéro du tournoi à sélectionner: ")) - 1
                if 0 <= tournament_index < len(existing_tournaments):
                    selected_tournament = existing_tournaments[
                        tournament_index]
                    self.view_tournaments.display_message(
                        f"Tournoi {selected_tournament["name"]} sélectionné avec succès !")
                    """recréé l'objet Tournament"""
                    self.selected_tournament = Tournament.recreate_tournament(
                        selected_tournament, self.all_players
                    )
                    if not self.selected_tournament:
                        self.view_tournaments.display_message(
                            "Erreur : le tournoi n'a pas pu être recréé."
                            )
                        return None
                    """Affiche les informations du tournoi sélectionné"""
                    self.display_tournament_info(self.selected_tournament)
                    return self.selected_tournament
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
                f"Erreur lors de la sélection du tournoi: {e}"
                )
        return None

    def display_tournament_info(self, selected_tournament):
        """
        Récupère les informations du tournoi et les envoie à la vue. """
        if not self.selected_tournament:
            self.view_tournaments.not_tournament()
            return
        """Prépare les participants pour l'affichage"""
        participants_table = []
        if self.selected_tournament.participant_tournament:
            for participant in self.selected_tournament.participant_tournament:
                player = participant["Player"]
                score = participant["Score"]
                """Récupére les player_id des adversaires"""
                adversaires_ids = [
                    adv.player_id for adv in participant["Adversaires"]]
                participants_table.append([
                    player.name, player.first_name,
                    player.player_id, score, adversaires_ids
                ])
            """Envoie les données à la vue"""
            tournament_data_table = self.selected_tournament.tournament_dict()
            self.view_tournaments.display_tournament_tabulate(
                tournament_data_table, participants_table
                )
            """ La vue Demande à l'utilisateur s'il souhaite démarrer un round """
            response = self.view_tournaments.ask_start_round()
            if response == "o":
                self.create_rounds(selected_tournament)
            else:
                print("Démarrage de round annulé.")

    def create_rounds(self, selected_tournament):
        """Crée et démarre les rounds du tournoi"""
        # Vérifier que les joueurs sont bien des objets Player
        players = [
            p["Player"] for p in selected_tournament.participant_tournament 
            if isinstance(p["Player"], Player)
            ]
        for p in players:
            print(type(p), p)
        if not players:
            print("Erreur : Aucun joueur valide trouvé dans le tournoi.")
            return
        round_number = len(selected_tournament.rounds) + 1
        if round_number > int(selected_tournament.nb_round):
            print("Le nombre maximum de rounds a été atteint.")
            return
        round_name = f"Round {round_number}"
        round_i = Round(round_number, round_name)
        # Enregistrer l'heure de début du round
        round_i.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.view_tournaments.display_message(
            f"\n Début du {round_name} à {round_i.start_time}\n"
            )
        if round_number == 1:
            random.shuffle(players)
        else:
            """Rounds suivants: Trie les joueurs par score décroissant"""
            players.sort(key=lambda p: next(
                (entry["Score"] for entry in self.tournament.participant_tournament
                    if entry["Player"] == p), 0), reverse=True
                )
        # Gestion des adversaires
        adversaires = {p.player_id: set() for p in players}
        available_players = players.copy()
        while available_players:
            player1 = available_players.pop(0)
            player2 = next((
                p for p in available_players if p.player_id
                not in adversaires[player1.player_id]), None)
            """Cherche un adversaire qui n'a pas encore joué contre player1"""
            if player2:
                print(player1)
                print(player2)
                available_players.remove(player2)
                round_i.matches.append(Match(player1, player2))
                print(f"Matchs créés pour le Round : {[(match.player1.player_id, match.player2.player_id) for match in round_i.matches]}")
                """Mettre à jour l'historique des adversaires"""
                adversaires[player1.player_id].add(player2.player_id)
                adversaires[player2.player_id].add(player1.player_id)
            # Ajouter le round au tournoi
        selected_tournament.rounds.append(round_i)
        # Afficher les matchs du round
        if round_i.matches:
            for match in round_i.matches:
                print(f"{match.player1.name} {match.player1.first_name} VS  {match.player2.name} {match.player2.first_name}")
            # Appel de la saisie des scores
            self.enter_scores(round_i, selected_tournament)
        else:
            print("Aucun match n'a été créé pour ce round.")

    def enter_scores(self, round_i, selected_tournament):
        """Permet la saisie des scores d'un round et met à jour les joueurs."""
        # Vérifier que le tournoi existe
        if not selected_tournament:
            self.view_tournaments.display_message("Aucun tournoi sélectionné.")
            return
        scores = self.view_tournaments.get_scores_from_user(round_i)
        for i, match in enumerate(round_i.matches):
            score1, score2 = scores[i]  # Récupérer les scores pour chaque match
            match.player1_score = score1
            match.player2_score = score2
            for participant in selected_tournament.participant_tournament:
                if participant["Player"] == match.player1:
                    participant["Score"] += int(score1)
                if participant["Player"] == match.player2:
                    participant["Score"] += int(score2)

        round_i.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n✅ Fin du {round_i.round_name} à {round_i.end_time}\n")
        # Sauvegarde du tournoi après chaque round
        self.save_tournament_to_json(selected_tournament)

    def find_player_by_id(self, player_id):
        """Retrouve un joueur par son ID dans la liste all_players."""
        for player in self.all_players:
            if player.player_id == player_id:
                return player
        return None

    def check_duplicate_tournament_name(self, tournament_name):
        """Vérifie si un tournoi avec ce nom existe déjà."""
        try:
            with open(self.tournaments_file, "r", encoding="utf-8") as file:
                existing_tournaments = json.load(file)
            return any(t["name"] == tournament_name for t in existing_tournaments)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erreur lors de la vérification des doublons : {e}")
            return False  # On considère qu'aucun tournoi n'existe en cas d'erreur
