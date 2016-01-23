from dock import Dock
from pprint import pformat


def create_docks_from_orders(orders):
    orders_by_targets = {}
    order_by_source = {}
    for order in orders:
        orders_by_targets.setdefault(order.target, []).append(order)
        order_by_source.setdefault(order.source, []).append(order)

    docks = [Dock(name, [order.create_source_cargo() for order in order_by_source[name]]) for name, order_items in orders_by_targets.iteritems()]

    for only_source in set(order_by_source.keys()) - set(orders_by_targets.keys()):
        docks.append(Dock(only_source))

    return docks


def create_docks_from_ships(ships, already_existing_docks):
    dock_names = set()
    for ship in ships:
        dock_names.add(ship.source)
        dock_names.add(ship.target)

    docks = []
    for dock_name in dock_names - set(already_existing_docks):
        docks.append(Dock(dock_name))
    return docks


def create_docks_by_name(ships, orders):
    docks = create_docks_from_orders(orders)
    docks += create_docks_from_ships(ships, [dock.name for dock in docks])

    return {dock.name: dock for dock in docks}


def order_commands(commands):
    commands.sort(key=lambda command: (command.day, command.dock))


def print_state(docks, ships_by_docks, ships, current_time):
    print 'Day: {day}'.format(day=current_time)
    print 'Docks:'
    for dock in docks:
        print ''
        print dock.name
        print pformat(dock.cargo_items)
        print pformat([ship.route_id for ship in ships_by_docks.get(dock.name, [])])

    print '\nShips:'
    for ship in ships:
        print '\n{name}, {target}'.format(name=ship.route_id, target='')
        print pformat(ship.cargo_items)


def day_json(docks, ships_by_docks, ships, current_time):
    docks_json = []
    for dock in docks:
        dock_json = {
            'name': dock.name,
            'cargo': [repr(cargo_item) for cargo_item in dock.cargo_items],
            'ships': [ship.route_id for ship in ships_by_docks.get(dock.name, [])]
        }
        docks_json.append(dock_json)

    ships_json = []
    for ship in ships:
        ship_json = {
            'name': '{name}, {target}'.format(name=ship.route_id, target=''),
            'cargo': [repr(cargo_item) for cargo_item in ship.cargo_items],
        }
        ships_json.append(ship_json)

    data = {
        'day: ': current_time,
        'Docks': docks_json,
        'Ships': ships_json,
    }

    return data
