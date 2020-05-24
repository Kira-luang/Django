class Test:
    pass


class A(Test):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)


class B(metaclass=A):
    pass


class Test1(type):
    def __new__(cls, name, bases, dict):
        print(cls)
        print(name)
        print(bases)
        print(dict)
        return super().__new__(cls, name, bases, dict)


class C(metaclass=Test1):
    pass


class D(C):
    pass
