from pprint import pformat
import json

from order import Order
from ship import Ship
import utility


class Port:
    def __init__(self, name, cargos):
        self.name = name
        self.cargos = cargos

    def __str__(self):
        return pformat(self.__dict__)


def move_ships_test(ships):
    for current_time in range(20):
        print '# day ', current_time
        for ship in ships:
            position = ship.get_position(current_time)
            if position:
                print '\t', ship.route_id, '\t', position


def game_loop(docks_by_name, all_ships):
    data = []
    money = 0
    for current_time in range(100):
        ships_by_docks = {}
        for ship in all_ships:
            position = ship.get_position(current_time)
            if position:
                ships_by_docks.setdefault(position, []).append(ship)

        if not ships_by_docks:
            continue

        for dock_name, ships in ships_by_docks.iteritems():
            money += docks_by_name[dock_name].handle_ships(ships, current_time)

        cargo_items = [cargo_item for dock in docks_by_name.values() for cargo_item in dock.cargo_items]
        cargo_items += [cargo_item for ship in ships for cargo_item in ship.cargo_items]

        data.append(utility.day_json([dock for dock in docks_by_name.values()], ships_by_docks, all_ships, current_time))

        if all([cargo_item.completed for cargo_item in cargo_items]):
            json.dump(data, open('out.json', 'w'))
            return money, [command for dock in docks_by_name.values() for command in dock.commands]

    json.dump(data, open('out.json', 'w'))
    raise Exception('Did not converge')


def main():
    ships = Ship.parse_input_file('menetrend.txt')
    orders = Order.parse_input_file('rakomany.txt')
    docks_by_name = utility.create_docks_by_name(ships, orders)
    money, commands = game_loop(docks_by_name, ships)
    print money
    utility.order_commands(commands)
    with open('output.txt', 'w') as output_file:
        for command in commands:
            output_file.write(command.get_string_line() + '\n')


if __name__ == '__main__':
    main()
