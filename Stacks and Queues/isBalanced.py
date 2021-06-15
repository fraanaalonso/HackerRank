class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.size+=1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size-=1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None  
         


def checkbrackets(statement):
    stack = Stack()
    last = ''
    for ch in statement:
        if ch in ('(', '{', '['):
            stack.push(ch)
        if ch in (')','}',']'):
            last = stack.pop()
        if last != '':
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
        else:
            continue
    if stack.size > 0:
        return 'NO'
    else:
        return 'YES'

m = "[{()}]("
s = checkbrackets(m)



print('{} {}'.format(m, s))