class Node:
  def __init__(self,data,next=None):
      self.data=data
      self.next=next

class LinkedList:
  def __init__(self,head=None):
    self.head=head

  def is_empty(self):
    return self.head==None

  def insert_at_start(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node

  def show_list(self):
    if self.head==None:
      print("list is empty")
      return
    curr_node=self.head
    while curr_node:
      print(curr_node.data)
      curr_node=curr_node.next

  def insert_at_last(self,data):
    new_node=Node(data)
    if self.head==None:
      # print("list is empty")
      self.head=new_node
      return
    last_node=self.head
    while last_node.next:
      # print(last_node.data)
      last_node=last_node.next
    last_node.next=new_node    
    

  def insert_at(self,pos,data):
    if pos==1:
      self.insert_at_start(data)
      return
    else:
      prev_node=None
      pos_node=self.head
      for i in range(1,pos):
        prev_node=pos_node
        pos_node=pos_node.next
        if pos_node==None:
          print("this position does not exist")
          print("list has only length upto " ,i)
          return
        new_node=Node(data)
        new_node.next=pos_node
        prev_node.next=new_node
        return


newLL=LinkedList()
print(newLL.is_empty())
newLL.insert_at_start(4)
newLL.insert_at_start(5)
newLL.insert_at_start(6)
newLL.insert_at_start(7)
newLL.insert_at_last(9)
newLL.insert_at(1,69)
newLL.insert_at(2,999)
newLL.insert_at(8,69)
print(newLL.is_empty())
newLL.show_list()