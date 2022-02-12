class RoundDB:
    @staticmethod
    def select_current_rounds(cursor):
        query = """
            SELECT distinct(round) from current_round;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        return [i[0] for i in result]

    @staticmethod
    def insert(data: dict, cursor):
        query = """
            INSERT INTO
                past_results
            (home_team_id, away_team_id, home_score, away_score, round, season, id, match_date)
            VALUES
            (%(home_team_id)s, %(away_team_id)s, %(home_score)s, %(away_score)s, %(round)s, %(season)s, %(id)s, %(match_date)s)
        """
        cursor.execute(query, data)

    @staticmethod
    def delete_set(data: dict, cursor):
        query = """
            DELETE FROM
                current_round
            WHERE
                round in %(rounds_to_remove)s
        """
        cursor.execute(query, data)

    @staticmethod
    def insert_current_round(data: dict, cursor):
        query = """
            INSERT INTO
                current_round
            (home_team_id, away_team_id, home_score, away_score, round, season, id, match_date, home_team_chances)
            VALUES
            (%(home_team_id)s, %(away_team_id)s, %(home_score)s, %(away_score)s, %(round)s, %(season)s, %(id)s, %(match_date)s, %(home_team_chances)s)
        """
        cursor.execute(query, data)

    @staticmethod
    def select_active_round(cursor):
        query = """
            select 
                t."name" as home_team, 
                t2."name" as away_team, 
                cr.home_score, 
                cr.away_score, 
                cr.match_date, 
                cr.round,
                t.logo as home_logo,
                t2.logo as away_logo,
                home_team_chances
            from 
                current_round cr 
            inner join 
                teams t on t.id = cr.home_team_id 
            inner join 
                teams t2 on t2.id = cr.away_team_id 
        """
        cursor.execute(query)
        return cursor.fetchall()