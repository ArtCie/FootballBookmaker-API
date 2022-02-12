from update_db.ChancesGenerator.ChancesGenerator import ChancesGenerator
from db_managers.teams_db import TeamsDB


class FormComparator(ChancesGenerator):
    def compare(self, home_team_id, away_team_id, current_home_chances, cursor):
        home_form = self._get_form(home_team_id, cursor)
        away_form = self._get_form(away_team_id, cursor, True)
        current_home_chances += self._get_score(home_form + away_form)
        return self.successor.compare(home_team_id, away_team_id, current_home_chances, cursor)

    def _get_form(self, team_id, cursor, negative=False):
        data = {
            "id": team_id
        }
        result = TeamsDB.select_team_form(cursor, data)
        score = self._get_score_from_form(result["form"][-5:])
        return score if not negative else score * (-1)

    @staticmethod
    def _get_score_from_form(result: str):
        map_result = list(result)
        scores = []

        for result in map_result:
            scores.append(1 if result == "W" else -1 if result == "L" else 0)
        return sum(scores)

    @staticmethod
    def _get_score(form_score):
        return (0.1 * form_score) * 0.15
