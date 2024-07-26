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