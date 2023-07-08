import json
from menu import menu, add_dish, remove_dish, update_availability
from order import orders, take_order, update_order_status, review_orders

def save_data():
    with open('data.json', 'w') as file:
        data = {
            'menu': menu,
            'orders': orders
        }
        json.dump(data, file)


def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            menu.extend(data['menu'])
            orders.extend(data['orders'])
    except FileNotFoundError:
        pass


def main():
    load_data()

    while True:
        print("Welcome to Swiggato Food Delivery App")
        print("1. Add a dish to the menu")
        print("2. Remove a dish from the menu")
        print("3. Update dish availability")
        print("4. Take a new order")
        print("5. Update order status")
        print("6. Review all orders")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            dish_id = int(input("Enter dish ID: "))
            name = input("Enter dish name: ")
            price = float(input("Enter dish price: "))
            add_dish(dish_id, name, price)
            print("Dish added to the menu.")

        elif choice == '2':
            dish_id = int(input("Enter dish ID to remove: "))
            remove_dish(dish_id)
            print("Dish removed from the menu.")

        elif choice == '3':
            dish_id = int(input("Enter dish ID to update availability: "))
            availability = input(
                "Enter availability (yes/no): ").lower() == 'yes'
            update_availability(dish_id, availability)
            print("Dish availability updated.")

        elif choice == '4':
            customer_name = input("Enter customer name: ")
            dish_ids = [int(dish_id) for dish_id in input(
                "Enter dish IDs (comma-separated): ").split(',')]
            take_order(customer_name, dish_ids)

        elif choice == '5':
            order_id = int(input("Enter order ID to update status: "))
            status = input("Enter new status: ")
            update_order_status(order_id, status)
            print("Order status updated.")

        elif choice == '6':
            status_filter = input(
                "Enter status to filter orders (leave empty to show all): ")
            review_orders(status_filter)

        elif choice == '7':
            save_data()
            print("Thank you for using Swiggato Food Delivery App. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == '__main__':
    main()
