def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    small = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    big = [x for x in arr if x > pivot]
    print(small, " AND ", mid, " AND ", big)
    return quicksort(small) + mid + quicksort(big)


print(quicksort([3, 6, 8, 10, 100, 1, 2, 1]))


'''
WOW, WHAT A COOL,ELEGENT CODE!
'''

'''

1. Pick an element, called a pivot, from the array.
2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, 
while all elements with values greater than the pivot come after it (equal values can go either way). 
3. After this partitioning, the pivot is in its final position. This is called the partition operation.
Recursively apply the above steps to the sub-array of elements with smaller values 
and separately to the sub-array of elements with greater values.

The base case of the recursion is arrays of size zero or one, which are in order by definition, 
so they never need to be sorted.

The pivot selection and partitioning steps can be done in several different ways; 
the choice of specific implementation schemes greatly affects the algorithm's performance.

'''
