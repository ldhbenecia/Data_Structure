# 반복 이용
def binarySearch(a, key): # 반복
  left = 0 # a = [ ....]
  right = len(a) - 1
  
  while left <= right:
    mid = (left + right) // 2
    print(a[mid])
    if key == a[mid]:
      return True # return mid
    elif key < a[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return False # return -1


# 재귀 이용 (이것을 주로 사용)

def binarySearch1(a, key, left, right):
  if left > right:
    return False
  else:
    mid = (left + right) // 2
    if key == a[mid]: # 탐색 성공
      return True
    elif key < a[mid]:
      return binarySearch1(a, key, left, mid-1)
    else:
      return binarySearch1(a, key, mid+1, right)