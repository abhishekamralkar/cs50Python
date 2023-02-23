#!/usr/bin/env python
# Ask use for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()

# title user's name
name = name.title()

# Say hello to user
print(f"Hello, {name}")
