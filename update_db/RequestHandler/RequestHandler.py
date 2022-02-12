import requests


class RequestHandler:
    def __init__(self):
        self.headers = {
         'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
         'x-rapidapi-key': "9551e75ac6msh38f9db82f846d88p186bd6jsn62dfa789a5cf"
     }
        self.paths = {
            'players': "https://api-football-v1.p.rapidapi.com/v3/players",
            'current_round_results': 'https://api-football-v1.p.rapidapi.com/v3/fixtures',
            'current_round': 'https://api-football-v1.p.rapidapi.com/v3/fixtures/rounds',
            'injuries': 'https://api-football-v1.p.rapidapi.com/v3/injuries',
            'teams': 'https://api-football-v1.p.rapidapi.com/v3/standings'
        }

    def send(self, path_key, params):
        response = requests.request("GET", self.paths[path_key], headers=self.headers, params=params).json()
        return response["response"] if "response" in response.keys() else None
