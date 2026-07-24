#=========================================================
# comprehensions_demo.py
# Concept: comprehensions — Python's one-line transformation syntax
# ============================================================
celsius_temps = [20, 25, 30, 35, 40]
# --- The traditional way ---
fahrenheit_traditional = []
for c in celsius_temps:
    fahrenheit_traditional.append((c * 9/5) + 32)
# --- The Pythonic way: a list comprehension ---
# Read it as: "for each c in celsius_temps, compute (c * 9/5) + 32"
fahrenheit_comprehension = [(c * 9/5) + 32 for c in celsius_temps]
print(f"Traditional:   {fahrenheit_traditional}")
print(f"Comprehension: {fahrenheit_comprehension}")
# --- A comprehension WITH a filter condition ---
students = [
    {"name": "Ananya", "marks": 88},
    {"name": "Vikram", "marks": 45},
    {"name": "Zara", "marks": 76},
]
# Read it as: "the name, for each student, but ONLY IF marks > 60"
passed_names = [s["name"] for s in students if s["marks"] > 60]
print(f"Students above 60: {passed_names}")
# --- A dict comprehension: building a lookup table in one line ---
products = ["Notebook", "Pen", "Backpack"]
prices = [40, 10, 650]
# zip() pairs up the two lists element-by-element
price_lookup = {product: price for product, price in zip(products, prices)}
print(f"Price lookup: {price_lookup}")