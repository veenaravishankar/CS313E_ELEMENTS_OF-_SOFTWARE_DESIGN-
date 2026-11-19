class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def parent(self, i):
        return (i - 1) // 2

    def l_child(self, i):
        return 2 * i + 1

    def r_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index):
        smallest = index
        l = self.l_child(index)
        r = self.r_child(index)

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l

        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def replace_root(self, val):
        self.heap[0] = val
        self.heapify_down(0)

    def get_root(self):
        return self.heap[0]

    def extract_min(self):
        if self.size() == 0:
            return None

        minimum = self.heap[0]
        last = self.heap.pop()

        if self.size() > 0:
            self.heap[0] = last
            self.heapify_down(0)

        return minimum

    def decrease_key(self, vertex, new_key):
        for i in range(self.size()):
            if self.heap[i][1] == vertex:
                self.heap[i] = (new_key, vertex)
                self._heapify_up(i)
                return


def prim(n, graph_rep, start=0):
    #list of list of tuples (neighor, edge cost)
    graph = []
    #init this with empty neighbors list
    for vertex in range(n):
        graph.append([])

    #storing each edge in the adj list, in both directions
    for u,v, weight in graph_rep:
        graph[u].append((v,weight))
        graph[v].append((u,weight))

    #MST: each mst entry will be a tuple (parent, vertex, weight)
    mst = []
    total_weight = 0
    #init key--cost and parent
    key = [float('inf')] * n
    parent = [None] * n

    #bool var to keep track of a vertex added to mst or not
    in_tree = [False] * n

    #create a minHeap obj
    queue = MinHeap()

    #init the cost to starting node to be 0
    key[start] = 0
    #building Minheap
    for vertex in range(n):
        queue.insert((key[vertex],vertex))

    while queue.size() > 0:
        #extract the min cost, root of min heap
        weight, vertex = queue.extract_min()
        #vertex added to MST indication
        in_tree[vertex] = True

        #add the edge that brought this vertex into MST
        #does not apply for starting vertex
        if parent[vertex] is not None:
            mst.append((parent[vertex],vertex,weight))
            total_weight+= weight

        for neighbor, weight in graph[vertex]:
            if not in_tree[neighbor] and weight< key[neighbor]:
                key[neighbor] = weight
                parent[neighbor] = vertex

                queue.decrease_key(neighbor,weight)
    return mst,total_weight







graph_rep = [
    (0, 1, 30),
    (1, 2, 15),
    (2, 3, 12),
    (3, 4, 16),
    (4, 1, 13),
    (4, 5, 21),
    (5, 3, 20),
    (5, 6, 22),
    (6, 0, 10),
]

mst, total_weight = prim(7, graph_rep, start=0)

print(mst)
print(total_weight)  # 92