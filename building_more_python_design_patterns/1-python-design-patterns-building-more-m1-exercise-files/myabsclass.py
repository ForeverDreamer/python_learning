import abc


class MyAbsClass(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def myproperty(self):
        pass

    @property
    @abc.abstractmethod
    def mymethod(self, value):
        pass


class MyConcreteClass(MyAbsClass):

    @property
    def myproperty(self):
        return 42

    def mymethod(self, value):
        assert 42 == 42


c = MyConcreteClass()
print(c.myproperty)
