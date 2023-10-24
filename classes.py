""""creating the restaurent class """

class Restaurents:

    def __init__(self,restaurent_name,cuisine_name):
        self.restaurent_name = restaurent_name
        self.cuisine_name = cuisine_name
        self.number_served = 0

    def describe_restaurent(self):
        print(f"\n{self.restaurent_name} is famous for {self.cuisine_name}")
        print(f"Total Number of Customers Served Today : {self.number_served}")

    def open_restaurent(self):
        print(f"{self.restaurent_name} open till 23:00")

    def set_number_served(self,number):
        self.number_served = number
        print(f"Total Number of Customers Served Today is {self.number_served}")

    def increment_num_served(self,increment):
        self.number_served += increment
        print(f"Total Number of Customers Served Today is Incremented By {self.number_served}")



restaurent = Restaurents('Devi','Chicken Biryani')
restaurent.describe_restaurent()
restaurent.open_restaurent()

restaurent1 = Restaurents('Paradise','Mutton Soup')
restaurent1.describe_restaurent()
restaurent1.set_number_served(500)
restaurent1.increment_num_served(200)







"""User Class"""

class User:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.village = 'Hyderabad'
        self.login_attempt = 0

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} from {self.village.title()}")

    def greet_user(self):
        print(f"Welcome to the Gan {self.first_name} {self.last_name}\n")

    def login_attempts(self):
        self.login_attempt += 1
        print(f"Login Attempts are {self.login_attempt}")

    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f"Login Attempts reset to {self.login_attempt}")


users = User('Chandu','Dhondi')
users.village= 'Delhi'
users.describe_user()
users.greet_user()
users.login_attempts()
users.login_attempts()
users.login_attempts()



"""Ice Cream Stand"""

class IceCreamStand(Restaurents):

    def __init__(self,restaurent_name,cuisine_name,flavours):
        self.flavours = flavours
        super().__init__(restaurent_name,cuisine_name)

    def dis_flavours(self):
        for flavour in self.flavours:
            print("\n",flavour)


ice_cream = IceCreamStand('Cream Stone','Ice-Creams',
                          ['Vanilla','Strawberry','Chocolate','butterscotch'])
ice_cream.dis_flavours()

"""Privileges"""
class Privileges:

    def __init__(self):
        privilages = ['can add a post', 'can delete a post', 'can ban a post']
        self.privilages = privilages

    def show_privileges(self):
        for privilage in self.privilages:
            print("\n",privilage.title())



"""Admin"""

class Admin(User):

    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.pri = Privileges()


admin = Admin('chandu',
              'dhondi')
admin.pri.show_privileges()



