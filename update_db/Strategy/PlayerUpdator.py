import time
from ResponseParser.PlayerParser import PlayerParser

from db_managers.player_db import PlayerDB
from db_managers.teams_db import TeamsDB


class PlayerUpdator:
    def handle(self, handlers, repositories, cursor):
        self._get_all_players(handlers["player"], repositories["player"], cursor)
        self._update_db(repositories["player"], cursor)

    @staticmethod
    def _get_all_players(handler, repository, cursor):
        teams = TeamsDB.select_teams(cursor)
        pages = [1, 2, 3]
        for team in teams:
            for page in pages:
                time.sleep(3)
                response = handler.get_players(team, "2021", page)
                PlayerParser.parse(response, repository)

    def _update_db(self, repository, cursor):
        for player in repository.get_repository():
            data = self._prepare_data(player)
            PlayerDB.update_player(data, cursor)

    @staticmethod
    def _prepare_data(player):
        return {
            "id": player.get_id(),
            "rating": player.get_rating(),
            "goals": player.get_goals()
        }
