# 두 수의 최대공약수와 나머지 한 수의 최대공약수가 세 수의 최대공약수가 된다.
# 최소공배수 또한 같다.

data = list(map(int, input().split()))

def gcd(a, b): # 유클리드 알고리즘을 이용한 최대공약수 풀이
  while b > 0:
    a, b = b, a % b
  return a

gcd_data = data[0] # 첫번째 인덱스에 저장
lcm_data = data[0] # 첫번째 인덱스에 저장

for i in range(len(data)):
  gcd_data = gcd(gcd_data, data[i]) 
  # 입력된 순서대로 2개의 수의 최대공약수를 구한 다음 그 최대공약수와 나머지 하나의 숫자의 최대공약수를 구해줌
print(gcd_data, end = ' ') 
# 원래 제일 밑에서 출력을 한번에 하려고 했는데 최대공약수가 계속 값이 변질되어서
# for문 과정을 직접 print해서 비교하다 밑에 최소공배수를 구하는 과정에서 
# 최대공약수 값이 변질되는 것을 알아내어 먼저 구한 최대공약수를 출력해주고
# 밑에 최소공배수와 같은 줄로 출력하기 위해 줄바꿈을 제거하고 띄어쓰기로 구분해주었음

for i in range(len(data)):
  gcd_data = gcd(lcm_data, data[i]) 
  # 최소공배수를 구하기 위한 최대공약수
  # 이 식이 반복될 때 위의 최대공약수 gcd_data 값이 변질되는 것을 알아냄
  lcm_data = lcm_data * data[i] // gcd_data # 최소공배수
  
print(lcm_data)