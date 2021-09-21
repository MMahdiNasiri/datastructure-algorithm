# Liskov Substitution Principle

class User:
    def __init__(self):
        pass


# without Principle
class EmployeeWithOutPrinciple(User):
    def __init__(self, salary):
        self.salary = salary


# with Principle
class Employee(User):
    def __init__(self):
        super().__init__()
        self.salary = None
        # some other stuff

    def set_salary(self, salary):
        self.salary = salary
