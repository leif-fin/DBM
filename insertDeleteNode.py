# LinkedList with Python Class

# Python Class

class Artifact:
    def __init__(self, name, artifact_set, stat):
        self.name = name
        self.stat = stat
        self.artifact_set = artifact_set

    def display(self):
        return self.name + ' - ' + self.artifact_set + ' - ' + self.stat


def run01():
    plume_of_death = Artifact('Plume of Death', "Shimenawa's Reminiscence", 'ATK %')
    print(plume_of_death.display())


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
                result = result + str(current_node.value.name) + ', '  # Put Artifact's name after value
                current_node = current_node.next
            result = result + str(current_node.value.name)  # Put Artifact's name after value
        return result

    def insert(self, node, target_node):  # insert before
        if self.first_node is None:
            self.first_node = node
            return 0
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                if current_node.next is target_node:

                    # insert
                    node.next = current_node.next
                    current_node.next = node
                    self.size += 1

                    current_node = node.next
                else:
                    current_node = current_node.next

    def delete(self, node):
        if self.first_node is None:
            return 0
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                if current_node.next is node:

                    # insert

                    current_node.next = node.next
                    self.size -= 1

                    current_node = node.next
                else:
                    current_node = current_node.next


def run04():
    plume_of_death = Artifact('Plume of Death', "Shimenawa's Reminiscence", 'ATK %')
    flower_of_life = Artifact('Flower of Life', "Royal Flora", 'HP %')
    sands_of_eon = Artifact('Sands of Eon', "Noblesse Oblige", 'Element Mastery')

    artifacts = LinkedList()

    node1 = Node(plume_of_death)
    node2 = Node(flower_of_life)
    node3 = Node(sands_of_eon)

    artifacts.append(node1)
    artifacts.append(node2)
    artifacts.append(node3)

    print(artifacts.list())

    goblet_of_eonothem = Artifact('Goblet of Eonothem', "Berserkere", 'Energy Recharge')

    node4 = Node(goblet_of_eonothem)

    artifacts.insert(node4, node3)

    print(artifacts.list())

    artifacts.delete(node2)
    print(artifacts.list())

run04()