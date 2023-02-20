print("Enter the numbers separated by space : ")
try:
    input
except:
    input = input

# splitting the numbers by space and passing it to the sum function
print("Sum of the Numbers is : " + str(sum(int(x) for x in input().split())))
