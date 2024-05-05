from typing import Any, Optional, List

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
        self.record: List[str] = list()

    def setter_app(self, app: Flask):

        for name_attr in self.record:
            setattr(app, name_attr, self.query(name_attr))

        self.app = app

        return self

    def judge_exists_app(self) -> bool:

        if not self.app:
            return False

        return True

    def insert(self, name: str, var: Any) -> bool:
        assert name not in self.private_attrs, "the attribute is private in application object"

        setattr(self.app, name, var)
        if name not in self.record:
            self.record.append(name)

        return True

    def query(self, name: str):

        return getattr(self.app, name, None)

    def destroy(self, name) -> bool:
        # TODO: 有些变量的删除必须阻止

        assert name not in self.private_attrs, "the attribute is private in application object"

        delattr(self.app, name)
        self.record.remove(name)

        return True


application = Application()
