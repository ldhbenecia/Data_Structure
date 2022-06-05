# 개방 주소 방식 (Open Addressing)
# 선형조사 (Linear Probing)

class Dictionary:
  def __init__(self, size):
    self.M = size
    self.keyList = [None] * size # 해시테이블
    self.valueList = [None] * size # key 관련 데이터 저장
  
  def hashFunc(self, key):
    return key % self.M # 나눗셈 함수
  
  def put(self, key, value): # 삽입 : Linear Probing
    initialPos = self.hashFunc(key) # 초기 위치
    i = initialPos
    while True:
      if self.keyList[i] == None: # 삽입 위치 발견
        self.keyList[i] = key # key를 해시테이블에 저장
        self.valueList[i] = value # key 관련 데이터 저장
        return
      if self.keyList[i] == key: # 이미 key가 존재하면
        self.valueList[i] = value # 데이터만 갱신
        return
      i = (i+1) % self.M # i의 다음 위치
      if i == initialPos:
        return
      
  def get(self, key): # 검색 (탐색)
    initialPos = self.hashFunc(key)
    i = initialPos
    while self.keyList[i] != None: # keyList[i]가 비어있지 않으면
      if self.keyList[i] == key:
        return self.valueList[i] # 탐색 성공
      i = (i+1) % self.M
      if i == initialPos:
        return