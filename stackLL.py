class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class StackLL:
    def __init__(self, first=None):
        self.first=first

    def is_empty(self):
        return self.first==None

    def push(self,data):
        n=Node(data)
        if self.is_empty():
            self.first=n
        else:
            n.next=self.first
            #if(self.first.next):
                #print("this",self.first.next.data)
            self.first=n

    def pop(self):
        if not self.is_empty():
            popped_node=self.first
            self.first=self.first.next
            return popped_node

    def peek(self):
        if not self.is_empty():
            return self.first

    def view_stack(self):
        print('all')
        if not self.is_empty():
            curr_node=self.first
            while curr_node:
                print(curr_node.data)
                curr_node=curr_node.next


st=StackLL()
print(st.is_empty())
st.push(5)
print(st.peek().data)
st.push(4)
st.push(7)
st.push(9)
print(st.pop().data)
#print(st.pop().data)
#print(st.pop().data)
st.view_stack()
