from update_db.ChancesGenerator.ChancesGenerator import ChancesGenerator

from db_managers.coach_db import CoachDB


class CoachesComparator(ChancesGenerator):
    def compare(self, home_team_id, away_team_id, current_home_chances, cursor):
        home_coach_percent_win = self._get_coach_win_coef(home_team_id, cursor)
        away_coach_percent_win = self._get_coach_win_coef(away_team_id, cursor)

        current_home_chances += self._get_score(home_coach_percent_win, away_coach_percent_win)
        return current_home_chances

    @staticmethod
    def _get_coach_win_coef(team_id, cursor):
        data = {
            "team_id": team_id
        }
        return CoachDB.select_win_percentage(data, cursor)

    @staticmethod
    def _get_score(home_coach_percent_win, away_coach_percent_win):
        return (float(home_coach_percent_win - away_coach_percent_win) * 1.666667) * 0.03
