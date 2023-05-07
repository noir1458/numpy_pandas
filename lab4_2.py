# ndarray attributes
import numpy as np

def testNumpyArray():
    a = np.array([1,2,3,4,5], dtype='i8')       # construct an ndarray
    #list up attributes
    print('a type : ', type(a), ' and element type :', a.dtype, sep='')
    print(a)
    # size, ndim, shape, nbytes, itemsize
    # parameters : i2, i4, i8
    L1 =  [1,2,3,4,5]
    L2 =  [1,2,3,4,5,1,2,3,4,5]
    dtypelist = ['i2','i4','i8']
    for tmp in dtypelist:
        a1 = np.array(L1, dtype = tmp)
        print('------type is',tmp)
        print('size :',a1.size)
        print('ndim :', a1.ndim)
        print('shape : ',a1.shape)
        print('nbytes : ',a1.nbytes)
        print('itemsize : ', a1.itemsize)
        print()
    for tmp in dtypelist:
        a1 = np.array(L2, dtype = tmp)
        print('------type is',tmp)
        print('size :',a1.size)
        print('ndim :', a1.ndim)
        print('shape : ',a1.shape)
        print('nbytes : ',a1.nbytes)
        print('itemsize : ', a1.itemsize)
        print()
    return None

def testNumpyArray2():
    b = np.array([1.3,2.44,-9.01687,4.99,0])
    print('dtype :', b.dtype) # f8
    print('nbytes :', b.nbytes)
    print('shape :', b.shape)
    print('itemsize :', b.itemsize)
    return None

def testNumpyArray3():
    c = np.array([10,2,3,4,5])
    print(c)
    c[0] = 100
    print('updated:', c)
    c[4] = -10.88      # float를 넣어도 원래 type인 int로 바뀌어서 들어간다
    print('updated2:', c)
    print(c.dtype)
    return None

def testNumpyArray4():
    c = np.array([100,2,3,4,-10])
    d = c[1:3]
    print(d)
    #d[1:3] = 30,40
    print(d)
    return None

def main():
    testNumpyArray()
    #testNumpyArray2()
    #testNumpyArray3()
    #testNumpyArray4()
    return None

if __name__ == '__main__':
    main()