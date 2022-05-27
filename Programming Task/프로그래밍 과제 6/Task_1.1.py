class Student:
  def __init__(self, st_no, name, dept, grade, score = None):
    self.st_no = st_no # 학번
    self.name = name # 이름
    self.dept = dept # 학과
    self.grade = grade # 학년
    self.score = score # 성적
    
class Node:
  def __init__(self, key, value, left = None, right = None):
    self.key = key # 키
    self.value = value # 값
    self.left = left
    self.right = right
    
    
class Course: # 수업
  def __init__(self):
    self.root = None
    self.st_no_list = [] # 학번 저장 리스트 (에러처리 용)
    self.st_cnt = 0 # 학생 수 카운트 
    self.dic2 = {} # 학번 성적 짝 지어서 저장
    self.dept_cnt = {} # 학과별 학생수 기록
    
  def search(self, key):
    return self._searchSubtree(self.root, key)
  def _searchSubtree(self, node, key):
    if node is None:
      return None
    elif key == node.key:
      return node.value
    elif key < node.key:
      return self._searchSubtree(node.left, key)
    else:
      return self._searchSubtree(node.right, key)
  
  def insert(self, key, value):
    self.root = self._insertSubtree(self.root, key, value)
  def _insertSubtree(self, node, key, value): 
    if node == None:        
      #노드 반환 전 그에 대응되는 학과 카운트 + 1
      if value.dept in self.dept_cnt: # 입력된 학과가 학과와 같다면
        self.dept_cnt[value.dept] += 1
      else: # 아니라면
        self.dept_cnt[value.dept] = 1
      return Node(key, value)
    elif key < node.key:              # 왼쪽 부트리에 노드를 삽입 
      node.left = self._insertSubtree(node.left, key, value)
    elif key > node.key:              # 오른쪽 부트리에 노드를 삽입
      node.right = self._insertSubtree(node.right, key, value)
    else:
      pass
    return node
  
  def _minNode(self, node):
    if node.left == None:
      return node
    else:
      return self._minNode(node.left)
  
  def delete(self, key, st_no_list):
    if key not in st_no_list: # 에러처리
      return False
    else:
      node = self.search(key) # 삭제할 학생의 노드 값 저장
      self.dept_cnt[node.dept] -= 1 # 학생 수 - 1
      self.root = self._deleteSubtree(self.root, key)
      return True
    
  # node가 루트인 이진탐색트리에서 key와 같은 키의 노드 삭제한 후 이진탐색트리의 루트 반환
  def _deleteSubtree(self, node, key):
    if node == None:
      return None
    if key < node.key: # 삭제할 키의 노드가 node의 왼쪽 서브트리인 경우
      node.left = self._deleteSubtree(node.left, key)
      return node
    elif key > node.key: # 삭제할 키의 노드가 node의 오른쪽 서브트리인 경우
      node.right = self._deleteSubtree(node.right, key)
      return node
    else: # node가 삭제할 키의 노드인 경우
      # 삭제하려는 노드가 단말노드일경우, 삭제하려는 노드의 자식노드가 하나일 경우
      if node.right == None: # node의 오른쪽 자식노드가 없을 경우
        return node.left
      elif node.left == None: # node의 왼쪽 자식노드가 없을 경우
        return node.right
      else:
      # 삭제하려는 노드의 자식노드가 두개일 경우
        rightMinNode = self._minNode(node.right) # node 오른쪽 부트리에서 최소키의 노드 찾음
        node.key = rightMinNode.key # node 오른쪽 부트리에서 최소키의 노드를 복사 node에 복사
        node.value = rightMinNode.value
        node.right = self._deleteSubtree(node.right, rightMinNode.key) # node의 오른쪽 서브트리에서 최소키의 노드 삭제
        return node

  def inorder(self): # 정보를 출력하는 inorder
    self._subtreeInorder(self.root)
  def _subtreeInorder(self, node):
    if node is not None:
      self._subtreeInorder(node.left)
      if node.value.score is None: # 학생 성적이 아직 주어지지 않은 상태라면 점수 출력 X
        print(node.value.st_no, node.value.name, node.value.dept, node.value.grade) # key값이 아닌 value값에 해당하는 값 출력 (key값이 학번이므로 출력 x)
      else: # 학생 성적이 주어진 상태라면 점수까지 출력
        print(node.value.st_no, node.value.name, node.value.dept, node.value.grade, node.value.score) # key값이 아닌 value값에 해당하는 값 출력 (key값이 학번이므로 출력 x)
      self._subtreeInorder(node.right)
      
  def dept_inorder(self, dept): # 같은 학과만 출력하는 inorder
    self._dept_subtreeInorder(self.root, dept)
  def _dept_subtreeInorder(self, node, dept):
    if node is not None:
      self._dept_subtreeInorder(node.left, dept)
      if (node.value.score is None) and (node.value.dept == dept): #성적 없고 학과 일치
        print(node.value.st_no, node.value.name, node.value.dept, node.value.grade) # 학생 성적이 아직 주어지지 않은 상태
      elif (node.value.score is not None) and (node.value.dept == dept): #성적 있고 학과 일치
        print(node.value.st_no, node.value.name, node.value.dept, node.value.grade, node.value.score) # 학생 성적이 주어진 상태
      self._dept_subtreeInorder(node.right, dept)
    
    
  def register(self, st_no, name, dept, grade): # 수강 신청, N
    st = Student(st_no, name, dept, grade) # class Student의 객체 가져오기
    self.insert(st_no, st) # key값에 학번, value 값에 Student의 st_no, name, dept, grade 객체 가져와서 넣기

    if st_no in self.st_no_list:
      print("error1") # 에러처리를 하기위해 그 학번의 학생의 학생이 이미 있다면 error1
    else:
      self.st_no_list.append(st_no) # 입력된 학번의 학생이 없다면 리스트에 저장
      self.st_cnt += 1 # 학생 수 카운트 += 1
      
  def score(self, st_no, score): # 학번 성적, G
    see = self.search(st_no) # 이진탐색트리 search 함수를 사용하여 입력된 학번 st_no에 해당하는 노드 찾기
    if st_no not in self.st_no_list:
        print("error2") # 에러처리, 성적을 입력하려했는데 그 학생이 등록이 안된 상태일 경우 error2
    else:
      see.score = score # 이진탐색트리에 None 값인 score 지정
      self.dic2[st_no] = score # 학번에 맞는 성적 저장
    
  def withdraw(self, st_no): # 수강 취소, C
    r_value = self.delete(st_no, self.st_no_list) # key값인 입력된 학번 delete
    if r_value == False:
      print("error2")
    elif r_value == True:
      self.st_no_list.remove(st_no)
      self.st_cnt -= 1 # 학생 수 카운트 -= 1
    
  def print_st_no(self, st_no): # R (학번 이름 학과 학년 성적 출력)
    see = self.search(st_no) # 입력된 학번에 해당하는 키밸류 값을 search함수로 찾기
    if st_no not in self.st_no_list: 
      print("error2") # 에러처리, R로 학생을 불렀는데 등록이 안된 경우 error2
    elif st_no not in self.dic2: # 딕셔너리를 만들어놓았는데 이 딕셔너리의 key값에 입력된 학번이 없다면
      print(see.st_no, see.name, see.dept, see.grade) # 성적이 주어지지 않은 학생이므로 성적은 출력 X
    else: #그게 아니라면
      print(see.st_no, see.name, see.dept, see.grade, see.score) # 성적이 주어진 경우이므로 성적까지 출력

  def dept_student(self, dept): # D (숫자 출력하고 학번 이름 학과 학년 출력)
    if dept in self.dept_cnt.keys(): # 입력된 학과가 학과 카운트 딕셔너리에 있다면
      print(self.dept_cnt[dept]) # 주어진 학과의 수강 학생 수 출력
      self.dept_inorder(dept) # 학과 전용 함수 출력
    else:
      print(0) # 등록되지 않은 학과일 경우 0
    
  def sorted_print(self): # P (숫자 출력하고 학번 이름 학과 학년 성적 출력)
    print(self.st_cnt) # 수강 학생 수 출력
    self.inorder() # 학생 정보 오름차순 출력

student_list = Course()

while True:
  command = input().split()

  if command[0] == 'N': # register
    student_list.register(command[1],command[2],command[3],command[4])
  elif command[0] == 'G': # score
    student_list.score(command[1],command[2])
  elif command[0] == 'C': # withdraw
    student_list.withdraw(command[1])
  elif command[0] == 'R': # print_st_no
    student_list.print_st_no(command[1])
  elif command[0] == 'D': # dept_student
    student_list.dept_student(command[1])
  elif command[0] == 'P': # sorted_print
    student_list.sorted_print()
  elif command[0] == 'Q':
    break