class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello, my name is {self.name}')


# Create a new instance of the Person class
p = Person('Matti')
p.hello() # Hello, my name is Matti