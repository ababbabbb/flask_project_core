from flask_projects.convension import project
from flask_project_restful.container import RestfulContainer
from flask_project_restful.logic import RestfulLogic
from flask_project_restful.scanner import RestfulScanner


project.setter_args(
    ip='0.0.0.0',
    port='8080',
    path=__file__,
    debug=True
).setter_extend(
    RestfulScanner,
    RestfulContainer,
    RestfulLogic
)


if __name__ == '__main__':
    project.byOrder()
