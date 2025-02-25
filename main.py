"""Entry point."""

from models.player_mod import Player
from controllers.controller_principal import ControllerPrincipal
from views.view_users import View
from views.view_tournaments import ViewTournament


def main():
    game = ControllerPrincipal()
    """instancie le controller_principal"""
    game.run()
    """fait executer le programme run du controller_principal"""


if __name__ == "__main__":
    main()
