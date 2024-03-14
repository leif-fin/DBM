from queue import Queue, LifoQueue

def run01(): #Queue
    # Initializing
    my_size = 5

    q = Queue(maxsize=my_size)

    q.put(12)
    q.put(13)
    q.put(14)

    if q.full():
        print("Full")
    else:
        print("Not full")

    print("Now, Dequeue the element out of Queue")
    print(q.get())  # Python built-in use "get" for Dequeue

    q.put(15)
    print(q.get())

def run02():
    stack = LifoQueue(maxsize=3)
    stack.put(12)  # Python built-in use "tut" for Push
    stack.put(13)
    stack.put(14)

    if stack.full():
        print("Full")
    else:
        print("Not full")

    print("Now, POP() the element out of Stack")

    print(stack.get())  # Python built-in use "Get" for Pop

    if stack.full():
        print("Full")
    else:
        print("Not full")

    stack.put(15)
    print(stack.get())

    if stack.full():
        print("Full")
    else:
        print("Not full")

    print(stack.get())
    print(stack.get())

    if stack.empty():
        print("Empty")
    else:
        print("Not empty")

    print('Number of elements in a stack:' + str(stack.qsize()))


class Account:
    def __init__(self, account_name, opening_balance):
        self.account_name = account_name
        self.balance = opening_balance

def run03():
    bank_account01 = Account('Mr.A',20000)
    bank_account02 = Account('Mr.B',15000)
    bank_account03 = Account('Mr.C',10000)

    my_size = 3
    q = Queue(maxsize=my_size)

    q.put(bank_account01)
    q.put(bank_account02)
    q.put(bank_account03)

    print(q.get().account_name)

    stack = LifoQueue(maxsize=my_size)
    stack.put(bank_account01)
    stack.put(bank_account02)
    stack.put(bank_account03)

    print(stack.get().account_name)

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first_node = None
        self.size = 0

    def append(self, node):
        if self.first_node is None:
            self.first_node = node
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                current_node = current_node.next

            current_node.next = node
        self.size += 1

    def list(self):
        result = ''
        if self.first_node is None:
            result = 'Empty LinkedList'
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                result = result + str(current_node.value) + ', '
                current_node = current_node.next
            result = result + str(current_node.value)
        return result

def run04():
    node3 = Node(3)
    node9 = Node(9)
    node7 = Node(7)
    node1 = Node(1)
    node14 = Node(14)
    node2 = Node(2)

    my_linked_list = LinkedList()
    #print(my_linked_list.list())

    my_linked_list.append(node3)
    my_linked_list.append(node9)
    my_linked_list.append(node7)
    my_linked_list.append(node1)
    my_linked_list.append(node14)
    my_linked_list.append(node2)

    print(my_linked_list.list())

#run03()
run04()
    # print(my_linked_list.size)

    #node5 = Node('Five')
    #bank_account01 = Account('Mr.A', 20000)
    #node_bank01 = Node(bank_account01)
