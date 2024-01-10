class Artifact:
    def __init__(self, name, artifact_set,stat):
        self.name = name
        self.artifact_set = artifact_set
        self.stat = stat

    def display(self):
        print(self.name + ' ' + self.artifact_set + ' ' + self.stat)

def run01():
    plume_of_death = Artifact('Plume of Death', "Shimenawa's Reminiscence", 'ATK %')
    plume_of_death.display()


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
            result = 'Empty Linkedlist'
        else:
            current_node = self.first_node
            while not (current_node.next is None):
                result = result + str(current_node.value.name) + ', '
                current_node = current_node.next
            result = result + str(current_node.value.name)
        return result

def run02():
    plume_of_death = Artifact('Plume of Death', "Shimenawa's Reminiscence", 'ATK %')
    flower_of_life = Artifact('Flower of Life', "Royal Flora", 'HP %')
    sands_of_eon = Artifact('Sands of Eon', "Noblesse Oblige", 'Element Mastery')

    artifact = LinkedList()
    artifact.append(Node(plume_of_death))
    artifact.append(Node(flower_of_life))
    artifact.append(Node(sands_of_eon))

    print(artifact.list())

run01()
run02()