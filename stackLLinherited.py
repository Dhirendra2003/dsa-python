from linkedlist import Sll ,Node

class StackLL(Sll):
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        super().insert_at_start(data)
    def pop(self):
        popped_node=self.head
        super().delet_first()
        return popped_node
    def peek(self):
        return self.head


st1=StackLL()
print(st1.is_empty())
st1.push(5)
st1.push(6)
st1.push(7)
st1.push(8)
st1.push(9)
st1.show_list()
print(st1.pop().data)
st1.show_list()
print(st1.peek().data)
print(st1.pop().data)
st1.show_list()
print(st1.peek().data)
print(st1.peek().data)
print(st1.pop().data)
st1.show_list()
print(st1.pop().data)
st1.show_list()


