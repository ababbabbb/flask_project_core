from typing import List, Any, Dict

from core.vars.abs import HttpAbs


class _Detail:

    def __init__(
            self,
            name: str,
            router: str,
            methods: List[str],
            resource: Any
    ):

        self.name = name
        self.router = router
        self.methods = methods
        self.resource = resource


class Http(HttpAbs):

    def __init__(self):

        self.map_detail: Dict[str, _Detail] = dict()
        self.map_routers: Dict[str, str] = dict()

    def insert(self, name: str, router: str, methods: List[str], resource: Any, **kwargs) -> bool:

        assert not self.map_detail.get(name, None), "the info of http has existed in project"

        detail = _Detail(name, router, methods, resource)

        if kwargs:
            for key, value in kwargs.items():
                setattr(detail, key, value)

        self.map_detail[name] = detail
        self.map_routers[name] = router

        return True

    def query(self, name: str):

        return self.map_detail.get(name, None)

    def query_router(self, name: str):

        return self.map_routers.get(name, None)

    def destroy(self, name: str) -> bool:
        del self.map_routers[name]
        del self.map_detail[name]

        return True


http = Http()
