from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

from .orm_model import OrmModel, OrmModels


class Orm(object):
    connection_url = None
    driver = None
    headers = None
    app_id = None

    def __init__(self, connection_url, headers=None):
        headers = headers or {}

        self.connection_url = connection_url
        self.driver = BigchainDB(connection_url, headers=headers)
        self.app_id = headers.get('app_id', '')
        self.models = OrmModels()

    def define(self, model_name, model_schema):
        setattr(self.models, model_name, OrmModel(
            model_name,
            model_schema,
            self.driver,
            self.app_id))

    @staticmethod
    def keypair():
        return generate_keypair()
