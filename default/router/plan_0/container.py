from default.router.NameFactory import name_extend
from tamp.interface.container import ContainerAbs
from tamp.interface.scanner import ScannerAbs


class Plan0RouterContainer(ContainerAbs):
    name = name_extend

    def __init__(self, project):
        self.cls_route = []
        super().__init__(project)

    def insert(self, path_dir: str, scanner: ScannerAbs):

        self.cls_route = scanner.scan(path_dir)

    def query(self):

        return self.cls_route
