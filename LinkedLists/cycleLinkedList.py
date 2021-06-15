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




def has_cycle(head):
    curr = head
    visited_nodes = []
    if head.next == head:
        return True    
    while curr:
        if curr.next in visited_nodes:
            return True
        visited_nodes.append(curr)
        curr = curr.next
    return False


iz = SingleList()
node1 = iz.insert_node(1)
node2 = iz.insert_node(1)
node3 = iz.insert_node(2)
node4 = iz.insert_node(4)
#node4.next = node1 uncomment this line to form a cycle

print(has_cycle(iz.head))
