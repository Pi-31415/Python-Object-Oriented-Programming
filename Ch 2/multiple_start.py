# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

# Class C has multiple inheritence, this is special to Python


class C(B, A):
    def __init__(self):
        super().__init__()

    def printprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

# Python interpreter uses Method Resolution Order to look up in class, if the properties is used in more than 1 super base class


c = C()
c.printprops()

print(C.__mro__)
# Look for Method Resolution Order
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# For this reason, the multiple inheritance is not used in the real world
# But useful in interface
