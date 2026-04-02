class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        node= Doubly_Linked_List_Node(x)
        if (self.head is None):
            self.head=node
            self.tail=node
            return
        node.next=self.head
        self.head.prev=node
        self.head=node
        ###########################
        pass

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        node=Doubly_Linked_List_Node(x)
        if (self.tail is None):
            self.head=node
            self.tail=node
            return
        self.tail.next=node
        node.prev=self.tail
        self.tail=node
        ###########################
        pass

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        x= self.head.item
        self.head.next.prev=None
        self.head=self.head.next
        ###########################
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        x= self.tail.item
        self.tail.prev.next=None
        self.tail=self.tail.prev
        ###########################
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        x1.prev.next=x2.next
        x2.next.prev=x1.prev
        L2.head=x1
        L2.tail=x2
        ###########################
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        L2.head.prev=x
        L2.tail.next=x.next
        x.next=L2.head
        L2.tail.next.prev=L2.tail
        L2.head=None
        L2.tail=None
        ###########################
        pass
