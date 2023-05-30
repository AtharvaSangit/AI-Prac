
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n

    def find(self,a):
        if self.parent[a]==a:
            return a
        self.find(self.parent[a])
        return self.parent[a]

    def union(self,a, b):
        parA = self.find(a)
        parB = self.find(b)
        if self.rank[parA]==self.rank[parB]:
            self.parent[parB] = parA
            self.rank[parA]+=1
        elif self.rank[parA] < self.rank[parB]:
            self.parent[parA] = parB
        else:
            self.parent[parB] = parA
        
class Edge:
    def __init__(self, s, d, w):
        #0--5---1
        self.src = s
        self.dest = d
        self.wt = w

def createGraph():
    graph = []
    graph.append(Edge(0, 1, 10))
    graph.append(Edge(0, 2, 15))
    graph.append(Edge(0, 3, 30))
    graph.append(Edge(1, 3, 40))
    graph.append(Edge(2, 3, 50))
  
    return graph


def kruskals(g):
    mstCost = 0
    mst = []
    count = 0
    g.sort(key=lambda x: x.wt)
    
    uf = UnionFind(len(g))
    while(count<len(g)-1):
  
        r1 = uf.find(g[count].src)
        r2 = uf.find(g[count].dest)
     
        if r1!=r2:
            uf.union(g[count].src, g[count].dest)
            mstCost += g[count].wt
            mst.append((g[count].src, g[count].dest, g[count].wt))
        count=count+1
    printMST(mst)
    print(mstCost)

def printMST(mst):
    for e in mst:
        print(f"Edge: {e[0]}->{e[1]} Weight:{e[2]}")

n=5
g = createGraph()
kruskals(g)
#TC - O(ElogE + ElogV)
#SC - O(|E| + |V|)
