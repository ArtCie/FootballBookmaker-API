class PlayerDB:
    @staticmethod
    def update_player(data: dict, cursor):
        query = """
                UPDATE
                    players
                SET
                    goals = %(goals)s,
                    rating = %(rating)s
                WHERE
                    id = %(id)s
            """
        cursor.execute(query, data)

    @staticmethod
    def select_top5_injured(data: dict, cursor):
        query = """
            select 
                count(*) 
            from (select id, has_injury from players where team_id = %(team_id)s order by rating desc limit 5) top 
            where 
                top.has_injury 
            is true;
        """
        cursor.execute(query, data)
        return cursor.fetchone()[0]
