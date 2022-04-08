class Node:
  def __init__(self, element):
    self.data = element
    self.link = None

class Stack:
  def __init__(self):
    self.top = None	# 데이터 저장을 위한 리스트 준비
  def isEmpty(self):
    return self.top == None
  def push(self, e):
    newNode = Node(e)
    newNode.link = self.top
    self.top = newNode
  def pop(self):
    if self.isEmpty():
      print("error")
      return
    e = self.top.data
    self.top = self.top.link
    return e
  
def compute_postfix(postfix):
  operand = Stack() 
  postfix = postfix[:-1]
  token_list = postfix.split()
  operators = ['*', '//', '+', '-', '%'] # operator 리스트 만듦.
      
  for token in token_list:
    if token not in operators: # 연산자가 아닐때. 즉 숫자일때 (0123456789)
      operand.push(int(token)) # int형변환
    if token in operators: #연산자일 경우
      n1 = operand.pop() # 해당 연산자 앞의 두 개의 피연산자에 대한 연산이므로, 앞서 스택에 들어갔던 피연산자 두 개를 pop 하여 다시 꺼내 연산을 처리
      n2 = operand.pop()
      result = calc(token, n2, n1)
      operand.push(result) # 그 결과값을 다시 스택에 넣는다. 
    
  return operand.pop()

def calc(i, op1, op2): #계산 함수
	if i == '+':
		return op1 + op2
	elif i == '-':
		return op1 - op2
	elif i == '*':
		return op1 * op2
	elif i == '//':
		return op1 // op2
	else:
		return op1 % op2
	
postfix_eval = input()
print("%d" %(compute_postfix(postfix_eval)))