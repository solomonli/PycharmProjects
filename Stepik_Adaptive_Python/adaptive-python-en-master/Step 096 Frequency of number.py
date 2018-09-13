n = int(input())
numbers = input().split()
counts = {i: 0 for i in set(numbers)}

# print("Initial Counts = {}".format(counts))
# Initialized frequency count

for item in numbers:
    counts[item] += 1

# print("Final Counts = {}".format(counts))
# frequency dict

print(1 if max(counts.values()) > n / 2 else 0)

'''
Sample Input:
5
2 3 9 2 2
'''
