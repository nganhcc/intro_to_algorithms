# Implement sequence interface via array, linkedlist, dynamic array underthe hood

class Array_Sequence:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        yield from self.A

    def build(self, X):  # O(n)
        self.A = [x for x in X]
        self.size = len(self.A)  # call from __len__

    def get_at(self, i):
        return self.A[i]

    def set_at(self, i, x):
        self.A[i] = x

    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j+k] = self.A[i+k]

    def _copy_backward(self, i, n, A, j):
        for k in range(n):
            A[j-k] = self.A[i-k]

    def insert_at(self, i, x):
        n = len(self.A)
        A = [None]*(n+1)
        self._copy_forward(0, i, A, i)
        A[i] = x
        self._copy_forward(i, n-i, A, i+1)
        self.build(A)

    def delete_at(self, i):
        n = len(self.A)
        A = [None] * (n-1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i+1, n-i-1, A, i)
        self.build(A)
        return x

    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
    def insert_last(self, x): self.insert_at(len(self.A), x)
    def delete_last(self): return self.delete_at(len(self.A)-1)


class LinkedList_Node:
    def __init__(self, x):
        self.item = x
        self.next = None

    def get(self):
        return self.item

    def set(self, x):
        self.item = x

    def later_node(self, i):
        if (i == 0):
            return self.head
        assert self.next
        return self.next.later_node(i-1)


class LinkedList_Sequence:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def build(self, X):
        for x in reversed(X):
            self.insert_fitst(x)

    def get_at(self, i):
        return self.head.later_node(i).get()

    def set_at(self, i, x):
        self.head.later_node(i).set(x)

    def insert_first(self, x):
        node = LinkedList_Node(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def delete_first(self):
        x = self.head.get()
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):
        node = LinkedList_Node(x)
        if i == 0:
            self.insert_first(x)
        else:
            ith_node = self.head.later_node(i-1)
            node.next = ith_node.next
            ith_node.next = node
            self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        else:
            ith_node = self.head.later_node(i-1)
            x = ith_node.get()
            ith_node.next = ith_node.next.next
            self.size -= 1
            return x

# amortized constant time


class Dynamic_Array_Seq(Array_Sequence):
    def __init__(self, r=2):
        super().__init__()
        self.size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self): return self.size  # O(1)

    def __iter__(self):  # O(n)

        for i in range(len(self)):
            yield self.A[i]

    def build(self, X):  # O(n)

        for a in X:
            self.insert_last(a)

    def _compute_bounds(self):  # O(1)

        self.upper = len(self.A)
        self.lower = len(self.A) // (self.r * self.r)

    def _resize(self, n):
        if (self.lower < n < self.upper):
            return

        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._compute_bounds()
        # O(1) or O(n)

    def insert_last(self, x):  # O(1)a

        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):  # O(1)a

        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, x):  # O(n)

        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):  # O(n)

        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x
    # O(n)
    def insert_first(self, x): self.insert_at(0, x)
    def delete_first(self): return self.delete_at(0)
