"""Define the principal controller."""
from views.view_users import View  
from views.view_tournaments import ViewTournament
from models.player_mod import Player
from models.tournament_mod import Tournament
import json

class ControllerPrincipal:
    """Principal controller."""

    def __init__(self):
        """Has a view, a list of players a tournament ."""
        self.view = View()
        self.view_tournaments = ViewTournament()
        self.all_players = [] 
        self.tournament = None  
        """Le tournoi courant"""
        self.players_file = "all_players_data.json"
        """Fichier pour stocker les joueurs"""
 
    def run(self):
        """Run the game"""
        print("Chargement des joueurs...")
        self.all_players = self.load_players_from_file() 
        """appel de la methode chargement de la liste de joueurs"""
        if not self.all_players:
            print("Aucun joueur trouvé. Veuillez vérifier le fichier des joueurs.")
            return
        print(f"{len(self.all_players)} joueurs chargés avec succès.")
        """Appeler le menu principal"""
        self.display_menu()

    

    def display_menu(self):
        """Méthode pour démarrer le programme."""
        # Appeler l'entête principale
        self.view.main_header()
        # Afficher le menu principal
        self.view.menu()
        self.view.first_prompt()
        user_choice = input()
        
        if user_choice == "1":
            self.player_add()
            
        if user_choice == "2":
            self.new_tournament()
        
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
        #player = Player.deserialize_player(player_input_data)
        print(f"========{player}")
        print("Le joueur a été ajouté avec succès.")
        # Sérialiser les données du joueur
        player_data = player.player_dict()
        self.save_player_to_file(player_data)
        #Passe l'argument player_data à cette méthode save_player_to_file
        self.display_all_players()
        
        
        

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

    
            
    def save_player_to_file(self, player_data):
        #Save player data to a JSON file, including existing players
        try:
            # Charger les données existantes du fichier JSON
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
        print("Selectionnez 8 participants pour ce tournois")
        self.display_all_players()
        
    def saisie_participant_tournament(self):
        random.shuffle(all_players)
        for i in range(0, 8):
            tournament.participant_tournois.append({"Player":all_players[i], 
                                                "Score":0, 
                                                "Adversaires":[]}
                                                )
        
    def display_all_players(self):
        """Affiche tous les joueurs chargés."""
        print("\nListe des joueurs :")
        print(f"\nNombre total de joueurs : {len(self.all_players)}")
        for player in self.all_players:
            # Imprime le nombre total de joueurs
            print(player)