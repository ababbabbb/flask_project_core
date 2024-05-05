from typing import Optional

from core.order.executor import loader
from core.proj.abs import ProjectAbs
from core.vars.abs import ProjectInfoAbs, ExtendsAbs, ApplicationAbs, OthersAbs
from core.vars.application import Application
from core.vars.extends import Extends
from core.vars.info import ProjectInfo
from core.vars.others import OthersVars
from tamp.interface.container import ContainerAbs
from tamp.interface.logic import LogicAbs
from tamp.interface.scanner import ScannerAbs
from tamp.interface.order import OrderAbs


class Project(ProjectAbs):

    def __init__(self):
        # 初始化，生成必要的容器/对象作为属性
        self.info: Optional[ProjectInfoAbs] = ProjectInfo()
        self.extends: Optional[ExtendsAbs] = Extends()
        self.application: Optional[ApplicationAbs] = Application()

        self.others: Optional[OthersAbs] = OthersVars()

        self.manager_shell = None

        # 向容器属性中加入默认/内置内容
        ...  # TODO 2024/4/21 初始化加载内容

    def setter_extend(self, scanner: ScannerAbs, container: ContainerAbs, logic: LogicAbs,
                      order: Optional[OrderAbs] = None):
        self.extends.insert(scanner, container, logic, order)

        return self

    def setter_app(self, scanner: ScannerAbs, container: ContainerAbs, logic: LogicAbs,
                   shell: Optional[OrderAbs] = None):
        # TODO 2024/4/21 app配置过程(主要是参考以前的老方案)

        return self

    def setter_args(
            self,
            ip: str = '0.0.0.0',
            port: int = 8080,
            *args,
            **kwargs
    ):
        self.info.insert('ip', ip)
        self.info.insert('port', port)
        self.info.insert('args', list(args))

        for key, value in kwargs.items():
            self.info.insert(key, value)

        return self

    def byOrder(self):
        executor = loader(self)
        executor()

    def __call__(self, *args, **kwargs):
        # TODO 2024/4/21 老版本里面重写了这个，既解决了部分配置，也从编码上使其看起来像创建对象，可以考虑设计一下

        return self


project = Project()
