import logging
import logging.config
import time

from pyms.flask.app import Microservice
from sqlalchemy import event
from sqlalchemy.engine import Engine

from project.models.init_db import db

logging.basicConfig()
logger = logging.getLogger("myapp.sqltime")
logger.setLevel(logging.DEBUG)


@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, *args, **kwargs):
    conn.info.setdefault('query_start_time', []).append(time.time())
    logger.debug("Start Query: %s, %s [%s]", statement, parameters, cursor)


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, *args, **kwargs):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    logger.debug("Query Complete!")
    logger.debug("Total Time: %f", total)


class MyMicroservice(Microservice):
    def init_libs(self) -> None:
        db.init_app(self.application)
        with self.application.test_request_context():
            db.create_all()

    def init_logger(self) -> None:
        if not self.application.config["DEBUG"]:
            super().init_logger()
        else:
            level = "DEBUG"
            LOGGING = {
                'version': 1,
                'disable_existing_loggers': False,
                'handlers': {
                    'console': {
                        'level': level,
                        'class': 'logging.StreamHandler',
                    },
                },
                'loggers': {
                    '': {
                        'handlers': ['console'],
                        'level': level,
                        'propagate': True,
                    },
                    'anyconfig': {
                        'handlers': ['console'],
                        'level': "WARNING",
                        'propagate': True,
                    },
                    'pyms': {
                        'handlers': ['console'],
                        'level': "WARNING",
                        'propagate': True,
                    },
                    'root': {
                        'handlers': ['console'],
                        'level': level,
                        'propagate': True,
                    },
                }
            }

            logging.config.dictConfig(LOGGING)
