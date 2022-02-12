import abc


class ChancesGenerator(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self.successor = successor

    @abc.abstractmethod
    def compare(self, home_team_id, away_team_id, current_home_chances, cursor):
        pass
