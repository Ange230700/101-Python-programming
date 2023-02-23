class Account(object):
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no

    def display(self):
        print("\nEmployee Details: ")
        print("\nCustomer name: ", name)
        print("\nAccount number: ", acc_no)


class Saving_account(Account):
    def __init__(self, name, acc_no, bal):
        super(Saving_account, self).__init__(name, acc_no)
        self.bal = bal

    def display(self):
        super(Saving_account, self).display()
        print("\nBalance: ", bal)


class Account_details(Saving_account):
    def __init__(self, name, acc_no, bal, deposits, withdrawal):
        super(Account_details, self).__init__(name, acc_no, bal)
        self.deposits = deposits
        self.withdrawal = withdrawal

    def display(self):
        super(Account_details, self).display()
        print("\nDeposits: ", deposits)
        print("\nWithdrawal: ", withdrawal)


name = input("\nEnter name: ")
acc_no = int(input("\nEnter account number: "))
bal = int(input("\nEnter balance: "))
deposits = int(input("\nEnter deposit amount: "))
withdrawal = int(input("\nEnter withdrawal amount: "))

ad = Account_details(name, acc_no, bal, deposits, withdrawal)
ad.display()
