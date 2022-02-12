from ResponseParser.Parser import Parser


class CurrentRoundParser(Parser):
    @staticmethod
    def parse(response, repository=None):
        return [int(round_[-1]) if round_[-2] == " " else int(round_[-2:]) for round_ in response]