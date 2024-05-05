from flask import Flask

from tamp.interface.factory import AppFactoryAbs


class DefaultAppFactory(AppFactoryAbs):
    def get_app(self) -> Flask:
        app = Flask('project')

        return app


default_factory = DefaultAppFactory()
