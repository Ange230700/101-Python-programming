from os.path import exists

print("Type the filename :")
file = input("> ")
if exists(file):
    txt_again = open(file, 'r')
    print(txt_again.read())
else:
    print("no such file")
