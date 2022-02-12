from psycopg2.pool import ThreadedConnectionPool
import os
import psycopg2
from psycopg2 import extras


class DBManager:
    __instance = None

    def __init__(self):
        self.thread_pool_connection = None

    @staticmethod
    def get_instance():
        if DBManager.__instance:
            return DBManager.__instance
        else:
            return DBManager()

    def connect(self):
        threaded_connection = ThreadedConnectionPool(
            minconn=1,
            maxconn=15,
            user='',
            host='',
            password='',
            database=''
        )
        threaded_connection.autocommit = False
        self.thread_pool_connection = threaded_connection

    def get_connection(self):
        return self.thread_pool_connection.getconn()

    def get_db_cursor_and_connection(self):
        connection = self.get_connection()
        return connection.cursor(cursor_factory=psycopg2.extras.DictCursor), connection

    @staticmethod
    def rollback_changes(connection):
        if connection:
            connection.rollback()

    @staticmethod
    def commit_changes(connection):
        connection.commit()

    def close_connection(self, connection, cursor):
        if cursor:
            self.close_cursor(cursor)
        if connection:
            try:
                self.put_connection(connection)
            except Exception as e:
                connection.close()

    def commit_and_close_connection(self, connection, cursor):
        if cursor:
            self.close_cursor(cursor)
        if connection:
            self.commit_changes(connection)
            try:
                self.put_connection(connection)
            except Exception as e:
                connection.close()

    def rollback_and_close_connection(self, connection, cursor):
        if cursor:
            self.close_cursor(cursor)
        if connection:
            self.rollback_changes(connection)
            try:
                self.put_connection(connection)
            except Exception as e:
                connection.close()

    def put_connection(self, connection):
        self.thread_pool_connection.putconn(connection)

    @staticmethod
    def close_cursor(cursor):
        if cursor:
            cursor.close()

    def close(self):
        self.thread_pool_connection.close()

    @staticmethod
    def insert_patient_report(data, cursor):
        query = """
        INSERT INTO
            teams
            (
                id,
                league_id,
                name,
                position,
                points,
                form,
                logo,
                played,
                win,
                draw,
                lose,
                goals_scored,
                goals_loss
            )
        VALUES
            (
                %(id)s,
                %(league_id)s,
                %(name)s,
                %(position)s,
                %(points)s,
                %(form)s,
                %(logo)s,
                %(played)s,
                %(win)s,
                %(draw)s,
                %(lose)s,
                %(goals_scored)s,
                %(goals_loss)s
            )
        """
        cursor.execute(query, data)

    @staticmethod
    def insert_coach(data, cursor):
        query = """
            INSERT INTO
                coaches
            (
                id,
                first_name,
                last_name,
                team_id
            )
            values
            (
                %(id)s,
                %(first_name)s,
                %(last_name)s,
                %(team_id)s
            )
        """
        cursor.execute(query, data)

    @staticmethod
    def insert_round_fixture(data, cursor):
        query = """
            INSERT INTO
                current_round
            (
                id,
                home_team_id,
                away_team_id,
                home_score,
                away_score,
                round,
                season,
                match_date
            )
            values
            (
                %(id)s,
                %(home_team_id)s,
                %(away_team_id)s,
                %(home_score)s,
                %(away_score)s,
                %(round)s,
                %(season)s,
                %(match_date)s
            )
        """
        cursor.execute(query, data)    \

    @staticmethod
    def insert_previous_fixture(data, cursor):
        query = """
            INSERT INTO
                past_results
            (
                id,
                home_team_id,
                away_team_id,
                home_score,
                away_score,
                round,
                season,
                match_date
            )
            values
            (
                %(id)s,
                %(home_team_id)s,
                %(away_team_id)s,
                %(home_score)s,
                %(away_score)s,
                %(round)s,
                %(season)s,
                %(match_date)s
            )
        """
        cursor.execute(query, data)


    @staticmethod
    def insert_players(data, cursor):
        query = """
            INSERT INTO
                players
            (
                id,
                name,
                team_id,
                has_injury,
                goals,
                rating
            )
            values
            (
                %(id)s,
                %(name)s,
                %(team_id)s,
                %(has_injury)s,
                %(goals)s,
                %(rating)s
            )
        """
        cursor.execute(query, data)