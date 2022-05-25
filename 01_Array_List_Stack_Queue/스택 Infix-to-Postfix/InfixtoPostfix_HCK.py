class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return len(self.items) == 0
  def push(self, e):
    self.items.append(e)
  def pop(self):
    try:
      return self.items.pop()
    except IndexError:
      print("Stack is Empty")
  def peek(self):
    try:
      return self.items[-1]
    except IndexError:
      print("Stack is Empty")
  
def InfixtoPostfix(expr):
  s = Stack()
  output = []
  
  for token in expr:
    if token in '(':
      s.push('(')
    
    elif token in ')':
      while not s.isEmpty():
        op = s.pop()
        if op == '(':
          break
        output.append(op)
          
    elif token in '+-*/':
      while not s.isEmpty():
        top = s.peek()
        if (prec(token) <= prec(top)):
          output.append(top)
          s.pop()
        else: break
      s.push(token)
      
    else:
      output.append(token)
      
  while not s.isEmpty:
    output.append(s.pop())
  return " ".join(output)

def prec(op):
  if op == '(' or op == ')':
    return 0
  if op == '+' or op == '-':
    return 1
  if op == '*' or op == '/':
    return 2
  else:
    return -1
  
expr = input()
a = InfixtoPostfix(expr)
print(a)

