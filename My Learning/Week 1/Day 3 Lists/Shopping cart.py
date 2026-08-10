# Shopping cart

print()

cart = []
prices = []

print("=== SHOPPING CART ===")
print("Type 'done' when finished adding items")

while True:
    item = input("Enter item name: ")
    if item.lower() == "done":
        break
    price = float(input(f"Enter price of {item}: Rs."))
    cart.append(item)
    prices.append(price)

print("\n=== YOUR CART ===")
for i in range(len(cart)):
    print(f"{cart[i]} : Rs.{prices[i]}")

print(f"\nTotal items: {len(cart)}")
print(f"Total cost: Rs.{sum(prices):.2f}")

print()