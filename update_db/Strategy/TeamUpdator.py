from ResponseParser.TeamParser import TeamParser

from db_managers.teams_db import TeamsDB


class TeamUpdator:
    def __init__(self, league, season):
        self.LEAGUE = league
        self.SEASON = season

    def handle(self, handlers, repositories, cursor):
        self._get_all_teams(handlers["team"], repositories["team"])
        self._update_db(repositories["team"], cursor)

    def _get_all_teams(self, handler, repository):
        response = handler.get_teams(self.SEASON, self.LEAGUE)
        TeamParser.parse(response, repository)

    def _update_db(self, repository, cursor):
        for team in repository.get_repository():
            data = self._prepare_data(team)
            TeamsDB.update_team(cursor, data)

    @staticmethod
    def _prepare_data(team):
        return {
            "position": team.get_position(),
            "points": team.get_points(),
            "form": team.get_form(),
            "played": team.get_played(),
            "win": team.get_win(),
            "draw": team.get_draw(),
            "lose": team.get_lose(),
            "goals_scored": team.get_goals_scored(),
            "goals_loss": team.get_goals_loss(),
            "id": team.get_id()
        }
