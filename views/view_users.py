
class View:
    def main_header(self):
        #Header before the main menu
        #self.clear_screen()
        print("\t**********************")
        print("\t* Tournois echec  *")
        print("\t**********************\n")
        
    
    def menu(self):
        #Display the main menu with some data info
        #num_of_players = self.number_of_player()
        print("\nMENU PRINCIPAL")
        print("1. Créer un joueur")
        print("2. Créer un tournoi")
        print("3. Editer un rapport")
        print("4. Supprimer un joueur ")
        print("\n5. Quitter le programme")
        print()

    #def number_of_players(self, all_players):
        """Récupère le nombre de joueurs"""
        #return len(all_players)
        
        
        def input_player_name(self):
        """Input for new player's last name."""
        return input("Nom du joueur : ").capitalize()
    
        def player_first_name_update(self, first_name):
        """Update player's first name."""

        def input_player_id(self):
        """Input for player's ID"""
        return input("\nIdentifiant du joueur (2 Lettres majuscules et 5 nombres): ").upper()