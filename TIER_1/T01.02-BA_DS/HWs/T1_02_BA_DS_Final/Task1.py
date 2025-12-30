class Node:
    def __init__(self, data=None):
        self.data = data          # value stored in this node
        self.next = None          # next node


class LinkedList:
    def __init__(self):
        self.head = None          # head (first node). If None = the list is empty

    def insert_at_end(self, data):
        new_node = Node(data)     # create a new node with given data

        if self.head is None:     # if the list is empty
            self.head = new_node  # new node becomes the head
            return

        cur = self.head           # start from the head
        while cur.next:           # if there is a next node:
            cur = cur.next        # move to the next node
        cur.next = new_node       # if current is last -> attach new_node at the end

    def print_list(self):
        cur = self.head           # start from the head
        while cur:                # while cur is not None
            print(cur.data)       # print current node's value
            cur = cur.next        # and move to the next node


# Task 1 - Reverse
    def reverse(self):
        prev = None               # prev will become the "previous node" in the reversed list
        cur = self.head           # cur starts at the current head of the list

        while cur:                # loop until last node - cur becomes None
            nxt = cur.next        # 1. saves next node
            cur.next = prev       # 2. reverse pointer: current node points backward
            prev = cur            # 3. move prev forward: prev becomes current
            cur = nxt             # 4. move cur forward: cur becomes the saved next node

        self.head = prev          # after loop, prev is the new head (old tail)


# Task 2 - Insertion sort
    def sort(self):
        """
        Take nodes one by one and insert them into a new sorted list
        """
        sorted_head = None        # head of the new sorted list
        cur = self.head

        while cur:                
            nxt = cur.next        # save next node from original list 
            sorted_head = self._insert_sorted(sorted_head, cur)  # insert cur into the sorted list
            cur = nxt             # move to the next node in the original list

        self.head = sorted_head   # replace head with the sorted list head


    def _insert_sorted(self, sorted_head, node):
        """
        Insert node into the correct position at 'sorted_head'
        Returns the head of the sorted list
        """
        # If sorted list is empty OR node should be the first element
        if sorted_head is None or node.data <= sorted_head.data:
            node.next = sorted_head   # node points to current head
            return node               # node becomes new head

        cur = sorted_head             # start from sorted list head
        # Find position: stop when next is None OR next value is >= node value
        while cur.next and cur.next.data < node.data:
            cur = cur.next            # move forward in the sorted list

        node.next = cur.next          # node points to the next element after cur
        cur.next = node               # cur now points to node (inserting node)
        return sorted_head


# Task 3 - Merge two sorted linked lists
def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged = LinkedList()
    fake_head = Node(0)           # fake_head node to simplify merging
    tail = fake_head              # tail always points to the last node in the merged chain

    a = list1.head                # pointers for list1 and list2
    b = list2.head 

    while a and b:                # while both lists still have nodes
        if a.data <= b.data:      # choose node from list1:
            tail.next = a         # attach 'a' node to the merged list
            a = a.next            # move 'a' forward
        else:                     # or choose node from list2:
            tail.next = b         # attach 'b' node to the merged list
            b = b.next            # move 'b' forward
        tail = tail.next          # move tail forward to the newly attached node

    tail.next = a if a else b     # attach remaining nodes from whichever list is not empty

    merged.head = fake_head.next  # real head is after dummy
    return merged                 # return the merged LinkedList


# Test
if __name__ == "__main__":
    l1 = LinkedList()
    for x in [3, 1, 5, 2]:
        l1.insert_at_end(x)

    print("Original:")
    l1.print_list()

    l1.reverse()
    print("\nReversed:")
    l1.print_list()

    l1.sort()
    print("\nSorted:")
    l1.print_list()

    l2 = LinkedList()
    for x in [0, 4, 6]:
        l2.insert_at_end(x)
    l2.sort()

    merged = merge_sorted_lists(l1, l2)
    print("\nMerged:")
    merged.print_list()
