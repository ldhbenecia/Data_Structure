'''
word = input()
word = word.lower()

def isPalindrome(word):
  if word == word[::-1]:
    return True
  else:
    return False

def longestPalindrome(word):
  substring = []
  length = 0
  
  for i in range(len(word)):
    # 홀수 길이회문 확인
    left, right = i, i
    while left >= 0 and right < len(word) and word[left] == word[right]:
      if (right - left + 1) > length:
        substring.append(word[left:right+1])
      left -= 1
      right += 1
      
    
  substring.sort(key = lambda x : len(x))
  print(substring)
      
  for i in substring:
    print(i, end=' ')

  return substring

longestPalindrome(word)
'''

# 위 코드는 실패


word = input()
word = word.lower()

def isPalindrome(word): # 입력받은 문자가 회문인지 판별하는 함수
  if word == word[::-1]:
    return True
  else:
    return False

def longestPalindrome(word): # 가장 긴 회문을 찾는 함수
  substring = [] # 회문을 저장할 리스트
  isPalindrome(word) # 위 함수 호출
  
  for i in range(len(word)):
    for j in range(len(word), i, -1):
      if word[i:j] == word[i:j][::-1]:
        substring.append(word[i:j]) # 입력받은 문자의 처음 그리고 끝에서부터 보며 같을 시에 substring 리스트에 저장
  
  substring.sort(key=len) # 모든 회문을 입력받은 리스트 정렬 / (key=len)으로도 되고 substring.sort(key = lambda x : len(x)로도 가능
      # 해야할일. 가장 길이가 긴 문자열을 찾아 그 문자열만 출력 <- 풀이과정 중 작성 주석
      # 처음에는 모든 입력받은 회문 중에 가장 길이가 긴 회문 제외 나머지 회문을 삭제하랴고 하였으나, 맘처럼 되지않아 방식을 바꿈
  length = len(substring[-1]) # 가장 길이가 긴 문자열의 길이가 몇인지 저장
  answer = [] # 최종 리스트 하나 만들어줌
  
  for i in range(len(substring)): # 모든 회문의 길이만큼 반복
    if length == len(substring[i]): # 가장 길이가 긴 길이 length와 substring의 회문의 길이 중 같은 것이 있다면
      answer.append(substring[i]) # answer 리스트에 추가 해줌
    
  answer.sort() # 그대로 예제를 시행하면 'bbb', 'bab', 'aba'가 나오기 때문에 이제 최종적으로 알파벳순 정렬
  
  for i in answer: # 리스트 요소 출력
    print(i, end = " ")
  
  return substring # 함수의 substring 반환

longestPalindrome(word) # 출력까지 안에서 전부 해결하여 함수에 word를 넣고 호출하면 함수 안의 내용이 수행됨.