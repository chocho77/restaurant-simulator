"""
Would you like this extended with features like quantities, discounts, or saving the bill to a file?
Yes

Great! Here's an enhanced version of the restaurant simulator with:

    Quantities for each item

    A discount option (e.g., 10% off if the total is above $20)

    Option to save the bill to a text file bill.txt.

"""

# Enhanced Restaurant Simulator

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

order = {}

def display_menu():
    print("\n--- Restaurant Menu ---")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item}: ${price:.2f}")

def take_order():
    while True:
        choice = input("\nEnter item name to order (or type 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        found = False
        for category in menu:
            if choice in menu[category]:
                try:
                    qty = int(input(f"Enter quantity for {choice}: "))
                    if choice in order:
                        order[choice]['quantity'] += qty
                    else:
                        order[choice] = {
                            'price': menu[category][choice],
                            'quantity': qty
                        }
                    print(f"Added {qty} x {choice}")
                    found = True
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
                break
        if not found:
            print("Item not found. Please choose from the menu.")

def print_bill():
    print("\n--- Your Bill ---")
    total = 0
    bill_lines = []
    for item, info in order.items():
        line_total = info['price'] * info['quantity']
        total += line_total
        line = f"{item} x {info['quantity']} = ${line_total:.2f}"
        bill_lines.append(line)
        print(line)
    
    discount = 0
    if total > 20:
        discount = total * 0.10
        print(f"Discount (10%): -${discount:.2f}")

    final_total = total - discount
    print("------------------")
    print(f"Total: ${final_total:.2f}")
    
    save_bill(bill_lines, discount, final_total)

def save_bill(bill_lines, discount, final_total):
    with open("bill.txt", "w") as f:
        f.write("--- Your Bill ---\n")
        for line in bill_lines:
            f.write(line + "\n")
        if discount > 0:
            f.write(f"Discount (10%): -${discount:.2f}\n")
        f.write("------------------\n")
        f.write(f"Total: ${final_total:.2f}\n")
    print("\nBill saved to 'bill.txt'")


# main function
def main():
    display_menu()
    take_order()
    print_bill()


# Run the app
if __name__ == '__main__':
    main()

