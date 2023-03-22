class Parent:

    a = 10
    b = 12

    def func1(self):
        print("this is parent class")

    def func_inherited(self):
        print("this is the first function")


class Child(Parent):
    def __init__(self):
        super().__init__()

    def func_inherited(self):
        super().func_inherited()
        print("this sentence has been joined to the function")


obj = Child()
print(obj.a+obj.b)
obj.func1()
obj.func_inherited()
