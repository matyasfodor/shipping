from pprint import pformat


class Ship:
    def __init__(self, route_id, capacity, source, target, duration1, duration2, start_day):
        self.route_id = route_id
        self.capacity = capacity
        self.source = source
        self.target = target
        self.duration1 = duration1
        self.duration2 = duration2
        self.start_day = start_day
        self.cargo_items = []

    def space_left(self):
        return self.capacity - sum([cargo_item.amount for cargo_item in self.cargo_items])

    def return_other_destination(self, destination):
        return self.target if self.source == destination else self.source if self.target == destination else None

    def add_cargo(self, new_cargo_item):
        # Just to check if all the cargo_items fits on the ship
        total_volume = sum([cargo_item.amount for cargo_item in self.cargo_items])
        if total_volume + new_cargo_item.amount > self.capacity:
            raise ValueError('too much cargo_items')
        self.cargo_items.append(new_cargo_item)

    def unload_cargo(self):
        all_cargo = self.cargo_items
        self.cargo_items = []
        return all_cargo

    def get_position(self, current_time):
        if current_time < self.start_day:
            return None

        whole_route_duration = self.duration1 + self.duration2
        place_in_route = (current_time - self.start_day) % whole_route_duration
        if place_in_route == 0:
            return self.source
        if place_in_route == self.duration1:
            return self.target
        return None

    def __str__(self):
        return pformat(self.__dict__)

    @staticmethod
    def parser(line):
        split_line = line.split()
        return Ship(split_line[0], int(split_line[1]), split_line[2], split_line[3], int(split_line[4]), int(split_line[5]), int(split_line[6]))

    @classmethod
    def parse_input_file(cls, filename):
        return [cls.parser(line) for line in open(filename, 'r') if not line.startswith('#')]
