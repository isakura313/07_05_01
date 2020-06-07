def adder(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum
print(adder(2,3))
print(adder(4,5,6,7,44,3))
