# dll on nodes only
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __next__(self):
        return self.next
    def __prev__(self):
        return self.prev
    def __str__(self):
        return str(self.data)
    def find(self, data):
        # left side nodes if exists:
        cur:Node = self.prev
        while cur:
            if cur.data == data:
                return cur
            cur = cur.prev
        # right side nodes if exists:
        cur:Node = self.next
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    def find_prev(self, data):
        # left side nodes if exists:
        cur:Node = self.prev
        while cur:
            if cur.data == data:
                return cur
            cur = cur.prev
        return None
    def find_next(self, data):  
        # right side nodes if exists:
        cur:Node = self.next
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    def insert_after(self, data):
        new_node = Node(data)
        new_node.next = self.next
        new_node.prev = self
        if self.next:
            self.next.prev = new_node
        self.next = new_node
        return new_node
    def insert_before(self, data):
        new_node = Node(data)
        new_node.prev = self.prev
        new_node.next = self
        if self.prev:
            self.prev.next = new_node
        self.prev = new_node
        return new_node
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return self.next if self.next else self.prev
    def __repr__(self):
        return f"Node({self.data})"
    def __str__(self):
        return str(self.data)
    def printList(self):
        cur:Node = self
        while cur.prev:
            cur = cur.prev
        while cur:
            print(f"({cur.data})" if cur==self else cur.data, end=" <-> ")
            cur = cur.next
        print("None")
    def moveRight(self):
        if self.next:
            return self.next
        return self
    def moveLeft(self):
        if self.prev:
            return self.prev
        return self

a=Node(1)
a.printList()
a=a.insert_before(2)
a.printList()
a=a.insert_before(3)
a.printList()
a=a.insert_after(4)
a.printList()
a=a.insert_after(5)
a.printList()
a.find(2).insert_after(4)
a.printList()
# a.find(2).insert_before(5) 
# a.printList()
# print(a.data)
a=a.moveLeft()
print(a.data)
a.printList()
a=a.delete()
a.printList()
# a=a.find(4)
# print(a.data)
# a.printList()
