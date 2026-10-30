


# Student Information
student_name = "Awais Mumtaz"
student_id = "S2026065053"

# Student ID is used as Restaurant Name
restaurant_name = student_id


# Dictionary to store menu items, prices and stock
menu = {
    "Burger": {"price": 800, "stock": 10},
    "Pizza": {"price": 1500, "stock": 8},
    "Sandwich": {"price": 500, "stock": 15},
    "Pasta": {"price": 1200, "stock": 10},
    "Fries": {"price": 300, "stock": 20},
    "Cold Drink": {"price": 150, "stock": 25}
}


# Dictionary to store customer orders
order = {}


# Function to display restaurant menu
def display_menu():

    print("\n========== RESTAURANT MENU ==========")

    print(f"{'Item':<15} {'Price (PKR)':<15} {'Available Stock'}")

    for item, details in menu.items():

        if details["stock"] > 0:

            print(
                f"{item:<15} "
                f"{details['price']:<15} "
                f"{details['stock']}"
            )

    print("=====================================")


# Function to add items to order
def add_item():

    display_menu()

    item = input("\nEnter item name: ").strip().title()

    if item not in menu:
        print("Invalid item! Please select an item from the menu.")
        return

    if menu[item]["stock"] <= 0:
        print("Sorry! This item is currently unavailable.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        # Check already ordered quantity
        already_ordered = order.get(item, 0)

        available_stock = menu[item]["stock"] - already_ordered

        if quantity > available_stock:
            print("Sorry! Requested quantity exceeds available stock.")
            print("Available quantity:", available_stock)
            return

        # Add quantity to existing item or create new entry
        order[item] = already_ordered + quantity

        print(f"{quantity} {item}(s) added successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


# Function to remove items from order
def remove_item():

    if not order:
        print("\nYour order is empty.")
        return

    print("\n========== YOUR CURRENT ORDER ==========")

    for item, quantity in order.items():
        print(f"{item}: {quantity}")

    item = input("\nEnter item name to remove: ").strip().title()

    if item not in order:
        print("This item is not present in your order.")
        return

    try:
        quantity = int(input("Enter quantity to remove: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > order[item]:
            print("You cannot remove more than the ordered quantity.")
            return

        order[item] -= quantity

        if order[item] == 0:
            del order[item]

        print(f"{quantity} {item}(s) removed successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


# Function to display current order
def display_order():

    if not order:
        print("\nYour order is currently empty.")
        return

    print("\n========== CURRENT ORDER ==========")

    for item, quantity in order.items():

        price = menu[item]["price"]

        print(
            f"{item} | Quantity: {quantity} | "
            f"Price: PKR {price} | "
            f"Total: PKR {price * quantity}"
        )


# Function to calculate bill and generate receipt
def generate_receipt():

    if not order:
        print("\nCannot confirm an empty order.")
        return

    subtotal = 0

    print("\n======================")
    print(f"              {restaurant_name}")
    print("             RESTAURANT RECEIPT")
    print("======================")

    print("Student Name:", student_name)
    print("Student ID:", student_id)

    print("------------------------")

    print(
        f"{'Item':<14} {'Qty':<5} "
        f"{'Price':<9} {'Total':<10}"
    )

    print("-------------------------")

    # Calculate subtotal
    for item, quantity in order.items():

        price = menu[item]["price"]

        line_total = price * quantity

        subtotal += line_total

        print(
            f"{item:<14} {quantity:<5} "
            f"{price:<9} {line_total:<10}"
        )

    # Apply discount
    discount_percentage = 0

    if subtotal > 10000:
        discount_percentage = 15

    elif subtotal > 5000:
        discount_percentage = 10

    discount_amount = subtotal * discount_percentage / 100

    final_amount = subtotal - discount_amount

    print("------------------------")

    print(f"Subtotal: PKR {subtotal}")

    print(f"Discount: {discount_percentage}%")

    print(f"Discount Amount: PKR {discount_amount:.2f}")

    print("------------------------")

    print(f"FINAL PAYABLE: PKR {final_amount:.2f}")

    print("======================")
    print("       Thank you for your order!")
    print("======================")


# Function to confirm order and update inventory
def confirm_order():

    if not order:
        print("\nYour order is empty. Add items first.")
        return

    # Final stock validation
    for item, quantity in order.items():

        if quantity > menu[item]["stock"]:

            print("Order cannot be confirmed due to insufficient stock.")
            return

    print("\nYour final order:")

    display_order()

    choice = input("\nConfirm order? (yes/no): ").strip().lower()

    if choice == "yes":

        # Reduce inventory only after confirmation
        for item, quantity in order.items():

            menu[item]["stock"] -= quantity

        generate_receipt()

        order.clear()

        print("\nOrder confirmed successfully!")

    elif choice == "no":

        print("\nOrder confirmation cancelled.")

    else:

        print("\nInvalid choice! Please enter yes or no.")




def main():

    while True:

        print("\n========== RESTAURANT ORDERING SYSTEM ==========")

        print("1. Display Restaurant Menu")
        print("2. Add Item to Order")
        print("3. Remove Item from Order")
        print("4. View Current Order")
        print("5. Confirm Order and Generate Receipt")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":

            display_menu()

        elif choice == "2":

            add_item()

        elif choice == "3":

            remove_item()

        elif choice == "4":

            display_order()

        elif choice == "5":

            confirm_order()

        elif choice == "6":

            print("\nThank you for visiting our restaurant!")
            break

        else:

            print("\nInvalid selection! Please choose between 1 and 6.")


# Start the program
main()
