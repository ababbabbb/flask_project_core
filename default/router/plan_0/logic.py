from core.vars.application import application
from core.vars.http import http
from default.router.NameFactory import name_extend
from default.router.convention import RouterBasic
from tamp.interface.container import ContainerAbs
from tamp.interface.logic import LogicAbs


class Plan0RouterLogic(LogicAbs):
    name = name_extend

    def execute(self, container: ContainerAbs):

        list_cls_route: list = container.query()

        for cls_route in list_cls_route:
            instance: RouterBasic = cls_route(application, http)
            instance.register()
            instance.bind()
