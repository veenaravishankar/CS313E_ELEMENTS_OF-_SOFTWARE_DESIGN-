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



def find_kth_largest(scores, k):
    #write code here
    min_heap = MinHeap()

    for score in scores:

        if min_heap.size() <k:
            min_heap.insert(score)
        elif score > min_heap.get_root():
            min_heap.replace_root(score)
    return min_heap.get_root()

    # Example
scores = [4, 12, 45, 23, 11]
k = 3
#returns the 3rd largest score which is 12
print(find_kth_largest(scores, k))
