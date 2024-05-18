from flask_projects.default.router.convention import RouterBasic


def view_func():

    return "hello"


class Unity(RouterBasic):
    def register(self):

        self.add_route('/hello', ['GET'], view_func)
