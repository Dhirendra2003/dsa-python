class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, data):
        self.append(data)

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('stack is empty')

    def size(self):
        return len(self)

st2 = Stack()
st2.push(2)
print(st2.peek())  # Output: 2
st2.push(4)
print(st2.peek())  # Output: 4
st2.push(5)
print(st2.peek())  # Output: 5
st2.pop()
print(st2.peek())  # Output: 4
print(st2.size())  # Output: 2
