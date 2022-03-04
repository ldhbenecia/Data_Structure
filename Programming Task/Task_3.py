n = int(input()) # 정수로 입력을 받으라고 되어있어서 정수로 입력
n_str = str(n) # 문자열로 형 변환
a = (n_str)[::-1] # 슬라이싱을 이옹해 문자열 거꾸로 출력
print(a.lstrip("0")) # lstrip 메서드를 사용하여 선행 숫자 0 제거