class Node:
  def __init__(self, element):
    self.data = element
    self.link = None
    
class LinkedStack:
  def __init__(self):
    self.top = None
  
  def isEmpty(self):
    return self.top == None
  
  def push(self, e):
    newNode = Node(e)
    newNode.link = self.top
    self.top = newNode
    
  def pop(self):
    if self.isEmpty():
      print("Stack is Empty")
      return 
    else:
      e = self.top.data
      self.top = self.top.link
      return e
    
class LinkedQueue:
  def __init__(self):
    self.front = self.rear = None
    
  def isEmpty(self):
    return self.front == None
  
  def enqueue(self, e):
    newNode = Node(e)
    if self.front == None:
      self.front = self.rear = newNode
    else:
      self.rear.link = newNode
      self.rear = newNode
      
  def dequeue(self):
    if self.isEmpty():
      print("Queue is Empty")
      return 
    e = self.front.data
    self.front = self.front.link
    if self.front == None:
      self.rear = None
    return e
  

q = LinkedQueue()
q.enqueue(10)
q.enqueue(30)
q.enqueue(20)
q.enqueue(15)
print(q.dequeue()) # 10, 제일 먼저 들어온게 10이므로 10부터 나감 (FIFO)
print(q.dequeue()) # 30
print(q.dequeue()) # 20


s = LinkedStack()
s.push(10)
s.push(30)
s.push(20)
s.push(15)
print(s.pop()) # 15, 가장 늦게 들어온게 15이므로 15부터 나감 (LIFO)
print(s.pop()) # 20
print(s.pop()) # 30