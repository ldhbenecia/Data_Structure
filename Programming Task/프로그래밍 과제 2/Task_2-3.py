answer = list(map(int, input().split())) # 문항별 정답
score = list(map(int, input().split())) # 문항별 배점
answer_num = int(input()) # 제출한 답안지 수

sum_list = [] # 배점 리스트
id_list = [] # 아이디 리스트

for i in range(answer_num): # 제출한 답안지 수만큼 제출한 답안지 수 입력
  sum = 0
  result = list(map(int, input().split())) # id와 답안 입력
  for j in range(len(answer)):
    if answer[j] == result[j+1]:
      sum += score[j]
  sum_list.append(sum) # 배점 리스트에 정답 점수 저장
  id_list.append(result[0]) # 아이디 리스트에 첫번째 값 아이디 = 저장
  
  
for i in range(len(sum_list)): # 정답 점수만큼 반복
  for j in range(i): # 버블 정렬을 통해 제일 뒤로 가장 높은 점수를 보냄
    if sum_list[j] > sum_list[j+1]:
      sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]
      id_list[j], id_list[j+1] = id_list[j+1], id_list[j] # 배점과 아이디를 연결해주기 위해 아이디 또한 뒤로 함께 보냄
# 둘 다 기본 sort()로 하면 예제 입력시 최고점은 20, id는 2222, 3333이 출력되기 때문에
# 버블정렬로 해줌
            
maxValue = sum_list[-1] # 가장 높은 점수 따로 저장
id_count = sum_list.count(maxValue) # 가장 높은 점수가 몇개인지 저장 (최고점이 여러개일 경우를 위해)

sort_idList = [] # 아이디 리스트 한개 더

# 아이디 리스트를 출력하기 위해서는 우선 최고점의 인덱스를 파악해야하는데
# 예시의 경우 최고점이 20으로 인덱스의 제일 뒤와 제일 뒤의 1칸 앞에 한개 더 있다. 2개이므로
# 고로 최고점이 3개일수도 있고 4개일수도 있기 때문에 최고점이 몇개인지에 대한 개수를
# 위에 id_count를 통해 maxValue를 받아준다.
# 그리고 id_list의 최고점의 개수값 만큼의 위치를 구하기 위해 반복문을 돌려 새 리스트에 저장해준다.
for i in range(len(id_list)-id_count, len(id_list), 1): 
  sort_idList.append(id_list[i])
  
# 이렇게 하면 1234 1122가 저장되므로 id를 정렬하기 위해 sort()를 해준다.
sort_idList.sort()

print(sum_list[-1]) # 최고점 출력

for i in sort_idList:
  print(i, end = " ") # 리스트의 요소 출력. 띄어서 출력하기 위해 end = " "