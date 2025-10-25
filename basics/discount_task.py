"""
Discount Calculator Tool
------------------------
A small CLI tool that calculates the final price after discount.

Showcases:
✔ Functions and modular design
✔ Type hints and doc_strings
✔ Input validation with exception handling
✔ Reusable calculation logic
✔ Clean formatted UI output
✔ Logging for debugging (common interview bonus)
"""

from typing import Optional
import logging

# Configure Logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_discount(price: float, discount: float) -> float:
    """
    Calculate the final price after applying a discount.

    Parameters
    ----------
    price : float
        Original product price (must be > 0)
    discount : float
        Discount percentage (0–100)

    Returns
    -------
    float
        Final price after applying discount

    Raises
    ------
    ValueError
        If invalid values are provided
    """
    
    if price <= 0:
        raise ValueError("Price must be greater than 0.")
    
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100.")
    
    discount_amount = (discount / 100) * price
    final_price = price - discount_amount

    logging.info(
        f"Calculation successful: Price={price}, Discount={discount}%, Final={final_price}"
    )
    
    return round(final_price, 2)


def get_float_input(message: str) -> float:
    """Safely get a float input from the user with validation."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def main() -> None:
    """Main function for CLI workflow."""
    print("\n🧮 Welcome to the Discount Calculator 🧮")
    print("-------------------------------------")

    price = get_float_input("Enter the original price: ")
    discount = get_float_input("Enter discount percentage (0-100): ")

    try:
        final_price = calculate_discount(price, discount)
        print(f"\n✅ Final Price after discount: KES {final_price:.2f}\n")
    except ValueError as e:
        logging.error(e)
        print(f"⚠ Error: {e}")


if __name__ == "__main__":
    # Program entry point
    main()