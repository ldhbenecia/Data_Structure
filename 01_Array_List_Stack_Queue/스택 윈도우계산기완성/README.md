# 스택활용 예시 4:: 윈도우계산기완성

- 실현 코드 작성
```python
from tkinter import Tk, Label, Button, Entry, StringVar
from functools import partial

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





def do_something():
    value = compute_postfix(infix_to_postfix(expr.get()))
    total.set("{0:.4f}".format(value))
    return

root = Tk()
root.title("My Calculator")
expr = StringVar()
title_label = Label(root, text="My Calcualtor").grid(row=0, columnspan=2)
input_exam = Label(root, text="Space between terms: ( 3 + 2 ) * 8").grid(row=1, columnspan=2)
exp_entry = Entry(root, textvariable=expr).grid(row=2, column=0)
total_label = Label(root, text="TOTAL").grid(row=3, column=0)
total = StringVar()
total.set('0')
value_label = Label(root, textvariable=total, width=20).grid(row=3, column=1)
equal_btn = Button(root, text=' = ', width=20, command=do_something).grid(row=2, column=1)
root.mainloop()
root.destroy()
```
