# Palindrome Check

목적: 디큐(dequeue)-에 대한 강의내용을 참고하고 check_palindrome함수를 구현한다.
입력: 길이가 0 이상인 문자열
출력: Palindrome 일 때 True, 아니면 False

1. deque 클래스 구현
    멤버 변수:
        items: 리스트
    멤버 함수: 
        a.__init__(self, s):  
        s 문자열을 받아서, 그 문자들의 리스트로 items를 초기화
        
        b. append(self, c): 
        c를 items 리스트의 오른쪽에 append 함
        
        c. appendleft(self. c):
        c를 items 리스트의 왼쪽에 append 함
        
        d. pop(self):
        items 리스트의 가장 오른쪽 원소를 삭제해서 리턴
        
        e. popleft(self):
        itmes 리스트의 가장 왼쪽 원소를 삭제해서 리턴
        
        f. __len__(self):
        items 리스트의 길이를 리턴
        
        g. right(self):
        items 리스트의 가장 오른쪽 원소를 삭제 안하고 리턴
        
        h. left(self):
        items 리스트의 가장 왼쪽 원소를 삭제 안하고 리턴

- 실현 코드 작성
```python
class deque:
    def __init__(self):
        self.items = []
        
    def __init__(self, s):
        self.items = []
        
    def append(self, c):
        self.items.append(c)
    
    def appendleft(self, c):
        self.items.appendleft(c)
    
    def pop(self):
        self.items.pop()
    
    def popleft(self):
        self.items.popleft()
        
    def __len__(self):
        return len(self.items)
    
    def right(self):
        return self.items[0]
    
    def left(self):
        return self.items[-1]
        


from collections import deque

def check_palindrome(s):
    dq = deque(s)
    palindrome = True
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
            
    return palindrome

n = input()
print(check_palindrome(n))
```
