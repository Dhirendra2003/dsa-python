class Queue:
    def __init__(self):
        self.item=[]

    def is_empty(self):
        return len(self.item)==0

    def enqueue(self,data):
        self.item.append(data)

    def dequeue(self):
        if not self.is_empty():
            deq_item=self.item[0]
            #self.item=self.item[1:]
            self.item.pop(0)
            return deq_item
        else:
            print("queue empty")
            return

    def get_front(self):
        if not self.is_empty():
            return self.item[0]

    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]

    def size(self):
        return len(self.item)

    def print_queue(self):
        print(self.item)

q1=Queue()
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
print(q1.get_front())
q1.enqueue(8)
print(q1.get_rear())
print(q1.size())
q1.print_queue()
print(q1.dequeue())
print(q1.dequeue())
q1.print_queue()
print(q1.dequeue())
print(q1.dequeue())
q1.print_queue()
print(q1.dequeue())

