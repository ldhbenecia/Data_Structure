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
  def peek(self):
    if not self.isEmpty():
      return self.items[(self.front + 1) % (len(self.items))]

k = 0 # 도착 전 1번 심사대 남은시간
l = 0 # 도착 전 2번 심사대 남은시간
k_wait = 0 # 도착 후 1번 심사대 대기시간
l_wait = 0 # 도착 후 2번 심사대 대기시간
sum = 0

# Algorithm
  # 1번 : 대기 시간 0 
  # 2번 : 1번 대기시간 (0) + 1번 심사시간(4) - 2번 도착시간 (2) = 2
  # 3번 : 2번 대기시간 (2) + 2번 심사시간(7) - 3번 도착시간 (1) = 8
  # 4번 : 3번 대기시간 (8) + 3번 심사시간(6) - 4번 도착시간 (2) = 12
  # 5번 : 4번 대기시간 (12) + 4번 심사시간(5) - 5번 도착시간(1) = 16
  # 2-1 알고리즘 같이 사용
  
expr = int(input())

Q_save = Queue() # 도착 시간 큐
Q_judge = Queue() # 심사 시간 큐

for i in range(expr):
  save, judge = map(int, input().split())
  Q_save.enqueue(save) # 도착 시간 저장
  Q_judge.enqueue(judge) # 심사 시간 저장

# 1번 심사대 k와 2번 심사대 l을 같이 돌리는 코드 구현
# 1번 심사대 k 코드만 if문으로 짠 다음 똑같이 else로 구현하면 됨
for i in range(expr):
  if k <= l: # 1번 심사대 k의 남은 시간이 2번 심사대 l보다 적다면
    k -= Q_save.peek() # 남은 시간에서 도착 시간 반환해서 빼주기
    l -= Q_save.dequeue() # k 심사대에서 심사하는 동안 l 심사대에서도 심사하므로 같이 시간 빼줌
    k_wait = k # 대기시간 k_wait에 저장, 그 다음 사람 도착할 때 써야 하므로
    
    if (k_wait < 0): # 대기시간이 없는 경우
      k_wait = 0 # 바로 심사 하니까 0
      k = 0 # 바로 심사 하니까 0
    sum += k_wait # 평균 값을 구하기 위해 k 심사대 대기 시간 저장
    k = k_wait + Q_judge.dequeue() # 2-1에서 짠 코드와 같이 심사시간 더해주기
    
  else: # 2번 심사대 l의 남은 시간이 1번 심사대 k보다 적다면
    k -= Q_save.peek() # 남은 시간에서 도착시간 반환해서 빼주기
    l -= Q_save.dequeue() # l 심사대에서 심사하는 동안 k 심사대에서도 심사하므로 같이 시간 빼줌
    l_wait = l
    if l_wait < 0: # 대기시간이 없는 경우
      l_wait = 0 # 바로 심사 하니까 0
      l = 0 # 바로 심사 하니까 0
    sum += l_wait # 평균 값을 구하기 위해 l 심사대 대기 시간 저장
    l = l_wait + Q_judge.dequeue() # 심사시간 더 해주기
    
    
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