from ResponseParser.Parser import Parser
from datetime import datetime


class RoundResultParser(Parser):
    @staticmethod
    def parse(response, repository, only_null=False):
        for fixture in response:
            data = {
                "id": fixture["fixture"]["id"],
                "home_team_id": fixture["teams"]["home"]["id"],
                "away_team_id": fixture["teams"]["away"]["id"],
                "home_score": fixture["score"]["fulltime"]["home"],
                "away_score": fixture["score"]["fulltime"]["away"],
                "round": fixture["league"]["round"][-1] if fixture["league"]["round"][-2] == " " else fixture["league"]["round"][-2:],
                "season": 21,
                "match_date": datetime.fromtimestamp(fixture["fixture"]["timestamp"])
            }
            if (only_null is True and data["home_score"] is None) or (only_null is False):
                repository.add(data)