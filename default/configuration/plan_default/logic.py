from core.vars.application import application
from default.configuration.NameFactory import name_extend
from tamp.interface.container import ContainerAbs
from tamp.interface.logic import LogicAbs


class DefaultConfigurationLogic(LogicAbs):
    name = name_extend

    def execute(self, container: ContainerAbs):
        configs = container.query()

        for config_cls in configs:
            config_cls(application)
