strings = ["my","world","apple","pear"]

lengths = map(lambda x: x+"s", strings)
print(list(lengths)) # [2, 5, 5, 4]




### Filter  ##
def longer_than_4(element):
    return len(element) > 4

strings = ["my","world","apple","pear"]
filtered = filter(longer_than_4, strings)
print(list(filtered)) # ['world', 'apple']



## Sum ##
numbers = [1,2,3,4,5]
print(sum(numbers,start=10)) # 25