# define a function
def print_factors(x):
    """This function takes a
    number and prints the factors"""

    print()
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i),


# take input from the user
num = int(input("Enter a number : "))

print_factors(num)
