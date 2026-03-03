# In this we will make the queue class to make it more encapsulating and effective

class Queue:
    def __init__(self):
        self.queue = []
    
    # Enqueue
    def enqueue(self,element):
        self.queue.append(element)
    
    # Dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
            
    # Peek
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    # isEmpty 
    def isEmpty(self):
        return not bool(self.queue)
    #Clear the queue
    def clear(self):
        return self.queue.clear()

    # Size

    def size(self):
        return len(self.queue)

# Creating a Queue
queue = Queue()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print(f"The Queue: {queue.queue}") # Prints the queue
print(f'Dequeue element: {queue.dequeue()}')
print(f'The queue after removing the top element: {queue.queue}')
print(f'The top element of the queue: {queue.peek()}')
print(f'isEmpty: {queue.isEmpty()}')
print(f'Size of the queue: {queue.size()}')
print(f'Clear the queue: {queue.clear()}') # this will clear the queue

queue.enqueue(1)
print(queue.queue)