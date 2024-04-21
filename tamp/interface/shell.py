from abc import abstractmethod

from tamp.interface.base import ProjectInterfaceBase


class ShellAbs(ProjectInterfaceBase):

    name: str = '...'  # 每一个shell必须要有唯一名称，用于core模块进行管理

    @abstractmethod
    def get_orders(self, *args, **kwargs):

        ...
