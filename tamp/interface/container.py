from abc import abstractmethod

from tamp.interface.base import ProjectInterfaceBase


class ContainerAbs(ProjectInterfaceBase):

    name: str = '...'  # 每一个container必须要有唯一名称，用于core模块进行管理

    @abstractmethod
    def insert(self, *args, **kwargs):

        ...

    @abstractmethod
    def query(self, *args, **kwargs):

        ...
