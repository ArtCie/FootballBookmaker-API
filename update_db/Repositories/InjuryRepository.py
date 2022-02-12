from update_db.Models.Injury import Injury


class InjuryRepository:
    _injury_repository: [Injury]

    def __init__(self):
        self._injury_repository = []

    def add(self, data):
        self._injury_repository.append(
            Injury(
                    data["id"],
                    data["name"],
                    )
        )