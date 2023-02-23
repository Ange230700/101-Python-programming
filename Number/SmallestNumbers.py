alist = list(map(int, input("Enter numbers : ").split()))

smallest = alist[0]

for small in alist:
    if small < smallest:
        smallest = small

print()
print("Smallest number is :", smallest)
