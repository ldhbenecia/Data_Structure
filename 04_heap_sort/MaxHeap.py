# 최대 힙의 구현

class MaxHeap:
  def __init__(self):
    self.heap = []
  
  def print(self):
    print(self.heap)
    
  def insert(self, value):
    self.heap.append(value)
    i = len(self.heap) - 1
    while (i != 0 and value > self.heap[(i-1)//2]): # 루트노드가 아니고 입력된 값이 부모노드보다 클 경우
      self.heap[i] = self.heap[(i-1)//2] # 부모노드의 값을 내림, 제일 밑 자리 값 = 부모노드
      i = (i-1)//2 # i를 부모노드 자리로 설정
    self.heap[i] = value # 부모노드 자리에 입력된 value 값이 삽입
    # 이와 같은 동작 반복 / 입력된 값이 부모노드보다 작을 경우 제일 밑에 추가되는 것이므로
    
  def delete(self): # down heap
    n = len(self.heap)
    if n == 0: # heap이 비어있으면 
      return None
    current = 0
    maxValue = self.heap[0] # 최대값 저장
    value = self.heap[n-1] # 마지막 원소를 value에 저장
    self.heap.pop() # 마지막 원소 삭제
    n = n - 1 # 원소 하나가 삭제되어 n을 1 줄임
    while (2 * current + 1 < n): # current가 leaf가 아니면
      leftChild = 2 * current + 1
      rightChild = leftChild + 1
      # 두 자식 노드 중 큰 값의 노드를 largerChild
      if rightChild < n and self.heap[rightChild] > self.heap[leftChild]:
        largerChild = rightChild
      else:
        largerChild = leftChild
        
      if value < self.heap[largerChild]: # largerChild의 값이 크면
        self.heap[current] = self.heap[largerChild]
        current = largerChild # current를 largerChild로 내림
      else:
        break
    
    self.heap[current] = value
    return maxValue