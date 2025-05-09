"""
A simple program in python console app simulate a restaurant. A main menu with foods and 
drinks with price. The user choose the foods and drinks . After that the program generate 
 a list of items that user choose and bill for pay .A bill contain a list of choose items  
 their price bellow common bill. 

 How it works:

    Displays a menu with foods and drinks.

    The user types the name of the item to add to the order.

    When the user types "done", it prints a bill with selected items and total price.

"""

# Restaurant Simulation Console App

menu = {
    "Foods": {
        "Burger": 5.99,
        "Pizza": 8.49,
        "Pasta": 7.25
    },
    "Drinks": {
        "Water": 1.00,
        "Soda": 1.50,
        "Juice": 2.25
    }
}

order = []

def display_menu():
    print("\n--- Restaurant Menu ---")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item}: ${price:.2f}")

def take_order():
    while True:
        choice = input("\nEnter item name to order (or type 'done' to finish): ").strip()
        found = False
        if choice.lower() == 'done':
            break
        for category in menu:
            if choice in menu[category]:
                order.append((choice, menu[category][choice]))
                print(f"Added {choice} - ${menu[category][choice]:.2f}")
                found = True
                break
        if not found:
            print("Item not found. Please choose from the menu.")

def print_bill():
    print("\n--- Your Bill ---")
    total = 0
    for item, price in order:
        print(f"{item}: ${price:.2f}")
        total += price
    print("------------------")
    print(f"Total: ${total:.2f}")

# Run the app

def main ():
    display_menu()
    take_order()
    print_bill()


if __name__ == '__main__':
    main()

