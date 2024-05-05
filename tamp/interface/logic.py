from abc import abstractmethod

from tamp.interface.base import ProjectInterfaceBase
from tamp.interface.container import ContainerAbs


class LogicAbs(ProjectInterfaceBase):

    name: str = '...'  # 每一个logic必须要有唯一名称，用于core模块进行管理

    @abstractmethod
    def execute(self, container: ContainerAbs):

        ...
