numbers = [4,5,3,-1,10]
sorted_numbers = sorted(numbers)
#sorted_numbers = sorted(numbers, reverse=True)
#print(sorted_numbers)


people= [
    {"name": "Harry", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]
sorted_people = sorted(people, key=lambda x: x["age"])
#print(sorted_people)



## Enumerate ##
tasks = ["task1", "task2", "task3"]

# for i in range(len(tasks)):
#     tasks= tasks[i]
#     print(f"{i+1}. {tasks}")

for i, task in enumerate(tasks):
    print(f"{i+1}. {task}")
 