# 재귀를 이용한 이진 탐색 코드

def binarySearch(A, left, right, item):
  if left <= right:
    mid = (left + right) // 2
    if item == A[mid]:
      return mid
    elif item < A[mid]:
      return binarySearch(A, left, mid-1, item)
    else:
      return binarySearch(A, mid+1, right, item)
  else:
    return -1 # return False