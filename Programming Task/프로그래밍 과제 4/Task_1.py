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
			return -1
		e = self.top.data
		self.top = self.top.link
		return e
	def peek(self):
		if self.isEmpty():
			return 'Stack is empty'
		return self.top.data
	
def compute_postfix(postfix):
	operand = Stack() 
	postfix = postfix[:-1] # 세미클론을 삭제해주기 위한 슬라이싱
	token_list = postfix.split()
	token_list2 = []
	
	for i in token_list:
		token_list2.append(token_list)
		
	operators = ['*', '//', '+', '-', '%'] # operator 리스트 만듦.
	
	for token in token_list:
		if len(token_list2) % 2 == 0: # 입력한 연산자, 피연산자의 개수가 짝수이면
			print("error")
			break
			
		if token not in operators: #숫자일 경우
			operand.push(int(token))
			
		elif token in operators: #연산자일 경우
			if operand.isEmpty():
				print('error')
				break
			else:
				n1 = operand.pop()
			if operand.isEmpty():
				print('error')
				break
			else:
				n2 = operand.pop()
			result = calc(token, n2, n1)
			operand.push(result)
			
	if operand.isEmpty():
		return None
	else:
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

if compute_postfix(postfix_eval) != None: # 값이 None이 아닐 시 출력
	print(f'{compute_postfix(postfix_eval)}')