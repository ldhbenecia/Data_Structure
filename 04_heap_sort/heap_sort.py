# 1 : 리스트를 최대힙으로 만듦
# 2 : 최대힙을 정렬된 리스트로 만듦

# down heap을 이용

def heapify(A, i, n): # rebuildHeap (혹은 downHeap)라고도 함
  # A: 완전이진트리를 나타내는 배열
  # i: 배열 인덱스 (노드 번호)
  # n: 정렬할 원소들 개수 (완전이진트리 크기)
  # 루트가 i인 서브트리가 완전이진트리이고, 노드 i의 leftsubtree와 rightsubtree가 모두 힙일 때, 루트가 i인 서브트리를 힙으로 만듦
  
  if n == 0: # heap이 비어있으면 
    return None
  current = i
  value = A[i] # 노드 i의 값을 value에 저장
  while (2 * current + 1 < n): # current가 leaf가 아니면
    leftChild = 2 * current + 1
    rightChild = leftChild + 1
    # 두 자식 노드 중 큰 값의 노드를 largerChild
    if rightChild < n and A[rightChild] > A[leftChild]:
      largerChild = rightChild
    else:
      largerChild = leftChild
        
    if value < A[largerChild]: # largerChild의 값이 크면
      A[current] = A[largerChild]
      current = largerChild # current를 largerChild로 내림
    else:
      break
    A[current] = value
    
def makeHeap(A):
  n = len(A)
  for i in range(n//2-1, -1, -1):
    heapify(A, i, n)
    
# 힙 정렬
def heapsort(A):
  n = len(A)
  makeHeap(A) # 단계 1
  
  # 단계 2
  for last in range(n-1, 0, -1):
    A[last], A[0] = A[0], A[last]
    heapify(A, 0, last)
  
  