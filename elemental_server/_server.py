import falcon

from elemental_backend import Controller, Model, serialization

from ._resource import Resource
from ._resource_collection import ResourceCollection


class Server(falcon.API):
    def __init__(self, **falcon_api_kwargs):
        super(Server, self).__init__(**falcon_api_kwargs)

        self._model = Model()
        self._controller = Controller(self._model)
        serialization.json.bind_to_controller(self._controller)

        self._resource = Resource(self._controller)
        self._content_types = ResourceCollection(self._controller, 'ContentType')
        self._attribute_types = ResourceCollection(self._controller, 'AttributeType')
        self._content_instances = ResourceCollection(self._controller, 'ContentInstance')
        self._attribute_instances = ResourceCollection(self._controller, 'AttributeInstance')

        self.add_route('/resources/{resource_id}', self._resource)
        self.add_route('/ContentType', self._content_types)
        self.add_route('/AttributeType', self._attribute_types)
        self.add_route('/ContentInstance', self._content_instances)
        self.add_route('/AttributeInstance', self._attribute_instances)

    def import_resource(self, resource_type, resource_data, data_format):
        self._controller.import_resource(resource_type, resource_data, data_format)