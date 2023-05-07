import numpy as np
def testArray():
    a = np.array([1,2,3], dtype=np.float32)
    b = np.array([[1,3,5,7,9],[0,2,4,6,8]],dtype=np.int16)
    print(a)
    print(b)

    # sum, prod
    print('sum of a:',a.sum())
    print('product of a:',a.prod())
    # std 표준편차, mean
    print('std of a:',a.std())
    print('mean of a:',a.mean())
    # cumsum(합), cumprod(곱)
    print('cumulative sum of a:',a.cumsum())
    print('cumprod of a:',a.cumprod())
    # math function
    print('1==',np.log(np.e))
    # 열 지정해서 합
    print(b[:,1].sum())
    # 열끼리 합
    #use_sum = []
    #for k in range(len(list(a[0]))):
    #   use_sum += [b[:,k]]

    # gradient
    print('gradient of a:', np.gradient(a))

    return None

def main():
    testArray()
    return None

if __name__ =='__main__':
    main()