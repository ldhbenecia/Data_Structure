# 스택활용 예시 1:: 괄호 짝 맞추기

1. 수식 (2+5)*7-((3-1)/(2+7)/4 라고 하면, 왼쪽 괄호와 오른쪽 괄호가 쌍을 이뤄 짝이 맞아야 한다.  
2. (()()) 경우는 올바른 짝이지만, (()))( 경우는 왼쪽과 오른쪽 괄호 개수는 3개로 같음에도 짝이 맞지 않는다.  
3. 왼쪽과 오른쪽 괄호가 섞인 괄호 시퀀스를 입력으로 받아 짝이 맞는 괄호라면 True를, 아니면 False를 출력하는 코드를 작성해보자.  
    * 괄호 시퀀스 S = ...(...)... 처럼 중간에 (...)가 등장한다고 해보자.  전체 시퀀스 짝이 맞기 위해선, 이 두괄호에 포함된 짧은 시퀀스 ... 역시 괄호 짝이 맞아야 함을 알 수 있다.  
    * S의 가장 왼쪽 괄호부터 차례대로 살펴보면서 현재까지 본 괄호들을 최대한 짝을 맞춘다고 가정하자.
    * 왼쪽 괄호 (이 등장하면 짝이 되는 오른쪽 괄호 )이 나중에 반드시 등장해야 하고, 두 괄호 안에 포함되는 괄호들도 짝이 맞아야 한다.
    * 짝이 맞는 괄호들은 즉시 시퀀스에서 빼버린다면, 오른쪽 괄호 )이 등장할 때, 자신의 왼쪽 괄호가 가장 최근에 짝을 못 맞춘 괄호로 기다리고 있어야 한다. 즉, 가장 최근에 짝을 못 맞춘 왼쪽 괄호가 가장 빨리 오른쪽 괄호와 짝을 맞추기 때문에 스택의 LIFO 원칙과 일치함
4. Pseudo 코드
<pre>
<code>
def parChecker(parSeq):
    s = Stack()
    for each symbol in parSeq:
        if symbol is "(":
            S.push(symbol)
        else: # symbol == ")"
            if S is empty: # if no left to be matched
                return False
            else: # symbol == ")": 스택에 저장된 건 ")"뿐
                S.pop()
    if S is empty: #스택에 남아 있는게 없어야 짝짓기 완성
        return True
    else:
        return False
</code>
</pre>


- 실현 코드 작성
<pre>
<code>
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

# pseudo code
def parChecker(parSeq):
    S = Stack()
    for symbol in parSeq:
        if symbol == "(":
            S.push(symbol)
        else:
            if S.isEmpty():
                return False
            else:
                S.pop()
                
    if S.isEmpty():
        return True
    else:
        return False
S = input()
ispar = parChecker(S)
print(ispar)
</code>
</pre>

