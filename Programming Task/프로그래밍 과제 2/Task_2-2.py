answer = list(map(int, input().split())) # 문항별 정답
score = list(map(int, input().split())) # 문항별 배점
answer_num = int(input()) # 제출한 답안지 수

sum_list = [] # 배점 리스트

for i in range(answer_num): # 제출한 답안지 수만큼 제출한 답안지 수 입력
  sum = 0
  result = list(map(int, input().split())) # id와 답안 입력
  for j in range(len(answer)):
    if answer[j] == result[j+1]:
      sum += score[j]
  sum_list.append(sum) # 배점 리스트에 정답 점수 저장
  
  
for i in range(len(sum_list)): # 정답 점수만큼 반복
  for j in range(i): # 버블 정렬을 통해 제일 뒤로 가장 높은 점수를 보냄
    if sum_list[j] > sum_list[j+1]:
      sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]
           
            
maxValue = sum_list[-1] # 가장 높은 점수 따로 저장
print(sum_list[-1]) # 최고점 출력


# 과제가 수정되기 전 2-2를 풀이한 상태여서
# 수정 전 2-2. 현 2-3 코드에서 id 관련 코드만 제거