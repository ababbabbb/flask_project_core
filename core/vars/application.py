from typing import Any, Optional

from flask import Flask

from core.vars.abs import ApplicationAbs


class Application(ApplicationAbs):
    """
        本对象用于存储app，并为app的挂载提供适配后的接口
    """

    private_attrs = [
        'g'
    ]   # app中受保护的属性

    def __init__(self, app: Flask = None):
        self.app: Optional[Flask] = app

    def setter_app(self, app: Flask):
        self.app = app

        return self

    def judge_exists_app(self) -> bool:

        if not self.app:
            return False

        return True

    def insert(self, name: str, var: Any) -> bool:
        setattr(self.app, name, var)

        return True

    def query(self, name: str):

        return getattr(self.app, name, None)

    def destroy(self, name) -> bool:
        # TODO: 有些变量的删除必须阻止

        assert name not in self.private_attrs, "the attribute is private in application object"

        delattr(self.app, name)

        return True
