from update_db.ChancesGenerator.ChancesGenerator import ChancesGenerator
from db_managers.teams_db import TeamsDB


class H2HComparator(ChancesGenerator):
    def compare(self, home_team_id, away_team_id, current_home_chances, cursor):
        h2h, results_number = self._get_h2h(home_team_id, away_team_id, cursor)
        current_home_chances += self._get_score(h2h, results_number)
        return self.successor.compare(home_team_id, away_team_id, current_home_chances, cursor)

    def _get_h2h(self, home_team_id, away_team_id, cursor):
        data = {
            "home_team_id": home_team_id,
            "away_team_id": away_team_id
        }
        result = TeamsDB.select_h2h(cursor, data)
        return self._get_score_from_h2h(home_team_id, result), len(result)

    def _get_score_from_h2h(self, home_team_id: int, result: list):
        win_counter = 0
        for match in result:
            win_counter += self._get_winner(home_team_id, match)
        return win_counter

    @staticmethod
    def _get_winner(home_team_id, match):
        if match["home_score"] > match["away_score"]:
            return 1 if str(match["home_team_id"]) == str(home_team_id) else -1
        elif match["home_score"] < match["away_score"]:
            return -1 if str(match["home_team_id"]) == str(home_team_id) else 1
        else:
            return 0

    @staticmethod
    def _get_score(h2h_score, results_number):
        return (1 / results_number) * h2h_score * 0.12 if results_number != 0 else 0
