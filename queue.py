# In this we will be looking at queues
# Queue is a linear data structure that follows FIFO(First In First Out)

# Set of operations that we can perform in queue
# 1. Enqueue - To add the item in the queue
# 2. Dequeue -  To remove and return the first(front) element of the queue
# 3. Peek - To return the front(first) element of the queue
# 4. isEmpty - To check if queue is empty or not
# 5. Size - to check the size of the queue 

queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append("C")
print("Queue: ",queue)

# Dequeue
queue.pop(0) #Removes the first element of the queue
print(f'Queue after removing the first element: {queue}')

# Peek
print(f'Top element of the queue: {queue[0]}')

# isEmpty 
print(f'isEmpty: {not bool(queue)}')

#Size
print(f'Size of the queue: {len(queue)}')