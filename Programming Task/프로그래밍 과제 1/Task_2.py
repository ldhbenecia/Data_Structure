n = int(input())

result = [] # 완전수를 저장할 리스트.

for i in range(1, n+1): # 1부터 입력한 숫자까지
    sum = 0
    for j in range(1, i): # 1부터 i까지, 약수를 구하기 위해
        if i % j == 0:  
            sum += j # 약수들의 합

    if i == sum: # 자신을 제외한 약수들의 합이 자신과 같으면,
        result.append(i)

print(len(result))