class Cargo:

    def __init__(self, name, amount, target, expiry, completed=False, visited=None):
        self.name = name
        self.amount = amount
        self.target = target
        self.expiry = expiry
        self.completed = completed
        self.visited = visited

    def can_go_to(self, target):
        return target not in self.visited

    def divide(self, remaining):
        if remaining >= self.amount:
            raise ValueError('Remaining should be less than the whole amount')
        new_cargo = Cargo(**self.__dict__)
        new_cargo.amount = self.amount - remaining
        self.amount = remaining
        return new_cargo

    @staticmethod
    def from_order(order):
        return Cargo(order.article, order.amount, order.target, order.deadline, visited={order.source})

    def __repr__(self):
        return ('*' if self.completed else '') + '{name}, {target}'.format(name=self.name, target=self.target)
