"""Define the principal controller."""
from views.view_users import View  
from views.view_tournaments import ViewTournament
from models.player_mod import Player
from models.tournament_mod import Tournament
import json
MAX_PLAYERS = 8


class ControllerPrincipal:
    """Principal controller."""

    def __init__(self):
        """Has a view, a list of players a tournament ."""
        self.view = View()
        self.view_tournaments = ViewTournament()
        #self.player = Player_input
        self.all_players = [] 
        self.tournament = None
        self.participant_tournament = []
        
        """Le tournoi courant"""
        self.players_file = "all_players_data.json"
        """Fichier pour stocker les joueurs"""
 
    def run(self):
        """Run the game"""
        print("Chargement des joueurs...")
        self.all_players = self.load_players_from_file() 
        """Chargement de la liste de joueurs dans all_players"""
        if not self.all_players:
            print("Aucun joueur trouvé. Veuillez vérifier le fichier des joueurs.")
            
        print(f"{len(self.all_players)} joueurs chargés avec succès.")
        self.display_menu()
        """Appeler le menu principal"""

    def display_menu(self):
        """Méthode pour démarrer le programme."""
        # Appeler l'entête principale
        self.view.main_header()
        # Afficher le menu principal
        self.view.menu()
        self.view.first_prompt()
        user_choice = input()
        """input() est une fonction intégrée de Python qui attend que l'utilisateur
            entre un texte via le clavier et appuie sur Entrée"""
        
        if user_choice == "1":
            self.player_add()
            
        elif user_choice == "2":
            self.new_tournament()
            
        elif user_choice == "5":
            print("à completer")
        
        else:
            print("Mauvaise saisie")
            
            
        
    def player_add(self):
        """Adding a new player and serialize in json file."""
        self.view.new_player_header()
        player_input_data = self.view.prompt_for_player()
        # Créer une instance de Player
        player = Player(
            name=player_input_data["name"],
            first_name=player_input_data["first_name"],
            date_of_birth=player_input_data["date_of_birth"],
            player_id=player_input_data["player_id"]
        )
        print(f"========{player}")
        print("Le joueur a été ajouté avec succès.")
        # Sérialiser les données du joueur
        player_data = player.player_dict()
        self.save_player_to_file(player_data)
        #Passe l'argument player_data à cette méthode save_player_to_file
        
        
        
        

    def load_players_from_file(self):
        """Charge les joueurs depuis le fichier JSON."""
        players_file = "all_players_data.json"
        try:
            with open(players_file, "r", encoding="utf-8") as file:
                players_data = json.load(file)
                # Retourne les données  en instances
                return [Player.deserialize_player(data) for data in players_data]
        except FileNotFoundError:
            print("Erreur : fichier de données des joueurs introuvable.")
            return []
        except Exception as e:
            print(f"Erreur lors du chargement des joueurs : {e}")
            return []
        self.display_all_players()

    
            
    def save_player_to_file(self, player_data):
        #Save player data to a JSON file, including existing players
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
            #Trier les joueurs par nom 
            players.sort(key=lambda x: x["name"].lower())  
            # Réécrire les données dans le fichier JSON
            with open(self.players_file, "w", encoding="utf-8") as file:
                json.dump(players, file, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"Erreur lors de la sauvegarde du fichier : {e}")
            
    def new_tournament(self):
        """Create a new tournament."""
        self.view_tournaments.tournament_new_header()
        tournament_input_data = self.view_tournaments.prompt_for_new_tournament()
        # Créer une instance de Tournament
        tournament = Tournament(
            name=tournament_input_data["name"],
            location=tournament_input_data["location"],
            date_initial=tournament_input_data["date_initial"],
            date_end=tournament_input_data["date_end"],
            description=tournament_input_data["description"],
            nb_round=tournament_input_data["nb_round"]
        )
        print(f"========{tournament}")
        print("Le tournoi a été créé avec succès.")
        print()
        self.select_participants_tournament()
        
        
    

    def display_all_players_with_num_rank(self):
        """Affiche all_players avec numéro incrémenté devant chaque joueur"""
        print("\nListe des joueurs :")
        for index, player in enumerate(self.all_players, start=1):
            print(f"{index}. {player}")  # Utilise __str__() implicitement
        
        
    def select_participants_tournament(self):
        """Sélectionne 8 joueurs en demandant les 3 premières lettres du nom"""

        while len(self.participant_tournament) < MAX_PLAYERS:
            # Demander les 3 premières lettres du nom du participant
            prefix =self. view.prompt_for_player_prefix()

            # Appel à la méthode letters_choice pour obtenir les joueurs correspondants
            matching_players = [player for player in self.all_players if player.name.lower().startswith(prefix)]
            # Si aucun joueur n'est trouvé, on recommence
            if not matching_players:
                print("Aucun joueur trouvé avec ce préfixe. Veuillez réessayer.")
                continue

            # Afficher les joueurs correspondants avec un numéro incrémenté
            print("\nJoueurs correspondants :")
            for index, player in enumerate(matching_players, start=1):
                print(f"{index}. {player}")

        # Demander à l'utilisateur de choisir un joueur parmi ceux qui correspondent
            try:
                selection = int(input(f"Choisissez un joueur (1 à {len(matching_players)}), sélectionnés : {len(self.participant_tournament)}/8 : "))
                if 1 <= selection <= len(matching_players):
                    selected_player = matching_players[selection - 1]
                    if selected_player not in self.participant_tournament:
                        self.participant_tournament.append(selected_player)
                        print(f"Joueur {selected_player.name} {selected_player.first_name} sélectionné.")
                    else:
                        print("Ce joueur a déjà été sélectionné.")
                else:
                    print("Sélection invalide.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        # Afficher les joueurs sélectionnés
        print("\nJoueurs sélectionnés :")
        for player in self.participant_tournament:
            print(f"{player.name} {player.first_name} (ID : {player.player_id})")

        return self.participant_tournament   
        