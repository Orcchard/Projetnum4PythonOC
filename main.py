"""Entry point."""
from controllers.controller_principal import ControllerPrincipal


def main():
    """A commenter"""
    game = ControllerPrincipal()
    """instancie le controller_principal"""
    game.run()
    """fait executer le programme run du controller_principal"""


if __name__ == "__main__":
    main()
