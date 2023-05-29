import heapq

class Edge:
    def __init__(self, s, d, w):
        #0--5---1
        self.src = s
        self.dest = d
        self.wt = w

def createGraph(vertices):
    graph = [[] for _ in range(vertices)]
    #[[(0,2,15),()],  ]
    # graph[0].append(Edge(0, 2, 15))
    graph[0].append(Edge(0, 3, 3))
    graph[0].append(Edge(0, 4, 12))

    graph[1].append(Edge(1, 2, 2))
    graph[1].append(Edge(1, 3, 5))

    graph[2].append(Edge(2, 4, 7))
    graph[2].append(Edge(2, 3, 3))
    graph[2].append(Edge(2, 1, 2))

    graph[3].append(Edge(3, 0, 3))
    graph[3].append(Edge(3, 1, 5))
    graph[3].append(Edge(3, 2, 3))

    graph[4].append(Edge(4, 0, 12))
    graph[4].append(Edge(4, 2, 7))
  
    
    return graph

def prims(graph):
    vis = [False]*len(graph)
    pq = []
    mst = []
    mstCost = 0
    heapq.heappush(pq, (0,0)) #cost, cur_rvertex
    while pq:
        c, v = heapq.heappop(pq)
        if vis[v]:
            continue

        vis[v] = True
        mstCost += c
        
        for e in graph[v]:
            if e.wt == c and vis[e.dest]==True:
                mst.append((e.src, e.dest, e.wt))
            heapq.heappush(pq, (e.wt, e.dest))
    print(mstCost)
    printMST(mst)

def printMST(mst):
    for e in mst:
        print(f"Edge: {e[0]}->{e[1]} Weight:{e[2]}")

g= createGraph(5)
prims(g)

     
          