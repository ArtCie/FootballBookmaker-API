class Player:
    def __init__(self, id_, name, team_id, has_injury, goals, rating):
        self.id = id_
        self._name = name
        self._team_id = team_id
        self._has_injury = has_injury
        self._goals = goals
        self._rating = rating

    def get_id(self):
        return self.id

    def get_name(self):
        return self._name

    def get_team_id(self):
        return self._team_id

    def get_injury(self):
        return self._has_injury

    def get_goals(self):
        return self._goals

    def get_rating(self):
        return self._rating
