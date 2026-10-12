
"""
CS1350 Homework 2
Dictionary Practice Exercises
Name: Ronnie Palermo
"""


import time
import sys


# ==================================================
# UNIT 1.1 - WHAT ARE DICTIONARIES?
# ==================================================

# Beginner - 5 points
def unit_1_1_beginner():
    print("\nUNIT 1.1 - BEGINNER")

    my_info = {
        "name": "Ronnie",
        "age": 19,
        "major": "Cyber Security"
    }

    print(my_info)


# Intermediate - 10 points
def unit_1_1_intermediate():
    print("\nUNIT 1.1 - INTERMEDIATE")

    menu = {
        "burger": 8.99,
        "fries": 3.49,
        "pizza": 12.50,
        "salad": 6.75
    }

    course_credits = {
        "CS1350": 3,
        "CS1330": 3,
        "MATH201": 4
    }

    print("Menu:", menu)
    print("Course credits:", course_credits)


# Advanced - 15 points
def unit_1_1_advanced():
    print("\nUNIT 1.1 - ADVANCED")

    weekly_temps = dict(
        Monday=72,
        Tuesday=75,
        Wednesday=68,
        Thursday=70,
        Friday=73,
        Saturday=77,
        Sunday=71
    )

    print("Weekly temperatures:", weekly_temps)


# ==================================================
# UNIT 1.2 - ACCESSING DICTIONARY ELEMENTS
# ==================================================

# Beginner - 5 points
def unit_1_2_beginner():
    print("\nUNIT 1.2 - BEGINNER")

    pet = {
        "name": "Buddy",
        "type": "dog",
        "age": 3
    }

    print("Pet name:", pet["name"])
    print("Pet age:", pet["age"])


# Intermediate - 10 points
def unit_1_2_intermediate():
    print("\nUNIT 1.2 - INTERMEDIATE")

    pet = {
        "name": "Buddy",
        "type": "dog",
        "age": 3
    }

    print("Pet color:", pet.get("color", "unknown"))

    grades = {
        "CS1350": 88,
        "MATH201": 67,
        "ENG101": 91
    }

    course = "CS1350"
    grade = grades.get(course)

    if grade is not None:
        if grade >= 70:
            print(course, "passed with grade", grade)
        else:
            print(course, "failed with grade", grade)
    else:
        print("Course grade not found")


# Advanced - 15 points
def unit_1_2_advanced():
    print("\nUNIT 1.2 - ADVANCED")

    products = {
        "laptop": 999.99,
        "mouse": 29.99,
        "keyboard": 79.99
    }

    for product_name in ["mouse", "monitor"]:
        price = products.get(product_name)

        if price is not None:
            print(f"{product_name}: ${price:.2f}")
        else:
            print("Product not available")


# ==================================================
# UNIT 1.3 - MODIFYING DICTIONARIES
# ==================================================

# Beginner - 5 points
def unit_1_3_beginner():
    print("\nUNIT 1.3 - BEGINNER")

    inventory = {}

    inventory["apples"] = 10
    inventory["bananas"] = 6
    inventory["oranges"] = 8

    print("Inventory:", inventory)


# Intermediate - 10 points
def unit_1_3_intermediate():
    print("\nUNIT 1.3 - INTERMEDIATE")

    scores = {
        "Team A": 45,
        "Team B": 38
    }

    scores["Team B"] = 52
    scores["Team C"] = 41

    removed_score = scores.pop("Team A")

    print("Removed Team A score:", removed_score)
    print("Updated scores:", scores)


# Advanced - 15 points
def unit_1_3_advanced():
    print("\nUNIT 1.3 - ADVANCED")

    cart = {}

    cart["baseball"] = 24.99
    cart["glove"] = 49.99
    cart["water bottle"] = 12.50

    cart["glove"] = 44.99

    removed_price = cart.pop("water bottle")

    print("Removed water bottle price:", removed_price)
    print("Final cart:", cart)

    total = sum(cart.values())
    print(f"Total price: ${total:.2f}")


# ==================================================
# UNIT 2.1 - HOW DICTIONARIES WORK
# ==================================================

# Beginner - 5 points
def unit_2_1_beginner():
    print("\nUNIT 2.1 - BEGINNER")

    examples = [
        ('"student_name"', True),
        ("[1, 2, 3]", False),
        ("100", True),
        ('("x", "y")', True),
        ('{"a": 1}', False),
        ("frozenset({1, 2})", True)
    ]

    reasons = {
        '"student_name"': "Strings are immutable.",
        "[1, 2, 3]": "Lists are mutable.",
        "100": "Integers are immutable.",
        '("x", "y")': "This tuple contains immutable strings.",
        '{"a": 1}': "Dictionaries are mutable.",
        "frozenset({1, 2})": "Frozensets are immutable."
    }

    for key, valid in examples:
        if valid:
            print(key, "is valid because", reasons[key])
        else:
            print(key, "is invalid because", reasons[key])

    print("Hash of my name:", hash("Ronnie"))
    print("Hash of 100:", hash(100))


# Intermediate - 10 points
def unit_2_1_intermediate():
    print("\nUNIT 2.1 - INTERMEDIATE")

    # Tuples can be used as dictionary keys.
    locations = {
        (40.7, -74.0): "New York",
        (34.0, -118.2): "Los Angeles"
    }

    print("Locations:", locations)

    data = {
        "a": 1,
        "b": 2,
        "a": 3,
        "b": 4
    }

    print("Dictionary:", data)
    print("Length:", len(data))
    print("The last value for each duplicate key is kept.")


# Advanced - 15 points
def unit_2_1_advanced():
    print("\nUNIT 2.1 - ADVANCED")

    high_scores = {
        ("Alex", "Racing"): 950,
        ("Jordan", "Puzzle"): 820,
        ("Taylor", "Racing"): 1100
    }

    print("High scores:", high_scores)
    print("Taylor's Racing score:",
          high_scores[("Taylor", "Racing")])

    big_list = list(range(100000))
    big_dict = {number: True for number in range(100000)}

    target = 99999

    start = time.perf_counter()
    list_result = target in big_list
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    dict_result = target in big_dict
    dict_time = time.perf_counter() - start

    print("Found in list:", list_result)
    print("List search time:", list_time)

    print("Found in dictionary:", dict_result)
    print("Dictionary search time:", dict_time)

    if dict_time > 0:
        print("List/dictionary time ratio:",
              list_time / dict_time)

    print("Timing can change between computers.")


# ==================================================
# UNIT 2.2 - keys() AND values() METHODS
# ==================================================

# Beginner - 5 points
def unit_2_2_beginner():
    print("\nUNIT 2.2 - BEGINNER")

    temps = {
        "Monday": 72,
        "Tuesday": 75,
        "Wednesday": 68
    }

    print("Days:", list(temps.keys()))
    print("Temperatures:", list(temps.values()))
    print("Number of days:", len(temps))


# Intermediate - 10 points
def unit_2_2_intermediate():
    print("\nUNIT 2.2 - INTERMEDIATE")

    temps = {
        "Monday": 72,
        "Tuesday": 75,
        "Wednesday": 68
    }

    print("Highest temperature:", max(temps.values()))
    print("Lowest temperature:", min(temps.values()))

    if "Friday" in temps:
        print("Friday is in the dictionary.")
    else:
        print("Friday is not in the dictionary.")

    temps.setdefault("Thursday", 70)
    print("After setdefault:", temps)

    days_view = temps.keys()

    print("Keys before adding Friday:", days_view)

    temps["Friday"] = 74

    print("Keys after adding Friday:", days_view)


# Advanced - 15 points
def unit_2_2_advanced():
    print("\nUNIT 2.2 - ADVANCED")

    prices = {
        "laptop": 999,
        "phone": 699,
        "tablet": 449,
        "watch": 299
    }

    total = sum(prices.values())
    average = total / len(prices)

    most_expensive = max(
        prices.items(),
        key=lambda item: item[1]
    )

    least_expensive = min(
        prices.items(),
        key=lambda item: item[1]
    )

    print(f"Total value: ${total:.2f}")
    print(f"Average price: ${average:.2f}")

    print(
        f"Most expensive: {most_expensive[0]} "
        f"${most_expensive[1]:.2f}"
    )

    print(
        f"Least expensive: {least_expensive[0]} "
        f"${least_expensive[1]:.2f}"
    )

    keys_view = prices.keys()
    keys_list = list(prices.keys())

    print("Keys view memory:",
          sys.getsizeof(keys_view), "bytes")

    print("Keys list memory:",
          sys.getsizeof(keys_list), "bytes")

    prices.update({
        "headphones": 129,
        "camera": 549,
        "speaker": 89
    })

    print("All products:")

    for name, price in prices.items():
        print(f"{name}: ${price:.2f}")


# ==================================================
# UNIT 2.3 - items() METHOD
# ==================================================

# Beginner - 5 points
def unit_2_3_beginner():
    print("\nUNIT 2.3 - BEGINNER")

    colors = {
        "apple": "red",
        "banana": "yellow",
        "grape": "purple"
    }

    for fruit, color in colors.items():
        print(f"The {fruit} is {color}")

    print("List of items:", list(colors.items()))


# Intermediate - 10 points
def unit_2_3_intermediate():
    print("\nUNIT 2.3 - INTERMEDIATE")

    prices = {
        "coffee": 4.50,
        "tea": 3.00,
        "juice": 5.25
    }

    for item, price in prices.items():
        taxed_price = price * 1.10
        print(
            f"{item}: ${price:.2f} + tax = "
            f"${taxed_price:.2f}"
        )

    count = 0

    for item, price in prices.items():
        if price > 4.00:
            count += 1

    print("Items costing more than $4.00:", count)

    x = 10
    y = 20

    x, y = y, x

    print("After swapping: x =", x, "y =", y)

    numbers = [1, 2, 3, 4, 5]

    first, *middle, last = numbers

    print("First element:", first)
    print("Middle elements:", middle)
    print("Last element:", last)


# Advanced - 15 points
def unit_2_3_advanced():
    print("\nUNIT 2.3 - ADVANCED")

    scores = {
        "Alice": 88,
        "Bob": 65,
        "Carol": 92,
        "Dave": 71,
        "Eve": 58
    }

    best_student, best_score = max(
        scores.items(),
        key=lambda item: item[1]
    )

    print(
        "Highest score:",
        best_student,
        "with",
        best_score
    )

    passed = {}
    failed = {}

    for name, score in scores.items():
        if score >= 70:
            passed[name] = score
        else:
            failed[name] = score

    print("Passed:", passed)
    print("Failed:", failed)

    average = sum(scores.values()) / len(scores)

    deviations = {}

    for name, score in scores.items():
        deviations[name] = score - average

    print(f"Class average: {average:.2f}")
    print("Score deviations:")

    for name, deviation in deviations.items():
        print(f"{name}: {deviation:.2f}")

    big_dict = {
        number: number * 2
        for number in range(50000)
    }

    start = time.perf_counter()

    for key, value in big_dict.items():
        result = key + value

    items_time = time.perf_counter() - start

    start = time.perf_counter()

    for key in big_dict.keys():
        value = big_dict[key]
        result = key + value

    keys_time = time.perf_counter() - start

    print(f"items() time: {items_time:.6f} seconds")
    print(f"keys() with lookup time: {keys_time:.6f} seconds")
    print("Timing can change between computers.")


# ==================================================
# RUN ALL EXERCISES
# ==================================================

def main():
    print("CS1350 Homework 2")
    print("Dictionary Practice Exercises")

    unit_1_1_beginner()
    unit_1_1_intermediate()
    unit_1_1_advanced()

    unit_1_2_beginner()
    unit_1_2_intermediate()
    unit_1_2_advanced()

    unit_1_3_beginner()
    unit_1_3_intermediate()
    unit_1_3_advanced()

    unit_2_1_beginner()
    unit_2_1_intermediate()
    unit_2_1_advanced()

    unit_2_2_beginner()
    unit_2_2_intermediate()
    unit_2_2_advanced()

    unit_2_3_beginner()
    unit_2_3_intermediate()
    unit_2_3_advanced()


if __name__ == "__main__":
    main()