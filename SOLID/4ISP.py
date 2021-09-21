# Interface Segregation Principle

# without Principle
class UserWithOutPrinciple:
    def clean_room(self):
        pass

    def program(self):
        pass

    def manage_costs(self):
        pass
# a Accountant doesn't need "program" & "clean_room" function


# with Principle
class User:
    pass


class Janitor(User):
    def clean_room(self):
        pass


class Programmer(User):
    def program(self):
        pass


class Accountant(User):
    def manage_costs(self):
        pass
