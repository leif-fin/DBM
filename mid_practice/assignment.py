class Weapon:
    def __init__(self,name, type, level):
        self.name = name
        self.type = type
        self.level = level

    def upgrade(self):
        self.level = str(int(self.level) + 1)
        print('weapon upgraded level to ' + self.level)

    def display(self):
        print(self.name + ' ' + self.type + ' ' + self.level)

def run():
    weapon1 = Weapon('revolver','pistol','2')
    weapon2 = Weapon('AK47','rifle','1')
    weapon1.upgrade()
    weapon1.display()
    weapon2.upgrade()
    weapon2.display()

class NodeWeapon:
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
                result = result + str(current_node.value.name) + ', ' # Name is attribute of Artifact
                current_node = current_node.next
            result = result + str(current_node.value.name) # Normally, LinkedList element is integer
        return result

def run02():
    weapon1 = Weapon('revolver','pistol','2')
    weapon2 = Weapon('AK47','rifle','1')

    weapons = LinkedList()
    weapons.append(NodeWeapon(weapon1))
    weapons.append(NodeWeapon(weapon2))

    print(weapons.list())

#run()
run02()