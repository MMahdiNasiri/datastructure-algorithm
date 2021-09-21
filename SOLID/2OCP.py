# Open - Close Principle

# without principle
class UserWithoutPrinciple:
    def task(self):
        if self.job == 'Accountant':
            # some task append
            pass
        elif self.job == 'Programmer':
            # some other task
            pass


# with principle
class User:
    def task(self):
        pass


class Accountant(User):
    def task(self):
        # do something relevant
        pass


class Programmer(User):
    def task(self):
        # do something relevant
        pass
