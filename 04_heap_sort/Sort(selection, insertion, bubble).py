# 선택 정렬
# 시간 복잡도 = O(n^2)

arr = []

def selection_sort(arr):
  n = len(arr)
  
  for i in range(n-1):
    least = i
    for j in range(i+1, n):
      if (arr[j] < arr[least]):
        least = j
    arr[i], arr[least] = arr[least], arr[i]
    

# 삽입 정렬
# 시간 복잡도 = 최선의 경우 O(n) - 이미 정렬되어 있는 경우: 비교 n-1번
# 시간 복잡도 = O(n^2) - 역순으로 정렬되어 있는 경우

# 최적화 된 삽입정렬 코드
def insertion_sort(arr): # swap 작업 없이 단순히 값들을 shift
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
    
# 일반적인 삽입 정렬 코드
def insertion_sort2(arr):
  n = len(arr)
  for end in range(1, n):
    for i in range(end, 0, -1):
      if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        
        
# 버블 정렬
# 시간 복잡도 = O(n^2)

# 최적화 -> 이전 패스에서 swap이 한 번도 일어나지 않았다면
# 정렬되지 않는 값이 하나도 없었다고 간주. 이럴 경우, 이후 패스를 수행하지 않아도 됨
def bubble_sort(arr):
  n = len(arr)
  
  for i in range(n-1, 0, -1):
    bChanged = False
    for j in range(i):
      if (arr[j] > arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        bChanged = True
  
    if not bChanged: break;
    
  
# 일반적인 버블 정렬 코드
def bubble_sort2(arr):
  n = len(arr)
  
  for i in range(n-1 , 0, -1):
    for j in range(i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]