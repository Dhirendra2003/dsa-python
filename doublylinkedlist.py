class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class Dll:
    def __init__(self,head=None):
        self.head=head
    def is_empty(self):
        return self.head==None
    def insert_at_start(self,data):
        if self.head==None:
            self.head=Node(data)
            print("executed")
            return
        else:
            old_node=self.head
            self.head=Node(data,old_node,None)
            old_node.prev=self.head

    def insert_at_last(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        #print(last_node.data)
        last_node.next=Node(data,None,last_node)

    def show_list(self):
        list_str="DLL"
        curr_node=self.head
        while curr_node:
            list_str=f"{list_str}<-->{curr_node.data}"
            curr_node=curr_node.next
        print(list_str)

    def delete_at_pos(self,pos):
        if self.is_empty():
            return "list is empty"
        pos_prev=None
        pos_next=self.head.next
        pos_node=self.head
        pos_counter=1
        while pos_node.next and 0<pos_counter<pos:
            pos_prev=pos_node
            pos_node=pos_next
            pos_next=pos_next.next
            pos_counter+=1
        if(pos_counter<pos):
            return print(f"list does not have {pos} element")
        else:
            #if(pos_prev and pos_node and pos_next):
                #print(pos_prev.data, pos_node.data,pos_next.data)
            if (pos_prev):
                pos_prev.next=pos_next
            else:
                self.head=pos_next
            if(pos_next):
                pos_next.prev=pos_prev


dll1=Dll()
print(dll1.is_empty())
dll1.show_list()
dll1.insert_at_start(5)
dll1.insert_at_start(6)
dll1.insert_at_start(7)
dll1.insert_at_start(8)
dll1.insert_at_last(66)
dll1.show_list()
dll1.delete_at_pos(1)
dll1.show_list()
dll1.delete_at_pos(4)
dll1.show_list()
dll1.delete_at_pos(3)
dll1.delete_at_pos(2)
dll1.delete_at_pos(1)
dll1.show_list()