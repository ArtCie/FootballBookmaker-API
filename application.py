import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

from flask_cors import CORS

from db_manager import DBManager
from endpoint_manager import EndpointManager
from update_db.update_db import UpdateDB
from endpoints_select.get_schedule import GetSchedule

application = Flask(__name__)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('application.log', maxBytes=1024, backupCount=5)
handler.setFormatter(formatter)
application.logger.addHandler(handler)

db_manager = DBManager.get_instance()

db_manager.connect()

endpoint_manager = EndpointManager(logger, db_manager)

update_db = UpdateDB(logger, db_manager)
get_all_information = GetSchedule(logger, db_manager)

cors = CORS(
    application,
    resources={
        r"/*": {
            "origins": "*"
        }
    }
)


@application.route('/')
def index():
    return 'index'


@application.route('/update', methods=['POST'])
def update_database():
    return endpoint_manager.handle_request(update_db)


@application.route('/get_round_info', methods=['GET'])
def get_info():
    return endpoint_manager.handle_request(get_all_information)
