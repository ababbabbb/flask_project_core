from flask_projects.default.middle.convention import InContextBackMiddle


class BackInContextMiddle(InContextBackMiddle):
    sort = 0

    def option_back_in_context(self, response):

        print(response)

        return response
