# Use BFS as part of the Ford-Fulkerson algorithm
def bfs(rGraph, s, t, parent):
    visited = [False] * len(rGraph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(rGraph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    rGraph = [i[:] for i in graph]  # Create a copy of the residual diagram

    while bfs(rGraph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, rGraph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while (v != source):
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

    return max_flow


# example
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5

max_flow = ford_fulkerson(graph, source, sink)
print(f"Maximum flow: {max_flow}")
