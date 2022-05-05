class ArrayList:
  def __init__(self):
    self.items = []
    self.historyitems = [] # self.items는 bakcward와 forward로 리스트 순서가 바뀌므로 go 명령어로만 저장된 값을 담기 위한 리스트 init
    self.b_ind = 0 # 오류 잡기 위한 인덱스 (backward)
    self.f_ind = 1 # 오류 잡기 위한 인덱스 (forward), 1인 이유는 초기 값 hufs 들어있으므로
  
  def go(self, addr): # 명령어 go, 주소값 추가해줌
    self.items.append(addr)
    
    # 먼저 나온 값 중복 제거를 위한 코드 (history)
    cnt = self.historyitems.count(addr) # 순정으로 입력된 리스트 값 개수
    if(cnt != 0): # 주소 개수 (여러개 나왔을 때)
      ind = self.historyitems.index(addr) # ind에 추가된 주소 index 저장
      del self.historyitems[ind] # 그 index에 위치하는 순정 리스트 요소 삭제
      self.historyitems.append(addr) # 먼저 나온 중복값 삭제된 이후에 저장 / 이러면 중복된 값 중 먼저 나온게 제거된 이후에 삽입됨.
    else: # 값 추가
      self.historyitems.append(addr)
      
    # forward 에러 검사 코드
    self.f_ind = len(self.items) # go가 나왔을 경우 앞으로 넘어갈 페이지가 존재하지 않으므로 이 코드를 작성함, 이 코드를 작성하면 forward 입력시 에러 발생
    
  def forward(self):
    if self.f_ind == (len(self.items)): # 만약 f_ind가 마지막 페이지일 경우
      #print("error") 출력 결과 없음
      pass
    else:
      self.items = self.items[1:] + self.items[:1] # 리스트 순서 바꿔주는 알고리즘
      print(self.items[-1])
      self.b_ind -= 1 # backward를 하다 forward가 나왔을 떄 값은 forward 상태로 바뀌는데 b_ind는 그대로이므로 -1 해줌
      self.f_ind += 1 # 앞으로 넘어갈 수 있는 페이지 
    # forward 에러 알고리즘
    # 1. go만으로 들어온 상태 -> 즉 backward가 취해지지 않은 상태에서 forward 안됨
    # 2. 시작하자마자 초기 값 hufs.ac.kr 있을 때 forward 안됨. (go가 한번도 안 나왔을 때)
    
  def backward(self):
    if self.b_ind == (len(self.items) - 1): # 초기값인 hufs가 나왔을때 backward가 나오면 안되는데 b_ind 값이 리스트 길이 -1일 경우 backward 불가능
      #print("error") 출력 결과 없음
      pass
    else: 
      self.b_ind += 1 # backward시 b_ind 1 추가
      self.items = self.items[-1:] + self.items[:-1] # 리스트 순서 바꿔주는 알고리즘
      print(self.items[-1])
      self.f_ind -= 1 #backward가 가능하다 -> 앞으로 넘어갈 수 있는 페이지가 존재
      
  # 리스트 순서 바꾸는 알고리즘
  # hufs(1), naver(2), ces(3), daum(4), ces(5) 라고 할때 
  # backward -> 5 1 2 3 4
  # backward -> 4 5 1 2 3
  # backward -> 3 4 5 1 2 이런 알고리즘
  # forward는 이와 반대로 작성
  
  def history(self):
    self.historyitems.reverse() # 역순으로 출력, go 함수에서 history 작성
    for i in self.historyitems:
      print(i)

  def quit(self):
    return 1

addList = ArrayList()
historyList = ArrayList()

initial_value = 'www.hufs.ac.kr' # 초기 값
print(initial_value)

addList.go(initial_value) # 초기 값 넣고 시작
historyList.go(initial_value) # 초기 값 넣고 시작

while True:
  command = list(input().split()) # 명령어 입력
  
  if command[0] == 'quit':
    if addList.quit() == 1:
      break
  
  if command[0] == 'forward':
    addList.forward()
    continue
  
  if command[0] == 'backward':
    addList.backward()
    continue
    
  if command[0] == 'history':
    historyList.history()
    continue
    
  else: #go
    addList.go(command[1])
    historyList.go(command[1])
    print(command[1])