from update_db.RequestHandler.RequestHandler import RequestHandler


class RoundResultRequestHandler:
    def __init__(self):
        self.request_handler = RequestHandler()

    def get_current_round_results(self, league, season, round_):
        query_string = {"league": league, "season": season, "round": round_}
        return self.request_handler.send("current_round_results", query_string)
