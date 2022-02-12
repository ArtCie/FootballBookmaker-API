class Round:
    def __init__(self, home_team_id, away_team_id, home_score, away_score, round, season, date, id, match_date, chances=None):
        self._home_team_id = home_team_id
        self._away_team_id = away_team_id
        self._home_score = home_score
        self._away_score = away_score
        self._round = round
        self._season = season
        self._id = id
        self._match_date = match_date
        self._chances = chances

    def get_home_team_id(self):
        return self._home_team_id

    def get_away_team_id(self):
        return self._away_team_id

    def get_home_score(self):
        return self._home_score

    def get_away_score(self):
        return self._away_score

    def get_round(self):
        return self._round

    def get_season(self):
        return self._season

    def get_id(self):
        return self._id

    def get_match_date(self):
        return self._match_date

    def get_changes(self):
        return self._chances