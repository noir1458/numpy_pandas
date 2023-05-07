import numpy as np

def testArray():
    a0 = [0,0.5,1.0,1.5,2.0]  # dim = 5
    # b = [1,2,3,4] dim = 4
    b = [1,2,3,4,5]
    a = np.array([a0,a0,b])
    print('Type of a =>',type(a))
    print(a)

    print('-------------')
    print(a[2:])
    print(a[2:][0][2])
    print('-------------')
    print(a[:,2],np.e)
    print('-------------')
    #aa = np.array([])
    #np.copyto(a,aa)
    #print(aa)
    return None

def main():
    testArray()
    return None

if __name__=='__main__':
    main()