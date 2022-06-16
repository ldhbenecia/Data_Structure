class DNode:
  def __init__(self, e):
    self.addr = e
    self.next = None
    self.back = None
    
class DLinkedList:
  def __init__(self):
    self.head = None
    
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
    
    
  def insert(self, pos, e):
    if pos < 0 or pos > self.size():
      return None
    else:
      location = self.getNode(pos)
      node = DNode(e)
      node.back = location.back
      node.next = location
      if location.back == None:
        self.head = node
      else:
        location.back.next = node
      location.back = node
    
  def delete(self, pos):
    if pos < 0 or pos > self.size():
      return None
    else:
      location = self.getNode(pos)
      e = location.data
      if location.back == None:
        self.head = location.next
        if location.next is not None:
          location.next.back = None
      else:
        location.back.next = location.next
        if location.next is not None:
          location.next.back = location.back
      return e