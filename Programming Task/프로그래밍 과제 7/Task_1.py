class Course: # 수업
  def __init__(self, size):
    # 학번을 key로 풀이할 예정 
    self.M = size # 테이블 크기
    self.keyList = [None] * size # 해시테이블
    self.valueList = [None] * size # key(학번) 관련 데이터 저장
    self.N = 0 # 저장된 항목 수 
    
    self.dic1 = {} # 학번과 이름을 짝 지을 딕셔너리 생성, P 전용
    self.st_no_list = [] # 학번 저장 리스트
    
  def hashFunc(self, key): # 나눗셈 함수
    return key % self.M
  
  def put(self, key, value): # 삽입연산
    initialPos = self.hashFunc(key) # 초기 위치
    i = initialPos
    d = 7 - (key % 7) # 2번째 해시함수
    j = 0
    
    while True:
      if self.keyList[i] == None: # 삽입 위치 발견
        self.keyList[i] = key # 학번을 해시 테이블에 저장
        self.valueList[i] = value # 학번 관련 데이터를 동일한 인덱스 하에 저장
        self.N += 1
        return
      if self.keyList[i] == key: # 이미 학번이 존재하면
        self.valueList[i] = value # 이름만 갱신
        return
      j += 1
      i = (initialPos + j*d) % self.M # i의 다음 위치
      if self.N > self.M: # 테이블이 Full이면
        break
      
  def get(self, key):
    initialPos = self.hashFunc(key)
    i = initialPos
    d = 7 - (key % 7) # 2번째 해시 함수
    j = 0
    while self.keyList[i] != None: # 비어있지 않으면
      if self.keyList[i] == key:
        return self.valueList[i] # 탐색 성공
      j += 1
      i = (initialPos + j*d) % self.M # i의 다음 위치
    return None # 탐색 실패
  
  def delete(self, key):
    initialPos = self.hashFunc(key)
    
    if self.keyList[initialPos] != 0:
      self.keyList[initialPos] = None
      return True
    else:
      return False


  def register(self, st_no, name): # 수강 신청, N   // key = 학번, value = 이름
    # 계속 문자열 관련 에러가 나와서 생각해보다가 key값이 지금 str 값으로 들어가고 있는 것을 파악 후
    # 입력받은 st_no를 int형으로 정수 변환하여 key 값으로 넣음. -> 에러 해결
    self.put(st_no, name) # 해시테이블에 삽입
    self.dic1[st_no] = name # key: 학번, value: 이름 저장, P를 구현하기 위함
    self.st_no_list.append(st_no) # 학번 리스트에 저장 # R 에러처리를 하기 위함
      
  def withdraw(self, st_no): # 수강 취소, C
    self.delete(st_no)
    self.st_no_list.remove(st_no) # 학번 저장 리스트에서 입력된 학번 삭제 # R 에러처리를 하기 위함
    del self.dic1[st_no] # 주어진 key값 학번을 딕셔너리에서 삭제 # P를 구현하기 위함
    
  def print_st_no(self, st_no): # R , 탐색
    if st_no not in self.st_no_list: # 해시테이블을 get으로 출력하면 C를 해도 R로 해당 학번을 재출력하면 학번은 나오는데 데이터는 None으로 나옴.
      pass # 그렇기 때문에 이미 삭제한 학번을 다시 입력했을 경우 pass로 처리
    else:
      print(st_no, self.get(st_no))

  def sorted_print(self): # P
    d1 = sorted(self.dic1.items()) # 학번과 이름을 동시에 출력해야 하는데 짝지어야 하므로 딕셔너리를 오름차순으로 정렬

    print(len(self.st_no_list)) # 학생 수 출력
    for key, value in d1:
      print(key, value) # key: 학번, value: 이름 출력
    
student_list = Course(13)

while True:
  command = input().split()
  
  if command[0] == 'N': # register
    student_list.register(int(command[1]),command[2])
    
  elif command[0] == 'C': # withdraw
    student_list.withdraw(int(command[1]))
    
  elif command[0] == 'R': # print_st_no
    student_list.print_st_no(int(command[1]))
    
  elif command[0] == 'P': # sorted_print()
    student_list.sorted_print()
    
  elif command[0] == 'Q':
    break