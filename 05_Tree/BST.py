class TreeNode:
  def __init__(self, key, value, left = None, right = None):
    self.key = key # 키(key)
    self.value = value # 값(value)
    self.left = left
    self.right = right
    
class BST:
  def __init__(self):
    self.root = None
    
  def search(self, key): # 탐색 연산
    return self._searchSubtree(self.root, key)
  
  def _searchSubtree(self, node, key):
    if node is None:
      return None
    elif key == node.key:
      return node.value
    elif key < node.key:
      return self._searchSubtree(node.left, key)
    else:
      return self._searchSubtree(node.right, key)
    
  def insert(self, key, value): # 삽입 연산
    self.root = self._insertSubtree(self.root, key, value)
    
  # 원소(key, value)의 노드를 삽입한 후 만들어진 이진탐색트리의 루트를 반환
  def _insertSubtree(self, node, key, value):
    if node == None:
      return TreeNode(key, value)
    elif key < node.key:
      node.left = self._insertSubtree(node.left, key, value)
    elif key > node.key:
      node.right = self._insertSubtree(node.right, key, value)
    else:
      pass
    return node
  
  # 최소키 노드 찾기
  def _minNode(self, node):
    if node.left == None:
      return node
    else:
      return self._minNode(node.left)
    
  def delete(self, key):
    self.root = self._deleteSubtree(self.root, key)
  
  # node가 루트인 이진탐색트리에서 key와 같은 키의 노드 삭제한 후 이진탐색트리의 루트 반환
  def _deleteSubtree(self, node, key):
    if node == None:
      return None
    if key < node.key: # 삭제할 키의 노드가 node의 왼쪽 서브트리인 경우
      node.left = self._deleteSubtree(node.left, key)
      return node
    elif key > node.key: # 삭제할 키의 노드가 node의 오른쪽 서브트리인 경우
      node.right = self._deleteSubtree(node.right, key)
      return node
    else: # node가 삭제할 키의 노드인 경우
      if node.right == None: # node의 오른쪽 자식노드가 없을 경우
        return node.left
      if node.left == None: # node의 왼쪽 자식노드가 없을 경우
        return node.right
      
      # 두 개의 자식을 가진 노드 삭제
      # 삭제할 위치에 오른쪽 서브트리의 가장 작은 노드가 들엉가면 이진탐색트리 조건을 계속 만족
      rightMinNode = self._minNode(node.right) # node의 오른쪽 서브트리에서 최소키의 노드를 찾음
      node.key = rightMinNode.key # node의 오른쪽 서브트리에서 최소키의 노드를 복사 node에 복사
      node.value = rightMinNode.value # key, value 둘 다 복사해서 옮김
      node.right = self._deleteSubtree(node.right, rightMinNode.key) # node의 오른쪽 서브트리에서 최소키의 노드를 삭제
      return node