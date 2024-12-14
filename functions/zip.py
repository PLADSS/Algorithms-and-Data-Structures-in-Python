names = ["Alice", "Bob", "Charlie","David"]
ages = [24, 50, 18, 30]

combined = list(zip(names, ages))

for name, age in combined:
    print(f"{name} is {age} years old")