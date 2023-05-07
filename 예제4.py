#숫자세기

str = 'a like b dream'

#a에다가 문자를 저장하고
#b에다가 문자의 개수를 저장하자
dict = {}
for k in str:
    dict[k] = dict.get(k,0) + 1

    
freq = max(list(dict.values()))
char = ''
for k,v in dict.items():
    if v==freq:
        char=k
        break
str = char*freq

print(str)