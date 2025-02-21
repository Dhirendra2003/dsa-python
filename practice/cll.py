class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Cll:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last==None

    def insert_at_start(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node

    def insert_at_last(self,data):
        new_node=Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=new_node

    def print_list(self):
        if not self.is_empty():
            curr_node=self.last.next

            while curr_node!=self.last:
                print(curr_node.data,end="->")
                curr_node=curr_node.next
                
            print(curr_node.data , "-> None")
        else:
            print("list is empty")

    def delete_first(self):
        if self.is_empty():
            print("list is empty")
            return
        elif self.last==self.last.next:
            self.last=None
            return
        else:
            self.last.next=self.last.next.next

    def delete_last(self):
        if self.is_empty():
            print("list is empty")
            return
        elif self.last==self.last.next:
            self.last=None
            return
        else:
            curr_node=self.last.next
            while curr_node.next!=self.last:
                curr_node=curr_node.next
            # print(curr_node.data)
            self.last=curr_node
            curr_node.next=curr_node.next.next

    def delete_data(self,data):
        curr_node=self.last.next
        prev_node=self.last
        while curr_node.data!=data:
            prev_node=curr_node
            curr_node=curr_node.next
            if(curr_node==self.last.next):
                print( "node does not exist")
                return 
        else:
            print("node not found")        
        print(curr_node.data,"curr node data")  
        
        print(prev_node.data,"prev node data")    
        prev_node.next=curr_node.next
        if(self.last==curr_node):
            self.last=prev_node
        
    def __iter__(self):
        return CllIterator(self.last.next)
            
class CllIterator:
    def __init__(self,start):
        self.start=start
        self.current=start
        self.end_reached=0

    def __iter__(self):
        return self

    def __next__(self):
        if( self.current)==None or (self.current==self.start and self.end_reached):
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        if (self.current==self.start) :
            self.end_reached=1
        else:
            self.end_reached=1
        
        return data




cll1=Cll()
cll1.print_list()
cll1.insert_at_start(1)
cll1.print_list()
cll1.insert_at_start(2)
cll1.print_list()
cll1.insert_at_start(3)
cll1.insert_at_start(4)
cll1.print_list()
cll1.delete_last()#1
cll1.print_list()

cll1.delete_last()#2
cll1.print_list()

cll1.delete_last()#3
cll1.print_list()

cll1.insert_at_start(5)
cll1.insert_at_start(6)
cll1.insert_at_start(7)
for i in cll1:
    print (i ,"from loop")
    
cll1.delete_data(4)
print("deleted 4")
cll1.print_list()

cll1.delete_data(7)
print("deleted 7")
cll1.print_list()


