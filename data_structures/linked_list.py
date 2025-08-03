class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head
        prev = None
        while temp:
            if temp.data == value:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                break
            prev = temp
            temp = temp.next

    def traverse(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result
