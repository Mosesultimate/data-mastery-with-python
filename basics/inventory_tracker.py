# Product Inventory Tracker v1

products = [
    {"id": 1, "name": "Laptop", "price": 85000, "quantity": 10},
    {"id": 2, "name": "Phone", "price": 42000, "quantity": 15},
]

# Log of all update operations as tuples
update_log = []


def display_menu():
    print("\n=== PRODUCT INVENTORY TRACKER ===")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Products")
    print("4. Update Product Quantity")
    print("5. Search Product")
    print("6. View Inventory Summary")
    print("7. Exit")


def add_product():
    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("❌ Invalid ID. Must be a number.")
        return

    # Check duplicate ID
    for product in products:
        if product["id"] == product_id:
            print("❌ Product with this ID already exists!")
            return

    name = input("Enter product name: ")

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
    except ValueError:
        print("❌ Invalid data format!")
        return

    if price < 0 or quantity < 0:
        print("❌ Price and quantity must be non-negative.")
        return

    products.append({
        "id": product_id,
        "name": name.title(),
        "price": price,
        "quantity": quantity
    })

    print(f"✅ Product '{name}' added successfully!")


def remove_product():
    try:
        product_id = int(input("Enter product ID to remove: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print(f"✅ Product ID {product_id} removed successfully!")
            return

    print("❌ Product not found.")


def view_products():
    if not products:
        print("📭 No products available.")
        return

    print("\n--- PRODUCT LIST ---")
    for product in products:
        print(f"ID: {product['id']} | {product['name']} | Price: {product['price']} | Stock: {product['quantity']}")


def update_product_quantity():
    try:
        product_id = int(input("Enter product ID to update: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for product in products:
        if product["id"] == product_id:
            try:
                new_quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("❌ Enter a valid number.")
                return

            if new_quantity < 0:
                print("❌ Quantity cannot be negative!")
                return

            old_quantity = product["quantity"]
            product["quantity"] = new_quantity

            update_log.append(("Updated", product_id, old_quantity, new_quantity))
            print(f"✅ Quantity updated: {old_quantity} → {new_quantity}")
            return

    print("❌ Product not found.")


def search_product():
    search_term = input("Search by Product ID or Name: ").lower()

    print("\n--- SEARCH RESULTS ---")
    found = False

    for product in products:
        if str(product["id"]) == search_term or product["name"].lower() == search_term:
            print(f"ID: {product['id']} | {product['name']} | KES {product['price']} | Qty: {product['quantity']}")
            found = True

    if not found:
        print("❌ No matching product found.")


def view_inventory_summary():
    total_items = len(products)
    total_value = sum(p["price"] * p["quantity"] for p in products)

    print("\n=== INVENTORY SUMMARY ===")
    print(f"Total Unique Products: {total_items}")
    print(f"Total Inventory Value: KES {total_value:,.2f}")

    if update_log:
        print("\nRecent Updates:")
        for log in update_log[-5:]:
            print(log)


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-7): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            view_products()
        elif choice == "4":
            update_product_quantity()
        elif choice == "5":
            search_product()
        elif choice == "6":
            view_inventory_summary()
        elif choice == "7":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select 1-7.")


if __name__ == "__main__":
    main()
