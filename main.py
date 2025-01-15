# The above code is a Python script that simulates a tournament with multiple rounds of matches
# between players. Here is a summary of what the code does:
from tournament_mod import Tournament
from round_mod import Round
from match_mod import Match
from player_mod import Player
import random
from pprint import pprint
MATCH_SCORE = [(1, 0),(0.5, 0.5),(0, 1)]
import json
# Liste des joueurs inscrits pour participer au tournois

all_players = [
Player(name="TESTNOM", first_name="TESTPRENOM", date_of_birth="15-12-1999", player_id="AZ5657"),
Player(name="Gourgues", first_name="Benjamin", date_of_birth="15-12-1952", player_id="AA34567"),
Player(name="Zidi", first_name="Dahlia", date_of_birth="14- 06-1960", player_id="AA98765"),
Player(name="Totem", first_name="Louise", date_of_birth="04- 07-1938", player_id="AB67854"),
Player(name="Marceau", first_name="Yvette", date_of_birth="23- 07-1958", player_id="AZ36873"),
Player(name="Lachaise", first_name="Gertrude", date_of_birth="04- 04-1965", player_id="VB34523"),
Player(name="Dumard", first_name="Louis", date_of_birth="07-11-2000", player_id="DZ87634"),
Player(name="Dumard", first_name="Nils", date_of_birth="24-12-1994", player_id="AA02345"),
Player(name="Pillet", first_name="Marie-Odile", date_of_birth="20-01-1963", player_id="AC12675"),
Player(name="Lecorvec", first_name="Danielle", date_of_birth="17-10-1957", player_id="AB27654"),
Player(name="Fouad", first_name="Nicole", date_of_birth="12-11-1973", player_id="AA87698"),
Player(name="Fourmond", first_name="Valérie", date_of_birth="07-04-1967", player_id="AZ65373"),
Player(name="Oussov", first_name="Leo", date_of_birth="03-10-1975", player_id="YU76584"),
Player(name="Vieille", first_name="Thomas", date_of_birth="03-05-1963", player_id="AA99087"),
Player(name="Dupont", first_name="Clementine", date_of_birth="13-03-1974", player_id="AC98456"),
Player(name="Dupontel", first_name="Gilles", date_of_birth="13-03-1975", player_id="AC98459"),
Player(name="Dupuis", first_name="Gauthier", date_of_birth="23-11-1975", player_id="AX67990"),
Player(name="Du Chemin", first_name="Gael", date_of_birth="23-11-1978", player_id="AX66990"),
Player(name="Durand", first_name="Gaston", date_of_birth="23-01-1978", player_id="AX66890"),
Player(name="Martin", first_name="Catherine", date_of_birth="23-06-1978", player_id="AD66898"),
Player(name="Martinez", first_name="Catherine", date_of_birth="23-08-1978", player_id="AD67898"),
Player(name="Moreau", first_name="Catherine", date_of_birth="22-09-1990", player_id="AN67898"),
Player(name="Anton", first_name="Nicole", date_of_birth="25-04-1990", player_id="AN57898"),
Player(name="Antonin", first_name="Serge", date_of_birth="04-04-1990", player_id="AN57888"),
Player(name="Antonin", first_name="Matteo", date_of_birth="04-04-1998", player_id="AV57867"),
Player(name="Vanderloof", first_name="Maia", date_of_birth="04-04-2000", player_id="AV57855"),
Player(name="Vita", first_name="Marguerite", date_of_birth="07-02-2000", player_id="AV57858"),
Player(name="Vacca", first_name="Maya", date_of_birth="07-02-2002", player_id="AM45095"),
Player(name="Vourc'h", first_name="Madeleine", date_of_birth="07-03-2002", player_id="AM45870"),
Player(name="Vignal", first_name="Mady", date_of_birth="07-09-2002", player_id="AM46856"),
Player(name="Vignali", first_name="Patrice", date_of_birth="07-09-1956", player_id="AM39675"),
Player(name="De girard", first_name="Patricia", date_of_birth="07-09-1958", player_id="AT78654"),
Player(name="Millard", first_name="Patrick", date_of_birth="07-11-1968", player_id="AT78674"),
Player(name="Millon", first_name="Pedro", date_of_birth="07-11-1978", player_id="AT63208"),
Player(name="Munchen", first_name="Pietro", date_of_birth="07-11-1988", player_id="AT63567"),
Player(name="Mathieu", first_name="Pierre", date_of_birth="07-11-2004", player_id="AU56340"),
Player(name="Garnieri", first_name="Penelope", date_of_birth="14-01-2004", player_id="AU89765"),
Player(name="Garnier", first_name="Veronique", date_of_birth="14-01-2000", player_id="AU89789"),
Player(name="Fournier", first_name="Vera", date_of_birth="15-02-2000", player_id="AV73789"),
Player(name="Labia", first_name="Valérie", date_of_birth="17-07-1999", player_id="AV09789"),
Player(name="Vectin", first_name="Victoire", date_of_birth="17-07-1990", player_id="AV89765"),
Player(name="Bernard", first_name="Victorine", date_of_birth="17-07-1991", player_id="AT45398"),
Player(name="Cousin", first_name="Violette", date_of_birth="17-07-1992", player_id="AT87698"),
Player(name="Brebion", first_name="Vincent", date_of_birth="13-03-1973", player_id="AC45987")
]

for p in all_players:
    print(f"---{p}---")

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

#serialisation des joueurs
all_players_data = [p.player_dict() for p in all_players]
all_players_data_sorted = sorted(all_players_data,key=lambda x: (x["name"], x["first_name"]))
with open("all_players_data.json", "w", encoding="utf-8") as jfile:
    json.dump(all_players_data_sorted, jfile, ensure_ascii=False, indent=4)
    jfile.write('\n')
#Impression pour test
for p in all_players:
    print(f"!!!!!!!!{p}!!!!!")

#serialisation tournois
with open("tournament_data.json", "w", encoding="utf-8") as file:
    json.dump(tournament.tournament_dict(), file, ensure_ascii=False, indent=4)
    
print("================================données sauvegardées=====================================")

"""Deserialisation"""
# Charger les données des joueurs depuis un fichier JSON
with open("all_players_data.json", "r", encoding="utf-8") as file:
    players_data = json.load(file)

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