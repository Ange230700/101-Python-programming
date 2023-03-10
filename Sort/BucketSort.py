# Bucket Sort Program

import math


def bucketsort(A):
    # get hash codes
    code = hashing(A)
    buckets = [list() for _ in range(code[1])]
    # distribute data into buckets: O(n)
    for i in A:
        x = re_hashing(i, code)
        buck = buckets[x]
        buck.append(i)

    for bucket in buckets:
        insertionsort(bucket)
        ndx = 0
    # merge the buckets: O(n)
    for b in range(len(buckets)):
        for v in buckets[b]:
            A[ndx] = v
            ndx += 1


def hashing(A):
    m = A[0]
    for i in range(1, len(A)):
        if (m < A[i]):
            m = A[i]
    result = [m, int(math.sqrt(len(A)))]
    return result


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


def insertionsort(aList):
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
        aList[k] = tmp


# User input
sort_list = list()
count = input("Enter number of elements : ")

print()
print('Enter '+str(count) + ' numbers : ')

print
for i in range(int(count)):
    n = input("number"+str(i+1)+": ")
    sort_list.append(int(n))

bucketsort(sort_list)

print
print("Elements in sorted order :")
print(sort_list)
