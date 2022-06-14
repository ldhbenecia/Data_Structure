class ArrayList:
  def __init__(self):
    self.items = []
  def size(self):
    return self.size() == 0
  def insert(self, pos, elem):
    if pos < 0 or pos > self.size():
      print("위치 error")
      return None
    else:
      self.items.insert(pos, elem)
  def delete(self, pos):
    if pos < 0 or pos >= self.size():
      print("위치 error")
      return None
    else:
      return self.items.pop(pos)
  def getEntry(self, pos):
    if pos < 0 or pos >= self.size():
      print("위치 error")
      return None
    else:
      return self.items[pos]
  def clear(self):
    self.items = []
  def replace(self, pos, elem):
    if pos < 0 or pos >= self.size():
      print("위치 error")
      return None
    else:
      return self.items[pos] == elem        

L = ArrayList()
print(L.size)
L.insert(0, 30) # [30]
L.insert(0, 25) # [25, 30]
L.insert(2, 50) # [25, 30, 50]

class LinkedList:
  def __init__(self):
    self.head = None
    
  def isEmpty(self):
    return self.head == None
  
  def clear(self):
    self.head = None
  
  # pos번째 노드 반환: getNode(pos)
  def getNode(self, pos):
    if pos < 0:
      return None
    node = self.head
    while pos > 0 and node != None:
      node = node.link
      pos -= 1
    return node