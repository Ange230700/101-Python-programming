array = list()
num = input("Enter number of elements : ")

print()
print('Enter '+str(num) + ' numbers in array : ')
for i in range(int(num)):
    n = input("num"+str(i+1)+": ")
    array.append(int(n))

print()
print("Numbers are : ")
print(array)

print()
find = int(input("Enter Number to find closest value : "))

print

# using lambda function


def takeClosest(num, collection): return min(
    collection, key=lambda x: abs(x-num))


print("Closest Value is : ", takeClosest(find, array))
