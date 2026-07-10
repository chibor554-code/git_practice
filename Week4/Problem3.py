# problem3.py — Chidi's Electricity Bill Estimator

def power_summary(**daily_hours):
    """
    Print a table of power vs outage hours for each day.
    Returns a dict like:
    {'Monday': {'power': 6, 'outage': 18}, ...}
    """
    summary = {}

    print(f"\n{'Day':<14}| Power (hrs) | Outage (hrs)")
    print("-" * 42)

    for day, hours in daily_hours.items():
        try:
            hours = float(hours)
        except (TypeError, ValueError):
            print(f"Warning: {hours!r} is not a valid number for {day}. Skipping.")
            continue

        if not (0 <= hours <= 24):
            raise ValueError(f"{day} has {hours} hours — must be between 0 and 24.")

        outage = 24 - hours
        summary[day] = {"power": hours, "outage": outage}
        print(f"{day:<14}|     {hours:<7}|    {outage}")

    return summary


def fuel_cost(hours_without_power, litres_per_hour=0.8, price_per_litre=1200):
    """Calculate total generator fuel cost."""
    if litres_per_hour <= 0:
        raise ValueError("Litres per hour must be greater than zero.")
    if price_per_litre <= 0:
        raise ValueError("Price per litre must be greater than zero.")

    total_hours = sum(hours_without_power)
    return round(total_hours * litres_per_hour * price_per_litre, 2)


# ==========================
# MAIN PROGRAM
# ==========================
if __name__ == "__main__":

    print("====== CHIDI'S ELECTRICITY BILL ESTIMATOR ======\n")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    daily_power = {}

    # Get power hours from the user
    for day in days:
        while True:
            try:
                hours = float(input(f"Enter power hours for {day} (0-24): "))

                if 0 <= hours <= 24:
                    daily_power[day] = hours
                    break
                else:
                    print("Hours must be between 0 and 24.")

            except ValueError:
                print("Please enter a valid number.")

    # Display summary
    summary = power_summary(**daily_power)

    # Get outage hours
    outage_hours = [summary[day]["outage"] for day in summary]

    # Optional: Let user change fuel settings
    print("\nFuel Cost Settings")

    litres = float(input("Enter litres used per hour (default 0.8): ") or 0.8)
    price = float(input("Enter fuel price per litre (default ₦1200): ") or 1200)

    # Calculate cost
    cost = fuel_cost(
        outage_hours,
        litres_per_hour=litres,
        price_per_litre=price
    )

    print(f"\nEstimated Generator Fuel Cost: ₦{cost:,.2f}")