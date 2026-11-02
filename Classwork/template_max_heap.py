import sys
class MaxHeap:
    '''
    Max Heap Implementation template (0-based index)
    '''
    
    def insert(self, element):
        '''
        Insert an element into the heap and maintain heap property
        '''
        self.heap_list.append(element)
        current = self.size - 1

        while current > 0 and self.heap_list[current] > self.heap_list[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def max_heapify(self, i):
        pass
        
    def build_max_heap(self, unsorted_list):
        pass

    def extract_max(self):
        pass
        
    def __str__(self):
        pass


def main():
    my_heap = MaxHeap()
    my_heap.insert(1)
    print(my_heap)
    my_heap.insert(4)
    print(my_heap)
    my_heap.insert(10)
    print(my_heap)
    my_heap.insert(13)
    print(my_heap)
    my_heap.insert(17)
    print(my_heap)
    my_heap.insert(9)
    print(my_heap)
    my_heap.insert(22)
    print(my_heap)

    


if __name__ == '__main__':
    main()
