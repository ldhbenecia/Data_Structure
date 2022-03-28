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
  S = Stack()
  openBracket = '({['
  closeBracket = ')}]'
  
  for ch in s:
    if ch in openBracket:
      S.push(ch)
    elif ch in closeBracket:
      if S.isEmpty():
        return 0
      else:
        openCh = S.pop()
        if (ch == ')' and openCh != '(') or (ch == '}' and openCh != '{') or (ch == ']' and openCh != '['):
          return 0
        
        
  if len(S) == 0:
    return 1
  else:
    return 0

expr = input()
print(Balance(expr))