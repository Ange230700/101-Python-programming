

tup1 = ('harry', 'ron')
tup2 = (1, 2, 3)
tup3 = (1, 2, 3)

list1 = ['a', 'b', 'c']

# Compares elements of both tuples.
# If tup1 is greater (1), if tup1 is smaller (-1), is both are same (0)
print("Comparison of tup1 & tup2: ", cmp(tup1, tup2))
print("Comparison of tup2 & tup3: ", cmp(tup2, tup3))

# Print length of a tuple
print('Length of tup2: ', len(tup2))

# Print item from the tuple with max value.
print('Max of tup2: ', max(tup2))

# Print item from the tuple with min value.
print('Min of tup2: ', min(tup2))

# Converts a list into tuple.
tup4 = tuple(list1)
print("Converted tuple from list: ", tup4)
