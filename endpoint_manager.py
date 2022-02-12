import json

import psycopg2
from flask import Response, request


class EndpointManager:

    def __init__(self, logger, db_manager):
        self.logger = logger
        self.db_manager = db_manager

    def handle_request(self, direct_manager, **kwargs):
        class_name = str(type(direct_manager).__name__)
        connection = cursor = None

        self.logger.info(class_name + ".handle_request() request content: " + str(kwargs))
        try:
            cursor, connection = self.db_manager.get_db_cursor_and_connection()
            response = direct_manager.process_request(kwargs, cursor)
            self.db_manager.commit_and_close_connection(connection, cursor)
            # self.db_manager.rollback_and_close_connection(connection, cursor)
            return response
        except psycopg2.errors.AdminShutdown as e:
            self.logger.info(class_name + "EndpointManager.handle_request() AdminShutdown: " + str(e))
            self.db_manager.rollback_and_close_connection(connection, cursor)
            return self.handle_request(direct_manager, **kwargs)
        except psycopg2.OperationalError as e:
            self.logger.info(class_name + "EndpointManager.handle_request() OperationalError: " + str(e))
            self.db_manager.rollback_and_close_connection(connection, cursor)
            return self.handle_request(direct_manager, **kwargs)
        except Exception as e:
            self.db_manager.rollback_and_close_connection(connection, cursor)
            self.logger.exception('Error in ' + class_name + ': %s', str(e))
            return Response(
                json.dumps({
                    "status": {
                        "code": 404,
                        "message": str(e)
                    },
                    "data": None
                })
            )
