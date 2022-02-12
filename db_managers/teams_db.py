class TeamsDB:
    @staticmethod
    def select_teams(cursor):
        query = """
            SELECT distinct(id) from teams;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        return [i[0] for i in result]

    @staticmethod
    def update_team(cursor, data: dict):
        query = """
            UPDATE 
                teams
            SET
                position = %(position)s, 
                points = %(points)s, 
                form = %(form)s, 
                played = %(played)s, 
                win = %(win)s, 
                draw = %(draw)s, 
                lose = %(lose)s,
                goals_scored = %(goals_scored)s, 
                goals_loss = %(goals_loss)s
            WHERE
                id = %(id)s
        """
        cursor.execute(query, data)

    @staticmethod
    def select_team_position(cursor, data: dict):
        query = """
            SELECT
                position
            FROM
                teams
            WHERE
                id = %(id)s
        """
        cursor.execute(query, data)
        return cursor.fetchone()[0]

    @staticmethod
    def select_team_form(cursor, data: dict):
        query = """
            SELECT
                form
            FROM
                teams
            WHERE
                id = %(id)s
        """
        cursor.execute(query, data)
        return cursor.fetchone()

    @staticmethod
    def select_h2h(cursor, data: dict):
        query = """
        select 
            home_team_id, 
	        home_score,
	        away_score
        from 
            past_results pr 
        where (
                pr.home_team_id = %(home_team_id)s
                    and 
                pr.away_team_id = %(away_team_id)s
               ) 
        or 
               (	
                pr.away_team_id = %(home_team_id)s 
                and 
                pr.home_team_id = %(away_team_id)s 
               ) 
        order by 
            match_date 
        desc 
            limit 5;
        """
        cursor.execute(query, data)
        return cursor.fetchall()
