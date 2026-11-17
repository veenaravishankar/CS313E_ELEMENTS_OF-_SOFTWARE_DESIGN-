class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Find the representative, using path compression.
        #the recursive call finds the root, and the assignment makes x point directly to that root. The vertices remain in the same set; we just shorten the path.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected; this edge creates a cycle.

        # Attach the shorter tree under the taller tree.
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n, edges):
    # Vertices: 0 through n - 1
    # Each edge: (u, v, weight)
    ds = DisjointSet(n)
    mst = []
    total_weight = 0
#This sorts the edges by weight, then processes them one at a time. Each edge is stored as a tuple
#edge[2] is the third value: the weight.
#lambda edge: edge[2] tells Python to use that weight for sorting.
#sorted returns a new list from smallest weight to largest:
    for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

            if len(mst) == n - 1:
                break

    return mst, total_weight

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4),
]

mst, total_weight = kruskal(4, edges)

print(mst)           # [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
print(total_weight)  # 19