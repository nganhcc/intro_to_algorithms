def height(A):
    if A: return A.height
    else: return -1
'''
if we use:  rebalacing take O(n log n) : O(log n): for balacing from leaves to root, O(n): for compute height each time balacing
def height(A): take O(n)  boi ta khong cap nhat va luu height cua moi node nen se ton O(n) de chay het xem nhanh nao co height cao hon
    if A is None: return -1
    return 1+max(height(self.left), height(self.right))
'''
class Binary_Node:
    def __init__(self, x):
        self.item=x
        self.left=None
        self.right=None
        self.parent=None
        self.subtree_update()
    def subtree_update(self):  #take O(1)  -> rebalncing take O(log n)
        self.height= 1+max(height(self.left), height(self.right) )
    def skew(self):  # O(1)
        return height(self.right)-height(self.left)
    def subtree_iter(self): #O(n)
        if self.left: yield from self.left.subtree_iter()
        yield self
        if self.right: yield from self.right.subtree_iter()
    def subtree_first(self): #O(log n)
        if self.left: return self.left.subtree_first()
        else: return self
    def subtree_last(self):
        if self.right: return self.right.subtree_last()
        else: return self
    def successor(self): #O(log n)
        if self.right: return self.right.subtree_first()
        while self.parent and (self.parent.right is self):
            self=self.parent
        return self.parent
    def predecessor(self):
        if self.left: return self.left.subtree_last()
        while self.parent and (self.parent.left is self):
            self=self.parent
        return self.parent
    def subtree_insert_before(self,B): #O(log n)
        if self.left:
            self=self.left.subtree_last()
            self.right, B.parent= B, self
        else:
            self.left, B.parent= B,self
        self.maintain()
    def subtree_insert_after(self,B):
        if self.right:
            self=self.right.subtree_first()
            self.left, B.parent= B, self
        else:
            self.right, B.parent= B,self
        self.maintain()
    def subtree_delete(self):
        if self.left or self.right:
            if self.left: B= self.predecessor()
            else: B=self.successor()
            self.item , B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self: self.parent.left=None
            else: self.parent.right=None
            self.parent.maintain()
        return self
    def subtree_rotate_right(D): # O(1)
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()
    def subtree_rotate_left(B): # O(1)
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()
    def rebalance(A): # O(1)
        if A.skew() == 2:
            if A.right.skew() < 0:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() > 0:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()
    def maintain(A): # O(log n)
        A.rebalance()
        A.subtree_update()
        if A.parent: A.parent.maintain()
            


    