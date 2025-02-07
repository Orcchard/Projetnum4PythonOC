"""Define the principal controller."""
from views.view_users import View
from views.view_tournaments import ViewTournament
from models.player_mod import Player
from models.tournament_mod import Tournament
import json
import os
MAX_PLAYERS = 8


class ControllerPrincipal:
    """Principal controller."""

    def __init__(self):
        """Has a view, a list of players a tournament ."""
        self.view = View()
        self.view_tournaments = ViewTournament()
        self.all_players = []
        self.tournament = None
        self.participant_tournament = []

        """Le tournoi courant"""
        self.players_file = "all_players_data.json"
        """Fichier pour stocker les joueurs"""

    def run(self):
        """Run the game"""
        print("Chargement des joueurs...")
        self.all_players = self.load_players_from_js_file()
        """Chargement de la liste de joueurs dans all_players"""
        if not self.all_players:
            print(
                "Aucun joueur trouvé."
                "Veuillez vérifier le fichier des joueurs"
            )
            print(f"{len(self.all_players)} joueurs chargés avec succès.")
        # Charger les tournois existants
        self.load_tournament_from_json()  # Charger les tournois à ce moment
        self.display_menu()
        """Appeler le menu principal"""

    def load_players_from_js_file(self):
        """Charge les joueurs depuis le fichier JSON."""
        try:
            with open(self.players_file, "r", encoding="utf-8") as file:
                players_data = json.load(file)
                # Retourne les données  en instances
                return [Player.recreate_player(data)
                        for data in players_data
                        ]
        except FileNotFoundError:
            print("Erreur : fichier de données des joueurs introuvable.")
            return []
        except Exception as e:
            print(f"Erreur lors du chargement des joueurs : {e}")
            return []

    def display_menu(self):
        """Méthode pour démarrer le programme."""
        # Appeler l'entête principale
        self.view.main_header()
        # Afficher le menu principal
        self.view.menu()
        self.view.first_prompt()
        user_choice = input()
        """
        input() est une fonction intégrée attend la saisie
        via le clavier et appuie sur Entrée
        """
        if user_choice == "1":
            self.player_add_input()
        elif user_choice == "2":
            self.new_tournament_input()
        elif user_choice == "5":
            print("à completer")
        else:
            print("Mauvaise saisie")

    def player_add_input(self):
        """Adding a new player."""
        self.view.new_player_header()
        player_input_data = self.view.prompt_for_player()
        # Créer une instance de Player en utilisant recreate_player
        player = Player.recreate_player(player_input_data)
        print(f"========{player}")
        print("Le joueur a été ajouté avec succès.")
        # Sérialiser les données du joueur
        player_data = player.player_dict()
        # Mettre à jour le fichier all_players avec le nouveau joueur
        self.record_new_player(player_data)

    def record_new_player(self, player_data):
        """Met à jour le fichier all_players en ajoutant un nouveau joueur."""
        try:
            # Charger les données existantes du fichier JSON afin de les lire
            try:
                with open(self.players_file, "r", encoding="utf-8") as file:
                    players = json.load(file)
            except FileNotFoundError:
                # Si le fichier n'existe pas, on crée une liste vide
                players = []
            # Ajouter le nouveau joueur
            players.append(player_data)
            """Trier les joueurs par nom"""
            players.sort(key=lambda x: x["name"].lower())
            # Réécrire les données dans le fichier JSON
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
        # Créer une instance de Tournament
        self.tournament = Tournament(
            name=tournament_input_data["name"],
            location=tournament_input_data["location"],
            date_initial=tournament_input_data["date_initial"],
            date_end=tournament_input_data["date_end"],
            description=tournament_input_data["description"],
            nb_round=tournament_input_data["nb_round"]
        )
        print(f"========{self.tournament}")
        print("Le tournoi a été créé avec succès.")
        print()
        """Charger les tournois existants"""
        self.save_tournament_to_json()
        """Sauvegarder tous les tournois, y compris le nouveau"""
        self.load_tournament_from_json()

    def save_tournament_to_json(self, filename="tournament_data.json"):
        """
        Sauvegarde la liste des tournois dans un fichier JSON.
        Utilise la méthode tournament_dict() de la classe Tournament.
        """
        try:
            tournaments = []
            """charger les anciens tournois"""
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    try:
                        data = json.load(file)
                        if isinstance(data, list):
                            """Vérifie si c'est une liste"""
                            tournaments = data
                        else:
                            print(
                                "Format de fichier incorrect,réinitialisation."
                                )
                    except json.JSONDecodeError:
                        print("Erreur de décodage JSON, fichier corrompu.")

            """Ajouter le tournoi actuel à la liste"""
            tournaments.append(self.tournament.tournament_dict())

            """ Sauvegarder les tournois (anciens + nouveau)."""
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(tournaments, file, ensure_ascii=False, indent=4)

            print(f"Données sauvegardées avec succès dans {filename}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier : {e}")
            # Sauvegarder les données dans un fichier JSON

    def load_tournament_from_json(self, filename="tournament_data.json"):
        """
        Charge les données du tournoi depuis un fichier JSON.
        Utilise la méthode recreate_tournament de la classe Tournament.
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                raw_data = file.read()
                print(f"Contenu brut du fichier : {raw_data}")
                """
                Ajout pour le debug
                data = json.loads(raw_data)
                Utiliser `loads` pour voir si ça plante ici
                """
                data = json.load(file)
            if not isinstance(data, list):
                print("Le format du fichier est invalide.")
                return
            self.tournaments = []
            """ Stocke tous les tournois chargés"""
            for tournament_data in data:
                tournament = Tournament.recreate_tournament(tournament_data)
                """recréer les joueurs associés au tournois"""
                if "participant_tournament" in tournament_data:
                    tournament.participant_tournament = [
                        Player.recreate_player(player_data) for player_data
                        in tournament_data["participant_tournament"]
                    ]
                self.tournament.append(tournament)
            if self.tournaments:
                """Assigner les précédents tournois chargés"""
                self.tournament = self.tournaments[-1]
                """ Prend le dernier tournoi chargé"""
                print(
                    f"{len(self.tournaments)}"
                    "tournois chargés depuis {filename}."
                )
            print(f"Données chargées avec succès depuis {filename}.")
        except FileNotFoundError:
            print(f"Erreur : le fichier {filename} est introuvable.")
        except Exception as e:
            print(f"Erreur lors du chargement du fichier : {e}")
        self.select_participants_tournament()

    def select_participants_tournament(self):
        """
        Sélectionne 8 joueurs en saisissant
        les 3 premières lettres du nom.
        """
        if not self.tournament:
            print("Aucun tournoi n'a été créé.")
            return

        while len(self.participant_tournament) < MAX_PLAYERS:
            """Demander les 3 premières lettres du nom du participant"""
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
            # Afficher les joueurs correspondants avec un numéro incrémenté
            print("\nJoueurs correspondants :")
            for index, player in enumerate(matching_players, start=1):
                print(f"{index}. {player}")

            """Demander à l'utilisateur de choisir un joueur par numéro"""
            try:
                selection = int(
                    input(
                        f"Choisissez un joueur (1 à {len(matching_players)}),"
                        f"saisis : {len(self.participant_tournament)}/8 : "
                        )
                    )
                if 1 <= selection <= len(matching_players):
                    selected_player = matching_players[selection - 1]
                    """Les listes en Python sont indexées à partir de 0"""
                    if selected_player not in self.participant_tournament:
                        self.participant_tournament.append(selected_player)
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
        # Ajouter les participants au tournoi
        self.tournament.players = self.participant_tournament
        # Afficher les joueurs sélectionnés
        print("\nJoueurs sélectionnés :")
        for player in self.participant_tournament:
            print(
                f"({player.name} {player.first_name})"
                f"(ID : {player.player_id})"
                )
        # Sauvegarder le tournoi avec les participants
        self.save_tournament_to_json
