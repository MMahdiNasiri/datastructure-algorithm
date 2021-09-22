# Dependency Inversion Principle


# Without Principle
class EmployeeWOP:#WOP means WithOut Principle
    pass


class AccountantWOP(EmployeeWOP):
    pass


class ManagerWOP:
    def __init__(self):
        self.subaltern = []

    def set_subaltern(self, _subaltern):
        self.subaltern.append(_subaltern)


# With Principle
# Abstraction Class
class Person:
    pass


class Employee(Person):
    pass


class Accountant(Person):
    pass


class Manager(Person):
    def __init__(self):
        self.subaltern = []

    def set_subaltern(self, _subaltern):
        self.subaltern.append(_subaltern)