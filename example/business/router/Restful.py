from flask_project_restful.convertion import RestfulRouterBasic, ResourceBaisc


class RestfulController(ResourceBaisc):

    def get(self):

        return 'flask_project_restful'


class Restful(RestfulRouterBasic):

    def register(self):

        self.dict_resource = {
            '/rest': RestfulController
        }
