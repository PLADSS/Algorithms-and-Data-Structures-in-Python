def binary_search(arr, target):
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None

for n in names:
    print(f"{n} is in position {binary_search(names, n)}")

