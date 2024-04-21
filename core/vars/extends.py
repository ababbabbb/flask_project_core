from typing import Dict, Optional

from core.vars.abs import ExtendsAbs
from tamp.interface.container import ContainerAbs
from tamp.interface.logic import LogicAbs
from tamp.interface.scanner import ScannerAbs
from tamp.interface.shell import ShellAbs


class Extends(ExtendsAbs):
    """
        本对象仅是为了方便集中管理扩展，用来存储所有的scanner、container、logic
    """

    def __init__(self):
        self.map_scanner: Dict[str, ScannerAbs] = dict()
        self.map_container: Dict[str, ContainerAbs] = dict()
        self.map_logic: Dict[str, LogicAbs] = dict()
        self.map_shell: Dict[str, ShellAbs] = dict()

    def insert(
            self,
            scanner: ScannerAbs,
            container: ContainerAbs,
            logic: LogicAbs,
            shell: Optional[ShellAbs] = None
    ) -> bool:
        # 校验名称
        if shell:
            assert scanner.name == container.name and scanner.name == logic.name and scanner.name == shell.name, "the name is not the universal name of this extend"
        else:
            assert scanner.name == container.name and scanner.name == logic.name, "the name is not the universal name of this extend"

        assert not self.map_scanner.get(scanner.name, None), "the name has been existed in scanners"
        assert not self.map_container.get(scanner.name, None), "the name has been existed in containers"
        assert not self.map_logic.get(scanner.name, None), "the name has been existed in logics"
        if shell:
            assert not self.map_shell.get(scanner.name, None), "the name has been existed in shells"

        self.map_scanner[scanner.name] = scanner
        self.map_container[container.name] = container
        self.map_logic[logic.name] = logic
        if shell:
            self.map_shell[shell.name] = shell

        return True

    def query(self, name: str):
        return getattr(self, name, None)

    def destroy(self, name) -> bool:
        delattr(self, name)

        return True
