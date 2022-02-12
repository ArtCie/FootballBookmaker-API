
from update_db.Repositories.RoundRepository import RoundRepository

from db_managers.coach_db import CoachDB


class CoachUpdator:
    def handle(self, repositories, cursor):
        self._update_db(repositories["round"], cursor)

    def _update_db(self, round_repository: RoundRepository, cursor):
        for round in round_repository.get_repository():
            teams_result = self._get_teams_id(round)
            if teams_result:
                self._update_coaches(teams_result, cursor)

    @staticmethod
    def _get_teams_id(round):
        home_team_id = round.get_home_team_id()
        away_team_id = round.get_away_team_id()
        if round.get_home_score():
            goal_diff = round.get_home_score() - round.get_away_score()
            is_home_winner = True if goal_diff > 0 else "Draw" if goal_diff == 0 else False
            is_away_winner = True if goal_diff < 0 else "Draw" if goal_diff == 0 else False
            return {
                "home_team": {"team_id": home_team_id, "is_winner": is_home_winner},
                "away_team": {"team_id": away_team_id, "is_winner": is_away_winner}
            }

    def _update_coaches(self, teams_result, cursor):
        self._update_coach(teams_result["home_team"], cursor)
        self._update_coach(teams_result["away_team"], cursor)

    @staticmethod
    def _update_coach(team_result, cursor):
        data = {"team_id": team_result["team_id"]}
        if team_result["is_winner"] is True:
            CoachDB.update_coach_wins(data, cursor)
        elif team_result["is_winner"] is False:
            CoachDB.update_coach_loss(data, cursor)
        else:
            CoachDB.update_coach_draws(data, cursor)