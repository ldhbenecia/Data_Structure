answer = list(map(int, input().split())) # 문제별 정답
score = list(map(int, input().split())) # 문제별 배점
solve = list(map(int, input().split())) # 제출한 답안지

correct = []

for i in range(len(answer)): # 문제 수만큼 비교하기 위해 반복
  if answer[i] == solve[i]: # 문제 정답과 제출한 답안지의 index가 같으면
    correct.append(score[i]) # 그 자리의 배점들을 correct 리스트에 저장
    
print(sum(correct)) # 맞춘 문제들의 배점 합 출력