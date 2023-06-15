# vector addition, hadammard & dot product
import numpy as np

def testBasicOp():
    a = np.array([1,2,3,4,5])
    b = np.array([-1,-2,-3,-4,-5])

    # addition
    print('a[] + b[] =', a+b)
    # hadamard product
    print('a[] * b[] =', a*b)
    # inner product
    print('a[] dot b[] =', a.dot(b))

    return None

def testOp2():
    a = np.array([1, np.pi, np.pi/2, 1/np.pi, np.pi/4])
    # mean
    avg = a.mean()
    print('avg :', avg)
    # min/max
    mina = a.min()
    print('min :',mina)
    # sin/cos
    arr_sin = np.sin(a)
    print('sin :',arr_sin)

    # floor
    x = np.floor(a[1])
    print(x)
    # ceil
    x = np.ceil(a[1])
    print(x)

    # gcd
    b = np.array([13413,1241])
    #print(np.gcd(b))

    return None

def testOp3():
    a = np.array([1,2,3,4,5])
    b = np.linspace(-2,2, num=5)
    print('Line space b[] :',b, 'of elt type:', b.dtype, sep='')
    #c = a + b
    #d = a * b
    #e = b.dot(a)
    #e2 = np.dot(a,b)
    return None

def main():
    testBasicOp()
    print('-----------------')
    testOp2()
    print('-----------------')
    testOp3()
    return None

if __name__ == '__main__':
    main()