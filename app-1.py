def get_city(worker):
    match worker:
        case {'address': {'city': worker_city}}:
            # if worker_city == 'London':
            #     print('OK')
            pass
        case _:
            raise ValueError('Cannot find worker city')

    return worker_city

if __name__ == '__main__':
    worker1 = {
        'name': 'John',
        'address': {'street': 'Green', 'city': 'London', 'number': 1}
    }
    print(get_city(worker1))

    worker2 = {
        'name': 'Anna',
        'address': {'street': 'Black', 'city': 'New York', 'number': 10}
    }
    print(get_city(worker2))

    worker3 = {
        'name': 'Anna'
    }
    print(get_city(worker3))