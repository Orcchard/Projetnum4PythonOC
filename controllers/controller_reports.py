"""Define the reports ."""
import json
import os
import random
from datetime import datetime
from tabulate import tabulate


from views.view_reports import ViewReports
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

    def display_report_choice(self):
        """Méthode pour démarrer le programme.Affiche le menu"""
        while True:
            self.view_reports.reports_new_header()
            self.view_reports.display_menu_reports()
            choix = self.view_reports.prompt_choice_report(["0", "1", "2", "3", "4", "10"])
            if choix == "1":
                pass
            elif choix == "2":
                pass
            elif choix == "3":
                # self.select_list_saved_tournaments(action_type="view")
                pass
            elif choix == "4":
                print("→ Affichage des rounds et matchs d un tournoi\n")
            elif choix == "0":
                self.view.clear_screen()
                self.view.main_header()
                self.view.menu()
                return
            elif choix == "10":
                print("👋 Au revoir !")
                exit()
