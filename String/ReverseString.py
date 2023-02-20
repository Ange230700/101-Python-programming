def reverse(s):
    r = ""
    for c in s:
        r = c + r
    return r


string = input("Enter a string to reverse : ")
print(reverse(string))
