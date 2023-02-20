string = input("Enter a string to reverse : ")
# using Generator Expression
print("".join(string[c] for c in range(len(string) - 1, -1, -1)))
