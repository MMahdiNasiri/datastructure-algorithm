# Single Responsibility Principle

# without principle
class UserWithoutPrinciple:
    def information(self):
        pass

    def accessibility(self):
        pass


# with principle

class User:
    def information(self):
        pass


class Access(User):
    def accessibility(self):
        pass
