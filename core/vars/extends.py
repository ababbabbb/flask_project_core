from typing import Dict, Optional

from core.vars.abs import ExtendsAbs
from tamp.interface.container import ContainerAbs
from tamp.interface.logic import LogicAbs
from tamp.interface.scanner import ScannerAbs
from tamp.interface.order import OrderAbs


class Extends(ExtendsAbs):
    """
        本对象仅是为了方便集中管理扩展，用来存储所有的scanner、container、logic
    """

    def __init__(self):
        self.map_scanner: Dict[str, ScannerAbs] = dict()
        self.map_container: Dict[str, ContainerAbs] = dict()
        self.map_logic: Dict[str, LogicAbs] = dict()
        self.map_order: Dict[str, OrderAbs] = dict()

    def insert(
            self,
            scanner: ScannerAbs,
            container: ContainerAbs,
            logic: LogicAbs,
            order: Optional[OrderAbs] = None
    ) -> bool:
        # 校验名称
        if order:
            assert scanner.name == container.name and scanner.name == logic.name and scanner.name == order.name, "the name is not the universal name of this extend"
        else:
            assert scanner.name == container.name and scanner.name == logic.name, "the name is not the universal name of this extend"

        assert not self.map_scanner.get(scanner.name, None), "the name has been existed in scanners"
        assert not self.map_container.get(scanner.name, None), "the name has been existed in containers"
        assert not self.map_logic.get(scanner.name, None), "the name has been existed in logics"
        if order:
            assert not self.map_order.get(scanner.name, None), "the name has been existed in orders"

        self.map_scanner[scanner.name] = scanner
        self.map_container[container.name] = container
        self.map_logic[logic.name] = logic
        if order:
            self.map_order[order.name] = order

        return True

    def query(self, name: str):
        if name not in self.map_scanner.keys():
            return {}

        return {
            'scanner': self.map_scanner.get(name),
            'container': self.map_container.get(name),
            'logic': self.map_logic.get(name),
            'order': self.map_order.get(name)
        }

    def query_names_scanner(self):

        return list(self.map_scanner.keys())

    def query_names_container(self):

        return list(self.map_container.keys())

    def query_names_logics(self):

        return list(self.map_logic.keys())

    def query_names_order(self):

        return list(self.map_order.keys())

    def query_scanner(self, name: str):

        return self.map_scanner.get(name, None)

    def query_container(self, name: str):

        return self.map_container.get(name, None)

    def query_logic(self, name: str):

        return self.map_logic.get(name, None)

    def query_order(self, name: str):

        return self.map_order.get(name, None)

    def destroy(self, name) -> bool:
        del self.map_scanner[name]
        del self.map_container[name]
        del self.map_logic[name]
        del self.map_order[name]

        return True
