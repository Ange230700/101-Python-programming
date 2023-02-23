size = int(input("Enter the size: "))  # Instead of input,
# convert it to integer!

print
char = input("Enter the character to draw: ")

print
for i in range(1, size+1):
    print(char*i)  # on the first iteration, prints 1 'x'
    # on the second iteration, prints 2 'x', and so on
