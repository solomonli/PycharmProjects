def partition(lst, k, n):
    reference = lst[-1]
    i, j = 0, 0
    while j < n - 1:
        if lst[j] < reference:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j += 1
        else:
            j += 1
    lst[i], lst[j] = lst[j], lst[i]

    if i == k:
        return lst[i]
    if i == 0:
        return partition(lst[1:], k - 1, n - 1)
    if k < i or i == n - 1:
        return partition(lst[:i], k, i)
    else:
        return partition(lst[i:], k - i, n - i)


n, k = (int(i) for i in input().split())
array = [int(i) for i in input().split()]
print(partition(array, k, n))

# array = [3, 6, 5, 7, 2, 9, 8, 10, 4, 1]
# print(partition(array, 0, 10))  # 1
# print(partition(array, 9, 10))  # 10
# print(partition(array, 4, 10))  # 5
