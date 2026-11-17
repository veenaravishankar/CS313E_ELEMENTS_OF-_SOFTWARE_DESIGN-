from _collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self,vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self,u,v):
        #create vertices in case they haven't been yet
        self.add_vertex(u)
        self.add_vertex(v)

        #undirected graph
        if v not in self.adj[u]:
            self.adj[u].append(v)

        if u not in self.adj[v]:
            self.adj[v].append(u)

    def display(self):
        for vertex,edges in self.adj.items():
            print(vertex,"-->",edges)

    def bfs(self, start):
        if start not in self.adj:
            print("Starting vertex does not exist.")
            return

        distance = {}
        parent = {}

        for vertex in self.adj:
            distance[vertex] = None
            parent[vertex] = None

        queue = deque([start])
        distance[start] = 0

        print("BFS order:", end=" ")

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.adj[current]:
                if distance[neighbor] is None:
                    distance[neighbor] = distance[current] + 1
                    parent[neighbor] = current
                    queue.append(neighbor)

        print()
        print("Vertex | Distance | Parent")

        for vertex in self.adj:
            print(vertex, "|", distance[vertex], "|", parent[vertex])

        return distance, parent

    def dfs(self, start):
        if start not in self.adj:
            print("Starting vertex does not exist.")
            return

        visited = set()
        parent = {}
        depth = {}
        order = []

        for vertex in self.adj:
            parent[vertex] = None
            depth[vertex] = None

        depth[start] = 0

        self.dfs_visit(start, visited, parent, depth, order)

        print("DFS order:", " ".join(str(v) for v in order))

        print("Vertex | Depth | Parent")
        for vertex in self.adj:
            print(vertex, "|", depth[vertex], "|", parent[vertex])

        return depth, parent

    def dfs_visit(self, current, visited, parent, depth, order):
        visited.add(current)
        order.append(current)

        for neighbor in self.adj[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                depth[neighbor] = depth[current] + 1

                self.dfs_visit(
                    neighbor, visited, parent, depth, order
                )
graph = Graph()

#adding vertices
vertices = ['A', 'B','C','D','E']
for vertex in vertices:
    graph.add_vertex(vertex)

#add edges
graph.add_edge('A','B')
graph.add_edge('A','C')
graph.add_edge('B','D')
graph.add_edge('C','E')

#display graph
graph.display()

#BFS call
graph.bfs('A')

#DFS call
graph.dfs('A')