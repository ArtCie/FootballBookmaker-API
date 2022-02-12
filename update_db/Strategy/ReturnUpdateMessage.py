from update_db.Strategy.Strategy import Strategy
from flask import jsonify


class ReturnUpdateMessage(Strategy):
    def handle(self, handlers=None, repositories=None, local_rounds=None, current_rounds=None, cursor=None):
        return jsonify(
            {
                "status": {
                    "code": 200,
                    "message": "Updated ;-))"
                },
                "data": None
            }
        )
