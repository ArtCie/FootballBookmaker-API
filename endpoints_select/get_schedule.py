from flask import jsonify

from db_managers.round_db import RoundDB
from db_manager import DBManager

from Endpoint import IEndpoint


class GetSchedule(IEndpoint):
    def __init__(self, logger, db_manager: DBManager):
        self.logger = logger
        self.db_manager = db_manager

    def process_request(self, kwargs, cursor):
        data = RoundDB.select_active_round(cursor)
        return jsonify(
            {
                "status": {
                    "code": 200,
                    "message": "Successfully loaded patient diary data"
                },
                "data": [dict(row) for row in data]
            }
        )
