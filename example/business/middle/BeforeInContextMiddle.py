from flask import request

from flask_projects.default.middle.convention import InContextBeforeMiddle


class BeforeInContextMiddle(InContextBeforeMiddle):
    sort = 0

    def option_before_in_context(self):

        print(request.args)
        print(request.url)
