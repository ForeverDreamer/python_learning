from abc import ABCMeta, abstractmethod


class AbsObserver(object, metaclass=ABCMeta):
    
    @abstractmethod
    def update(self, value):
        pass
    
    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass
