str = 'a like b dream'
#처음에 a와 b를 공백으로 두고(숫자만 아니면 됨 - 위치가 있으면 여기에 숫자가 들어갈테니까)
a = ''
b = ''

#like와 dream위치가 있으면 그걸 a와 b에 넣고
a = str.find('like') 
b = str.find('dream')



if a!='' and b!='':
    #a가 0이 아니고 b가 0이 아니면
    #a와 b가 있다는 뜻이니까 nightmare로 바꾸고
    str = str.replace(str[a:b+5+1],'nightmare')
else:
    # 없으면 like만 love로 바꿔준다
    str = str.replace('like','love')
