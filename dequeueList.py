class Dequeue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_at_front(self,data):
        self.items.insert(0,data)
    def insert_at_last(self,data):
        self.items.append(data)
    def delete_last(self):
        if not (self.is_empty()):
            self.items.pop()
        else:
            raise IndexError("empty queue")
    def delete_first(self):
        if not (self.is_empty()):
            self.items.pop(0)
        else:
            raise IndexError("empty queue")
    def get_front(self):
        if not (self.is_empty()):
            return self.items[0]
        else:
            raise IndexError("empty queue")
    def get_rear(self):
        if not (self.is_empty()):
            return self.items[-1]
        else:
            raise IndexError("empty queue")
    def print_queue(self):
        print(self.items)

# Create an object of Dequeue class
dq = Dequeue()

# Test is_empty function
print("Is the dequeue empty?", dq.is_empty())  # Expected output: True

# Test insert_at_front function
dq.insert_at_front(10)
dq.insert_at_front(20)
dq.insert_at_front(30)
dq.print_queue()  # Expected output: [30, 20, 10]

# Test insert_at_last function
dq.insert_at_last(40)
dq.insert_at_last(50)
dq.print_queue()  # Expected output: [30, 20, 10, 40, 50]

# Test get_front function
print("Front element:", dq.get_front())  # Expected output: 30

# Test get_rear function
print("Rear element:", dq.get_rear())  # Expected output: 50

# Test delete_first function
dq.delete_first()
dq.print_queue()  # Expected output: [20, 10, 40, 50]

# Test delete_last function
dq.delete_last()
dq.print_queue()  # Expected output: [20, 10, 40]

# Test the state of the queue
print("Is the dequeue empty?", dq.is_empty())  # Expected output: False

# Attempt to get front and rear elements again
print("Front element:", dq.get_front())  # Expected output: 20
print("Rear element:", dq.get_rear())  # Expected output: 40

# Clear the queue and test error handling
dq.delete_first()
dq.delete_first()
dq.delete_first()

# Uncommenting below lines will raise IndexError as the queue will be empty
dq.delete_first()
dq.delete_last()
dq.get_front()
dq.get_rear()