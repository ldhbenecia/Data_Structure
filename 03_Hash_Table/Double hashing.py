# 개방 주소 방식 (Open Addressing)
# 이중해싱 (Double hashing)

class Dictionary:
  def __init__(self, size):
    self.M = size # 테이블 크기
    self.keyList = [None] * size # 해시테이블
    self.valueList = [None] * size # key 관련 데이터 저장
    self.N = 0 # 저장된 항목 수 
    
  def hashFunc(self, key):
    return key % self.M # 나눗셈 함수
  
  def put(self, key, value): # 삽입 : quadratic probing
    initialPos = self.hashFunc(key) # 초기 위치
    i = initialPos
    d = 7 - (key % 7) # 두 번째 해시 함수, 충돌이 일어났을 때 사용
    j = 0
    while True:
      if self.keyList[i] == None: # 삽입 위치 발견
        self.keyList[i] = key # key를 해시테이블에 저장
        self.valueList[i] = value # key 관련 데이터 저장
        self.N += 1
        return
      if self.keyList[i] == key: # 이미 key가 존재하면
        self.valueList[i] = value # 데이터만 갱신
        # 충돌이 일어나서 d를 한번 더 수행했는데 또 충돌이 일어날 시 계속 d 수행
        # 그러면서 j += 1
        return
      j += 1
      i = (initialPos + j*d) % self.M # i의 다음 위치
      if self.N > self.M: # 해시테이블이 full이면
        return
      
  def get(self, key): # 탐색 연산
    initialPos = self.hashFunc(key)
    i = initialPos
    d = 7 - (key % 7) # 두 번째 해시 함수
    j = 0
    while self.keyList[i] != None: # keyList[i]가 비어있지 않으면
      if self.keyList[i] == key:
        return self.valueList[i] # 탐색 성공
      j += 1
      i = (initialPos + j*d) % self.M # i의 다음 위치
    return None # 탐색 실패