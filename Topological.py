class TopologicalSortGraph:
    def __init__(self, vertices):
        self.graph = {v: [] for v in vertices}
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        from collections import deque
        in_degree = {v: 0 for v in self.vertices}
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1
        queue = deque([v for v in self.vertices if in_degree[v] == 0])
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        if len(topo_order) == len(self.vertices):
            return topo_order
        else:
            return "Graph has a cycle!"


if __name__ == "__main__":
    topo_graph = TopologicalSortGraph(['A', 'B', 'C', 'D', 'E'])
    topo_graph.add_edge('A', 'B')
    topo_graph.add_edge('A', 'C')
    topo_graph.add_edge('B', 'D')
    topo_graph.add_edge('C', 'D')
    topo_graph.add_edge('D', 'E')

    print("Topological Sort:", topo_graph.topological_sort())