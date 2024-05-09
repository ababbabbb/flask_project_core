from core import project
from tamp.extends.restful.container import RestfulContainer
from tamp.extends.restful.logic import RestfulLogic
from tamp.extends.restful.scanner import RestfulScanner


project.setter_args(
    ip='0.0.0.0',
    port='8080',
    path=__file__
).setter_extend(
    RestfulScanner,
    RestfulContainer,
    RestfulLogic
)


if __name__ == '__main__':
    project.byOrder()
