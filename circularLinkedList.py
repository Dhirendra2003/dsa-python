class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class CircLL:
    def __init__(self,last =None):
        self.last=last

    def is_empty(self):
        return self.last==None

    def inset_at_start(self,data):
        n = Node(data)
        if(self.is_empty()):

            self.last=n
            n.next=n
        else:
            n.next=self.last.next
            self.last.next=n
    def show_list(self):
        list_str="CLL"
        curr_node=self.last.next
        while curr_node:
            list_str=f"{list_str}-->{curr_node.data}"
            curr_node=curr_node.next
            if(curr_node==self.last.next):
                break
        print(list_str)
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            self.last=n
            n.next=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search_node(self,data):
        #counter=1
        if self.is_empty():
            return None
        else:
            temp = self.last.next
            while temp :
                if(temp.data==data):
                    #return counter
                    return temp
                temp=temp.next
                #counter+=1
                if(temp==self.last.next):
                    return
    def insert_after(self,temp,data):
        pos_node=self.search_node(temp)
        if(pos_node==None):
            print("the node given is not found in the list")
            return
        else:
            n1 =Node(data,pos_node.next)
            pos_node.next=n1

    def delete_first(self):
        if(self.is_empty()):
            return
        elif(self.last.next==self.last):
            self.last=None
            return
        else:
            self.last.next=self.last.next.next

    def delete_last(self):
        if (self.is_empty()):
            return
        elif (self.last.next == self.last):
            self.last = None
            return
        else:
            second_last=self.last.next
            while second_last :
                if (second_last.next == self.last):
                    break
                second_last=second_last.next

            #print(second_last.data)
            second_last.next=self.last.next
            self.last=second_last

    def delete_data(self,data):
        if(self.last.next):
            if(self.last.next==self.last):
                self.last=None
                return
            elif(self.last.next.data==data):
                self.delete_first()
            else:
                temp=self.last.next

                while temp!=self.last:
                    if(temp.next==self.last):
                        self.delete_last()
                        break
                    if(temp.next.data==data):
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return  CLLIterator(self.last.next,self.last)
class CLLIterator():
    def __init__(self,starter,last):
        self.current=starter
        self.last=last
        self.to_last=0
    def __iter__(self):
        return self
    def __next__(self):

        if self.current==None or self.to_last==1:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        if (self.current == self.last.next):
            if(self.to_last==0):
                self.to_last=1
                return data
            raise StopIteration
        return data

strll=""
cll1=CircLL()
cll1.inset_at_start(5)
cll1.show_list()
cll1.inset_at_start(8)
cll1.show_list()
cll1.insert_at_last(89)
cll1.show_list()
cll1.insert_at_last(6)
cll1.show_list()
cll1.inset_at_start(4)
cll1.show_list()
cll1.inset_at_start(3)
cll1.show_list()
print(cll1.search_node(3))
cll1.insert_after(5,666)
cll1.show_list()
cll1.insert_after(666,6661)
cll1.show_list()
cll1.delete_first()
cll1.show_list()
cll1.delete_last()
cll1.show_list()
cll1.delete_last()
cll1.show_list()
cll1.delete_last()
cll1.show_list()
for i in cll1:
    strll=f"{strll}=>{i}"
print(strll)
cll1.delete_data(666)
cll1.show_list()
cll1.delete_data(8)
cll1.show_list()




