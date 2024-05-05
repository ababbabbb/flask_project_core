from abc import ABCMeta, abstractmethod


class ProjectInterfaceBase(metaclass=ABCMeta):

    def __init__(self, project):

        self.project = project
