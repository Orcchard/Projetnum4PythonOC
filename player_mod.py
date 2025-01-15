class Player: 
    def __init__(self, name, first_name, date_of_birth, player_id):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.player_id = player_id
        

    def __str__(self):
        return f"Nom: {self.first_name}, Prenom: {self.name}, Date de Naissance: {self.date_of_birth}, ID: {self.player_id}"

    """serialise les joueurs"""
    def player_dict(self):
        return{
            "name" : self.name,
            "first_name" : self.first_name,
            "date_of_birth" : self.date_of_birth,
            "player_id" : self.player_id
        }

        




