from update_db.ChancesGenerator.ChancesGenerator import ChancesGenerator
from db_managers.player_db import PlayerDB


class InjuriesComparator(ChancesGenerator):
    def compare(self, home_team_id, away_team_id, current_home_chances, cursor):
        number_of_top_players_injured_home = self._get_injured_top5(home_team_id, cursor)
        number_of_top_players_injured_away = self._get_injured_top5(away_team_id, cursor)

        current_home_chances += self._get_score(number_of_top_players_injured_home, number_of_top_players_injured_away)
        return self.successor.compare(home_team_id, away_team_id, current_home_chances, cursor)

    @staticmethod
    def _get_injured_top5(team_id, cursor):
        data = {
            "team_id": team_id
        }
        return PlayerDB.select_top5_injured(data, cursor)

    @staticmethod
    def _get_score(injured_home, injured_away):
        return ((injured_away - injured_home) * 0.2) * 0.07
