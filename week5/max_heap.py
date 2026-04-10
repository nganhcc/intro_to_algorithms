class PriorityQueue:
    def __init__(self, A):
        self.n = 0
        self.A = A

    # absorb element A[n] into the queue
    def insert(self):
        if not self.n < len(self.A):
            raise IndexError("insert into full priority queue")
        self.n += 1

    # remove element A[n-1] from the queue
    def delete_max(self):
        if self.n < 1:
            raise IndexError("pop from empty priority queue")
        self.n -= 1   # NOT correct on its own!

    @classmethod
    def sort(cls, A):
        pq = cls(A)  # make empty priority queue

        # insert all elements
        for _ in range(len(A)):   # n × T_insert
            pq.insert()

        # delete max repeatedly
        for _ in range(len(A)):   # n × T_delete_max
            pq.delete_max()

        return pq.A

def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i

def left(i, n):
    l = 2 * i + 1
    return l if l < n else i

def right(i, n):
    r = 2 * i + 2
    return r if r < n else i
class PQ_Heap(PriorityQueue):

    # O(log n)
    def insert(self, *args):
        super().insert(*args)      # append to end of array
        n, A = self.n, self.A
        max_heapify_up(A, n, n - 1)

    # O(log n)
    def delete_max(self):
        n, A = self.n, self.A
        A[0], A[n - 1] = A[n - 1], A[0]   # swap root with last element
        max_heapify_down(A, n - 1, 0)
        return super().delete_max()       # pop from end of array

def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, -1, -1): # O(n) loop backward over array
        max_heapify_down(A, n, i) # O(log n - log i)) fix max heap

def max_heapify_up(A, n, c): # T(c) = O(log c)
    p = parent(c) # O(1) index of parent (or c)
    if A[p].key < A[c].key: # O(1) compare
        A[c], A[p] = A[p], A[c] # O(1) swap parent
        max_heapify_up(A, n, p) # T(p) = T(c/2) recursive call on parent
def max_heapify_down(A, n, p): # T(p) = O(log n - log p)
    l, r = left(p, n), right(p, n) # O(1) indices of children (or p)
    c = l if A[r].key < A[l].key else r # O(1) index of largest child
    if A[p].key < A[c].key: # O(1) compare
        A[c], A[p] = A[p], A[c] # O(1) swap child
        max_heapify_down(A, n, c) # T(c) recursive call on child