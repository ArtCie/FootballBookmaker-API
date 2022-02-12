from update_db.Models.Round import Round
from update_db.Repositories.RoundRepositoryIterator import RoundRepositoryIterator

class RoundRepository:
    _round_repository: list

    def __init__(self):
        self._round_repository = list()

    def __iter__(self) -> RoundRepositoryIterator:
        return RoundRepositoryIterator(self._round_repository)

    def add(self, data):
        self._round_repository.append(
            Round(
                    data["home_team_id"],
                    data["away_team_id"],
                    data["home_score"],
                    data["away_score"],
                    data["round"],
                    data["season"],
                    "",
                    data["id"],
                    data["match_date"],
                )
        )

    def get_repository(self):
        return self._round_repository

    def empty(self):
        self._round_repository = []
