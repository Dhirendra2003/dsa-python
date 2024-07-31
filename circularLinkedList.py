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



