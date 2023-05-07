str = 'a like b dream'
a = str.find('like')
print(a)
#like위치는 2(맨 처음이 0부터 시작, 공백 포함해서 2)
b = str.find('dream')
print(b)
#dream 위치는 9
# 9는 시작 위치라서 dream이 끝나는 위치는 9+5 = 14

# str[2:14+1] = 이게 바꿔야 할 내용이 된다 (뒷 내용을 14로 입력하면 14전까지 (13까지)만 들어감)
print(str[2:14+1], '<- 바꿔야 할 내용')
str = str.replace(str[2:14+1],'바꾼 내용')
print(str)