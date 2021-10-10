# 스택활용 예시 3:: Postfix 계산

- Postfix 수식을 하나의 문자열로 입력받는다.
    - 허용하는 연산자는 모두 이항 연산자로 +, -, *, /, ^ 다섯 가지이다.
    - 문자열의 연속된 두 항(operand와 operator) 사이에는 모두 공백 하나 ' '이 들어있다.
- conpute_postfix(postfix) 함수를 작성한다.
    - postfix 문자열 수식을 계산한 결과를 리턴한다.
- 여러분은 계산 결과를 소수점 이하 4자리까지만 출력한다.

- 실현 코드 작성
```python
class Stack:
        def __init__(self):
        self.items = []    # 데이터 저장을 위한 리스트 준비
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:    # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:    # indexError 발생
            print("Stack is empty")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):    # len()로 호출하면 stack의 item 수 반환
         return len(self.items)
    def isEmpty(self):
        return self.__len__() == 0

    
def compute_postfix(postfix):
    operand = Stack() 
    token_list = postfix.split()
    operators = ['*', '/', '+', '-','^'] # operator 리스트 만듦.
    
    for token in token_list:
        if token not in operators: # 연산자가 아닐때. 즉 숫자일때 (0123456789)
            operand.push(int(token)) # int형변환
            
        else: #연산자일 경우
            n1 = operand.pop() # 해당 연산자 앞의 두 개의 피연산자에 대한 연산이므로, 앞서 스택에 들어갔던 피연산자 두 개를 pop 하여 다시 꺼내 연산을 처리
            n2 = operand.pop()
            result = calc(token, n2, n1)
            operand.push(result) # 그 결괏값을 다시 스택에 넣는다. 
    return operand.pop()

def calc(i, op1, op2): #계산 함수
    if i == '+':
        return op1 + op2
    elif i == '-':
        return op1 - op2
    elif i == '*':
        return op1 * op2
    elif i == '/':
        return op1 / op2
    else:
        return op1 ** op2
    
    
postfix_eval = input()
print("%.4f" %(compute_postfix(postfix_eval)))
```
