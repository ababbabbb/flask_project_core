from abc import ABCMeta, abstractmethod
from typing import Any, Optional

from flask import Flask

from tamp.interface.container import ContainerAbs
from tamp.interface.logic import LogicAbs
from tamp.interface.scanner import ScannerAbs
from tamp.interface.shell import ShellAbs


class VarAbs(metaclass=ABCMeta):

    @abstractmethod
    def insert(self, *args, **kwargs) -> bool:
        """
            用于向存储对象插入对应的变量
        :param args:
        :param kwargs:
        :return: 为真表示正常，为false表异常
        """
        ...

    @abstractmethod
    def query(self, *args, **kwargs):
        """
            用于从对象中查询对应的变量
        :param args:
        :param kwargs:
        :return:
        """
        ...

    @abstractmethod
    def destroy(self, *args, **kwargs) -> bool:
        """
            用于从对象中删除对应的变量
        :param args:
        :param kwargs:
        :return:为真表示正常，为false表异常
        """
        ...


class ProjectInfoAbs(VarAbs):

    @abstractmethod
    def insert(self, name: str, var: Any) -> bool:
        ...

    @abstractmethod
    def query(self, name: str):

        ...

    @abstractmethod
    def destroy(self, name) -> bool:

        ...


class ExtendsAbs(VarAbs):

    @abstractmethod
    def insert(
            self,
            scanner: ScannerAbs,
            container: ContainerAbs,
            logic: LogicAbs,
            shell: Optional[ShellAbs] = None
    ) -> bool:
        ...

    @abstractmethod
    def query(self, name: str):
        ...

    @abstractmethod
    def destroy(self, name) -> bool:
        ...


class ApplicationAbs(VarAbs):

    @abstractmethod
    def setter_app(self, app: Flask):
        ...

    @abstractmethod
    def judge_exists_app(self) -> bool:
        ...

    @abstractmethod
    def insert(self, name: str, var: Any) -> bool:
        ...

    @abstractmethod
    def query(self, name: str):
        ...

    @abstractmethod
    def destroy(self, name) -> bool:
        ...


class OthersAbs(VarAbs):
    @abstractmethod
    def insert(self, name: str, var: Any) -> bool:
        ...

    @abstractmethod
    def query(self, name: str):
        ...

    @abstractmethod
    def destroy(self, name) -> bool:
        ...
