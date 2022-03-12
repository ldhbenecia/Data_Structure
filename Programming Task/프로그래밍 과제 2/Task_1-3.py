yy1, yy2 = map(int, input().split()) # 두 년도
day = input() # 요일

leap = 0 # 윤년이 몇번 있었는 지

def isLeap(y): # 윤년 함수
  if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
    return True
  else:
    return False


for y in range(yy1, yy2+1):
  if isLeap(y): # 함수 사용
    leap += 1 # 두 년도 사이에 윤년이 있었다면 추가
    
difference = (yy2 - yy1) * 365 + leap # 날짜 수 차이

if isLeap(yy2):
  difference -= 1
  # 윤년인 해는 1월 1일 요일을 계산하므로 그 해는 +1이 들어가서는 안됨.
  # 2010년 1월 1일부터 2022년 1월 1일까지 4383일
  # 365 * 12 = 4380
  # 2012, 2016, 2020년 윤년이여서 +3
  
week = ['월','화','수', '목', '금', '토', '일'] 
result = week[(week.index(day) + difference)%7]

print(result)
