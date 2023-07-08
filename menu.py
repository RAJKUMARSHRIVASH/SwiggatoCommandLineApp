menu = []

dish = {
    'id': 1,
    'name': 'Pizza Margherita',
    'price': 10.99,
    'availability': True
}


def add_dish(dish_id, name, price):
    new_dish = {
        'id': dish_id,
        'name': name,
        'price': price,
        'availability': True
    }
    menu.append(new_dish)

def remove_dish(dish_id):
    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            break


def update_availability(dish_id, availability):
    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = availability
            break

