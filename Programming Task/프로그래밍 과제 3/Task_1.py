class Stack:
  def __init__(self):
    self.items = []

  def push(self, val):
    self.items.append(val)

  def pop(self):
    try:
      return self.items.pop()
    except IndexError:
      print("Stack is empty")

  def top(self):
    try:
      return self.items[-1]
    except IndexError:
      print("Stack is empty")

  def __len__(self):
    return len(self.items)

  def isEmpty(self):
    return self.__len__() == 0
  

def Balance(s):
  S = Stack() # 스택 준비
  openBracket = '({[' # 여는 괄호
  closeBracket = ')}]' # 닫는 괄호
  
  for ch in s: # 입력 문자열을 하나씩 읽으며 반복
    if ch in openBracket: # 만약 여는 괄호면 스택에 push
      S.push(ch)
    elif ch in closeBracket: # 닫는 괄호이면
      if S.isEmpty(): # 스택이 비어있을 경우(여는 괄호가 없을 경우)
        return 0 # 0 출력
      else: # 스택이 비어있지 않으면
        openCh = S.pop() # pop() 변수 지정
        if (ch == ')' and openCh != '(') or (ch == '}' and openCh != '{') or (ch == ']' and openCh != '['):
          return 0 # ch에 대응하는 여는 괄호가 아닐 경우 짝이 맞지 않으므로 0 출력
        
  if len(S) == 0: # 스택의 길이가 0일 경우 
    return 1
  else:
    return 0

expr = input()
print(Balance(expr))