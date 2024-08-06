class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DequeDll:
    def __init__(self):
        self.rear=None
        self.front=None

    def is_empty(self):
        return self.front==None

    def insert_at_end(self,data):
        n=Node(data)
        if not self.is_empty():
            self.rear.next=n
            n.prev=self.rear
            self.rear=n
        else:
            self.rear=n
            self.front=n

    def insert_at_start(self,data):
        n=Node(data)
        if not self.is_empty():
            self.front.prev=n
            n.next=self.front
            self.front=n
        else:
            self.rear=n
            self.front=n

    def delete_at_end(self):
        if(self.is_empty()):
            return None
        elif (self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
            if (self.rear.prev==None):
                self.front=None

    def delete_at_start(self):
        if(self.is_empty()):
            return None
        elif (self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.front=self.front.next
            self.front.prev=None
            if(self.is_empty()):
                self.rear=None
    def get_front(self):
        return self.front.data

    def get_rear(self):
        return self.rear.data

    def print_queue(self):
        if not (self.is_empty()):
            list_str="deq"
            curr_node=self.front
            while curr_node:
                list_str=(f"{list_str}==>{curr_node.data}")
                curr_node=curr_node.next
            print(list_str)

# Create an object of DequeDll class
# deque = DequeDll()
# deque.insert_at_start(5)
# deque.insert_at_start(6)
# deque.print_queue()

# Create an object of DequeDll class
deque = DequeDll()

# Test is_empty function
print("Is the deque empty?", deque.is_empty())  # Expected output: True

# Test insert_at_start function
deque.insert_at_start(10)
deque.insert_at_start(20)
deque.insert_at_start(30)
deque.print_queue()  # Expected output: deq==>30==>20==>10

# Test insert_at_end function
deque.insert_at_end(40)
deque.insert_at_end(50)
deque.print_queue()  # Expected output: deq==>30==>20==>10==>40==>50

# Test get_front function
print("Front element:", deque.get_front())  # Expected output: 30

# Test get_rear function
print("Rear element:", deque.get_rear())  # Expected output: 50

# Test delete_at_start function
deque.delete_at_start()
deque.print_queue()  # Expected output: deq==>20==>10==>40==>50

# Test delete_at_end function
deque.delete_at_end()
deque.print_queue()  # Expected output: deq==>20==>10==>40

# Test the state of the deque
print("Is the deque empty?", deque.is_empty())  # Expected output: False

# Attempt to get front and rear elements again
print("Front element:", deque.get_front())  # Expected output: 20
print("Rear element:", deque.get_rear())  # Expected output: 40

# Clear the deque and test error handling
deque.delete_at_start()
deque.print_queue()
deque.delete_at_start()
deque.print_queue()
print("Front element 3rd:", deque.get_front())  # Expected output: 20
print("Rear element 3rd:", deque.get_rear())  # Expected output: 40
deque.delete_at_start()
deque.print_queue()  # Expected output: deq

print("Is the deque empty?", deque.is_empty())  # Expected output: True

# Uncommenting below lines will raise an error as the deque will be empty
# print(deque.get_front())
# print(deque.get_rear())
