# CS1350 Homework 2
# Name: Ron Palermo
# Course: CS1350 Computer Science II

# ============================================================
# UNIT 1.1 - WHAT ARE DICTIONARIES?
# ============================================================

print("\n===== UNIT 1.1 =====")

# Beginner
my_info = {
    "name": "YourFirstName",
    "age": 19,
    "major": "Cyber Security"
}

print("My information:", my_info)


# Intermediate

# 1. Menu with at least 4 food items and prices
menu = {
    "Burger": 8.99,
    "Fries": 3.49,
    "Pizza": 12.99,
    "Chicken Sandwich": 9.99
}

print("Menu:", menu)

# 2. Course names mapped to credit hours
course_credits = {
    "CS1350": 3,
    "CS1330": 3,
    "CYS1100": 3,
    "MATH201": 3
}

print("Course credits:", course_credits)


# Advanced
weekly_temps = dict(
    Monday=72,
    Tuesday=75,
    Wednesday=68,
    Thursday=70,
    Friday=74,
    Saturday=77,
    Sunday=73
)

print("Weekly temperatures:", weekly_temps)


# ============================================================
# UNIT 1.2 - ACCESSING DICTIONARY ELEMENTS
# ============================================================

print("\n===== UNIT 1.2 =====")

pet = {
    "name": "Buddy",
    "type": "dog",
    "age": 3
}

# Beginner
print("Pet name:", pet["name"])
print("Pet age:", pet["age"])


# Intermediate

# 1. Safely access color
print("Pet color:", pet.get("color", "unknown"))

# 2. Check if a student passed a course
grades = {
    "CS1350": 85,
    "MATH201": 62
}

course = "CS1350"
grade = grades.get(course)

if grade is not None:
    if grade >= 70:
        print(course, "passed with a grade of", grade)
    else:
        print(course, "was not passed with a grade of", grade)
else:
    print(course, "not found")


# Advanced
products = {
    "laptop": 999.99,
    "mouse": 29.99,
    "keyboard": 79.99
}

product_name = "mouse"
price = products.get(product_name)

if price is not None:
    print(product_name, "costs $", price)
else:
    print("Product not available")

product_name = "monitor"
price = products.get(product_name)

if price is not None:
    print(product_name, "costs $", price)
else:
    print("Product not available")


# ============================================================
# UNIT 1.3 - MODIFYING DICTIONARIES
# ============================================================

print("\n===== UNIT 1.3 =====")

# Beginner
inventory = {}

inventory["apples"] = 10
inventory["bananas"] = 15
inventory["oranges"] = 8

print("Inventory:", inventory)


# Intermediate
scores = {
    "Team A": 45,
    "Team B": 38
}

scores["Team B"] = 52
scores["Team C"] = 41

removed_score = scores.pop("Team A")

print("Removed Team A score:", removed_score)
print("Updated scores:", scores)


# Advanced
cart = {}

cart["Laptop"] = 999.99
cart["Mouse"] = 29.99
cart["Keyboard"] = 79.99

# Update one price
cart["Mouse"] = 24.99

# Remove an item
removed_item = cart.pop("Keyboard")

print("Removed item price:", removed_item)
print("Final cart:", cart)

# Bonus
total_price = sum(cart.values())

print("Total price: $", total_price)


# ============================================================
# UNIT 2.1 - HOW DICTIONARIES WORK
# ============================================================

print("\n===== UNIT 2.1 =====")

# Beginner
print("\nDictionary key validity:")

print('"student_name" - valid: strings are immutable and hashable')
print('[1, 2, 3] - invalid: lists are mutable')
print('100 - valid: integers are immutable and hashable')
print('("x", "y") - valid: tuples are immutable')
print('{"a": 1} - invalid: dictionaries are mutable')
print('frozenset({1, 2}) - valid: frozensets are immutable')


# Intermediate

# 1. Fix the locations dictionary by using tuples
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}

print("Locations:", locations)

# 2. Predict and verify duplicate keys
data = {
    "a": 1,
    "b": 2,
    "a": 3,
    "b": 4
}

print("Data:", data)
print("Length:", len(data))

# 3. Hash values
print("Hash value of my name:", hash("YourFirstName"))
print("Hash value of 100:", hash(100))


# Advanced

# 1. Game high scores using tuples as keys
high_scores = {
    ("Alex", "Minecraft"): 5000,
    ("Jordan", "Fortnite"): 8200,
    ("Taylor", "Mario Kart"): 4500
}

print("Alex's Minecraft score:",
      high_scores[("Alex", "Minecraft")])


# 2. Compare list vs dictionary lookup times
import time

big_list = list(range(100000))
big_dict = {i: i for i in range(100000)}

start = time.time()
result = 99999 in big_list
list_time = time.time() - start

start = time.time()
result = 99999 in big_dict
dict_time = time.time() - start

print("List lookup time:", list_time)
print("Dictionary lookup time:", dict_time)

if dict_time < list_time:
    print("Dictionary lookup was faster.")
else:
    print("List lookup was faster.")


# ============================================================
# UNIT 2.2 - KEYS() AND VALUES()
# ============================================================

print("\n===== UNIT 2.2 =====")

temps = {
    "Monday": 72,
    "Tuesday": 75,
    "Wednesday": 68
}

# Beginner
print("Days:", temps.keys())
print("Temperatures:", temps.values())
print("Number of days:", len(temps))


# Intermediate

# 1. Highest and lowest temperatures
print("Highest temperature:", max(temps.values()))
print("Lowest temperature:", min(temps.values()))

# 2. Check for Friday
if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")

# 3. Add Thursday only if it does not exist
temps.setdefault("Thursday", 70)
print("After setdefault:", temps)

# 4. Demonstrate dynamic views
keys_view = temps.keys()

print("Before adding Friday:", keys_view)

temps["Friday"] = 74

print("After adding Friday:", keys_view)


# Advanced
prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

# 1. Total and average price
total_value = sum(prices.values())
average_price = total_value / len(prices)

print("Total value:", total_value)
print("Average price:", average_price)

# 2. Most and least expensive items
most_expensive = max(prices, key=prices.get)
least_expensive = min(prices, key=prices.get)

print("Most expensive:",
      most_expensive, "$", prices[most_expensive])

print("Least expensive:",
      least_expensive, "$", prices[least_expensive])

# 3. Compare memory usage
import sys

keys_view = prices.keys()
keys_list = list(prices.keys())

print("keys() memory:", sys.getsizeof(keys_view), "bytes")
print("list(keys()) memory:", sys.getsizeof(keys_list), "bytes")

# 4. Add three new products
prices.update({
    "headphones": 199,
    "speaker": 149,
    "camera": 799
})

print("All products:", prices)


# ============================================================
# UNIT 2.3 - ITEMS() METHOD
# ============================================================

print("\n===== UNIT 2.3 =====")

colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# Beginner

# 1. Print each fruit and color
for fruit, color in colors.items():
    print("The", fruit, "is", color)

# 2. Predict and verify items()
print("list(colors.items()):", list(colors.items()))


# Intermediate
prices = {
    "coffee": 4.50,
    "tea": 3.00,
    "juice": 5.25
}

# 1. Print each item with 10% tax
for item, price in prices.items():
    with_tax = price * 1.10
    print(f"{item}: ${price:.2f} + tax = ${with_tax:.2f}")

# 2. Count items over $4.00
count = 0

for item, price in prices.items():
    if price > 4.00:
        count += 1

print("Items costing more than $4.00:", count)

# 3. Swap variables
x = 10
y = 20

x, y = y, x

print("x =", x)
print("y =", y)

# 4. Extended unpacking
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# Advanced
scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

# 1. Find highest scoring student
best_student, best_score = max(
    scores.items(),
    key=lambda item: item[1]
)

print("Highest score:",
      best_student, best_score)


# 2. Create passed and failed dictionaries
passed = {}
failed = {}

for student, score in scores.items():
    if score >= 70:
        passed[student] = score
    else:
        failed[student] = score

print("Passed:", passed)
print("Failed:", failed)


# 3. Calculate class average and deviations
class_average = sum(scores.values()) / len(scores)

deviations = {}

for student, score in scores.items():
    deviations[student] = score - class_average

print("Class average:", class_average)
print("Score deviations:", deviations)


# 4. Performance test with 50,000 entries
big_dict = {
    i: i * 2
    for i in range(50000)
}

start = time.time()

for key, value in big_dict.items():
    result = key + value

items_time = time.time() - start


start = time.time()

for key in big_dict.keys():
    value = big_dict[key]
    result = key + value

keys_time = time.time() - start


print("items() iteration time:", items_time)
print("keys() + lookup time:", keys_time)

if items_time < keys_time:
    print("items() iteration was faster.")
else:
    print("keys() + lookup was faster.")


print("\n===== HOMEWORK COMPLETE =====")