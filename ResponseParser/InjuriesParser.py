from ResponseParser.Parser import Parser
from update_db.Repositories.InjuryRepository import InjuryRepository


class InjuriesParser(Parser):
    @staticmethod
    def parse(response, injury_repository: InjuryRepository):
        for injury in response:
            data = {
                "id": injury["player"]["id"],
                "name": injury["player"]["reason"]
            }
            injury_repository.add(data)