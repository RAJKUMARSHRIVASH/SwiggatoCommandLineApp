from menu import menu

orders = []

order = {
    'order_id': 1,
    'customer_name': 'John',
    'dish_ids': [1, 3, 5],
    'status': 'received'
}


def take_order(customer_name, dish_ids):
    available_dish_ids = [dish['id'] for dish in menu if dish['availability']]
    if set(dish_ids).issubset(available_dish_ids):
        order_id = len(orders) + 1
        total_price = 0.0
        ordered_dishes = []
        for dish_id in dish_ids:
            for dish in menu:
                if dish['id'] == dish_id:
                    total_price += dish['price']
                    ordered_dishes.append(dish['name'])
                    break

        new_order = {
            'order_id': order_id,
            'customer_name': customer_name,
            'dish_ids': dish_ids,
            'status': 'received',
            'total_price': total_price
        }
        orders.append(new_order)
        print(f"Order {order_id} received and being processed.")
        print(f"Ordered Dishes: {', '.join(ordered_dishes)}")
        print(f"Total Price: ${total_price}")
    else:
        print("Some of the selected dishes are not available.")


def update_order_status(order_id, status):
    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = status
            break

def review_orders(status_filter=None):
    for order in orders:
        if status_filter is None or order['status'] == status_filter:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Dish IDs: {order['dish_ids']}")
            print(f"Status: {order['status']}")
            print(f"Total Price: ${order['total_price']}")
            print("----------------------")

