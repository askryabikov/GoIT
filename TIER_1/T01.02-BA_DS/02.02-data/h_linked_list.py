class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
    # some useful methods
    def __getitem__(self, index):
        if not self.search_element(index): raise IndexError("Index out of range")
        return self.search_element(index).data 
    def __sub__(self,data):
        self.insert_at_beginning(data)
    def __add__(self, data):
        self.insert_at_end(data)
ll=LinkedList()
ll+10
ll+"\'20\'"
ll+30
ll+(lambda x: x**2)
print(ll.head)
ll.print_list()
ll-4
ll-5
ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
print(ll[10])
# print(ll[3])