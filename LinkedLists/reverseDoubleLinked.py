


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node
    def iter(self):
        current = self.head

        while current:
            value = current.data
            current = current.next
            yield value

def size(head):
    current = head
    count = 0
    
    while current:
        count+=1
        current = current.next
    return count

def reverse(head):
    d = DoublyLinkedList()
    if size(head) == 1:
        return head
    curr = head
    while curr:
        new_node = DoublyLinkedListNode(curr.data)
        if d.head is None and d.tail is None:
            d.head = new_node
            d.tail = d.head
        else:
            new_node.next = d.head
            d.head.prev = new_node
            d.head = new_node
        curr = curr.next
    return d

d = DoublyLinkedList()
d.insert_node(1)
d.insert_node(2)
d.insert_node(3)

x = reverse(d.head)

for i in x.iter():
    print('Elemento: ', i)