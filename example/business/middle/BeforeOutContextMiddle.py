from flask_projects.default.middle.convention import OutContextBeforeMiddle


class BeforeOutContextMiddle(OutContextBeforeMiddle):
    sort = 0

    def option_before_out_context(self, environ, start_response):

        print(environ)
