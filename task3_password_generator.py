# task3_password_generator.py

import random
import string

print("Password Generator")

# Step 1: Ask user for desired password length
length = int(input("Enter desired password length: "))

# Step 2: Define characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

# Step 4: Display the password
print(f"Generated Password: {password}")
