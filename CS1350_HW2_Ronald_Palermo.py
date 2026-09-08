# CS1350 Mini-Project 1: Contact Manager - Dictionaries & Dictionary Patterns
# Rename this file to CS1350_HW2_FirstName_LastName.py before submitting.

# ---------------------------------------------------------------------------
# Data (Phases 2-6)
# ---------------------------------------------------------------------------

# Contact records: name -> dictionary of details
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}

# ===========================================================================
# Phase 1: Creating Contact Manager
# ===========================================================================
print("=== Phase 1: Quick Contacts ===")

# Build the quick_contacts dictionary one entry at a time
quick_contacts = {}
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"
print(quick_contacts)

print("--- Access and Modify ---")
# Bracket notation lookup
print(f"Mom's number: {quick_contacts['Mom']}")

# Update Dad's number
quick_contacts["Dad"] = "555-4321"

# Add a new contact
quick_contacts["Dentist"] = "555-2222"

# Safe lookup with get() - won't crash on a missing key
grandma_lookup = quick_contacts.get("Grandma", "Contact not found")
print(f"Looking up Grandma: {grandma_lookup}")

print(f"Updated contacts: {quick_contacts}")

print("--- Delete and Analyze ---")
# Remove with del (no return value)
del quick_contacts["Pizza Place"]

# Remove with pop() (returns the value that was removed)
old_work = quick_contacts.pop("Work")
print(f"Removed work number: {old_work}")

print(f"Contacts remaining: {len(quick_contacts)}")
print(f"Contact names: {list(quick_contacts.keys())}")
print(f"Phone numbers: {list(quick_contacts.values())}")


# ===========================================================================
# Phase 2: Per-Contact Statistics - Nested Iteration
# ===========================================================================
print("\n=== Phase 2: Contact Activity ===")

# Every later phase depends on this dictionary
total_minutes = {}

for name, months in call_log.items():
    num_months = len(months)
    total = sum(months.values())
    avg = total / num_months

    # Running-maximum pattern to find the busiest month
    busiest_month = None
    busiest_minutes = 0
    for month, minutes in months.items():
        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month

    total_minutes[name] = total

    print(f"{name}: {num_months} month(s), {total} min total, "
          f"avg: {avg:.2f}, busiest: {busiest_month} ({busiest_minutes})")


# ===========================================================================
# Phase 3: Flipping the Data & Aggregating with get()
# ===========================================================================
print("\n=== Phase 3: Aggregations ===")

# --- Part A: month_stats (call_log organized by month instead of contact) ---
month_stats = {}
for name, months in call_log.items():
    for month, minutes in months.items():
        if month not in month_stats:
            month_stats[month] = {"minutes": [], "total": 0, "avg": 0, "contacts": 0}
        month_stats[month]["minutes"].append(minutes)

for month, stats in month_stats.items():
    stats["total"] = sum(stats["minutes"])
    stats["contacts"] = len(stats["minutes"])
    stats["avg"] = stats["total"] / stats["contacts"]

print("Monthly summary (sorted by average, highest first):")
for month, stats in sorted(month_stats.items(), key=lambda item: item[1]["avg"], reverse=True):
    print(f"  {month}: {stats['total']} min total, {stats['avg']:.2f} avg "
          f"({stats['contacts']} contacts)")

# --- Part B: category / city / headcount rollups using the get() pattern ---
minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for name, total in total_minutes.items():
    info = contact_book[name]
    category = info["category"]
    city = info["city"]

    minutes_by_category[category] = minutes_by_category.get(category, 0) + total
    minutes_by_city[city] = minutes_by_city.get(city, 0) + total
    contacts_per_city[city] = contacts_per_city.get(city, 0) + 1

print(f"Minutes by category: {minutes_by_category}")
print(f"Minutes by city: {minutes_by_city}")
print(f"Contacts per city: {contacts_per_city}")


# ===========================================================================
# Phase 4: Dictionary Comprehensions
# ===========================================================================
print("\n=== Phase 4: Comprehensions ===")

phone_book = {name: info["phone"] for name, info in contact_book.items()}

local_contacts = {name: info["phone"] for name, info in contact_book.items()
                   if info["city"] == "Fort Wayne"}

activity_level = {name: ("Frequent" if total >= 200 else "Occasional")
                   for name, total in total_minutes.items()}

print(f"Phone book: {phone_book}")
print(f"Local contacts (Fort Wayne): {local_contacts}")
print(f"Activity level: {activity_level}")


# ===========================================================================
# Phase 5: Tiers, Distribution, and Rankings
# ===========================================================================
print("\n=== Phase 5: Tier Report ===")


def get_tier(minutes):
    """Classify total minutes into a loyalty tier."""
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"


# --- Part A: Classify ---
tiers = {}
for name, total in total_minutes.items():
    tier = get_tier(total)
    tiers[name] = tier
    print(f"{name}: {total} min ({tier})")

# --- Part B: Count ---
print("--- Tier Distribution ---")
tier_counts = {"Platinum": 0, "Gold": 0, "Silver": 0, "Bronze": 0, "Inactive": 0}
for name, tier in tiers.items():
    if tier == "Platinum":
        tier_counts["Platinum"] += 1
    elif tier == "Gold":
        tier_counts["Gold"] += 1
    elif tier == "Silver":
        tier_counts["Silver"] += 1
    elif tier == "Bronze":
        tier_counts["Bronze"] += 1
    else:
        tier_counts["Inactive"] += 1

for tier, count in tier_counts.items():
    print(f"{tier}: {count}")

# --- Part C: Rank ---
print("--- Top and Bottom ---")

top_name = None
top_minutes = 0
for name, total in total_minutes.items():
    if total > top_minutes:
        top_minutes = total
        top_name = name

# Start above any real value, per the running-comparison hint
bottom_name = None
bottom_minutes = float("inf")
for name, total in total_minutes.items():
    if total < bottom_minutes:
        bottom_minutes = total
        bottom_name = name

grand_total = sum(total_minutes.values())
average_minutes = grand_total / len(total_minutes)

print(f"Most contacted: {top_name} ({top_minutes} min)")
print(f"Least contacted: {bottom_name} ({bottom_minutes} min)")
print(f"Total minutes: {grand_total}")
print(f"Average per contact: {average_minutes:.2f}")

print("--- Above Average Contacts ---")
for name, total in total_minutes.items():
    if total > average_minutes:
        print(f"{name}: {total}")


# ===========================================================================
# Phase 6: The Contact Hub Report
# ===========================================================================
print("\n=== Phase 6: Contact Hub Report ===")

print(f"{'Name':<12}{'Category':<10}{'City':<14}{'Minutes':>8}  Tier")
print("-" * 57)

sorted_contacts = sorted(total_minutes.items(), key=lambda item: item[1], reverse=True)
for name, total in sorted_contacts:
    info = contact_book[name]
    tier = get_tier(total)
    print(f"{name:<12}{info['category']:<10}{info['city']:<14}{total:>8}  {tier}")

print("-" * 57)
print(f"{len(total_minutes)} contacts | {grand_total} total minutes | "
      f"{average_minutes:.2f} average")