class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        node = Node(data)

        if head is None:
            return node

        curr = head
        while curr and curr.next:
            if curr.next is not None:
                curr = curr.next

        curr.next = node

        return head
