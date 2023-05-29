class Edge:
    def __init__(self, s, d, w):
        self.src = s
        self.dest = d
        self.wt = w

def createGraph(vertices):
    graph = [[] for _ in range(vertices)]
    # 0 vertex
    graph[0].append(Edge(0, 1, 1))
    graph[0].append(Edge(0, 2, 1))

    # 1 vertex
    graph[1].append(Edge(1, 0, 1))
    graph[1].append(Edge(1, 3, 1))

    # 2 vertex
    graph[2].append(Edge(2, 0, 1))
    graph[2].append(Edge(2, 4, 1))

    # 3 vertex
    graph[3].append(Edge(3, 1, 1))
    graph[3].append(Edge(3, 4, 1))
    graph[3].append(Edge(3, 5, 1))

    # 4 vertex
    graph[4].append(Edge(4, 2, 1))
    graph[4].append(Edge(4, 3, 1))
    graph[4].append(Edge(4, 5, 1))

    # 5 vertex
    graph[5].append(Edge(5, 3, 1))
    graph[5].append(Edge(5, 4, 1))
    graph[5].append(Edge(5, 6, 1))

    # 6 vertex
    graph[6].append(Edge(6, 5, 1))
    return graph

def dfsSimple(g,vis, curr):
    print(curr)
    vis[curr] = True
    for e in g[curr]:
        if vis[e.dest]:
            continue
        dfsSimple(g,vis,e.dest)


g = createGraph(7)
vis = [False]*len(g)
dfsSimple(g,vis,0)