class Item:
    def __init__(self, item_id, item_name, category, unit_price, stock_quantity, min_stock_threshold):
        self.item_id = item_id
        self.item_name = item_name
        self.category = category
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity
        self.min_stock_threshold = min_stock_threshold

    def display(self):
        print("Item ID:", self.item_id)
        print("Item Name:", self.item_name)
        print("Category:", self.category)
        print("Unit Price (INR):", self.unit_price)
        print("Current Stock Quantity:", self.stock_quantity)
        print("Minimum Stock Threshold:", self.min_stock_threshold)
# Create an empty list to store inventory data
inventory = []

# Function to add items to the inventory
def add_item():
    item_name = input("Item Name: ")
    category = input("Category (e.g., grains, spices, dairy, etc.): ")

    # Use a loop to ensure valid input for unit price
    while True:
        try:
            unit_price = float(input("Unit Price (in INR): "))
            if unit_price < 0:
                raise ValueError("Unit price cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Use a loop to ensure valid input for current stock quantity
    while True:
        try:
            stock_quantity = int(input("Current Stock Quantity: "))
            if stock_quantity < 0:
                raise ValueError("Stock quantity cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Use a loop to ensure valid input for minimum stock threshold
    while True:
        try:
            min_stock_threshold = int(input("Minimum Stock Threshold: "))
            if min_stock_threshold < 0:
                raise ValueError("Minimum stock threshold cannot be negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Generate a unique Item ID (assuming it starts from 1 and increments)
    if len(inventory) == 0:
        item_id = 1
    else:
        item_id = inventory[-1].item_id + 1

    # Create an instance of the Item class and add it to the inventory list
    new_item = Item(item_id, item_name, category, unit_price, stock_quantity, min_stock_threshold)
    inventory.append(new_item)
    print("Item added to inventory successfully!")

def display_inventory():
    print("\nInventory List:")
    for item in inventory:
        item.display()
        print("-" * 40)


def search_item():
    search_term = input("Enter the item name or category to search for: ")
    found_items = []

    for item in inventory:
        if search_term.lower() in item.item_name.lower() or search_term.lower() in item.category.lower():
            found_items.append(item)

    if found_items:
        print("\nSearch Results:")
        for found_item in found_items:
            found_item.display()
            print("-" * 40)
    else:
        print("No matching items found.")


def update_stock_quantity():
    item_id = int(input("Enter the Item ID of the item you want to update: "))

    for item in inventory:
        if item.item_id == item_id:
            new_quantity = int(input(f"Enter the new stock quantity for '{item.item_name}': "))
            item.stock_quantity = new_quantity
            print("Stock quantity updated successfully.")
            return

    print("Item not found with the specified Item ID.")

def generate_low_stock_list():
    low_stock_items = [item for item in inventory if item.stock_quantity < item.min_stock_threshold]

    if low_stock_items:
        print("\nLow Stock Items:")
        for item in low_stock_items:
            item.display()
            print("-" * 40)
    else:
        print("No low stock items found.")

# Main program loop (unchanged)
while True:
    print("\nMain Menu:")
    print("1. Add Item to Inventory")
    print("2. Display Inventory List")
    print("3. Search for Item")
    print("4. Update Stock Quantity")
    print("5. Generate List of Low Stock Items")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        display_inventory()
    elif choice == "3":
        search_item()
    elif choice == "4":
        update_stock_quantity()
    elif choice == "5":
        generate_low_stock_list()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")