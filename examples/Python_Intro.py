integer_var = 3
string_var = "Hello"
print(integer_var) # 3
print(string_var) # Hello



int_a = 5
int_b = int_a
print(int_b) # 5



array_a = [1,2,3]
array_b = array_a
array_b[0] = 5          # This also changes "array_a" because both variables point to the same memory place
print(array_a)          # [5, 2, 3]



a = 5
b = a # Now 'b' also points to the number 5
b = 6 # Now 'b' points to a memory place with the number 6
print(a) # But the original 'a' variable still points to the number 5



list_var = ['a', 'b', 'c', 10, 20, True] # It can contain different types
tuple_var = ('a', 'b', 'c', 10, 20, True) # It can contain different types, but tuple can't be modified after creation
set_var = {'a', 'b', 'c', 10, 20, True} # It can contain different types but not duplicates
string_var = "abc" # It can contain only characters
# Indexing:
list_var[0] # 'a'
tuple_var[0] # 'a'
# Set's elements can't be accessed with indexing
string_var[0] # 'a'



string_var = 'abc'
for character in string_var:
    print(character)
# a
# b
# c

# Note: Exactly the same code can be applied to lists, tuples and sets.



dict_var = {'name': 'Mika', 'age': 35, 'is_member': True}
for elem in dict_var: # Also dict_var.keys()
    print(elem)
# 'name'
# 'age'
# 'is_member'

for elem in dict_var.values():
    print(elem)
# 'Mika'
# 35
# True

# Remember that you can also iterate through both:
for key, value in dict_var.items():
    print(key, value)
# 'name' 'Mika'
# 'age' 35
# 'is_member' True



# Flow control
# If statement
if int_a == 1:
    print('int_a is 1')
    # execute something
elif int_b == 2:
    print('int_b is 2')
    # execute some other thing
else:
    print('int_a is not 1 and int_b is not 2')
    # execute something else



# For loop
for i in range(5):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
for v in ['a', 'b', 'c']:
    print(v)
    # a
    # b
    # c



# While loop
a = 0
while a < 100:
    b = int(input('Say a number: '))
    a += b



# Operators
# Arithmetic operators
a = 5
b = 2
a + b # 7
a - b # 3
a * b # 10
a / b # 2.5
a // b # 2
a % b # 1
a ** b # 25

# Comparison operators
a == b # False
a != b # True
a > b # True
a < b # False
a >= b # True
a <= b # False

# Logical operators
boolseal_a = True
boolseal_b = False
boolseal_a and boolseal_b # False
boolseal_a or boolseal_b # True
not boolseal_a # False



# Functions
def my_function(a, b):
    return a + b
result = my_function(3, 4)
print(result) # 7



def my_function(parameter):
# Do something inside the function
    return f'You passed this parameter to the function: {parameter}'



# Classes
class MyClass():
    def __init(self):
        self.my_property = 1
    def increase(self):
        self.my_property += 1
    def decrease(self):
        self.my_property -= 1



my_object = MyClass()
print(my_object.my_property) # 1
my_object.increase()
print(my_object.my_property) # 2
my_object.decrease()
print(my_object.my_property) # 1



# Example of a class Variable
class Car:
    wheels = 4  # Class variable

    def __init__(self, color):
        self.color = color  # Instance variable

# All cars have 4 wheels, shared by all instances
car1 = Car("Red")
car2 = Car("Blue")

print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4

Car.wheels = 6  # Changing the class variable affects all instances
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6