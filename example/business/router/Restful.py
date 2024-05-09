from tamp.extends.restful.convertion import RestfulRouterBasic, ResourceBaisc


class RestfulController(ResourceBaisc):

    def get(self):

        return 'restful'


class Restful(RestfulRouterBasic):

    def register(self):

        self.dict_resource = {
            '/rest': RestfulController
        }
