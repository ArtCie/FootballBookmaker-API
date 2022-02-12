from update_db.RequestHandler.RequestHandler import RequestHandler


class CurrentRoundRequestHandler:
    def __init__(self):
        self.request_handler = RequestHandler()

    def get_current_round(self, league, season):
        query_string = {"league": league, "season": season, "current": "true"}
        return self.request_handler.send("current_round", query_string)
