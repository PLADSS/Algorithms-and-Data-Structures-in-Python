def sum(num):
    if not num:
        return 0
    print("Calling sum(%s)" % num[1:])
    remaining_sum = sum(num[1:])
    print("Call to sum(%s) returning %d + %d" % (num[1:], num[0], remaining_sum))
    return num[0] + remaining_sum

print(sum([1, 2, 3, 4, 5]))  