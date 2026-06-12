arr = [2, 4, 1, 3, 5]

prefix = []
curr_sum = 0

for num in arr:
    curr_sum += num
    prefix.append(curr_sum)

print(prefix)