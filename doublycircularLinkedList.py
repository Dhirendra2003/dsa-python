class Node:
    def __init__(self,data, next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DCll:
    def __init__(self,head=None):
        self.head=head

    def is_empty(self):
        return self.head==None

    def insert_at_start(self,data):
        n=Node(data)
        if(self.is_empty()):
            self.head=n
            n.next=n
            n.prev=n
            #print("if")
        elif(self.head==self.head.next):
            n.next = self.head
            n.prev = self.head
            self.head.next=n
            self.head.prev=n
            self.head=n
            #print("elif")
        else:
            n.next=self.head
            n.prev=self.head.prev
            self.head.prev.next=n
            self.head.prev=n
            self.head=n
            #print("else")

    def show_list(self):
        list_str="CDLL"
        curr_node=self.head
        #looped=False
        while curr_node:
            list_str=f"{list_str}<-->{curr_node.data}"
            curr_node=curr_node.next
            if(curr_node==self.head):
                break
        print(list_str)

    def search(self,data):
        if(self.is_empty()):

            return  "list is empty"
        curr_node=self.head

        while curr_node:
            if(curr_node.data==data):
                #print(curr_node.data)
                return curr_node
            curr_node=curr_node.next
            if(curr_node==self.head):
                break

    def insert_at_last(self,data):
        if(self.is_empty()):
            self.insert_at_start(data)
        elif(self.head.next==self.head):
            n = Node(data)
            n.next = self.head
            n.prev = self.head
            self.head.next=n
            self.head.prev = n
        else:
            n=Node(data)
            n.next = self.head
            n.prev = self.head.prev
            self.head.prev.next = n
            self.head.prev = n


    def insert_after(self,data,temp):
        data_node=self.search(temp)
        if(data_node==None):
            print("node not found!!")
            return
        if(data_node==self.head.prev):
            self.insert_at_last(data)
        else:
            n=Node(data,data_node.next,data_node)
            data_node.next.prev=n
            data_node.next=n

    def delete_start(self):
        if(self.is_empty()):
            return
        elif (self.head==self.head.next):
            self.head=None
        else:
            self.head.next.prev=self.head.prev
            self.head.prev.next=self.head.next
            self.head=self.head.next

    def delete_data(self,data):
        data_node=self.search(data)
        if data_node is None:
            print('node not found')
            return
        elif self.head.data==data:
            self.delete_start()
        else:
            data_node.next.prev=data_node.prev
            data_node.prev.next=data_node.next

    def __iter__(self):
        return  CLLIterator(self.head)
class CLLIterator():
    def __init__(self,starter):
        self.current=starter
        self.head=starter
        self.to_last=0
    def __iter__(self):
        return self
    def __next__(self):

        if self.current==None or self.to_last==1:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        if (self.current == self.head):
            if(self.to_last==0):
                self.to_last=1
                return data
            raise StopIteration
        return data


cdll1=DCll()
cdll1.delete_start()
cdll1.show_list()
cdll1.insert_at_last(111)
cdll1.show_list()
cdll1.delete_start()
cdll1.show_list()
cdll1.insert_at_last(112)
cdll1.show_list()
cdll1.insert_at_start(5)
cdll1.show_list()
cdll1.insert_at_start(12)
cdll1.show_list()
cdll1.insert_at_start(4)
cdll1.show_list()
cdll1.insert_at_start(77)
cdll1.show_list()
cdll1.search(77)
cdll1.insert_at_last(767)
cdll1.show_list()
cdll1.insert_after(666,12)
cdll1.show_list()
cdll1.insert_after(666,12312)
cdll1.show_list()
cdll1.delete_data(5)
cdll1.show_list()
cdll1.delete_data(77)
cdll1.show_list()
cdll1.delete_data(767)
cdll1.show_list()
strll=""
for i in cdll1:
    strll=f"{strll}=>{i}"
print(strll)
