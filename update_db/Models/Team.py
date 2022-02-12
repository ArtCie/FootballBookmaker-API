class Team:
    def __init__(self, id_, league_id, name, position, points, form, logo, played, win, draw, lose, goals_scored, goals_loss):
        self.id = id_
        self._league_id = league_id
        self._name = name
        self._position = position
        self._points = points
        self._form = form
        self._logo = logo
        self._played = played
        self._win = win
        self._draw = draw
        self._lose = lose
        self._goals_scored = goals_scored
        self._goals_loss = goals_loss

    def get_id(self):
        return self.id

    def get_league_id(self):
        return self._league_id

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def get_points(self):
        return self._points

    def get_form(self):
        return self._form

    def get_logo(self):
        return self._logo

    def get_played(self):
        return self._played

    def get_win(self):
        return self._win

    def get_draw(self):
        return self._draw

    def get_lose(self):
        return self._lose

    def get_goals_scored(self):
        return self._goals_scored

    def get_goals_loss(self):
        return self._goals_loss
