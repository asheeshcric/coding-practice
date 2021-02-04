class MaxHeap:

    """
    Consider this heap: [15, 50, 23, 88, 90, 32, 74, 80]
    The indices are:    [0,  1,  2,  3,  4,  5,  6,  7]

    Max value in the heap is always: heap[0]
    Parent of any element at index "i": heap[(i-1)//2]
    Left child of any element at "i":   heap[i*2+1]
    Right child of any element at "i":  heap[i*2+2]
    """

    def __init__(self, items=[]):
        self.heap = []
        for i in items:
            self.heap.append(i)

    def push(self, data):
        self.heap.append(data)
        # Move the last element towards the top based on the values
        self._heapify(len(self.heap)-1, action='float_up')

    def peek(self):
        # Just return the max value in the heap (i.e. the root node)
        # The position of the root node in the "heap" array is len(heap)//2
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            print('Heap Empty')
            return None

    def pop(self):
        # Store the root element
        # Swap the last element with the root
        #  Heapify and return the stored root element
        root = self.peek()
        if root is None:
            return None
        # Remove the last element and move it in place of root
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            # Now, move the root element towards the bottom of the tree
            self._heapify(0, action='bubble_down')
        else:
            self.heap.pop()
        return root

    def _parent(self, idx):
        # Position and value of left child of any element at "i":   heap[i*2+1]
        pos = (idx-1) // 2
        return pos if pos < len(self.heap) else None

    def _left_child(self, idx):
        # Position and value of left child of any element at "i":   heap[i*2+1]
        pos = idx*2+1
        return pos if pos < len(self.heap) else None

    def _right_child(self, idx):
        # Position and value of right child of any element at "i":   heap[i*2+2]
        pos = idx*2+2
        return pos if pos < len(self.heap) else None

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _get_value(self, pos):
        if pos < len(self.heap):
            return self.heap[pos]
        else:
            return float('-inf')

    def _heapify(self, pos, action):
        # If the list is not in proper heap order, heapify it from bottom right
        if action == 'float_up':
            # Move the element at pos towards the top of the tree
            self._float_up(pos)
        else:
            # The action is bubble_down, so move the element towards the bottom of the tree
            self._bubble_down(pos)

    def _float_up(self, pos):
        parent_pos = self._parent(pos)
        if parent_pos is None:
            return
        elif self.heap[parent_pos] < self.heap[pos]:
            self._swap(parent_pos, pos)
            self._float_up(parent_pos)

    def _bubble_down(self, pos):
        left_child_pos = self._left_child(pos)
        right_child_pos = self._right_child(pos)
        size = len(self.heap)
        if left_child_pos >= size and right_child_pos >= size:
            return
        else:
            child_pos = left_child_pos if self.heap[left_child_pos] > self.heap[right_child_pos] else right_child_pos
            if self.heap[pos] < self.heap[child_pos]:
                self._swap(pos, child_pos)
                self._bubble_down(child_pos)
