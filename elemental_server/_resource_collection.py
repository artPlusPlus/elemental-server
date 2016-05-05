import falcon

from elemental_backend import transactions, errors


class ResourceCollection(object):
    def __init__(self, controller, resource_type):
        self._controller = controller
        self._resource_type = resource_type

    def on_post(self, req, resp):
        inbound_payload = str(req.stream.read(), encoding='utf-8')
        transaction = transactions.Post(self._resource_type, 'json', inbound_payload)
        self._controller.process_transaction(transaction)

        if transaction.errors:
            pass
        else:
            resp.status = falcon.HTTP_201
            resp.location = 'resources/{0}'.format(transaction.resource_id)
