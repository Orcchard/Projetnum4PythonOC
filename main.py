"""Entry point."""

from models.player_mod import Player
from controllers.controller_principal import Controller
from views.view_utilisateurs import View

game = Controller()

"""instancie le controller_principal"""
game.run()
"""fait executer le programme run du controller_principal"""

if __name__ == "__main__":
    main()
