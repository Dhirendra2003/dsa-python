class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def is_empty(self):
        return self.front==None

    def enqueue(self,data):
        n=Node(data)
        if(self.is_empty()):
            self.front=n
            self.rear=n
        else:
            self.rear.next=n
            self.rear=n

    def dequeue(self):

        if not(self.is_empty()):
            node=self.front
            self.front=self.front.next
            if(self.is_empty()):
                self.rear=None

            return node

    def print_list(self):
        curr_node=self.front
        list_str="Q"
        while curr_node:
            list_str=f"{list_str}==>{curr_node.data}"
            curr_node=curr_node.next
        print(list_str)

q1=Queue()
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1.print_list()
print(q1.dequeue().data)
print(q1.dequeue().data)
print(q1.dequeue().data)
print(q1.dequeue().data)
print(q1.dequeue().data)
