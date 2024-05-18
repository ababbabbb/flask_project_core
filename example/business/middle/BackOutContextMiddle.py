from flask_projects.default.middle.convention import OutContextBackMiddle


class BackOutContextMiddle(OutContextBackMiddle):
    sort = 0

    def option_back_out_context(self, response):

        print(response)

        return response
