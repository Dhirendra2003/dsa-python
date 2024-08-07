class Node:
    def __init__(self, data, priority, next=None):
        self.priority = priority
        self.data = data
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.head = None
        self._item_count = 0

    def is_empty(self):
        return self.head is None

    def push(self, data, priority):
        n = Node(data, priority)
        if self.is_empty() or priority < self.head.priority:
            n.next = self.head
            self.head = n
        else:
            temp = self.head
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self._item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("queue empty")
        else:
            data = self.head.data
            self.head = self.head.next
            self._item_count -= 1
            return data

    def size(self):
        return self._item_count

    def print_queue(self):
        temp = self.head
        while temp:
            print(f"({temp.data}, {temp.priority})", end=" -> ")
            temp = temp.next
        print("None")

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
pq.print_queue()
# Expected output: (task4, 0) -> (task2, 1) -> (task3, 2) -> (task5, 2) -> (task1, 3) -> None

# Test size function
print("Size of the priority queue:", pq.size())  # Expected output: 5

# Test pop function
print("Popped element:", pq.pop())  # Expected output: 'task4'
print("Popped element:", pq.pop())  # Expected output: 'task2'
pq.print_queue()
# Expected output: (task3, 2) -> (task5, 2) -> (task1, 3) -> None

# Test pop function again
print("Popped element:", pq.pop())  # Expected output: 'task3'
print("Popped element:", pq.pop())  # Expected output: 'task5'
print("Popped element:", pq.pop())  # Expected output: 'task1'

# Test is_empty function after popping all elements
print("Is the priority queue empty?", pq.is_empty())  # Expected output: True

# Uncommenting below line will raise an IndexError as the queue will be empty
# print("Popped element:", pq.pop())
