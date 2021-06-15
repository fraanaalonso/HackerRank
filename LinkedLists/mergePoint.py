


class SingleNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SingleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SingleNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

        return node
    





def findMergeNode(head1, head2):
    curr = head1
    curr1 = head2
    l1 = l2 = value= 0
    while curr: 
        l1+=1 
        curr = curr.next
    while curr1: 
        l2+=1
        curr1 = curr1.next
    if l2 - l1 >= 0: 
        value = (l2 - l1)
        for i in range(value):
             head2 = head2.next
    
    else: 
        value = (l1 - l2)
        for i in range(value):
             head1 = head1.next
    
    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next

iz = SingleList()
der = SingleList()
cent = SingleList()

node1 = iz.insert_node(1)
node2 = der.insert_node(1)
node3 = cent.insert_node(2)
node4 = cent.insert_node(4)
node1.next = node3
node2.next = node3

print(findMergeNode(node1, node2))