


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

def size(head):
    current = head
    count = 0
    
    while current:
        count+=1
        current = current.next
    return count

def insertNodeAtPosition(head, data, position):
    new_node = Node(data)
    pos = 0
    if size(head) == 0:
        head = Node(data)
    elif position == 0:
        new_node.next = head
    else:
        node = head
        while node:
            if pos == position-1:
                new_node.next = node.next
                node.next = new_node
            pos+=1
            node = node.next
    
    return head
