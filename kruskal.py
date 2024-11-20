class KruskalAlgorithm:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def kruskal_mst(self):
        
        self.edges.sort()
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            root1, root2 = find(v1), find(v2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        mst = []
        for weight, u, v in self.edges:
            if find(u) != find(v):
                 mst.append((u, v, weight))
                 union(u, v)
        return mst

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    kruskal_graph = KruskalAlgorithm(vertices)
    kruskal_graph.add_edge('A', 'B', 3)
    kruskal_graph.add_edge('A', 'C', 1)
    kruskal_graph.add_edge('B', 'C', 7)
    kruskal_graph.add_edge('B', 'D', 5)
    kruskal_graph.add_edge('C', 'D', 2)
    kruskal_graph.add_edge('D', 'E', 7)

    print("Kruskal's MST:", kruskal_graph.kruskal_mst())
