import abc


class AbsFactory(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def create_economy():
        pass

    @staticmethod
    @abc.abstractmethod
    def create_sport():
        pass

    @staticmethod
    @abc.abstractmethod
    def create_luxury():
        pass
