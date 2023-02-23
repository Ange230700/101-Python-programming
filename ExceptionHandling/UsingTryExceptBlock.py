# program that uses try-except, else

while True:
    # Read int from console.
    denominator = int(input("Enter number : "))

    # Use int as denominator.
    try:
        i = 1 / denominator
    except:
        print("Error")
        raise
    else:
        print("OK")
