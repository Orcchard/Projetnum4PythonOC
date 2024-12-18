from tournament_mod import Tournament
from round_mod import Round
from match_mod import Match
from player_mod import Player
import random
from pprint import pprint
MATCH_SCORE = [(1, 0),(0.5, 0.5),(0, 1)]
# Liste des joueurs inscrits pour participer au tournois

all_players = [
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


tournament = Tournament("Championnat 2024", location="Paris", date_initial="01/01/2025", date_end="30/01/2025", nb_round=4, description="Premier tournois dans la capitale")
print("-" *120)
print(tournament)
print("-" *120)
random.shuffle(all_players)
for i in range(0, 8):
    tournament.participant_tournois.append({"Player":all_players[i], "Score":0, "Adversaires":[]})

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
        print("???")
        
    
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
        
        #sauvegarde des adversaires
        tournament.participant_tournois[i]["Score"] += match.player1_score
        tournament.participant_tournois[i+1]["Score"] +=match.player2_score
            
        
            #Ajout du match au round
    
        round_i.matches.append(match)
                
        """    for participant in tournament.participant_tournois:
            # Trouver le joueur 1 et ajouter son score
            if participant["Player"].player_id == match.player1.player_id:
                participant["Score"] += match.player1_score
            # Trouver le joueur 2 et ajouter son score
                elif participant["Player"].player_id == match.player2.player_id:
                    participant["Score"] += match.player2_score
        """
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
        print(" - " + adversaire.name+ " " + adversaire.first_name) 
    #print("Debug:", player["Adversaires"])

#Afficher le classement final
print("\nClassement des joueurs :")
print(f"{'Nom':<15}{'ID':<10}{'Score':<10}")
print("=" * 35)
for i, participant in enumerate(sorted_players, 1):
    print(f"{i}. {participant['Player'].name:<15} {participant['Player'].first_name:<10} {participant['Player'].player_id:<10} {participant['Score']:<5}")
"""
pprint(tournament.participant_tournois)
for participant in tournament.participant_tournois:
    print(f"Clés : {list(participant.keys())}")
    print(f"Valeurs : {participant}")
    print("-" * 40)
"""