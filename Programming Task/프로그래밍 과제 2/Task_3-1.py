def palindrome(word): # 회문 판별 함수
  word = word.lower() # 입력받은 문자 소문자로 변환
  if word == word[::-1]: # 뒤에서부터 출력한 값과 같다면
    return True # 회문 True
  else: # 아니면
    return False # 회문 False
  
word = input() # 값 입력

if palindrome(word) == True: # 맞을시 yes 아닐시 no 출력
  print("yes")
else:
  print("no")