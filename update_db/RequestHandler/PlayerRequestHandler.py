from update_db.RequestHandler.RequestHandler import RequestHandler


class PlayerRequestHandler:
    def __init__(self):
        self.request_handler = RequestHandler()

    def get_players(self, team, season, page):
        query_string = {"team": team, "season": season, "page": page}
        return self.request_handler.send("players", query_string)