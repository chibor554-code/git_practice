# problem1.py — Mama Ngozi's Market Price Calculator


def calculate_total(*prices):
    """Add up all item prices. Skips any non-number values."""
    total = 0
    for price in prices:
        try:
            total += price  # will raise TypeError if price is not a number
        except TypeError:
            print(f"Skipping invalid price: {price!r}")
    return total


def apply_discount(total, discount_percent=0):
    """Return the price after removing the given discount percentage."""
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100%.")
    return total * (1 - discount_percent / 100)


def add_vat(price, vat_rate=7.5):
    """Return the final price with VAT added, rounded to 2 decimal places."""
    if vat_rate < 0:
        raise ValueError("VAT rate cannot be negative.")
    return round(price * (1 + vat_rate / 100), 2)


if __name__ == "__main__":
    prices = (1500, 2000, 3500, 800)

    total   = calculate_total(*prices)       # 7800
    after_d = apply_discount(total, 10)      # 7020.0
    final   = add_vat(after_d)              # 7546.5
    print(f"Total: ₦{final}")               # Total: ₦7546.5

    # Error cases
    print("\n--- Error cases ---")

    try:
        apply_discount(5000, 110)
    except ValueError as e:
        print(f"ValueError: {e}")           # Discount must be between 0 and 100%.

    result = calculate_total(200, "abc", 300)
    print(f"Total (skipping 'abc'): {result}")  # 500
