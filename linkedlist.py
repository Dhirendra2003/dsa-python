print("working")
# making node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self,head=None):
        self.head=head
    def is_empty(self):
        return self.head==None
    def insert_at_start(self,data):

        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def show_list(self):
        current_node=self.head
        list_str="LL"
        while current_node:
            #print(current_node.data)
            list_str=(f"{list_str}-->{current_node.data}")
            current_node=current_node.next
        print(list_str)
    def search(self,data):
        current_node = self.head
        position =1
        while current_node:
            if current_node.data==data:
                return f"data {data} is present at position {position}"
            current_node = current_node.next
            position +=1
        return "given data not found"

    def insert_at_last(self,data):
        last_node=self.head
        #print(last_node.data)
        #traverse to last
        while last_node.next:
            last_node = last_node.next
        #print(last_node.data)
        last_node.next=Node(data)

    def remove_last_node(self):
        if self.head is None:
            print("No elements present to remove")
            return

        if self.head.next is None:
            # The list has only one node
            self.head = None
            return


        last_node = self.head
        while last_node.next.next:
            last_node = last_node.next
        #print(last_node.data)
        last_node.next=None

    def insert_at(self,data,pos):
        if pos==1:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            return

        prev_node=None
        pos_node = self.head
        lenght=0
        for i in range(1,pos):
            if(pos_node.next==None):
                if (lenght+2 == pos):
                    self.insert_at_last(data)
                    lenght+=1
                    return
                else:
                    print(f"list does not have {pos} elements")
                    print("legth is",lenght)
                return
            prev_node=pos_node
            pos_node = pos_node.next
            lenght+=1
        #print(pos_node.data)
        new_node=Node(data)
        new_node.next=pos_node
        prev_node.next=new_node

    def rev_list(self):
        if(self.head == None) or (self.head.next == None):
            return
        else:
            temp_node=self.head
            prev_node=None
            next_node=self.head.next
            #self.head.next=None
            while temp_node is not None:
                next_node = temp_node.next
                temp_node.next=prev_node
                prev_node=temp_node
                temp_node = next_node

            self.head = prev_node
    def __iter__(self):
        return LLiterator(self.head)
class LLiterator:
    def __init__(self,head):
        self.current=head
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data


ll1=Sll(head=None)
ll1.insert_at_start(2)
ll1.insert_at_start(5)
ll1.insert_at_start(8)
ll1.insert_at_start(7)
ll1.insert_at_start(3)
ll1.insert_at_start(90)
ll1.show_list()
print(ll1.search(5))
print(ll1.search(1))
print(ll1.search(90))
ll1.insert_at_last(1)
ll1.show_list()
ll1.remove_last_node()
ll1.show_list()

ll1.insert_at(69,3)
ll1.show_list()
ll1.insert_at(69,1)
ll1.show_list()
ll1.insert_at(101,9)
ll1.show_list()
ll1.insert_at(121,10)
ll1.show_list()
ll1.rev_list()
ll1.show_list()
for i in ll1:
    print(i)