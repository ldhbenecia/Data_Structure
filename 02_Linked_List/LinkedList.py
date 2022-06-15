class Node:
  def __init__(self, element):
    self.data = element
    self.link = None

class LinkedList:
  def __init__(self):
    self.head = None
    
  def isEmpty(self):
    return self.head == None
  
  def size(self):
    count = 0
    node = self.head
    while node != None:
      count += 1
      node = node.link
    return count

  def getNode(self, pos):
    if pos < 0:
      return None
    node = self.head
    while pos > 0 and node != None:
      node = node.link
      pos -= 1
    return node
  
  def getEntry(self, pos):
    node = self.getNode(pos)
    if node == None:
      return None
    else:
      return node.data
    
  def insert(self, pos, elem):
    node = Node(elem)
    before = self.getNode(pos - 1) # before 노드 찾음
    if before == None: # 맨 앞에 삽입
      node.link = self.head
      self.head = node
    else: # 중간에 삽입
      node.link = before.link
      before.link = node
      
  def delete(self, pos):
    if pos < 0 or pos >= self.size():
      print("위치 error")
      return None
    before = self.getNode(pos-1)
    if before == None: # 시작 노드 삭제
      elem = self.head.data
      self.head = self.head.link
    else: # 중간에 있는 노드 삭제
      elem = before.link.data
      before.link = before.link.link
    return elem
  
  def printAll(self):
    node = self.head
    while node != None:
      print(node.data)
      node = node.link
      
  def find(self, item):
    pos = 0
    node = self.head
    while node is not None:
      if node.data == item:
        return pos
      else:
        pos += 1
        node = node.link
    return -1