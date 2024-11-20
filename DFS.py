class DFSGraph:
    def __init__(self, vertices):
        self.graph = {v: [] for v in vertices}
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        traversal = []

        def dfs_recursive(v):
            visited.add(v)
            traversal.append(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return traversal

if __name__ == "__main__":
    dfs_graph = DFSGraph(['A', 'B', 'C', 'D', 'E'])
    dfs_graph.add_edge('A', 'B')
    dfs_graph.add_edge('A', 'C')
    dfs_graph.add_edge('B', 'D')
    dfs_graph.add_edge('C', 'D')
    dfs_graph.add_edge('D', 'E')

    print("DFS from 'A':", dfs_graph.dfs('A'))