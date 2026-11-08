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