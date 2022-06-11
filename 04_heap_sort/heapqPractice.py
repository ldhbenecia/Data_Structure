# 파이썬 heapq 연습

# heapq.heappush(heap, item) # insert() 메소드와 동일
# heapq.heappop(heap) # delete_min() 메소드와 동일
# heapq.heapify(h) # 리스트 h를 힙으로 만듬

import heapq

heap = []

# 힙에 원소 추가
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap) # [1, 3, 7, 4]
# 힙의 형태로 나타남. 가장 작은 1이 인덱스 0에 위치 (루트 노드)
# 1이 제일 위, 1의 왼쪽 자식 노드 3 (1*2+1), 오른쪽 자식노드 4 (3+1), 3의 왼쪽 자식 노드 7 (3*2+1)
# O(logN) 시간 복잡도

# 힙에서 원소 삭제
print(heapq.heappop(heap)) # 1
print(heap) # [3, 4, 7]
# 가장 작은 1이 삭제되어 리턴

print(heapq.heappop(heap)) # 3
print(heap) # [4, 7]
# 가장 작은 3이 삭제되어 리턴
# O(logN) 시간 복잡도
# 가장 작은 값이 삭제 됨
# heappop()은 원소를 삭제 할때마다 이진트리의 재배치를 통해 새로운 최소 값을 인덱스 0에 배치 시킴

# 최소값 삭제하지 않고 얻기
print(heap[0]) # 4
# 리스트 인덱스 접근 방식과 동일


# 기존 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap) # [1, 3, 5, 4, 8, 7]
# O(N) 시간 복잡도