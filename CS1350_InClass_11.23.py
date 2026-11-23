# Unit 1, Intermedite
import re

filenames = [
    "report.pdf", "image.jpg", "notes.txt",
    "script.py", "data.csv", "photo.PNG",
    "noext", ".hidden", "tricky.pdf.exe"
]

for name in filenames:
    lower_name = name.lower()

    # TODO 1: Check if file ends with .pdf using $ anchor and escaped dot
    is_pdf = re.search(r"\.pdf$", lower_name)

    # TODO 2: Check if file ends with .jpg or .png
    is_image = re.search(r"\.(jpg|png)$", lower_name)

    # TODO 3: Check if filename starts with a dot (hidden file)
    is_hidden = re.match(r"^\.", name)

    label = []

    if is_pdf:
        label.append("PDF")
    if is_image:
        label.append("IMAGE")
    if is_hidden:
        label.append("HIDDEN")

    print(f"{name:<20} → {', '.join(label) if label else 'other'}")
# Unit 2, Beginner
import re

text = "My phone is 555-1234 and my zip is 46802"

# TODO 1: Find the first sequence of one or more digits
match = re.search(r"\d+", text)
if match:
    print(f"First number: {match.group()}")

# TODO 2: Find the first sequence of one or more word characters
match2 = re.search(r"\w+", text)
if match2:
    print(f"First word: {match2.group()}")

# TODO 3: Search for optional "s" — match "cat" or "cats"
for word in ["cat", "cats", "catch"]:
    m = re.search(r"^cats?$", word)
    found = m.group() if m else "no match"
    print(f"'{word}' → {found}")
# Unit 3, Beginner
import re
# TODO 1: Match a string that is exactly 5 digits (like a ZIP code)
zips = ["46802", "1234", "123456", "4680A"]

for z in zips:
    match = re.fullmatch(r"\d{5}", z)
    result = "valid ZIP" if match else "invalid"
    print(f"{z} → {result}")

# TODO 2: Match exactly 2 uppercase letters (state abbreviation)
states = ["IN", "Ca", "NYC", "OH"]

print()

for s in states:
    match = re.fullmatch(r"[A-Z]{2}", s)
    result = "valid state" if match else "invalid"
    print(f"{s} → {result}")