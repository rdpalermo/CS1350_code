"""
HW4: Dictionary Advanced and Set
"""

# ============================================================
# UNIT 3.1 - Iterating Through Dictionaries
# ============================================================
print("\n--- Unit 3.1: Beginner (5 pts) ---")
inventory = {"apples": 50, "bananas": 30, "oranges": 25}

# 1. Print each product name using default iteration.
for product in inventory:
    print(product)

# 2. Calculate total items using values().
total_items = sum(inventory.values())
print(f"Total items: {total_items}")

# 3. Print each product with quantity using items().
for product, qty in inventory.items():
    print(f"{product}: {qty}")

print("\n--- Unit 3.1: Intermediate (10 pts) ---")
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# 1. Print products sorted alphabetically.
for product in sorted(prices):
    print(product)

# 2. Print products sorted by price (cheapest first).
for product in sorted(prices, key=prices.get):
    print(f"{product}: ${prices[product]}")

# 3. Find and print the most expensive item using items().
most_expensive = max(prices.items(), key=lambda item: item[1])
print(f"Most expensive: {most_expensive[0]} (${most_expensive[1]})")

print("\n--- Unit 3.1: Advanced (15 pts) ---")
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

# 1. Calculate average temperature using values().
avg_temp = sum(temps.values()) / len(temps)
print(f"Average temp: {avg_temp:.1f}")

# 2. Find the hottest and coldest days in a single loop.
hottest_day = coldest_day = None
for day, temp in temps.items():
    if hottest_day is None or temp > temps[hottest_day]:
        hottest_day = day
    if coldest_day is None or temp < temps[coldest_day]:
        coldest_day = day
print(f"Hottest: {hottest_day} ({temps[hottest_day]}), "
      f"Coldest: {coldest_day} ({temps[coldest_day]})")

# 3. Count how many days were above the average.
above_avg_count = sum(1 for temp in temps.values() if temp > avg_temp)
print(f"Days above average: {above_avg_count}")

# ============================================================
# UNIT 3.2 - Advanced Iteration & Nested Dictionaries
# ============================================================
print("\n--- Unit 3.2: Beginner (5 pts) ---")
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

# 1. Print the laptop's price.
print(f"Laptop price: {products['laptop']['price']}")

# 2. Print each product with its stock level.
for name, info in products.items():
    print(f"{name}: stock = {info['stock']}")

print("\n--- Unit 3.2: Intermediate (10 pts) ---")

# 1. Given two lists, create a dictionary using zip():
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
country_capitals = {}
for country, capital in zip(countries, capitals):
    country_capitals[country] = capital
print(country_capitals)

# 2. Add a new product "tablet" to products.
products["tablet"] = {"price": 449, "stock": 30}
print(products)

# 3. Safely remove all products with stock < 20.
for name, info in list(products.items()):
    if info["stock"] < 20:
        del products[name]
print(f"After removing low stock: {products}")

print("\n--- Unit 3.2: Advanced (15 pts) ---")
company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

# 1. Print all employees with their salaries (nested iteration).
for dept, employees in company.items():
    for name, salary in employees.items():
        print(f"{dept} - {name}: ${salary}")

# 2. Calculate the average salary per department.
for dept, employees in company.items():
    avg_salary = sum(employees.values()) / len(employees)
    print(f"{dept} average: ${avg_salary:,.2f}")

# 3. Find the highest-paid employee across all departments.
highest_name, highest_salary, highest_dept = None, -1, None
for dept, employees in company.items():
    for name, salary in employees.items():
        if salary > highest_salary:
            highest_name, highest_salary, highest_dept = name, salary, dept
print(f"Highest paid: {highest_name} ({highest_dept}, ${highest_salary})")

# ============================================================
# UNIT 3.3 - Dictionary Patterns & Transformations
# ============================================================
print("\n--- Unit 3.3: Beginner (5 pts) ---")

# 1. Comprehension mapping numbers 1-5 to their cubes.
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)

# 2. temps dict -> new dict with Celsius values.
temps_f = {"Mon": 72, "Tue": 68, "Wed": 75}
temps_c = {day: round((f - 32) * 5 / 9, 1) for day, f in temps_f.items()}
print(temps_c)

print("\n--- Unit 3.3: Intermediate (10 pts) ---")
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

# 1. Create passing dict with only scores >= 70.
passing = {name: score for name, score in scores.items() if score >= 70}
print(f"Passing: {passing}")

# 2. Create letter_grades dict converting scores to letters.
def to_letter(s):
    if s >= 90:
        return "A"
    if s >= 80:
        return "B"
    if s >= 70:
        return "C"
    return "F"

letter_grades = {name: to_letter(score) for name, score in scores.items()}
print(f"Letter grades: {letter_grades}")

# 3. Invert student_ids to look up by ID.
student_ids = {"Alice": 101, "Bob": 102}
id_lookup = {id_: name for name, id_ in student_ids.items()}
print(f"ID lookup: {id_lookup}")

print("\n--- Unit 3.3: Advanced (15 pts) ---")
sales = [
    ("North", "Alice", 5000), ("South", "Bob", 4500),
    ("North", "Carol", 6000), ("South", "Alice", 3500)
]

# 1. Calculate total sales by region.
by_region = {}
for region, person, amount in sales:
    by_region[region] = by_region.get(region, 0) + amount
print(f"By region: {by_region}")

# 2. Calculate total sales by salesperson.
by_person = {}
for region, person, amount in sales:
    by_person[person] = by_person.get(person, 0) + amount
print(f"By person: {by_person}")

# 3. Create a nested dict: {region: {person: total}}.
nested = {}
for region, person, amount in sales:
    nested.setdefault(region, {})
    nested[region][person] = nested[region].get(person, 0) + amount
print(f"Nested: {nested}")


print("\n" + "=" * 70)
print("LECTURE 4: SETS IN PYTHON")
print("=" * 70)

# ============================================================
# UNIT 1 - Set Theory and Python Sets
# ============================================================
print("\n--- Unit 1: Beginner (5 pts) ---")

# 1. Create a set called vowels containing all vowels.
vowels = {"a", "e", "i", "o", "u"}
print(vowels)

# 2. Set from list with duplicates - how many elements?
nums = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"Unique elements: {nums} -> count = {len(nums)}")

# 3. What's wrong with `empty = {}`?
print("`{}` creates an empty DICTIONARY, not a set. "
      "Use `empty = set()` for an empty set.")

print("\n--- Unit 1: Intermediate (10 pts) ---")

# 1. text = "mississippi" -> set of unique characters, how many?
text = "mississippi"
unique_chars = set(text)
print(f"Unique chars: {unique_chars} -> count = {len(unique_chars)}")

# 2. Remove duplicates from emails list, convert back to list.
emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = list(set(emails))
print(f"Unique emails: {unique_emails}")

# 3. Why does `s = {[1, 2], [3, 4]}` fail?
print("It fails with TypeError: unhashable type: 'list'. "
      "Lists are mutable, so they can't be hashed and can't be set elements "
      "(use tuples instead, e.g. {(1, 2), (3, 4)}).")

print("\n--- Unit 1: Advanced (15 pts) ---")
import time

# 1. Compare membership check time: set vs list (1 million elements).
big_set = set(range(1_000_000))
big_list = list(range(1_000_000))

start = time.perf_counter()
999999 in big_set
set_time = time.perf_counter() - start

start = time.perf_counter()
999999 in big_list
list_time = time.perf_counter() - start

print(f"Set lookup: {set_time:.8f}s | List lookup: {list_time:.8f}s")
print("Set lookup is O(1) (hash table); list lookup is O(n) (linear scan) "
      "and is dramatically slower for large collections.")

# 2. Create a frozenset and use it as a dictionary key.
fs = frozenset([1, 2, 3])
lookup_by_fs = {fs: "first group"}
print(lookup_by_fs)

# 3. Given edges, create a set of unique nodes.
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
nodes = set()
for a, b in edges:
    nodes.add(a)
    nodes.add(b)
print(f"Unique nodes: {nodes}")

# ============================================================
# UNIT 2 - Set Operations
# ============================================================
print("\n--- Unit 2: Beginner (5 pts) ---")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. Find all unique numbers (union).
print(f"Union: {a | b}")

# 2. Find numbers in both sets (intersection).
print(f"Intersection: {a & b}")

# 3. Find numbers only in set a (difference).
print(f"a - b: {a - b}")

print("\n--- Unit 2: Intermediate (10 pts) ---")
morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

# 1. Employees who work ALL shifts.
all_shifts = morning_shift & evening_shift & weekend_shift
print(f"Work all shifts: {all_shifts}")

# 2. Employees who work at least one shift (any shift).
any_shift = morning_shift | evening_shift | weekend_shift
print(f"Work at least one shift: {any_shift}")

# 3. Employees who ONLY work morning (not evening or weekend).
only_morning = morning_shift - evening_shift - weekend_shift
print(f"Only morning: {only_morning}")

# 4. Employees who work exactly one shift.
in_two_plus = ((morning_shift & evening_shift) |
               (morning_shift & weekend_shift) |
               (evening_shift & weekend_shift))
exactly_one = any_shift - in_two_plus
print(f"Exactly one shift: {exactly_one}")

print("\n--- Unit 2: Advanced (15 pts) ---")
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

# 1. Students eligible to enroll (must meet ALL three criteria).
eligible = prereqs_met & has_space & paid_tuition
print(f"Eligible: {eligible}")

# 2. Students who met prereqs but haven't paid tuition.
prereqs_not_paid = prereqs_met - paid_tuition
print(f"Prereqs met, not paid: {prereqs_not_paid}")

# 3. Students missing at least one requirement (prereqs OR tuition).
all_students = prereqs_met | has_space | paid_tuition
meets_both = prereqs_met & paid_tuition
missing_one = all_students - meets_both
print(f"Missing prereqs or tuition: {missing_one}")

# ============================================================
# UNIT 3 - Set Methods, Comprehensions & Patterns
# ============================================================
print("\n--- Unit 3: Beginner (5 pts) ---")

# 1. Create {1, 2, 3}, add 4, remove 1.
s = {1, 2, 3}
s.add(4)
s.remove(1)
print(s)

# 2. Set comprehension: all even numbers from 0-20.
evens = {x for x in range(21) if x % 2 == 0}
print(evens)

# 3. discard() vs remove() on a missing element.
demo_set = {1, 2, 3}
demo_set.discard(99)  # No error
print(f"After discard(99): {demo_set}")
try:
    demo_set.remove(99)  # Raises KeyError
except KeyError:
    print("remove(99) raised KeyError as expected")

print("\n--- Unit 3: Intermediate (10 pts) ---")

# 1. Remove duplicates while preserving order.
data = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
seen = set()
ordered_unique = []
for item in data:
    if item not in seen:
        seen.add(item)
        ordered_unique.append(item)
print(f"Order-preserved unique: {ordered_unique}")

# 2. Set comprehension: unique words from sentence (lowercase).
sentence = "To be or not to be that is the question"
unique_words = {word.lower() for word in sentence.split()}
print(f"Unique words: {unique_words}")

# 3. Find the missing numbers.
expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}
missing = expected - actual
print(f"Missing numbers: {missing}")

print("\n--- Unit 3: Advanced (15 pts) ---")

# 1. find_duplicates(lst): return set of elements appearing more than once.
def find_duplicates(lst):
    seen = set()
    dupes = set()
    for item in lst:
        if item in seen:
            dupes.add(item)
        else:
            seen.add(item)
    return dupes

print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))

# 2. Three sets of employee skills.
alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

skills_all_three = alice & bob & carol
skills_only_alice = alice - bob - carol
skills_everyone_combined = alice | bob | carol
print(f"All three have: {skills_all_three}")
print(f"Only Alice has: {skills_only_alice}")
print(f"All unique skills: {skills_everyone_combined}")

# 3. common_chars(s1, s2): return common characters as a set.
def common_chars(s1, s2):
    return set(s1) & set(s2)

print(common_chars("hello", "world"))