from typing import Any

from core.vars.abs import OthersAbs


class OthersVars(OthersAbs):
    def insert(self, name: str, var: Any) -> bool:
        setattr(self, name, var)

        return True

    def query(self, name: str):
        return getattr(self, name, None)

    def destroy(self, name) -> bool:
        delattr(self, name)

        return True
