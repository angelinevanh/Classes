"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: dictionary about green bond with 6 fields
# 2. Process: reading, updating, deleting and displaying final value
# 3. Out:original and modified values
# 4. My object, my five fields, and why those: Object is green bond.
#       Five fields are name, issuer, coupon, maturity and currency.


# Your code below
bond = {
    "name": "Green Climate Bond",
    "issuer": "EIB",
    "coupon": 3.5,
    "maturity": "2030",
    "currency": "EUR",
    "rating": "AAA"
    }
print("Issuer:", bond["issuer"])
bond["coupon"] = 3.75
del bond["rating"]
print("Updated Bond Dictionary:", bond)