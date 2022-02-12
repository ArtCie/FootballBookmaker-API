from ResponseParser.Parser import Parser
from update_db.Repositories.TeamRepository import TeamRepository


class TeamParser(Parser):
    @staticmethod
    def parse(response, team_repository: TeamRepository):
        response = response[0]["league"]["standings"][0]
        for team in response:
            data = {
                    'id': team['team']['id'],
                    'league_id': 39,
                    'name': team['team']['name'],
                    'position': team['rank'],
                    'points': team['points'],
                    'form': team['form'],
                    'logo': team['team']['logo'],
                    'played': team['all']['played'],
                    'win': team['all']['win'],
                    'draw': team['all']['draw'],
                    'lose': team['all']['lose'],
                    'goals_scored': team['all']['goals']['for'],
                    'goals_loss': team['all']['goals']['against'],
            }
            team_repository.add(data)
