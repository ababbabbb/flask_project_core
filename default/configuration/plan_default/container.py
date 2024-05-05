from typing import Optional

from default.configuration.NameFactory import name_extend
from tamp.interface.container import ContainerAbs
from tamp.interface.scanner import ScannerAbs


class DefaultConfigurationContainer(ContainerAbs):
    name = name_extend

    def __init__(self, project):
        self.configs: Optional = None
        super().__init__(project)

    def insert(self, path_dir: str, scanner: ScannerAbs):
        self.configs = scanner.scan(path_dir)

    def query(self):

        return self.configs
