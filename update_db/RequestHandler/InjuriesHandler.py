from update_db.RequestHandler.RequestHandler import RequestHandler


class InjuriesRequestHandler:
    def __init__(self):
        self.request_handler = RequestHandler()

    def get_injuries(self, league, date):
        query_string = {"league": league, "date": date}
        return self.request_handler.send("current_round_results", query_string)
