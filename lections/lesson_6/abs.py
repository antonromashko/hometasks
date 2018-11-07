from abc import abstractmethod, ABC, ABCMeta


class A(ABC):
    pass


class B(metaclass=ABCMeta):
    pass


class C:
    @abstractmethod
    def foo(self):
        pass


class D(ABC):
    @abstractmethod
    def foo(self):
        pass


class E(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

a=A()
b=B()
c=C()

try:
    d=D()
except Exception as e:
    print("Error:", str(e))

try:
    d=E()
except Exception as e:
    print("Error:", str(e))


class Iter(ABC):
    @abstractmethod
    def __iter__(self):
        pass


class MyIter(Iter):
    def __iter__(self):
        yield "Yo"


for i in MyIter():
    print(i)


class F:
    pass


B.register(F)

print("F is a child of B?", isinstance(F(),B))
print("F is a subclass of B?", issubclass(F,B))

print("F MRO:", F.mro())
