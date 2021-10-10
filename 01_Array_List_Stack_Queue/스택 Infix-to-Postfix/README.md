# 스택활용 예시 2:: Infix-to-Postfix

- 스택을 이용해서 Infix 수식을 Postfix 수식으로 바꾸는 함수 infix-to-postfix()를 완성한다.
입력: +, -, /, *, ^, (, )와 숫자가 섞인 Infix 수식.  
##### 연산자와 operand들이 space 문자 (' ')-로 분리되어 있다고 가정
출력: Postfix 수식  

1. 괄호와 연산자를 저장하기 위한 스택 opstack = stack() 준비
2. Postfix 수식(결과)을 저장하기 위한 리스트 outstack 준비
3. Infix 수식을 tokenize 해서 연산자와 Operand들의 리스트 token_list를 얻는다.
4. Pseudo 코드
```python
for each token in token_list:
if token == operand:
    outstack.append(token)
if token == '(':
    opstack.push(token)
if token == ')':
    opstack에 저장된 연산자를 (를 만날때까지 계속 pop한 후 outstack에 append함
if token in '+-*/^':
    a. opstack에 있는 자신보다 우선순위가 높거나 같은 연산자는 차례로 모두 pop한 후 outstack에 append함
    b. opstack.push(token)
```
5. opstack에 남아있는 모든 연산자를 pop한 후 outstack에 append
6. return " ".join(outstack)


- 실현 코드 작성
```python
'''
Infix to postfix
'''
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

def infix_to_postfix(infix):
  opstack = Stack()
  outstack = []
  token_list = infix.split(' ')
  prec = {'(':1, '+':2, '-':2, '*':3, '/':3, '^':4}
  
  for token in token_list:
    if token == '(':
      opstack.push(token)
      
    elif token == ')':
      while True:
        infix = opstack.pop()
        if infix == '(':
          break
        outstack.append(infix)

    elif token in '+-/*^':
      while(not opstack.isEmpty()) and (prec[opstack.top()] >= prec[token]):
        outstack.append(opstack.pop())
      opstack.push(token)
            
    else: # operand일 때
      outstack.append(token)
    
  while not(opstack.isEmpty()):
    outstack.append(opstack.pop())
  return " ".join(outstack)

    
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)
```
