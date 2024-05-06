from core import project


project.setter_args(
    ip='0.0.0.0',
    port='8080',
    path=__file__
)


if __name__ == '__main__':
    project.byOrder()
