# Python password generator

import random

# All possible inputs for the password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}<>.,/!£$%^&*#"

# Input the password will have
upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols


# Length of passwords
length = 24

# Number of passwords generated
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)