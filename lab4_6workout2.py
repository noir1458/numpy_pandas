import numpy as np
import time

def work1():
    # [12,38) 사이의 값으로 채워진 ndarray를 생성하고 출력하기
    a = np.arange(12,38)
    print(a)
    return None

def work2():
    # 10x10 ndarray를 생성하고 checkerboard꼴로 채우기
    tmp1 = np.arange(1,10)
    a = tmp1 % 2
    b = (tmp1 + 1) % 2
    A = a+b
    print(A)
    return None

def work3():
    # ndarray 2개가 주어질때 공통값 찾기
    a = np.array([0,10,20,40,60])
    b = np.array([10,11,12])
    result = np.intersect1d(a,b)
    print(result)
    return None

def work4():
    # 주어진 ndarray가 차지하는 메모리 크기는
    a = np.array([[1,2,3],[4,5,6]])
    print(a.nbytes)
    return None

def work5():
    # 5x5 random matrix 생성하고 normaliz3e
    np.random.seed(int(time.time()))
    A = np.random.rand(25).reshape((5,5))
    print(A)
    mean_A = np.mean(A)
    std_A = np.std(A)
    result = (A - mean_A)/std_A
    print(result)
    return None

def work6():
    # 크기가 10인 ndarray를 생성한 후 가장 큰 값을 0 으로 대체하라
    np.random.seed(int(time.time()))
    A = np.random.rand(10)
    print(A)
    print(A.argmax())
    A[A.argmax()] = 0
    print(A)
    return None

def work7():
    # 주어진 ndarray에서 0이 아닌 원소의 개수를 구하시오
    np.random.seed(int(time.time()))
    A = np.random.randint(0,3,10)
    print(A)
    result = A.nonzero()
    print(result)

    return None

def main():
    #work1()
    work2() #다시..
    #work3()
    #work4()
    #work5()
    #work6()
    #work7()
    return None

if __name__ == '__main__':
    main()