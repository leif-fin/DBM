class Account:
    def __init__(self,account_name,opening_balance):
        self.account_name = account_name
        self.balance = opening_balance

    def display(self):
        # Balance Inquiry
        return self.account_name + ' ' + f"{self.balance:,.2f}"

    def setAccountName(self, new_name):
        self.account_name = new_name

def run():
    my_list = [10, 20, 30, 'Gun', 'Musket', 40, 11.0, 'Cannon']

    #print (len(my_list))
    size = len(my_list)

    print (my_list[-2])

    my_num = 1
    my_num = 2

    bank01 = Account('Dhirachat Ch', 5000.00)
    print(bank01.display())
    bank02 = Account('Hello World', 1500.00)
    print(bank02.display())

run()