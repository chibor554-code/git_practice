# # ────────────────────────────────────────
# # CLASS 1: MenuItem
# # ────────────────────────────────────────

# class MenuItem:
#     def __init__(self, name, price, available=True, is_drink=False):
#         # --- Guard: stop bad data before it enters ---
#         if price < 0:
#             raise ValueError(f"Price cannot be negative. You gave: {price}")
 
#         self.name      = name
#         self.price     = price
#         self.available = available   # True = can order it, False = sold out
#         self.is_drink  = is_drink    # True = qualifies for Buy-2-Get-1 promo
 

#     def __str__(self):
#         status = "✅" if self.available else "❌ (unavailable)"
#         return f"{self.name} — ₦{self.price}  {status}"
 

#     def __repr__(self):
#         return f"MenuItem('{self.name}', ₦{self.price}, available={self.available})"
 
 
# # ────────────────────────────────────────
# # CLASS 2: Restaurant
# # ────────────────────────────────────────
 
# class Restaurant:
#     def __init__(self, name, location):
#         self.name     = name
#         self.location = location
#         self.menu     = []   # a plain list — starts empty
 
#     def add_item(self, item):
#         self.menu.append(item)
 
#     def show_menu(self):
#         print(f"\n=== {self.name} Menu ({self.location}) ===")
#         for item in self.menu:
#             print(" ", item)   # calls MenuItem.__str__ automatically
#         print("=" * 38)
 
 
# # ────────────────────────────────────────
# # CLASS 3: Order
# # ────────────────────────────────────────
 
# class Order:
#     def __init__(self, customer_name, restaurant):
#         self.customer_name = customer_name
#         self.restaurant    = restaurant
#         self.items         = []   # cart starts empty
 
#     # Add an item — but reject unavailable ones (Task 4)
#     def add_item(self, item):
#         if not item.available:
#             raise ValueError(f"Sorry! '{item.name}' is not available right now.")
#         self.items.append(item)
 
 
#     @property
#     def total(self):
#         food_total  = 0
#         drink_total = 0
#         drink_count = 0
 
#         for item in self.items:
#             if item.is_drink:
#                 drink_count += 1
#                 drink_total += item.price
#             else:
#                 food_total += item.price
 
 
#         drinks_only = [i for i in self.items if i.is_drink]
#         drinks_only.sort(key=lambda i: i.price)  # cheapest first
 
#         free_count  = drink_count // 3   # e.g. 3 drinks → 1 free, 6 drinks → 2 free
#         discount    = sum(i.price for i in drinks_only[:free_count])
 
#         return food_total + drink_total - discount
 
#     # ── __len__: len(order) = number of items in cart (Task 2) ──
#     def __len__(self):
#         return len(self.items)
 
#     # ── __add__: order1 + order2 = group order (Task 2) ─────────
#     def __add__(self, other_order):
#         # Create a new merged order
#         merged_name = self.customer_name + " & " + other_order.customer_name
#         merged      = Order(merged_name, self.restaurant)
#         merged.items = self.items + other_order.items   # combine both carts
#         return merged
 
#     # ── __str__: print(order) shows a receipt (Task 2) ──────────

#     def __str__(self):
#         lines = []
#         lines.append("================================")
#         lines.append("       AbaBite Receipt 🧾")
#         lines.append(f"  Customer : {self.customer_name}")
#         lines.append(f"  From     : {self.restaurant.name}")
#         lines.append("--------------------------------")
#         for item in self.items:
#             lines.append(f"  {item.name:<20} ₦{item.price}")
#         lines.append("--------------------------------")
#         lines.append(f"  TOTAL    ({len(self)} items)   ₦{self.total}")
#         lines.append("================================")
#         return "\n".join(lines)
 
#     # ── __repr__: for devs debugging in console (Task 2) ────────
#     def __repr__(self):
#         names = [i.name for i in self.items]
#         return f"Order(customer='{self.customer_name}', items={names}, total=₦{self.total})"
 
 
 
# print("\n========== AbaBite Demo ==========\n")
 
# # Step 1: Create a restaurant
# Ikenna_Restaurants = Restaurant("Ikenna_Restaurants & Kitchen", "Aba")
 
# # Step 2: Add items to the menu
# Ikenna_Restaurants.add_item(MenuItem("Jollof Rice",    1500))
# Ikenna_Restaurants.add_item(MenuItem("Egusi + Eba",    1800))
# Ikenna_Restaurants.add_item(MenuItem("Fried Chicken",  2200))
# Ikenna_Restaurants.add_item(MenuItem("Peppered Gizzard", 1200, available=False))  # sold out!
# Ikenna_Restaurants.add_item(MenuItem("Coca-Cola",       300, is_drink=True))
# Ikenna_Restaurants.add_item(MenuItem("Fanta",           300, is_drink=True))
# Ikenna_Restaurants.add_item(MenuItem("Sprite",          300, is_drink=True))      # 3rd drink → FREE
 
# Ikenna_Restaurants.show_menu()
 
# # Step 3: Customer 1 places an order
# print("\n--- Chidi's Order ---")
# order1 = Order("Chidi", Ikenna_Restaurants)
# order1.add_item(Ikenna_Restaurants.menu[0])   # Jollof Rice
# order1.add_item(Ikenna_Restaurants.menu[2])   # Fried Chicken
# order1.add_item(Ikenna_Restaurants.menu[4])   # Coca-Cola
# order1.add_item(Ikenna_Restaurants.menu[5])   # Fanta
# order1.add_item(Ikenna_Restaurants.menu[6])   # Sprite ← this one is FREE (buy 2 get 1)
 
# print(order1)                         # calls __str__ → receipt
# print(f"\nlen(order1) = {len(order1)} items")   # calls __len__
 
# # Step 4: Customer 2 places an order
# print("\n--- Ngozi's Order ---")
# order2 = Order("Ngozi", Ikenna_Restaurants)
# order2.add_item(Ikenna_Restaurants.menu[1])   # Egusi + Eba
# print(order2)
 
# # Step 5: Merge into one group order
# print("\n--- Group Order (order1 + order2) ---")
# group = order1 + order2             # calls __add__
# print(group)
 
# # Step 6: Dev debugging — repr
# print("\n--- repr() for devs ---")
# print(repr(order1))
 
# # ── Error Handling ───────────────────────────────
# print("\n--- Error Handling ---")
 
# # Try to order a sold-out item
# try:
#     order1.add_item(Ikenna_Restaurants.menu[3])   # Peppered Gizzard — unavailable
# except ValueError as e:
#     print(f"Caught: {e}")
 
# # Try to create an item with a negative price
# try:
#     bad = MenuItem("Fake Food", -200)
# except ValueError as e:
#     print(f"Caught: {e}")
 
# print("\n✅ Done! Ready for Flask/FastAPI.\n")










class MenuItem:
    def __init__(self, name, price, available=True, is_drink=False):
        # --- Guard: stop bad data before it enters ---
        if price < 0:
            raise ValueError(f"Price cannot be negative. You gave: {price}")
 
        self.name      = name
        self.price     = price
        self.available = available   # True = can order it, False = sold out
        self.is_drink  = is_drink    # True = qualifies for Buy-2-Get-1 promo
 
    # __str__ → what you see when you print(item)
    # Task 2 wants:  "Jollof Rice — ₦1500"
    def __str__(self):
        status = "✅" if self.available else "❌ (unavailable)"
        return f"{self.name} — ₦{self.price}  {status}"
 
    # __repr__ → what devs see in the console / debugger
    def __repr__(self):
        return f"MenuItem('{self.name}', ₦{self.price}, available={self.available})"
 
 
# ────────────────────────────────────────
# CLASS 2: Restaurant
# ────────────────────────────────────────
 
class Restaurant:
    def __init__(self, name, location):
        self.name     = name
        self.location = location
        self.menu     = []   # a plain list — starts empty
 
    def add_item(self, item):
        self.menu.append(item)
 
    def show_menu(self):
        print(f"\n=== {self.name} Menu ({self.location}) ===")
        for item in self.menu:
            print(" ", item)   # calls MenuItem.__str__ automatically
        print("=" * 38)
 
 
# ────────────────────────────────────────
# CLASS 3: Order
# ────────────────────────────────────────
 
class Order:
    def __init__(self, customer_name, restaurant):
        self.customer_name = customer_name
        self.restaurant    = restaurant
        self.items         = []   # cart starts empty
 
    # Add an item — but reject unavailable ones (Task 4)
    def add_item(self, item):
        if not item.available:
            raise ValueError(f"Sorry! '{item.name}' is not available right now.")
        self.items.append(item)
 
    @property
    def total(self):
        food_total  = 0
        drink_total = 0
        drink_count = 0
 
        for item in self.items:
            if item.is_drink:
                drink_count += 1
                drink_total += item.price
            else:
                food_total += item.price
 
        drinks_only = [i for i in self.items if i.is_drink]
        drinks_only.sort(key=lambda i: i.price)  # cheapest first
 
        free_count  = drink_count // 3   # e.g. 3 drinks → 1 free, 6 drinks → 2 free
        discount    = sum(i.price for i in drinks_only[:free_count])
 
        return food_total + drink_total - discount
 
    # ── __len__: len(order) = number of items in cart (Task 2) ──
    def __len__(self):
        return len(self.items)
 
    # ── __add__: order1 + order2 = group order (Task 2) ─────────
    def __add__(self, other_order):
        # Create a new merged order
        merged_name = self.customer_name + " & " + other_order.customer_name
        merged      = Order(merged_name, self.restaurant)
        merged.items = self.items + other_order.items   # combine both carts
        return merged
 
    # ── __str__: print(order) shows a receipt (Task 2) ──────────
    def __str__(self):
        lines = []
        lines.append("================================")
        lines.append("       AbaBite Receipt 🧾")
        lines.append(f"  Customer : {self.customer_name}")
        lines.append(f"  From     : {self.restaurant.name}")
        lines.append("--------------------------------")
        for item in self.items:
            lines.append(f"  {item.name:<20} ₦{item.price}")
        lines.append("--------------------------------")
        lines.append(f"  TOTAL    ({len(self)} items)   ₦{self.total}")
        lines.append("================================")
        return "\n".join(lines)
 
    # ── __repr__: for devs debugging in console (Task 2) ────────
    def __repr__(self):
        names = [i.name for i in self.items]
        return f"Order(customer='{self.customer_name}', items={names}, total=₦{self.total})"
 
 
# ════════════════════════════════════════
#  SETUP — Ikenna's Restaurant + Menu
# ════════════════════════════════════════
 
Ikenna_Restaurants = Restaurant("Ikenna's Kitchen", "Aba")
 
Ikenna_Restaurants.add_item(MenuItem("Jollof Rice",       1500))
Ikenna_Restaurants.add_item(MenuItem("Egusi + Eba",       1800))
Ikenna_Restaurants.add_item(MenuItem("Fried Chicken",     2200))
Ikenna_Restaurants.add_item(MenuItem("Peppered Gizzard",  1200, available=False))  # sold out!
Ikenna_Restaurants.add_item(MenuItem("Coca-Cola",          300, is_drink=True))
Ikenna_Restaurants.add_item(MenuItem("Fanta",              300, is_drink=True))
Ikenna_Restaurants.add_item(MenuItem("Sprite",             300, is_drink=True))    # 3rd drink → FREE
 
Ikenna_Restaurants.show_menu()
 
# ════════════════════════════════════════
#  INTERACTIVE CART — Customer adds items
# ════════════════════════════════════════
 
# Ask for the customer's name first
customer_name = input("\nEnter your name to start your order: ").strip()
if not customer_name:
    customer_name = "Customer"
 
order1 = Order(customer_name, Ikenna_Restaurants)
 
print(f"\nHi {customer_name}! Type the NUMBER of the item to add it to your cart.")
print("Type 'done' when you are finished.\n")
 
# Keep looping until the customer types "done"
while True:
    # Show the menu with numbers so the customer can pick
    print("─── Menu ───────────────────────────")
    for index, item in enumerate(Ikenna_Restaurants.menu):
        print(f"  {index + 1}. {item}")   # e.g.  1. Jollof Rice — ₦1500 ✅
    print("────────────────────────────────────")
    print(f"  Items in cart so far: {len(order1)}")
    print("────────────────────────────────────")
 
    choice = input("Pick a number (or type 'done'): ").strip()
 
    # Customer is finished
    if choice.lower() == "done":
        break
 
    # Make sure they typed a number, not letters
    if not choice.isdigit():
        print("⚠️  Please type a number from the menu, or 'done' to finish.\n")
        continue
 
    # Convert to a list index (they type 1, we need index 0)
    index = int(choice) - 1
 
    # Make sure the number is within range
    if index < 0 or index >= len(Ikenna_Restaurants.menu):
        print(f"⚠️  Please pick a number between 1 and {len(Ikenna_Restaurants.menu)}.\n")
        continue
 
    # Try to add the item — will fail if it's unavailable
    selected_item = Ikenna_Restaurants.menu[index]
    try:
        order1.add_item(selected_item)
        print(f"✅ '{selected_item.name}' added to your cart!\n")
    except ValueError as e:
        print(f"❌ {e}\n")
 
# ── Show the final receipt ───────────────
print("\n" + "=" * 40)
print("        YOUR FINAL ORDER")
print("=" * 40)
 
if len(order1) == 0:
    print("  Your cart is empty. Nothing to order!")
else:
    print(order1)   # calls __str__ → prints receipt


