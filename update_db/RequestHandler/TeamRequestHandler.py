from update_db.RequestHandler.RequestHandler import RequestHandler


class TeamRequestHandler:
    def __init__(self):
        self.request_handler = RequestHandler()

    def get_teams(self, season, league):
        query_string = {"season": season, "league": league}
        return self.request_handler.send("teams", query_string)