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

  def top(self): # peek
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
  count = 0
      
  # 괄호 대응 에러 
  for ch in s: # 입력 문자열을 하나씩 읽으며 반복
    count += 1
    if ch in openBracket: # 만약 여는 괄호면 스택에 push
      S.push(ch)
    elif ch in closeBracket: # 닫는 괄호이면
      if S.isEmpty(): # 스택이 비어있을 경우(여는 괄호가 없을 경우)
        S.push(ch)
        if ch == ')':
          print(count-1, 'error1')
          return False
        if ch == '}':
          print(count-1, 'error2')
          return False
        if ch == ']':
          print(count-1, 'error3')
          return False
      else: # 스택이 비어있지 않으면
        openCh = S.pop() # pop() 변수 지정
        if (ch == ')' and openCh != '('): # 여는 괄호가 아니면
          print(count-1, 'error1')
          return False
        if (ch == '}' and openCh != '{'): # 여는 괄호가 아니면
          print(count-1, 'error2')
          return False
        if (ch == ']' and openCh != '['): # 여는 괄호가 아니면
          print(count-1, 'error3')
          return False
        
  if S.isEmpty() == False:
      if S.top() == '(':
        print(count-1, 'error4')
        return False
      if S.top() == '{':
        print(count-1, 'error5')
        return False
      if S.top() == '[':
        print(count-1, 'error6')
        return False
  
  # 짝이 맞는 경우 1을 출력하는 코드
  for ch in s: # 입력 문자열을 하나씩 읽으며 반복
    if ch in openBracket: # 만약 여는 괄호면 스택에 push
      S.push(ch)
    elif ch in closeBracket: # 닫는 괄호이면
      if S.isEmpty(): # 스택이 비어있을 경우(여는 괄호가 없을 경우)
        return False
      else: # 스택이 비어있지 않으면
        openCh = S.pop() # pop() 변수 지정
        if (ch == ')' and openCh != '(') or (ch == '}' and openCh != '{') or (ch == ']' and openCh != '['):
          return False
  if len(S) == 0: # 스택의 길이가 0일 경우 
    print(1)
    
expr = input()
Balance(expr)
