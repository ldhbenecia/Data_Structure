class Student:
  def __init__(self, st_no, name):
    self.st_no = st_no # 학번
    self.name = name # 이름
    
class Course: # 수업
  def __init__(self):
    self.st_list = [] # 학생 이름 저장 리스트
    self.st_no_list = [] # 학번 저장 리스트
    self.dic1 = {} # 학번과 이름을 짝 지을 딕셔너리 생성
    
  def register(self, st_no, name): # 수강 신청, N
    if st_no in self.st_no_list: # 에러처리가 문제에서 주어지지 않았지만 pass로 처리
      pass
    else:
      self.st_no_list.append(st_no) # 학번 리스트에 저장
      self.st_list.append(name) # 이름 리스트에 저장
      
      self.dic1[st_no] = name # key: 학번, value: 이름 저장

  def withdraw(self, st_no): # 수강 취소, C
    if st_no not in self.st_no_list: # 에러처리
      pass
    else:
      idx = self.st_no_list.index(st_no) # 입력된 학번에 대한 인덱스 찾기
      self.st_no_list.remove(st_no) # 학번 저장 리스트에서 입력된 학번 삭제
      self.st_list.pop(idx) # 인덱스에 해당하는 학생 이름 삭제
      del self.dic1[st_no] # 주어진 key값 학번을 딕셔너리에서 삭제
    
  def print_st_no(self, st_no): # R
    idx = self.st_no_list.index(st_no) # 정보를 조회할 학생 학번 인덱스 찾기
    print(st_no, self.st_list[idx]) # 학번과 학생 이름 출력
    
  def sorted_print(self): # P
    d1 = sorted(self.dic1.items()) # 학번과 이름을 동시에 출력해야 하는데 짝지어야 하므로 딕셔너리를 오름차순으로 정렬
    
    print(len(self.st_list)) # 학생 수 출력
    for key, value in d1:
      print(key, value) # key: 학번, value: 이름 출력
    
student_list = Course()

while True:
  command = input().split()
  
  if command[0] == 'N': # register
    student_list.register(command[1],command[2])
    
  elif command[0] == 'C': # withdraw
    student_list.withdraw(command[1])
    
  elif command[0] == 'R': # print_st_no
    student_list.print_st_no(command[1])
    
  elif command[0] == 'P': # storted_print()
    student_list.sorted_print()
    
  elif command[0] == 'Q':
    break