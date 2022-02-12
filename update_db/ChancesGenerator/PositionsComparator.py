from update_db.ChancesGenerator.ChancesGenerator import ChancesGenerator

from db_managers.teams_db import TeamsDB


class PositionsComparator(ChancesGenerator):
    def compare(self, home_team_id, away_team_id, current_home_chances, cursor):
        home_team_position = self._get_team_position(home_team_id, cursor)
        away_team_position = self._get_team_position(away_team_id, cursor)

        current_home_chances += self._analyse_positions(home_team_position, away_team_position) * 0.13
        return self.successor.compare(home_team_id, away_team_id, current_home_chances, cursor)

    @staticmethod
    def _get_team_position(team_id, cursor):
        data = {
            "id": team_id
        }
        return TeamsDB.select_team_position(cursor, data)

    @staticmethod
    def _analyse_positions(home_team_position, away_team_position):
        coefficient = 1 if home_team_position < away_team_position else -1
        return (0.055555 * abs(away_team_position - home_team_position) - 0.055555) * coefficient
