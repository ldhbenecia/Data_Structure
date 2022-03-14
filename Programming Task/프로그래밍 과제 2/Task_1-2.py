n = int(input())

def perfect_number(n):
  list = [] # 약수들을 저장할 리스트
  for i in range(1, n):
    if n % i == 0: 
      list.append(i) # n의 약수들을 저장
  if sum(list) == n: # 약수들의 합이 n과 같다면?
    return True 
  else:
    return False
      
result = [] # 완전수 저장할 리스트

def percfect_add(n): # 위의 리스트에서 True 값을 추가하기 위한 함수
    if perfect_number(n) == True: # 1부터 n까지 수 중 완전수 판별 함수에 True값이 되는 수는 result 리스트에 저장
      result.append(n)
      
for i in range(1, n+1):
  percfect_add(i) # 1부터 n까지 위 함수에 주입

print(len(result)) # 완전수의 개수