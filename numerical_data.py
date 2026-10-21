"""Show the numeric types in Python: int, float and complex (plus bool)."""

print("Python has three numeric types: int, float, and complex")

# Each value is a different type.
values = [
    42,      # int
    3.14,    # float
    5j,      # complex
    True,    # bool (a subtype of int)
]

for value in values:
    print(f"{value} is of the data type {type(value)}")
