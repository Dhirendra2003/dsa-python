class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoublyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        return self.head is None

    def insert_at_start(self,data):
        new_node=Node(data,self.head)
        # new_node.next=self.head
        if(self.head):
            new_node.prev=self.head.prev
            self.head.prev=new_node
        self.head=new_node

    def print_list(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node=curr_node.next
        print('None')

    def print_list_rev(self):
        curr_node = self.head.prev
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.prev
        return

    def search(self,data):
        cur_node=self.head
        while cur_node:
            if(cur_node.data==data):
                return  cur_node
            cur_node=cur_node.next
        else:
            print('Node not found')
            return

    def insert_after(self,value,data):
        pos_node=self.search(value)
        if(pos_node):
            new_node=Node(data)
            new_node.next=pos_node.next
            new_node.prev=pos_node
            if(pos_node.next):
                pos_node.next.prev=new_node
            pos_node.next=new_node

    def delete_start(self):
        if self.head is not None:
            self.head=self.head.next
            if(self.head):
                self.head.prev=None
    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
            return
        else:
            prev_node=self.head
            while prev_node.next.next:
                    prev_node=prev_node.next
            prev_node.next=None

    def delete_data(self,data):
        data_node=self.search(data)

        if data_node:
            prev_node=data_node.prev
            next_node=data_node.next
            if prev_node:
                prev_node.next=next_node
            if next_node:
                next_node.prev=prev_node
            if self.head==data_node:
                self.head=next_node
        else:
            print('Node not found with data ',data)
            return
    def __iter__(self):
        return DllIterator(self.head)

class DllIterator:
    def __init__(self,start):
        self.current=start

    def __iter__(self):
        return  self

    def __next__(self):
        if( self.current) is None:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data


dll1=DoublyLinkedList()
dll1.insert_at_start(1)
dll1.insert_at_start(2)
dll1.insert_at_start(3)
dll1.print_list()
# dll1.print_list_rev()
dll1.search(1)
dll1.insert_after(5,4)
dll1.print_list()
dll1.delete_start()
dll1.print_list()
dll1.delete_last()
dll1.print_list()
dll1.delete_last()
dll1.print_list()

dll1.insert_at_start(5)
dll1.insert_at_start(6)
dll1.insert_at_start(7)
dll1.insert_at_start(8)
dll1.insert_at_start(9)
dll1.insert_at_start(10)
dll1.print_list()
dll1.delete_last()
dll1.print_list()

dll1.delete_data(9)
dll1.print_list()

for i in dll1:
    print(i, end=" , ")