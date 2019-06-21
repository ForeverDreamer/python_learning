import abc


class AbsCar(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def description(self):
        pass

    @property
    @abc.abstractmethod
    def cost(self):
        pass
