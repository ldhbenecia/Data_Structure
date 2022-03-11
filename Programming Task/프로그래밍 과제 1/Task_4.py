yy1, yy2 = map(int, input().split()) # 두 년도
day = input() # 요일

leap = 0 # 윤년이 몇번 있었는 지

for y in range(yy1, yy2+1):
  if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
    leap += 1 # 두 년도 사이에 윤년이 있었다면 추가
    
difference = (yy2 - yy1) * 365 + leap # 날짜 수 차이

if ((yy2 % 4 == 0) and (yy2 % 100 != 0)) or (yy2 % 400 == 0):
  difference -= 1
  # 2010년 1월 1일부터 2022년 1월 1일까지 4383일
  # 365 * 12 = 4380
  # 2012, 2016, 2020년 윤년이여서 +3
  
  # 1월 1일 계산하는 것이므로 2010 2024를 하면
  # 5113이 나와야하는데 2024년은 윤년이라 5114가 되어 오답이 나오는 중
	
	# 해결!!!!
  
week = ['월','화','수', '목', '금', '토', '일'] 
result = week[(week.index(day) + difference)%7]

print(result)