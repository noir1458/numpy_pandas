def homework1_1(str):
    # your code here
    # like부터 dream까지 모두 nightmare로 바꾸어서 str에 저장하고 return
    like_idx_start, dream_idx_end = None, None
    for idx in range(len(str)):
        if str[idx:idx+4] == 'like':    # 먼저 등장하는 like를 찾고
            like_idx_start = idx
            break   
    for idx in range(5,len(str)):
        if str[idx-5:idx] == 'dream':
            dream_idx_end = idx
            break
    # like는 있는데 dream 이 없는 경우 => like만 love로
    # like 있고 dream 있는 경우 => nightmare로 바꾸고 남은 like를 love로
    # like 없고 dream만 있는 경우 => str 그대로
    # like 없고 dream도 없는 경우 => str 그대로
    # like 있고 dream 있는 경우를 위로, 나머지는 else 아래로
    
    if (like_idx_start != None) and (dream_idx_end != None): # like와 dream 둘다 있는 경우
        change_nightmare = str[like_idx_start:dream_idx_end]
        str = str.replace(change_nightmare,'nightmare')
        str = str.replace('like','love') # 남아있는 like 바꾸기
    else: # like는 없는경우(나머지 경우) 또는 like는 있는데 dream이 없는 경우
        str = str.replace('like','love')
    return str

def homework1_2(str):
    # your code here
    # 주어진 문자열에서 가장 많이 반복되는 문자와 freq를 구한다.
    # 가장 많이 반복된 문자를 반복 횟수 값으로 모두 대체하여 str에 저장한 후 return
    tmp_dict = {}
    for k in str:
        if k==' ': # 공백은 반복된문자 수에 체크하지 않는다.
            continue
        tmp_dict[k] = tmp_dict.get(k,0) + 1
    freq = max(list(tmp_dict.values()))
    char = ''
    for k,v in tmp_dict.items():
        if v == freq:
            char = k
            break
    str = char*freq
    #print(freq)
    return str

def main():
    str = "내가 나중에 넣을 것임"
    res = homework1_1(str)
    print(res)
    ret = homework1_2(str)
    print(ret)
    return None
if __name__ == "__main__":
    main()