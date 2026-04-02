# comparision model -> always take O(log n) for searching operation
# we can improve to make it constant time O(1) for searching; in trade off space complexity O(u) u is large

class DirectAccessArray:
    def __init__(self, u): self.A=[None]*u
    def find(self,k): return self.A[k]
    def insert(self, x): self.A[x.key]=x
    def delete(self, k): self.A[k]=None
    def find_next(self, k):
        for i in range(k, len(self.A), 1):
            if (self.A[i] is not None):
                return self.A[i]
    def find_max(self):
        for i in range(len(self.A)-1, -1 ,-1):
            if self.A[i] is not None:
                return self.A[i]
    def delete_max(self):
        for i in range(len(self.A)-1, -1 ,-1):
            if self.A[i] is not None:
                x= self.A[i]
                self.A[i]=None
                return x


