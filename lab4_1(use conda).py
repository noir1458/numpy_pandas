import numpy as np

def testArray():
    a = np.array([0,0.5,1.0,1.5,2.0])
    print('Type of a =>',type(a))

    print(a[:2])
    return None

def main():
    testArray()
    return None

if __name__=='__main__':
    main()