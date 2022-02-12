from update_db.Models.Player import Player


class PlayerRepository:
    _player_repository: [Player]

    def __init__(self):
        self._player_repository = []

    def add(self, data):
        self._player_repository.append(
            Player(
                data["id"],
                data["name"],
                data["team_id"],
                data["has_injury"],
                data["goals"],
                data["rating"]
            )
        )

    def get_repository(self):
        return self._player_repository
