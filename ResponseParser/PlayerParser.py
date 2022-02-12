from ResponseParser.Parser import Parser
from update_db.Repositories.PlayerRepository import PlayerRepository


class PlayerParser(Parser):
    @staticmethod
    def parse(response, player_repository: PlayerRepository):
        for player in response:
            if player["statistics"][0]["league"]["id"] == 39 and player["statistics"][0]["games"]["rating"] is not None:
                data = {
                    "id": player["player"]["id"],
                    "name": player["player"]["name"],
                    "has_injury": player["player"]["injured"],
                    "goals": player["statistics"][0]["goals"]["total"],
                    "rating": player["statistics"][0]["games"]["rating"],
                    "team_id": player["statistics"][0]["team"]["id"]
                }
                player_repository.add(data)
