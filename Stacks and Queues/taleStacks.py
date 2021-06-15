

class MyQueue(object):
    def __init__(self):
        self.inbound_stack = []
    
    def peek(self):
        return self.inbound_stack[0]
        
    def pop(self):
        curr = self.inbound_stack
        curr.pop(0)
        
    def put(self, value):
        self.inbound_stack.append(value)

    def iter(self):
        curr = self.inbound_stack
        for i in range(len(curr)):
            yield curr[i]



q = MyQueue()

q.put(1)
q.put(3)
q.put(2)
q.put(7)
q.put(11)





for i in q.iter():
    print(f'Elemento: {i}')