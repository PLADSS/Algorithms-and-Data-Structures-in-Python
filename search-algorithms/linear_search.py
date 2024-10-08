import sys 
from load import load_numbers

names = load_strings(sys.argv[1])

def index_of_item(item, values):
    for i in range(len(values)):
        if item == values[i]:
            return i
    return None

for n in names:
    print(f"{n} is in position {index_of_item(n, names)}")
    