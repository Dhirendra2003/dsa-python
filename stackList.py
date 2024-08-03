class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return  len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty() :
            return self.items.pop()
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('stack is empty')
    def size(self):
         return len(self.items)

st1=Stack()
st1.push(2)
print(st1.peek())
st1.push(4)
print(st1.peek())
st1.push(5)
print(st1.peek())
st1.pop()
print(st1.peek())
print(st1.size())