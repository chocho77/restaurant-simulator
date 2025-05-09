"""

Would you like to add features like multiple customers, tax calculation, or a simple GUI next?
You said:
Yes

Perfect! Let's add the next features step by step. Here's an upgraded version with:

    Tax Calculation (e.g., 5% tax)

    Multiple Customers Support (loop until user exits)

    Improved Bill Format (itemized with tax, discount, final total)

    Summary of Features:

    Handles multiple customers, each with a separate bill.

    Applies tax (5%) and discount (10%) if subtotal > $20.

    Saves each bill to a separate file with timestamp and customer ID.

"""

import datetime

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

TAX_RATE = 0.05  # 5%
DISCOUNT_THRESHOLD = 20.0
DISCOUNT_RATE = 0.10

def display_menu():
    print("\n--- Restaurant Menu ---")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f"  {item}: ${price:.2f}")

def take_order():
    order = {}
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
    return order

def calculate_bill(order):
    lines = []
    subtotal = 0
    for item, info in order.items():
        line_total = info['price'] * info['quantity']
        subtotal += line_total
        lines.append(f"{item:<12} x {info['quantity']} = ${line_total:.2f}")
    
    discount = DISCOUNT_RATE * subtotal if subtotal > DISCOUNT_THRESHOLD else 0
    tax = TAX_RATE * (subtotal - discount)
    total = subtotal - discount + tax

    return lines, subtotal, discount, tax, total

def print_and_save_bill(customer_id, lines, subtotal, discount, tax, total):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"bill_customer_{customer_id}.txt"
    with open(filename, "w") as f:
        f.write(f"--- Customer {customer_id} Bill ---\n")
        f.write(f"Date: {timestamp}\n\n")
        for line in lines:
            f.write(line + "\n")
        f.write(f"\nSubtotal: ${subtotal:.2f}\n")
        if discount > 0:
            f.write(f"Discount (10%): -${discount:.2f}\n")
        f.write(f"Tax (5%): +${tax:.2f}\n")
        f.write(f"Total: ${total:.2f}\n")
    print(f"\nBill saved to '{filename}'")

def main():
    customer_id = 1
    while True:
        print(f"\n--- New Customer #{customer_id} ---")
        display_menu()
        order = take_order()
        if not order:
            print("No items ordered.")
        else:
            lines, subtotal, discount, tax, total = calculate_bill(order)
            print("\n".join(lines))
            print(f"\nSubtotal: ${subtotal:.2f}")
            if discount > 0:
                print(f"Discount: -${discount:.2f}")
            print(f"Tax: +${tax:.2f}")
            print(f"Total to Pay: ${total:.2f}")
            print_and_save_bill(customer_id, lines, subtotal, discount, tax, total)

        again = input("\nServe next customer? (y/n): ").lower()
        if again != 'y':
            print("Closing restaurant. Goodbye!")
            break
        customer_id += 1


# Start the restaurant simulation
if __name__ == '__main__':
    main()
