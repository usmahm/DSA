from readline import insert_text


class Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.next = None
    
    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.later_node(i - 1)

class Linked_List_Seq:
    def __init__(self): # O(1)
        self.head = None
        self.size = 0

    def __len__(self): return self.size # O(1)

    def __iter__(self): # O(n)
        node = self.head

        while node:
            yield node.item
            node = node.next

    def build(self, X): # O(n)
        for a in reversed(X):
            self.insert_first(a)

    def insert_first(self, x): # O(1)
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self): # O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def get_at(self, i): # O(n)
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_at(self, i, x):
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node_before = self.head.later_node(i - 1)
        new_node.next = node_before.next
        node_before.next = new_node
        self.size += 1

    def delete_at(self, i):
        if i == 0:
            return self.delete_first()
        
        node_before = self.head.later_node(i - 1)
        x = node_before.next.item
        node_before.next = node_before.next.next
        self.size -= 1
        return x

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)