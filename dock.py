import random


class Command:
    def __init__(self, day, route_id, cargo_name, expiry, amount, dock):
        self.day = day
        self.route_id = route_id
        self.cargo_name = cargo_name
        self.expiry = expiry
        self.amount = amount
        self.dock = dock

    def get_string_line(self):
        return '{day} {route_id} {cargo_name} {expiry} {amount}'.format(
            day=self.day,
            route_id=self.route_id,
            cargo_name=self.cargo_name,
            expiry=self.expiry,
            amount=self.amount
        )


class Dock:
    def __init__(self, name, cargo=None):
        self.name = name
        self.cargo_items = cargo or []
        self.commands = []

    def add_to_ship(self, ship, cargo, current_time):
        command = Command(current_time, ship.route_id, cargo.name, cargo.expiry, cargo.amount, self.name)
        self.commands.append(command)
        ship.add_cargo(cargo)

    def handle_ships(self, ships, current_time):
        ship_cargo_items = []
        for ship in ships:
            ship_cargo_items += ship.unload_cargo()

        money = 0
        for ship_cargo in ship_cargo_items:
            if ship_cargo.target == self.name:
                ship_cargo.completed = True
                money += ship_cargo.amount * (30 if ship_cargo.expiry > current_time else 10)

        self.cargo_items += ship_cargo_items

        for cargo_item in self.cargo_items:
            cargo_item.visited.add(self.name)

        cargo_items_to_further_ship = [cargo_item for cargo_item in self.cargo_items if not cargo_item.completed]
        cargo_ids_to_remove = set()
        ships_to_upload = set()

        for ship in ships:
            for cargo_item in cargo_items_to_further_ship:
                if ship.space_left() == 0:
                    break
                if cargo_item.can_go_to(ship.return_other_destination(self.name)):
                    if cargo_item.amount > ship.space_left():
                        new_cargo_item = cargo_item.divide(cargo_item.amount - ship.space_left())
                        self.add_to_ship(ship, new_cargo_item, current_time)
                    else:
                        self.add_to_ship(ship, cargo_item, current_time)
                        cargo_ids_to_remove.add(id(cargo_item))
            if ship.space_left() > 0:
                ships_to_upload.add(ship)

        self.cargo_items = [cargo_item for cargo_item in self.cargo_items if id(cargo_item) not in cargo_ids_to_remove]

        for ship in ships_to_upload:
            for cargo_item in self.cargo_items:
                if ship.space_left() == 0:
                    break
                if random.choice([True, False]):
                    if cargo_item.amount > ship.space_left():
                        new_cargo_item = cargo_item.divide(cargo_item.amount - ship.space_left())
                        self.add_to_ship(ship, new_cargo_item, current_time)
                    else:
                        self.add_to_ship(ship, cargo_item, current_time)
                        cargo_ids_to_remove.add(id(cargo_item))

        self.cargo_items = [cargo_item for cargo_item in self.cargo_items if id(cargo_item) not in cargo_ids_to_remove]

        return money
