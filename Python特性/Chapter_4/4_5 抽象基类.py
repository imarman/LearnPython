# 用抽象基类避免继承错误(ABC)
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        raise NotImplementedError()

    @abstractmethod
    def bar(self):
        raise NotImplementedError()


class Concrete(Base):
    def foo(self):
        return 'foo() called'

    def bar(self):
        return 'bar() called'


c = Concrete()
