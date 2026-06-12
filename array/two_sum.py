nums = [2, 7, 11, 15]
target = 9

hashmap = {}

for i, num in enumerate(nums):
    diff = target - num

    if diff in hashmap:
        print([hashmap[diff], i])
        break

    hashmap[num] = i