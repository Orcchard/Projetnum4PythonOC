"""Module de gestion des joueurs pour un système de tournois d'échecs.
Ce module définit la classe Player qui représente un joueur participant à un tournoi,
avec ses informations personnelles et des méthodes de sérialisation.
"""


class Player:
    """défini un joueur participant à un tournoi.
    Attributes:
        name (str): Nom de famille du joueur.
        first_name (str): Prénom du joueur.
        date_of_birth (str): Date de naissance au format JJ/MM/AAAA.
        player_id (str): Identifiant unique du joueur.
    """

    def __init__(self, name, first_name, date_of_birth, player_id):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.player_id = player_id

    def __str__(self):
        """Retourne une représentation lisible de l'objet joueur"""
        return (
                f"Nom: ({self.name}, Prenom: {self.first_name},"
                f" Date de Naissance: ({self.date_of_birth},"
                f"ID: {self.player_id}"
            )

    def player_dict(self):
        """Serialisation des données du joueur"""
        return {
            "name": self.name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "player_id": self.player_id
        }

    def recreate_player(self, data):
        """Reconstruction des objets players"""
        return Player(
            name=data["name"],
            first_name=data["first_name"],
            date_of_birth=data["date_of_birth"],
            player_id=data["player_id"]
        )
