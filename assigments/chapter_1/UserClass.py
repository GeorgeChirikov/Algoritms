class User:
    def __init__(self, firstName, lastName, username, email, location):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f'Name: {self.firstName} {self.lastName}')
        print(f'Username: {self.username}')
        print(f'Email: {self.email}')
        print(f'Location: {self.location}')

    def greet_user(self):
        print(f'Welcome back {self.username}!')


Matti= User('Matti', 'Paajanen', 'mpaajanen', 'm.paajanen@gmail.com', 'Helsinki')
Matti.describe_user()

Maila= User('Maila', 'Halonen', 'm_halonen', 'm.halonen@mtv.fi', 'Vaasa')
Maila.greet_user()