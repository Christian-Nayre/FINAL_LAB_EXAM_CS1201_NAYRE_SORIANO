class MyClass:
    def __init__(self, name):
        self.name = name

    def function(self, name):
        print(f'my name is {name}')

# var = MyClass("string")
input_name = input("enter: ")
MyClass.function("args" , input_name)

