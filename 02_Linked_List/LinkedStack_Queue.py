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
  