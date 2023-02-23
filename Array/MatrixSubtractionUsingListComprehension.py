print("Enter the value of row : ")
x = int(input())

print("Enter the value of column : ")
y = int(input())

a = [[0 for row in range(0, x)] for col in range(0, y)]
b = [[0 for row in range(0, x)] for col in range(0, y)]
result = [[0 for row in range(0, x)] for col in range(0, y)]

print()
print("Enter elements of first matrix : ")
for i in range(x):
    for j in range(y):
        a[i][j] = int(input())

print()
print("Enter the elements of second matrix : ")
for i in range(x):
    for j in range(y):
        b[i][j] = int(input())

print()
print("Elements of First matrix is : ")
for row in a:
    print(row)

print()
print("Elements of Second matrix is :")
for row in b:
    print(row)

# Using list comprehension
result = [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

print()
# print the Subtraction of 2 matrix
print("Subtraction is : ")
for r in result:
    print(r)
