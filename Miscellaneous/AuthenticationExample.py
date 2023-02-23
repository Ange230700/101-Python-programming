class Authentication(Exception):
    def display(self):
        print("\nAuthentication Failed...")


name = input("\nEnter your name: ")
password = int(input("\nEnter your password: "))

try:
    if (password == 123):
        print("\nAuthenticated User...")
    else:
        raise Authentication()
except Authentication as a:
    a.display()
