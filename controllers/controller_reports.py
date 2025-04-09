"""Define the report controller."""
import json
import os
import random
from datetime import datetime
from tabulate import tabulate


from views.view_users import View
from views.view_tournaments import ViewTournament
from views.view_reports import ViewReports
from models.player_mod import Player
from models.tournament_mod import Tournament
from models.round_mod import Round
from models.match_mod import Match




class ControllerReports:
    """Report controller."""

    def __init__(self):
        """Initialise le controler  ."""
        self.view = View()
        self.view_tournaments = ViewTournament()
        self.view_reports = ViewReports()


    def display_menu_principal(self):
        """
        Méthode pour démarrer le programme.Affiche le menu"""
        while True:
            self.view.clear_screen()
            self.view.main_header()
            self.view.menu()
            self.view.first_prompt()
            user_choice = input()
            if user_choice == "1":
                self.player_add_input()
            elif user_choice == "2":
                self.new_tournament_input()
            elif user_choice == "3":
                self.select_list_saved_tournaments(action_type="view")
                # L'utilisateur choisit un tournoi
            elif user_choice == "4":
                pass
            elif user_choice == "5":
                self.view.clear_screen()
                self.select_list_saved_tournaments(action_type="create_round")
            elif user_choice == "6":
                self.view_tournaments.display_message("à completer")
            else:
                self.view_tournaments.display_message("Mauvaise saisie")
            input("\n Appuyez sur Entrée pour continuer...")
