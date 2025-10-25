"""
Invoice System — Intermediate Python Practice
Author: Moses Matola

This script:
✅ Accepts multiple product entries (price + quantity)
✅ Applies tiered discount based on subtotal
✅ Calculates VAT (16%)
✅ Handles invalid inputs safely
✅ Prints a clean professional invoice
"""

VAT_RATE = 0.16

def get_numeric_input(prompt: str) -> float:
    """Safely request a positive numeric value from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError:
            print("❌ Invalid input — enter a positive numeric value.\n")


def calculate_discount(subtotal: float) -> float:
    """Return the discount rate based on the subtotal tier."""
    if subtotal > 20_000:
        return 0.10
    elif subtotal >= 5_000:
        return 0.05
    return 0.00


def format_currency(amount: float) -> str:
    """Format numbers as KES currency."""
    return f"KES {amount:,.2f}"


def main() -> None:
    print("\n🧾 CUSTOMER INVOICE SYSTEM")
    print("-" * 35)

    num_items = int(get_numeric_input("How many different products? "))

    subtotal = 0.0

    for i in range(1, num_items + 1):
        print(f"\nProduct {i}:")
        price = get_numeric_input("  Enter price (KES): ")
        qty = get_numeric_input("  Enter quantity: ")
        subtotal += price * qty

    discount_rate = calculate_discount(subtotal)
    discount_amount = subtotal * discount_rate
    taxable_amount = subtotal - discount_amount
    tax = taxable_amount * VAT_RATE
    final_total = taxable_amount + tax

    print("\n" + "=" * 35)
    print("✅ INVOICE SUMMARY".center(35))
    print("=" * 35)
    print(f"Subtotal:        {format_currency(subtotal)}")
    print(f"Discount ({discount_rate*100:.0f}%): -{format_currency(discount_amount)}")
    print(f"Taxable Amount:  {format_currency(taxable_amount)}")
    print(f"VAT (16%):       {format_currency(tax)}")
    print("-" * 35)
    print(f"TOTAL DUE:       {format_currency(final_total)}")
    print("=" * 35)
    print("✅ Thank you for shopping with us!\n")


if __name__ == "__main__":
    main()
