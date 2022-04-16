class Queue:
  MAX_QSIZE = 200 # 큐에 대한 크기 설정
  def __init__(self):
    self.items = [None] * Queue.MAX_QSIZE
    self.front = -1
    self.rear = -1
    self.size = 0
  def isEmpty(self):
    return self.size == 0
  def enqueue(self, e):
    if self.size == len(self.items):
      print("Queue is full")
      self.resize(2 * len(self.items))
    else:
      self.rear = (self.rear + 1) % (len(self.items))
      self.items[self.rear] = e
      self.size += 1
  def dequeue(self):
    if self.isEmpty():
      print("Queue is empty")
    else:
      self.front = (self.front + 1) % (len(self.items))
      e = self.items[self.front]
      self.size -= 1
      return e
  def resize(self, cap):
    olditems = self.items
    self.items = [None] * cap
    walk = self.front
    for k in range(self.size):
      self.items[k] = olditems[walk]
      walk = (walk + 1) % len(olditems)
    self.front = -1
    self.rear = self.size -1
  def printQueue(self):
    print(self.items)
    
# 공백 상태: front = rear
# 포화 상태: front == (rear + 1) % MAX_QSIZE
# rear은 꼬리(tail)의 위치, enqueue 될 때 +1씩 늘어남
# front는 -1로 시작하지만 dequeue 될 때 +1씩 늘어남

def judgeTime(expr):
  Q_save = Queue() # 도착 시간 큐
  Q_judge = Queue() # 심사 시간 큐

  # Algorithm (입력 예시 1번으로 짠 알고리즘)
  # 1번 : 대기 시간 0 
  # 2번 : 1번 대기시간 (0) + 1번 심사시간(4) - 2번 도착시간 (2) = 2
  # 3번 : 2번 대기시간 (2) + 2번 심사시간(7) - 3번 도착시간 (1) = 8
  # 4번 : 3번 대기시간 (8) + 3번 심사시간(6) - 4번 도착시간 (2) = 12
  # 5번 : 4번 대기시간 (12) + 4번 심사시간(5) - 5번 도착시간(1) = 16
  
  time = 0 # 도착해서 기다리고 검사가 끝날 때까지 시간
  wait = 0 # 대기 시간
  sum = 0 # 합
  
  for _ in range(expr):
    save, judge = map(int, input().split()) # 도착시간, 심사시간 입력
    
    Q_save.enqueue(save)
    Q_judge.enqueue(judge)
    
  for _ in range(expr):
    wait = time - Q_save.dequeue() # 대기시간 + 심사시간 - 도착시간
    if wait < 0: # 음수 -> 대기 없는 경우
      wait = 0 # 0으로 초기화
    sum += wait # 대기시간 총 합 
    
    time = wait + Q_judge.dequeue() # 대기시간 + 심사시간
    if time < 0:
      time = 0 # 0이 나오는 경우 = 음수가 나올 경우
  
  
  # 파이썬의 반올림 방식은 오사오입법을 사용한다
  # 하지만 이 문제에서의 반올림은 사사오입법으로 계산해야 하기 때문에 반올림 함수를 사용하면 아닌 케이스가 존재한다.
  average = sum / expr
  average2 = str(average)[:4] # 소수 둘째자리까지 출력이므로 둘째짜리까지만 뽑아냄
  average3 = float(average2) # 문자열을 다시 실수로 변환
  if round(average, 2) != average3: # 반올림을 한 값이 같지 않다면
    print(f'{average:.2f}') # 그대로 출력
  else:
    average += 0.0000001 # 반올림을 해주기 위해 미세한 값을 추가해줌
    print(f'{average:.2f}') # 출력하면 사사오입법식 반올림이 완성됨.
		
expr = int(input())
judgeTime(expr)
