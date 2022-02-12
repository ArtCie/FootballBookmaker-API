from update_db.Models.Team import Team


class TeamRepository:
    _team_repository: [Team]

    def __init__(self):
        self._team_repository = []

    def add(self, data):
        self._team_repository.append(
            Team(
                data["id"],
                data["league_id"],
                data["name"],
                data["position"],
                data["points"],
                data["form"],
                data["logo"],
                data["played"],
                data["win"],
                data["draw"],
                data["lose"],
                data["goals_scored"],
                data["goals_loss"]
                )
        )

    def get_repository(self):
        return self._team_repository
