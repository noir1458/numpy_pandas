import numpy as np

def work1():
    # array의 type와 value의 type을 확인하시오
    a = np.array([3.1,11.2,6.7,213.11])
    print(type(a))
    print(a.dtype)
    return None

def work2():
    # array a의 크기, 차원, 형태(shape)을 확인하시오
    a = np.array([3.1,11.2,6.7,213.11])
    print(a.size)
    #print(a.nbytes) 이건 크기가 아니고 용량인가?
    print(a.ndim)
    print(a.shape)
    return None

def work3():
    # array a의 3번째 원소를 100으로 변경하시오
    a = np.array([3.1,11.2,6.7,213.11])
    a[2]=100
    print(a)
    return None

def work4():
    # array a의 1-3번째 원소들을 선택하여 새로운 array를 생성하시오
    a = np.array([3.1,11.2,6.7,213.11])
    b = a[:3]
    print(b)
    return None

def work5():
    # 다음 array ar의 짝수값만 출력하시오
    ar = np.array([1,2,3,4,5,6,7,8])
    print(ar[1::2])
    return None

def work6():
    # array ar의 mean(평균)과 median(중위값)을 찾으시오
    ar = np.array([1,2,3,4,5,6,7,8])
    print(np.mean(ar))
    print(np.median(ar))
    return None

def work7():
    # numpy의 mathematical function을 사용하여 다음 두 array의 뺄셈을 수행
    a = np.array([1,2,3,4,5])
    b = np.array([0,1,2,3,4])
    print(a-b)
    return None

def work8():
    # Hadamard mul과 Dot product를 확인
    a = np.array([1,2,3,4,5])
    b = np.array([0,1,2,3,4])
    print(a*b)
    print(np.dot(a,b))
    return None

def work9():
    # 범위 [5,4]안에 6개의 원소로 된 array를 생성하여 lin_arr에 저장하고 출력하시오.
    lin_arr = np.linspace(5,4,num = 6)
    print(lin_arr)
    return None

def work10():
    #A에 저장하고 size, dim, shape를 확인하시오
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    A = np.array(a)
    print(A.size)
    print(A.ndim)
    print(A.shape)
    return None

def work11():
    #A의 첫번째 row의 처음 두 개의 원소를 출력하시오
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    A = np.array(a)
    print(A[0,:2])
    return None

def work12():
    #다음 2-D array와 A의 Hadamard Mul과 matrix mul의 가능 여부를 확인한 후, 가능한 경우 결과를 출력하시오
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    A = np.array(a)
    B = np.array([[0,1],[1,0],[1,1],[-1,0]])
    #print(A*B)
    print(np.dot(A,B))
    return None

def main():
    #work1()
    #work2()
    #work3()
    #work4()
    #work5()
    #work6() #?? - median 이게 맞나
    #work7() # 맞나?
    #work8()
    #work9()
    #work10()
    #work11()
    work12()
    return None

if __name__ == '__main__':
    main()