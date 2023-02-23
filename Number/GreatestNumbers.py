alist = list(map(int, input("Enter numbers : ").split()))

largest = alist[0]

for large in alist:
    if large > largest:
        largest = large

print()
print("Largest number is :", largest)
