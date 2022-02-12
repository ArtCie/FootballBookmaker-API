from update_db.Strategy.Strategy import Strategy
from flask import jsonify
from copy import deepcopy

from ResponseParser.RoundResultParser import RoundResultParser

from update_db.Strategy.PlayerUpdator import PlayerUpdator
from update_db.Strategy.CoachUpdator import CoachUpdator
from update_db.Strategy.ResultUpdator import ResultUpdator
from update_db.Strategy.TeamUpdator import TeamUpdator


class Updator(Strategy):
    def __init__(self):
        self.PREMIER_LEAGUE_ID = 39
        self.SEASON = 2021

    def handle(self, handlers, repositories, local_rounds, current_rounds, cursor):
        rounds_to_remove = set(local_rounds) - set(current_rounds)
        if rounds_to_remove:
            self._get_results(rounds_to_remove, handlers, repositories)
            CoachUpdator().handle(deepcopy(repositories), cursor)
            ResultUpdator(self.PREMIER_LEAGUE_ID, self.SEASON).transfer_old_rounds(repositories, current_rounds, local_rounds, cursor)

            PlayerUpdator().handle(handlers, repositories, cursor)
            TeamUpdator(self.PREMIER_LEAGUE_ID, self.SEASON).handle(handlers, repositories, cursor)

        rounds_to_add = set(current_rounds) - set(local_rounds)
        if rounds_to_add:
            ResultUpdator(self.PREMIER_LEAGUE_ID, self.SEASON).add_new_round(rounds_to_add, handlers, repositories, cursor)

        return jsonify(
            {
                "status": {
                    "code": 200,
                    "message": "Updated!"
                },
                "data": None
            }
        )

    def _get_results(self, rounds_to_remove, handlers, repositories):
        for round in rounds_to_remove:
            response = handlers["round"].get_current_round_results(self.PREMIER_LEAGUE_ID, self.SEASON,
                                                                   "Regular Season - " + str(round))
            RoundResultParser.parse(response, repositories["round"])
