# 2.3  ###############################################################
words = ["kiwi", "fig", "banana", "plum", "apple"]

# TODO 1: Use filter and a lambda to keep the words with more than 4 letters.
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words) # ['banana', 'apple']

# TODO 2: Use sorted() with key=lambda ... to order the words by length.
by_length = sorted(words, key=lambda word: len(word))
print(by_length) # ['fig', 'kiwi', 'plum', 'apple', 'banana']
# 2.4  ###############################################################
class Adder:
    def __init__(self, amount):
        self.amount = amount

    # Returns the value plus the amount
    def __call__(self, value):
        return value + self.amount

add_ten = Adder(10)

print(add_ten(5))       # 15
print(callable(add_ten)) # True
# 3.1  ###############################################################
def count_up_to(n):
    """Yield 1, 2, 3, ... up to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

print(list(count_up_to(3)))  # [1, 2, 3]

gen = count_up_to(2)
print(next(gen))  # 1
print(next(gen))  # 2
# 3.2  ###############################################################
squares = (x * x for x in range(5))

print(next(squares)) # 0
print(next(squares)) # 1
print(list(squares)) # [4, 9, 16]
# 4.1  ###############################################################
def total(*numbers):
    """Return the sum of all the arguments."""
    return sum(numbers)

print(total(1, 2, 3)) # 6
print(total()) # 0

prices = [5, 10, 15]

# Unpack the list using *
result = total(*prices)
print(result) # 30
# 4.2  ###############################################################
def describe(name, age):
    return f"{name} is {age}"

person = {"name": "Ada", "age": 36}

# Unpack the dictionary
result = describe(**person)

print(result) # Ada is 36
