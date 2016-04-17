import falcon

from elemental_backend import transactions, errors


class ResourceCollection(object):
    def __init__(self, controller, resource_type):
        self._controller = controller
        self._resource_type = resource_type

    def on_post(self, req, resp):
        transaction = transactions.Post(self._resource_type, 'json',
                                        req.stream.read())
        self._controller.ProcessTransaction(transaction)

        if transaction.errors:
            pass
        else:
            resp.status = falcon.HTTP_201
            resp.location = 'resources/{0}'.format(transaction.resource_id)
