class PriorityQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
             index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("queue empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)

# Create an object of PriorityQueue class
pq = PriorityQueue()

# Test is_empty function
print("Is the priority queue empty?", pq.is_empty())  # Expected output: True

# Test push function
pq.push("task1", 3)
pq.push("task2", 1)
pq.push("task3", 2)
pq.push("task4", 0)
pq.push("task5", 2)

# Verify the internal state of the priority queue
print("Queue items after pushes:", pq.items)
# Expected output: [('task4', 0), ('task2', 1), ('task3', 2), ('task5', 2), ('task1', 3)]

# Test size function
print("Size of the priority queue:", pq.size())  # Expected output: 5

# Test pop function
print("Popped element:", pq.pop())  # Expected output: 'task4'
print("Popped element:", pq.pop())  # Expected output: 'task2'
print("Queue items after pops:", pq.items)
# Expected output: [('task3', 2), ('task5', 2), ('task1', 3)]

# Test pop function again
print("Popped element:", pq.pop())  # Expected output: 'task3'
print("Popped element:", pq.pop())  # Expected output: 'task5'
print("Popped element:", pq.pop())  # Expected output: 'task1'

# Test is_empty function after popping all elements
print("Is the priority queue empty?", pq.is_empty())  # Expected output: True

# Uncommenting below line will raise an IndexError as the queue will be empty
# print("Popped element:", pq.pop())

