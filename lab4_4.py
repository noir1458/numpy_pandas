# 2-dim Numpy array => matrix
import numpy as np

def dim2test():
    # creating a 3x3 matrix
    a = [[1,2,3],[4,5,6],[7,8,9]]
    A = np.array(a, dtype='i4')
    print('Matrix :A\n', A)

    # slicing
    b = A[0:2,1]
    c = A[1,0:2]
    print('Sliced vector b[]:', b)
    print('sliced vec c[] :',c)
    return None

def main():
    dim2test()
    return None

if __name__ == '__main__':
    main()