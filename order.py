from pprint import pformat

from cargo import Cargo


class Order:
    def __init__(self, article, amount, source, target, deadline):
        self.article = article
        self.amount = amount
        self.source = source
        self.target = target
        self.deadline = deadline
        self.completed = False

    def create_source_cargo(self):
        return Cargo.from_order(self)

    def __str__(self):
        return pformat(self.__dict__)

    @staticmethod
    def parser(line):
        split_line = line.split()
        return Order(split_line[0], int(split_line[1]), split_line[2], split_line[3], int(split_line[4]))

    @classmethod
    def parse_input_file(cls, filename):
        return [cls.parser(line) for line in open(filename, 'r') if not line.startswith('#')]
