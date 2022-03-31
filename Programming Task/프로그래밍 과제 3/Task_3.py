import sys

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
	newBracket = '\n'
	count = 0
	bre = [] # 에러 4,5,6을 위한 인덱스 저장 리스트
	line = 0
	line_count = [] # 에러 4,5,6을 위한 라인 저장 리스트
	
	# 괄호 대응 에러 
	for ch in s: # 입력 문자열을 하나씩 읽으며 반복
		line += 1
		for i in ch:
			count += 1
			if i in newBracket:
				count = 0
			if i in openBracket: # 만약 여는 괄호면 스택에 push
				line_count.append(line) # 열린괄호 리스트 저장
				bre.append(count) # 열린괄호 위치 저장
				S.push(i)
			elif i in closeBracket: # 닫는 괄호이면
				if S.isEmpty(): # 스택이 비어있을 경우(여는 괄호가 없을 경우)
					if i == ')':
						print('error 1: ) at position', count, 'in line', line)
						return False
					if i == '}':
						print('error 2: } at position', count, 'in line', line)
						return False
					if i == ']':
						print('error 3: ] at position', count, 'in line', line)
						return False
				else: # 스택이 비어있지 않으면
					openCh = S.pop() # pop() 변수 지정
					bre.pop() # 닫는 괄호가 나와서 짝이 지어진 괄호에 해당하는 인덱스들은 전부 삭제
					line_count.pop() # 닫는 괄호가 나와서 짝이 지어진 괄호에 해당하는 라인들은 전부 삭제
					if (i == ')' and openCh != '('): # 여는 괄호가 아니면
						print('error 1: ) at position', count, 'in line', line)
						return False
					if (i == '}' and openCh != '{'): # 여는 괄호가 아니면
						print('error 2: } at position', count, 'in line', line)
						return False
					if (i == ']' and openCh != '['): # 여는 괄호가 아니면
						print('error 3: ] at position', count, 'in line', line)
						return False
	

	if S.isEmpty() == False: # 짝이 맞는 괄호들을 없애고 남은 괄호에 따라 error 출력
		if S.top() == '(':
			print('error 4: ( at position', bre[-1], 'in line', line_count[-1])
			return False
		if S.top() == '{':
			print('error 5: { at position', bre[-1], 'in line', line_count[-1])
			return False
		if S.top() == '[':
			print('error 6: [ at position', bre[-1], 'in line', line_count[-1])
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
		
expr = sys.stdin.readlines()
Balance(expr)


