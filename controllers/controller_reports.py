"""Define the reports ."""

from views.view_reports import ViewReports
from views.view_users import View
from views.view_tournaments import ViewTournament


class ControllerReports:
    """Report controller."""

    def __init__(self, controller_principal):
        """Initialise le controler  ."""
        self.view = View()
        self.view_tournaments = ViewTournament()
        self.view_reports = ViewReports()
        self.controller_principal = controller_principal

    def display_report_choice(self):
        """Méthode pour démarrer le programme.Affiche le menu"""
        while True:
            self.view_reports.reports_new_header()
            self.view_reports.display_menu_reports()
            choix = self.view_reports.prompt_choice_report(["0", "1", "2", "3", "4", "10"])
            if choix == "1":
                self.view.clear_screen()
                self.display_all_players_report()
                self.view_reports.wait_for_user()
            elif choix == "2":
                self.view.clear_screen()
                self.display_all_tournaments()
                self.view_reports.wait_for_user()
            elif choix == "3":
                self.view.clear_screen()
                self.display_players_of_tournament()
                self.view_reports.wait_for_user()

            elif choix == "4":
                self.view.clear_screen()
                self.display_rounds_and_matches_report()
                self.view_reports.wait_for_user()
            elif choix == "0":
                self.view.clear_screen()
                self.view.main_header()
                self.view.menu()
                return
            elif choix == "10":
                self.view_reports.good_by()
                exit()

    def display_all_tournaments(self):
        """Affiche tous les tournois enregistrés (vue rapport simple)."""
        tournaments = self.controller_principal.load_tournaments_from_json()
        if not tournaments:
            self.view_reports.no_tournament_to_display()
            return
        self.view_reports.display_tournament_list(tournaments)

    def display_rounds_and_matches_report(self):
        """Permet de choisir un tournoi pour afficher ses rounds et matchs."""
        tournaments = self.controller_principal.load_tournaments_from_json()
        if not tournaments:
            self.view_reports.no_tournament_to_display()
            return
        self.view_reports.display_tournament_list(tournaments)
        index = self.view_reports.prompt_for_tournament_index(len(tournaments))
        if index is None:
            return
        selected_data = tournaments[index]
        tournament = self.controller_principal.recreate_tournament_controlleur(
            selected_data, self.controller_principal.all_players
        )
        if tournament:
            if not tournament.rounds:
                # Vérifie si le tournoi n'a pas de rounds
                self.view_reports.no_round_played()
            self.controller_principal.display_tournament_rounds_and_matches(tournament)
        else:
            self.view_reports.error_construction()

    def display_players_of_tournament(self):
        """Affiche les joueurs d'un tournoi via ViewTournament."""
        tournaments = self.controller_principal.load_tournaments_from_json()
        if not tournaments:
            self.view_reports.no_tournament_to_display()
            return
        self.view_reports.display_tournament_list(tournaments)
        index = self.view_reports.prompt_for_tournament_index(len(tournaments))
        if index is None:
            return
        selected_data = tournaments[index]
        tournament = self.controller_principal.recreate_tournament_controlleur(
            selected_data,
            self.controller_principal.all_players
        )
        if tournament:
            self.controller_principal.display_tournament_info(tournament)
        else:
            self.view_reports.error_loading_tournament()

    def display_all_players_report(self):
        """Affiche tous les joueurs enregistrés dans la base de données."""
        players = self.controller_principal.load_players_from_js_file()
        if not players:
            self.view_reports.no_players_found()
            return
        # Transformation en tableau
        players_table = [
            [player.name, player.first_name, player.player_id, player.date_of_birth]
            for player in players
        ]
        # Envoi à la vue
        self.view_reports.display_all_players(players_table)
