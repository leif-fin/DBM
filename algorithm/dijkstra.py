import sys

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}


def dijkstra(graph, start):
    shortest_distance = {}  # Record the shortest distance from the starting point to all other points
    predecessor = {}  # The previous node that records the shortest path
    unseenNodes = graph  # The node that was not processed
    infinity = sys.maxsize
    path = []  # Stores the shortest path
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
#core
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = 'F'  # Suppose we want the final node to be F
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance['F'] != infinity:
        print("Shortest distance is " + str(shortest_distance['F']))
        print("And the path is " + str(path))


dijkstra(graph, 'B')
