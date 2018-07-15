import uuid

# The likelihood to generate a vanity address that is 11 times "Burn" is extremely low:
# Use_of_vanitygen_to_try_to_attack_addresses - https: // en.bitcoin.it/wiki/Vanitygen
BURN_ADDRESS = 'BurnBurnBurnBurnBurnBurnBurnBurnBurnBurnBurn'


class OrmModels(object):
    pass


class OrmModel(object):

    _name = None
    _schema = None
    _driver = None
    _app_id = None

    def __init__(self, model_name, model_schema, driver, app_id='', tx_list=[]):
        self._name = model_name
        self._schema = model_schema
        self._driver = driver
        self._app_id = app_id

        if len(tx_list) > 0:
            self.tx_history = tx_list
            self.id = tx_list[0].get('asset').get(
                'data').get(self._get_id(), {}).get('id')
            self.data = dict()
            for txh in self.tx_history:
                self.data.update(txh.get('metadata'))

    def _get_id(self):
        return "{}-{}".format(self._app_id, self._name)

    def retrieve(self, inputs=None):
        query_id = inputs or self._get_id()
        assets = self._driver.assets.get(search=query_id, limit=2)
        result = []
        print(assets)
        for asset in assets:
            result.append(OrmModel(
                self._name, self._schema, self._driver, self._app_id,
                self._driver.transactions.get(asset_id=asset.get('id'))
            ))
        return result

    def create(self, inputs):
        payload = {}
        query_id = "id:{}:{}".format(self._app_id, uuid.uuid4())
        payload = {
            'data': {
                self._get_id(): {
                    'schema': self._schema,
                    'id': query_id,
                }
            }
        }

        prepared_creation_tx = self._driver.transactions.prepare(
            operation='CREATE',
            signers=inputs.get('keypair').public_key,
            asset=payload,
            metadata=inputs.get('data'),
        )

        # fulfill and send the transaction
        fulfilled_creation_tx = self._driver.transactions.fulfill(
            prepared_creation_tx,
            private_keys=inputs.get('keypair').private_key)

        # send commit
        result = self._driver.transactions.send_commit(fulfilled_creation_tx)
        return OrmModel(
            self._name, self._schema, self._driver, self._app_id,
            self._driver.transactions.get(asset_id=result.get('id'))
        )

    def append(self, inputs):
        pass

    def burn(self, inputs):
        pass
