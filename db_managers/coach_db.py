class CoachDB:
    @staticmethod
    def update_coach_wins(data: dict, cursor):
        query = """
                UPDATE
                    coaches
                SET
                    league_wins = league_wins + 1
                WHERE
                    id = %(team_id)s
            """
        cursor.execute(query, data)

    @staticmethod
    def update_coach_draws(data: dict, cursor):
        query = """
                UPDATE
                    coaches
                SET
                    league_draws = league_draws + 1
                WHERE
                    team_id = %(team_id)s
            """
        cursor.execute(query, data)

    @staticmethod
    def update_coach_loss(data: dict, cursor):
        query = """
                UPDATE
                    coaches
                SET
                    league_loss = league_loss + 1
                WHERE
                    team_id = %(team_id)s
            """
        cursor.execute(query, data)

    @staticmethod
    def select_all_coaches(cursor):
        query = """
            SELECT 
                *
            FROM
                coaches
        """
        cursor.execute(query)
        return cursor.fetchall()

    @staticmethod
    def select_win_percentage(data: dict, cursor):
        query = """
            SELECT
                cast(league_wins as decimal) / (cast(league_wins as decimal) + cast(league_loss as decimal) + cast(league_draws as decimal))
            FROM
                coaches
            WHERE
                team_id = %(team_id)s
        """
        cursor.execute(query, data)
        return cursor.fetchone()[0]