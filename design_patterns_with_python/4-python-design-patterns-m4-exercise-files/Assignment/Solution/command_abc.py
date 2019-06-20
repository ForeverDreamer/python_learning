import abc


class AbsCommand(object, metaclass=abc.ABCMeta):  # Python 3.x

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass
