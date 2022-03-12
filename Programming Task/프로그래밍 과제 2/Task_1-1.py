data = list(map(int, input().split()))

def gcd(a, b): # 유클리드 알고리즘을 이용한 최대공약수 풀이
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b): # 최소공배수 함수
    return (a * b) // gcd(a, b)

gcd_data = data[0] # 첫번째 인덱스에 저장
lcm_data = data[0] # 첫번째 인덱스에 저장

for i in range(len(data)):
  gcd_data = gcd(gcd_data, data[i]) 
  # 입력된 순서대로 2개의 수의 최대공약수를 구한 다음 그 최대공약수와 나머지 하나의 숫자의 최대공약수를 구해줌
print(gcd_data, end = ' ') 

for i in range(len(data)):
  gcd_data = gcd(lcm_data, data[i]) # 세 수의 최대공약수
  lcm_data = lcm(lcm_data, data[i]) # 세 수의 최소공배수
  
print(lcm_data)