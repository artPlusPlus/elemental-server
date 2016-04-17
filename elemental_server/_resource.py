import falcon

from elemental_backend import transactions, errors


class Resource(object):
    def __init__(self, controller):
        self._controller = controller

    def on_get(self, req, resp, resource_id):
        transaction = transactions.Get(resource_id, outbound_format='json')
        self._controller.process_transaction(transaction)

        if transaction.errors:
            if isinstance(transaction.errors[0], errors.ResourceNotFoundError):
                resp.status = falcon.HTTP_404
            else:
                resp.status = falcon.HTTP_500
            resp.body = transaction.errors[0].message
        else:
            resp.status = falcon.HTTP_200
            resp.body = transaction.outbound_payload

    def on_put(self, req, resp, resource_id):
        transaction = transactions.Put(resource_id, 'json', req.stream.read())
        self._controller.process_transaction(transaction)

        if transaction.errors:
            pass
        else:
            resp.status = falcon.HTTP_204

    def on_delete(self, req, resp, resource_id):
        transaction = transactions.Delete(resource_id)
        self._controller.process_transaction(transaction)

        if transaction.errors:
            pass
        else:
            resp.status = falcon.HTTP_204
