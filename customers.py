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