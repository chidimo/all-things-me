# There are n houses built in a line. A thief wants to maximum_loot the maximum possible money from these houses. The only restriction the thief has is that he can’t maximum_loot from two consecutive houses, as that would alert the security system. How should the thief maximize his maximum_looting?

# Problem Statement
# Given a number array representing the wealth of n houses, determine the maximum amount of money the thief can loot without alerting the security system.

def maximum_loot(arr):

    n = len(arr)

    # if there are no item in the array, return 0
    if n == 0:
        return 0

    # if there is just one item, return it
    if n == 1:
        return arr[0]

    # if there are two items, find their maximum and return it
    if n == 2:
        return max(arr)

    # on getting to door 3 onwards (represented as i),
    # we need to decide between the value there and that in the previous index
    # we could either pick a) value at i + second adjacent value OR b) keep our previous maximum
    # depending on which is bigger
    max_value = None
    initial_max = arr[0]
    max_on_reaching_i = max(initial_max, arr[1])

    for i in range(2, len(arr)):
        max_value = max(arr[i] + initial_max, max_on_reaching_i)
        initial_max = max_on_reaching_i
        max_on_reaching_i = max_value

    return max_value


assert(maximum_loot([]) == 0)
assert(maximum_loot([5]) == 5)
assert(maximum_loot([5, 10]) == 10)
assert(maximum_loot([1, 2, 4]) == 5)
assert(maximum_loot([2, 5, 1, 3, 6, 2, 4]) == 15)
assert(maximum_loot([2, 10, 14, 8, 1]) == 18)
