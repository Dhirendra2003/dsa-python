class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __repr__(self):
        return str(self.data)
class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        return  self.head is None

    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def print_list(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node=curr_node.next
        print("None")

    def search_by_value(self,value):
        curr_node=self.head
        while curr_node:
            if curr_node.data==value:
                return curr_node
            curr_node=curr_node.next

    def search_by_pos(self,pos):
        if pos < 1:  # Handle invalid positions
            print("Invalid position")
            return None
        curr_node=self.head
        if(pos==1):
            return self.head
        for i in range(pos-1):

            curr_node=curr_node.next
            if curr_node is None:
                print(f"The list has only {i+1} nodes")
                return
        return curr_node

    def insert_at(self,data,pos):
        if(pos<1):
            print("this position is not allowed")
            return
        if(pos==1):
            self.insert_at_start(data)
            return
        new_node = Node(data)
        prev_node=self.search_by_pos(pos-1)
        if prev_node is None :
            print ('node not found')
            return
        new_node.next=prev_node.next
        prev_node.next=new_node

    def delete_at(self,pos):
        if(pos<1):
            print("this position is not allowed")
            return
        if(pos==1):
            self.head=self.head.next
            return
        prev_node=self.search_by_pos(pos-1)
        pos_node=prev_node.next
        if prev_node is None :
            print ('node not found')
            return
        if pos_node is None:
            print ('position does not exist')
            return
        if pos_node.next is None:
            prev_node.next=None
            return
        prev_node.next=pos_node.next

    def reverse_list(self):
        prev_node=None
        pos_node=self.head
        next_node=self.head.next
        while pos_node:
            #print(pos_node.data)
            pos_node.next=prev_node
            prev_node=pos_node
            pos_node=next_node
            if(next_node):
                next_node=next_node.next
            else:
                self.head=prev_node
        self.print_list()
    def __iter__(self):
        return SLLIterable(self.head)

class SLLIterable:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data





ll1=LinkedList()
ll1.insert_at_start(2)
ll1.insert_at_start(3)
ll1.insert_at_start(4)
ll1.insert_at_start(5)
ll1.insert_at_start(5)
ll1.insert_at_start(5)
ll1.print_list()

ll1.insert_at(8,7)

ll1.print_list()

ll1.delete_at(1)

ll1.print_list()
ll1.reverse_list()

for i in ll1:
    print (i,"from loop")