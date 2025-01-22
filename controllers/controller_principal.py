"""Define the principal controller."""
from views.view_users import View  # Importer la vue ici si elle est dans un autre fichier
from models.player_mod import Player
import json

class ControllerPrincipal:
    """Principal controller."""

    def __init__(self):
        """Has a view, a list of players a tournament ."""
        self.view = View()
        self.all_players = [] 
        self.tournament = None  # Le tournoi courant
        self.players_file = "all_players_data.json"  # Fichier pour stocker les joueurs
    
      
    
    def run(self):
        """Run the game"""
        print("Chargement des joueurs...")
        self.all_players = self.load_players_from_file()
        
        if not self.all_players:
            print("Aucun joueur trouvé. Veuillez vérifier le fichier des joueurs.")
            return
        
        
        print(f"{len(self.all_players)} joueurs chargés avec succès.")
        # Appeler le menu principal
        self.display_menu()
        self.display_all_players()
        

    
    def load_players_from_file(self):
        """Charge les joueurs depuis le fichier JSON."""
        players_file = "all_players_data.json"
        try:
            with open(players_file, "r", encoding="utf-8") as file:
                players_data = json.load(file)
                # Retourner les données telles qu'elles sont ou les convertir en instances
                return [Player.deserialize_player(data) for data in players_data]
        except FileNotFoundError:
            print("Erreur : fichier de données des joueurs introuvable.")
            return []
        except Exception as e:
            print(f"Erreur lors du chargement des joueurs : {e}")
            return []
    
    def display_all_players(self):
        """Affiche tous les joueurs chargés."""
        print("\nListe des joueurs :")
        print(f"\nNombre total de joueurs : {len(self.all_players)}")
        for player in self.all_players:
            # Imprime le nombre total de joueurs
            print(player)
            
            

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
            
        
    def player_add(self):
        """Adding a new player and serialize in json file."""
        self.view.new_player_header()
        player_input_data = self.view.prompt_for_player()
           # Créer une instance de Player
        player = Player(
            name=player_input_data["name"],
            first_name=player_input_data["first_name"],
            date_of_birth=player_input_data["birth_date"],
            player_id=player_input_data["player_id"]
        )

        print(f"========{player}")
        print("Le joueur a été ajouté avec succès.")
        # Sérialiser les données du joueur
        player_data = player.player_dict()
        
        self.save_player_to_file(player_data)
        #Passe l'argument player_data à cette méthode save_player_to_file
        
        
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


    
        



        
        
       
        
    """
    #def get_players(self):
        #Get some players
       # while len(self.all_players) < 8:  # nombre maxi 8 joueurs
            

            if not player_datas:
                print("Erreur : Les données fournies sont invalides. Veuillez réessayer.")
                continue

            # Création et ajout du joueur
            try:
                # Valider et créer le joueur
                required_keys = ["name", "first_name", "player_id", "birth_date"]
                missing_keys = [key for key in required_keys if key not in player_datas]

                if missing_keys:
                    print(f"Erreur : Clés manquantes dans les données du joueur : {', '.join(missing_keys)}.")
                    continue

                player = Player(
                    name=player_datas["name"],
                    first_name=player_datas["first_name"],
                    player_id=player_datas["player_id"],
                    birth_date=player_datas["birth_date"],
                )

                self.all_players.append(player)
                print(f"Joueur {player.name} ajouté avec succès.")

            except Exception as e:
                print(f"Une erreur inattendue est survenue : {e}.")
        
    def serialize_players(self):
        #Sérialise les joueurs dans un fichier JSON
        # Sérialisation des joueurs : création de la liste de dictionnaires
        #all_players_data = [p.player_dict() for p in self.all_players]

        # Trier les joueurs par nom et prénom
        #all_players_data_sorted = sorted(all_players_data, key=lambda x: (x["name"], x["first_name"]))

        # Sauvegarder les données des joueurs dans un fichier JSON
        #with open("all_players_data.json", "w", encoding="utf-8") as jfile:
            #json.dump(all_players_data_sorted, jfile, ensure_ascii=False, indent=4)
        
        
    #def load_all_players_from_json(self, json_file_path="all_players_data.json"):   
        #Charger les données des joueurs depuis un fichier JSON
        #try:
            # Charger les données depuis le fichier JSON
            #with open(json_file_path, "r", encoding="utf-8") as file:
                #players_data = json.load(file)

            # Ajouter chaque joueur à la liste all_players
            #for player_datas in players_data:
                #self.all_players.append(player_datas)
                #print(all_players)
                
        #except FileNotFoundError:
            #print(f"Erreur : Le fichier '{json_file_path}' n'existe pas.")
        #except json.JSONDecodeError as e:
            #print(f"Erreur lors du décodage du fichier JSON : {e}")  
        

    

        

tournament = Tournament("Championnat 2024", location="Paris", date_initial="01/01/2025", date_end="30/01/2025", nb_round=4, description="Premier tournois dans la capitale")
print("-" *120)
print(tournament)
print("-" *120)
random.shuffle(all_players)
for i in range(0, 8):
    tournament.participant_tournois.append({"Player":all_players[i], 
                                            "Score":0, 
                                            "Adversaires":[]}
                                           )
    

# boucle et défininition des rounds 
for round_number in range(1, tournament.nb_round +1):
    round_name = f"====Round numéro: {round_number}===="
    round_i = Round(round_number, round_name)
    
    #organiser le tri des participants selon le round
    if round_number == 1:
        random.shuffle(tournament.participant_tournois)
        print("ça trie?")
    else:
        # Trie joueurs par ordre décroissant des scores
        tournament.participant_tournois = sorted(tournament.participant_tournois,
            key=lambda x: x["Score"],
            reverse=True
        )
        print("?????")
        
    
    #organisation des matchs dans le round
    for i in range(0,len(tournament.participant_tournois),2):
        player1 = tournament.participant_tournois[i]["Player"] #[Player] Récupère la valeur associée à la clé "Player".
        player2 = tournament.participant_tournois[i + 1]["Player"]

        match = Match(player1, player2, player1_score=0, player2_score=0)
        #Attribuer un score de facon aléatoire
        score = random.choice(MATCH_SCORE)
        match.player1_score = float(score[0])
        match.player2_score = float(score[1])
            
        #sauvegarde des adversaires
        tournament.participant_tournois[i]["Adversaires"].append(player2)
        tournament.participant_tournois[i+1]["Adversaires"].append(player1)
        
        #sauvegarde des Scores
        tournament.participant_tournois[i]["Score"] += match.player1_score
        tournament.participant_tournois[i+1]["Score"] +=match.player2_score
            
        
        #Ajout du match au round
    
        round_i.matches.append(match)
                
    #Ajouter les rounds au tournois de Paris
    tournament.rounds.append(round_i)
    
    #afficher les infos du round
    print()
    print("*" *50)
    print("Scores des participants pour les 4 tournois")    
    print()
    print(f"{round_name} :")
    print("-" *15)
    for match in round_i.matches:
        print(f"{match.player1.name} {match.player1.first_name} ({match.player1_score}) "
            f"VS {match.player2.name} {match.player2.first_name} ({match.player2_score})"
            )
    # Trier les joueurs par leur score final
sorted_players = sorted(
    tournament.participant_tournois,
    key=lambda x: x["Score"],
    reverse=True
)  # Pour trier du score le plus élevé au plus bas  

# Selection des 8 joueurs de maniere aleatoir à partir de all_players.
print("******* 8 Joueurs selectionnés pour le tournois de Paris*******")
print()
print(f"{'Nom':<8}{'Prénom':<10}{'ID':<8}{'Score':<5}")
print("-" * 50)
for player in tournament.participant_tournois:
    print(player["Player"].name + " " + player["Player"].first_name + " " + 
          player["Player"].player_id + " Score :" + str(player["Score"]))
    # Parcours des adversaires
    print("A affronté:")
    for adversaire in player["Adversaires"]:
        print(" - " + adversaire.name + " " + adversaire.first_name) 
    #print("Debug:", player["Adversaires"])

#Afficher le classement final
print("\nClassement des joueurs :")
print(f"{'Nom':<15}{'ID':<10}{'Score':<10}")
print("=" * 35)
for i, participant in enumerate(sorted_players, 1):
    print(f"{i}. {participant['Player'].name:<15} {participant['Player'].first_name:<10} {participant['Player'].player_id:<10} {participant['Score']:<5}")


#Impression pour test
for p in all_players:
    print(f"!!!!!!!!{p}!!!!!") 

#serialisation tournois
with open("tournament_data.json", "w", encoding="utf-8") as file:
    json.dump(tournament.tournament_dict(), file, ensure_ascii=False, indent=4)

print("================================données sauvegardées=====================================")
"""
"""Deserialisation"""

"""
# Recréer les objets Player
all_players = [Player(
    name=data["name"],
    first_name=data["first_name"],
    date_of_birth=data["date_of_birth"],
    player_id=data["player_id"]
) for data in players_data]

#impression pour test
for player in all_players:
    print(f"Nom : {player.name}, Prénom : {player.first_name}, Date de naissance : {player.date_of_birth}, ID : {player.player_id}")
    print((len(all_players)))
    
    
# Charger les données du tournoi depuis un fichier JSON
with open("tournament_data.json", "r", encoding="utf-8") as file:
    tournament_data = json.load(file)
    

def recreate_tournament(tournament_data, all_players):
    # Recréer les participants
    participant_tournois = []
    for participant in tournament_data["participant_tournois"]:
        player = next((p for p in all_players if p.player_id == participant["player"]), None)
        if player:
            participant_tournois.append({
                "Player": player,
                "Score": participant["score"],
                "Adversaires": [next((p for p in all_players if p.player_id == adv), None) for adv in participant["adversaires"]]
            })

    # Recréer les rounds
    rounds = [recreate_round(round_data, all_players) for round_data in tournament_data["rounds"]]

    # Recréer l'objet Tournament
    return Tournament(
        name=tournament_data["name"],
        location=tournament_data["location"],
        date_initial=tournament_data["date_initial"],
        date_end=tournament_data["date_end"],
        nb_round=tournament_data["nb_round"],
        description=tournament_data["description"]
    ).update_tournament_data(participant_tournois, rounds)

# Ajout d'une méthode pour mettre à jour les données du tournoi après création
def update_tournament_data(self, participant_tournois, rounds):
    self.participant_tournois = participant_tournois
    self.rounds = rounds
    #permet à la méthode de retourner l'objet une fois qu'elle a fini d'exécuter son travail.
    return self

Tournament.update_tournament_data = update_tournament_data
def recreate_round(round_data, all_players):
    matches = [recreate_match(match_data, all_players) for match_data in round_data["matches"]]
    return Round(
        round_number=round_data["round_number"],
        round_name=round_data["round_name"],
        start_time=round_data["start_time"],
        end_time=round_data["end_time"],
        matches=matches
    )
def print_tournament_details(tournament):
    print("\n=== Tournoi ===")
    print(f"Nom : {tournament.name}")
    print(f"Lieu : {tournament.location}")
    print(f"Date de début : {tournament.date_initial}")
    print(f"Date de fin : {tournament.date_end}")
    print(f"Description : {tournament.description}")
    print(f"Nombre de rounds prévus : {tournament.nb_round}")
    print("\n=== Participants ===")
    for participant in tournament.participant_tournois:
        player = participant["Player"]
        print(f"- {player.name} {player.first_name} (ID : {player.player_id})")
        print(f"  Score : {participant['Score']}")
        adversaires = ", ".join(
            [adversary.name for adversary in participant["Adversaires"] if adversary]
        )
        print(f"  Adversaires rencontrés : {adversaires if adversaires else 'Aucun'}")

    print("\n=== Rounds ===")
    for round_obj in tournament.rounds:
        print(f"Round {round_obj.round_number}: {round_obj.round_name}")
        print(f"  Début : {round_obj.start_time}")
        print(f"  Fin : {round_obj.end_time}")
        print("\n  Matches :")
        for match in round_obj.matches:
            print(f"    - {match.player1.name} vs {match.player2.name}")
            print(f"      Scores : {match.player1_score} - {match.player2_score}")

# Appeler la fonction pour afficher les détails
print_tournament_details(tournament)
"""