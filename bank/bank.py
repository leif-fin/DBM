class Account:
   def __init__(self,account_name,opening_balance):
       self.account_name = account_name
       self.balance = opening_balance
   def display(self):
       #Balance Inquiry
       return self.account_name + ' ' + f"{self.balance:,.2f}"
   def setAccountName(self, new_name):
       self.account_name = new_name

def run():
    my_list = [10, 20, 30, 'Gun', 'Musket', 40, '11.0', 'Cannon']
    size = len(my_list)
    print(size)
    print(my_list[size-1])

    my_num = 1
    my_num = 2
    print(my_num)

    bank01 = Account('Linfeng Zhang', 5000)
    print(bank01)

from queue import Queue, LifoQueue

def run03():
    bank_account1 = Account('Mr.A',20000)
    bank_account2 = Account('Mr.B',15000)
    bank_account3 = Account('Mr.C',10000)

    my_size = 3
    q = Queue(maxsize=my_size)

    q.put(bank_account1)
    q.put(bank_account2)
    q.put(bank_account3)

    print(q.get().account_name)

    stack = LifoQueue(maxsize=my_size)
    stack.put(bank_account1)
    stack.put(bank_account2)
    stack.put(bank_account3)

    print(stack.get().account_name)

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.fisr_node = None
        self.sezi = 0

def append(self, node):
    if self.first_node is Node:
        self.first_

def run04():
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node.bank01 = Node(bank_account)
