import random  ## random str을 생성하기 위한 import 학생은 해당 x



def homework1_1(str):
    if "like" in str and "dream" in str:
        start = str.index("like")
        end = str.index("dream") + len("dream")
        str = str[:start] + "nightmare" + str[end:]
    else:
        str = str.replace("like", "love")
    
    return str

def homework1_2(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    max_char = ''
    max_freq = 0
    for char, freq in freq_dict.items():
        if freq > max_freq:
            max_char = char
            max_freq = freq
    sen = text.replace(max_char, str(max_freq))
    
    return sen


def main():

    ## random str을 생성하기 위한 import 학생은 해당 x
    with open('english.txt', 'r') as f:
        words = f.read().split()
    words.extend(['dream', 'like'])
    sentence = ""

    while len(sentence) < 100000 or ('dream' not in sentence or 'like' not in sentence):
        word = random.choice(words)
        sentence += word + " "
        str = sentence.replace(" ", '')
    ## random str을 생성하기 위한 import 학생은 해당 x
    

    res = homework1_1(str)
    print(res)
    print("*******************************************************************")
    ret = homework1_2(str)
    print(ret)
    return None
if __name__ == "__main__":
    main()