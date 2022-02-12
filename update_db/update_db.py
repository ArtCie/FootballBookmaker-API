from update_db.Repositories.InjuryRepository import InjuryRepository
from update_db.Repositories.PlayerRepository import PlayerRepository
from update_db.Repositories.RoundRepository import RoundRepository
from update_db.Repositories.TeamRepository import TeamRepository

from update_db.RequestHandler.RoundResultRequestHandler import RoundResultRequestHandler
from update_db.RequestHandler.PlayerRequestHandler import PlayerRequestHandler
from update_db.RequestHandler.CurrentRoundRequestHandler import CurrentRoundRequestHandler
from update_db.RequestHandler.InjuriesHandler import InjuriesRequestHandler
from update_db.RequestHandler.TeamRequestHandler import TeamRequestHandler

from ResponseParser.CurrentRoundParser import CurrentRoundParser

from db_managers.round_db import RoundDB

from update_db.Strategy.ReturnMessage import NoUpdateMessageReturner
from update_db.Strategy.Updator import Updator
from db_manager import DBManager

from Endpoint import IEndpoint


class UpdateDB(IEndpoint):
    def __init__(self, logger, db_manager: DBManager):
        self.logger = logger
        self.db_manager = db_manager
        self.PREMIER_LEAGUE_ID = 39
        self.SEASON = 2021

    def process_request(self, kwargs, cursor):
        strategy = NoUpdateMessageReturner()

        repositories = self.get_repositories()
        current_round_handler, handlers = self.get_handlers()
        current_rounds, local_rounds = self.get_rounds(current_round_handler, cursor)
        if set(current_rounds) != set(local_rounds):
            strategy = Updator()

        return strategy.handle(handlers, repositories, local_rounds, current_rounds, cursor)

    @staticmethod
    def get_repositories():
        return {
            "injury": InjuryRepository(),
            "player": PlayerRepository(),
            "round": RoundRepository(),
            "team": TeamRepository()
        }

    @staticmethod
    def get_handlers():
        return CurrentRoundRequestHandler(), {
            "injury": InjuriesRequestHandler(),
            "player": PlayerRequestHandler(),
            "round": RoundResultRequestHandler(),
            "team": TeamRequestHandler()
        }

    def get_rounds(self, handler: CurrentRoundRequestHandler, cursor):
        current_rounds = self.get_current_rounds(handler)
        local_rounds = RoundDB.select_current_rounds(cursor)
        return current_rounds, local_rounds

    def get_current_rounds(self, handler: CurrentRoundRequestHandler):
        response = handler.get_current_round(self.PREMIER_LEAGUE_ID, self.SEASON)
        return CurrentRoundParser.parse(response)
