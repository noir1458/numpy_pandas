# arrange, reshape, resize, transpose (or T)
import numpy as np
import time

def testNp1():
    a = np.arange(20)
    print('a ranged vector :',a)

    A = a.reshape((2,10))   # reshape - method
    print(A)
    B = np.resize(a,(4,2))  # resize - element 개수가 바뀐다, numpy function
    print(B)
    print(B.transpose())    # transpose - method (data 바뀌지 않음)
    
    # 아래 두개의 차이에 유의
    print(A[:2,1])
    print(A[:2][1])
    return None
def testNp2():
    dt_student = np.dtype([
        ('Name', np.unicode_, 10), # name tag S10
        ('Age', np.int16), # age tag i4
        ('Height', np.float32), # height f
        ('Children/Pets', np.int8, 2)  # child/pets i4
    ]
    )
    student = np.array([
        ('아이유',45,1.70,(0,1)),
        ('Jones',53,1.60,(2,2)),
        ('Kim',20,1.60,(1,1))
    ]
        , dtype= dt_student)
    arr_name_student = student["Name"]
    print(arr_name_student)
    arr_height_student = student["Height"]
    print(arr_height_student.mean())

    return None

def testNp3():
    np.random.seed(int(time.time()))
    A = np.arange(12).reshape((4,3))
    print('print random 4x3 matrix A')
    print(A)
    B = np.random.randint(1,10,12,dtype=np.int32).reshape((2,6))
    # [1,10) random 12개 int
    print(B)

    return None

def main():
    #testNp1()
    # testNp2()
    testNp3()
    return None

if __name__ == '__main__':
    main()