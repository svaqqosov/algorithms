"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]
"""

import collections
import time

# Time complexity O(n^2)
def delete_nth_naive(array, n):
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans


# Time Complexity O(n), using hash tables.
def delete_nth(array, n):
    result = []
    counts = collections.defaultdict(int)  # keep track of occurrences
    
    for i in array:

        if counts[i] < n:
            result.append(i)
            counts[i] += 1

    return result

def delete_nth_with_set(array, n):
    k = dict.fromkeys(array, 0)
    newl = []
    for x in array:
        if (k[x] < n):
            newl.append(x)
            k[x] += 1
    return newl


n = 2
l = [1, 2, 3, 1, 2, 1, 2, 3]

print("\n----delete_nth_with_set----")
start = time.time()
res3 = delete_nth_with_set(l, n)
end = time.time()
print(res3)
print(end - start)

print("\n----delete_nth_naive----")
start = time.time()
res1 = delete_nth_naive(l, n)
end = time.time()
print(res1)
print(end - start)

print("\n----delete_nth----")
start = time.time()
res2 = delete_nth(l, n)
end = time.time()
print(res2)
print(end - start)


