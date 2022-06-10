from xml.etree.ElementTree import _ElementFactory


class Tnode:
  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
    
class BinaryTree:
  def __init__(self):
    self.root = None
    
  # 순회(traversal)
  
  def preorder(self):
    self._subtreePreorder(self.root)
    
  def _subtreePreorder(self, p): # 전위 순회 -> VLR
    if p is not None:
      print(p.data)
      self._subtreePreorder(p.left)
      self._subtreePreorder(p.right)
      
  def inorder(self):
    self._subtreeInorder(self.root)
    
  def _subtreeInorder(self, p): # 중위 순회 -> LVR
    if p is not None:
      self._subtreeInorder(p.left)
      print(p.data)
      self._subtreeInorder(p.right)
      
      
  def postorder(self):
    self._subtreePostorder(self.root)
    
  def _subtreePostorder(self, p): # 후위 순회 -> LRV
    if p is not None:
      self._subtreePostorder(p.left)
      self._subtreePostorder(p.right)
      print(p.data)
      
      
  # 높이 연산
  def height(self):
    return self._subtreeHeight(self.root)
  
  def _subtreeHeight(self, p):
    if p is None:
      return 0
    else:
      hleft = self._subtreeHeight(p.left)
      hright = self._subtreeHeight(p.right)
      return max(hleft, hright) + 1 # 1은 루트노드
    
    
  # 노드 개수
  def size(self):
    return self._subtreeSize(self.root)
  
  def _subtreeSize(self, p):
    if p is None:
      return 0
    else:
      return 1 + self._subtreeSize(p.left) + self._subtreeSize(p.right) # 왼쪽 + 오른쪽 서브트리 + 루트 노드
    
  # 단말 노드의 수
  def _subtreeCountLeaf(self, p):
    if p is None:
      return 0
    elif p.left is None and p.right is None:
      return 1 # 루트노드만 있는데 루트노드가 단말노드가 되므로
    else:
      return self._subtreeCountLeaf(p.left) + self._subtreeCountLeaf(p.right)