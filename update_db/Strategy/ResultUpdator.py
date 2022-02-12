from update_db.Strategy.Strategy import Strategy
from flask import jsonify

from update_db.Repositories.RoundRepository import RoundRepository
from ResponseParser.PlayerParser import PlayerParser

from db_managers.round_db import RoundDB
from ResponseParser.RoundResultParser import RoundResultParser

from update_db.ChancesGenerator.PositionsComparator import PositionsComparator
from update_db.ChancesGenerator.FormComparator import FormComparator
from update_db.ChancesGenerator.H2HComparator import H2HComparator
from update_db.ChancesGenerator.InjuriesComparator import InjuriesComparator
from update_db.ChancesGenerator.CoachesComparator import CoachesComparator


class ResultUpdator:
    def __init__(self, premier_league_id, season):
        self.PREMIER_LEAGUE_ID = premier_league_id
        self.SEASON = season
        self.chances_chain = PositionsComparator(FormComparator(H2HComparator(InjuriesComparator(CoachesComparator()))))

    def transfer_old_rounds(self, repositories, current_rounds, local_rounds, cursor):
        self.upload_to_db_old_round(repositories["round"], cursor)

        data = {
            "rounds_to_remove": tuple(set(local_rounds) - set(current_rounds))
        }
        RoundDB.delete_set(data, cursor)
        repositories["round"].empty()

    def upload_to_db_old_round(self, repository: RoundRepository, cursor):
        repository = repository.get_repository()
        for round in repository:
            data = self._prepare_data(round)
            RoundDB.insert(data, cursor)

    def _update_new_round(self, repository: RoundRepository, cursor):
        repository = repository.get_repository()
        for round in repository:
            current_chances = 0.5
            data = self._prepare_data(round)
            current_chances = self.chances_chain.compare(round.get_home_team_id(), round.get_away_team_id(), current_chances, cursor)
            data["home_team_chances"] = current_chances
            RoundDB.insert_current_round(data, cursor)

    @staticmethod
    def _prepare_data(round):
        return {
                "home_team_id": round.get_home_team_id(),
                "away_team_id": round.get_away_team_id(),
                "home_score": round.get_home_score(),
                "away_score": round.get_away_score(),
                "round": round.get_round(),
                "season": round.get_season(),
                "id": round.get_id(),
                "match_date": round.get_match_date(),
            }

    def add_new_round(self, rounds_to_add, handlers, repositories, cursor):
        for round in rounds_to_add:
            response = handlers["round"].get_current_round_results(self.PREMIER_LEAGUE_ID, self.SEASON,
                                                                   "Regular Season - " + str(round))
            if round == max(rounds_to_add):
                RoundResultParser.parse(response, repositories["round"])
            else:
                RoundResultParser.parse(response, repositories["round"], only_null=True)

        self._update_new_round(repositories["round"], cursor)

