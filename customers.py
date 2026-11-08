# ISM2411 Lab 11 — Customer Dictionary & Lookup
# Name: Ahraya Dalaq
#
# REFLECTION
# 1. (answer goes here)
# 2. (answer goes here)


# ---------------------------------------------------------------
# Exercise 1 — One customer
# ---------------------------------------------------------------
print("=== Exercise 1: One customer ===")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# ---------------------------------------------------------------
# Exercise 2 — Update and add
# ---------------------------------------------------------------
print("\n=== Exercise 2: Update and add ===")
customer["phone"] = "813-555-0142"     # add a new field
print(customer)

customer["tier"] = "platinum"          # update an existing field
print(customer)

del customer["email"]                  # delete a field
print(customer)



# ---------------------------------------------------------------
# Exercise 3 — Safe lookup
# ---------------------------------------------------------------
print("\n=== Exercise 3: Safe lookup ===")
email = customer.get("email", "no email on file")
print("Using .get():", email)

try:
    print(customer["email"])
except KeyError as error:
    print("Using brackets: KeyError for", error)


# ---------------------------------------------------------------
# Exercise 4 — Iterate
# ---------------------------------------------------------------
print("\n=== Exercise 4: Iterate ===")
for key, value in customer.items():
    print(f"{key}: {value}")

print("--- without .items() ---")
for key in customer:
    print(key)
# Looping over a dict directly only gives you the KEYS.
# .items() gives you (key, value) pairs, so you can unpack both at once.
# Without .items() you'd have to write customer[key] to get each value.




# ---------------------------------------------------------------
# Exercise 5 — Lookup table
# ---------------------------------------------------------------
print("\n=== Exercise 5: Lookup table ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate:.0%}")
print(f"Final price on ${purchase}: ${final_price:.2f}")


# ---------------------------------------------------------------
# Exercise 6 — List of dicts
# ---------------------------------------------------------------
print("\n=== Exercise 6: List of dicts ===")
customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 1250.00},
    {"name": "Marcus", "tier": "silver", "ytd_spend": 430.50},
    {"name": "Priya", "tier": "bronze", "ytd_spend": 85.00},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount = purchase * rate
    print(f"{c['name']:<8} | {c['tier']:<9} | discount on ${purchase}: ${discount:.2f}")


    

# ---------------------------------------------------------------
# Exercise 7 — Nested catalog
# ---------------------------------------------------------------
print("\n=== Exercise 7: Nested catalog ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} — only {info['stock']} left")


# ---------------------------------------------------------------
# Exercise 8 — Sales by region
# ---------------------------------------------------------------
print("\n=== Exercise 8: Sales by region ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for t in transactions:
    region = t["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + t["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")