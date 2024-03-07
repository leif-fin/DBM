class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            print(f"Going left from {root.val} to insert {key}")
            root.left = insert(root.left, key)
        else:
            print(f"Going right from {root.val} to insert {key}")
            root.right = insert(root.right, key)
    return root

def search(root, key):
    # This function remains unchanged, as it was not part of the confusion.
    if root is None or root.val == key:
        return True  # Return True if found
    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Create the root node
root = Node(50)
# Perform insertions
insertions = [30, 20, 40, 70, 60, 80, 10]
for key in insertions:
    insert(root, key)
    print("")

# Search for a value
if search(root, 60):
    print("Found")
else:
    print("Not Found")
