'''
pandas Series : basic and attributes
'''
import numpy as np
import pandas as pd

def testPd1():
    ser_a = pd.Series(
        np.array([1,2,3,4,5]), # data
        index=['a','b','c','d','e'], # index - key값은 다 달라야 한다
        dtype=np.float64) # element data type
    #print('series a[]', ser_a, sep='\n')

    #print('The index structure')
    #print(ser_a.index)

    print('1:', ser_a[1])
    print('2:', ser_a['b'])

    # attributes
    print('ndim',ser_a.ndim,'size',ser_a.size,'nbytes',ser_a.nbytes,'shape',ser_a.shape,sep='\n')
    print('values :',ser_a.values)
    print('empty :',ser_a.empty)

    # at, iat, loc, iloc
    print('1-th element:',ser_a.at['a'])
    print('1-th element:',ser_a.iat[1])
    print('group element:',ser_a.loc[:'c'],sep='\n')
    print('group element:',ser_a.iloc[:2],sep='\n')

    # index가 없는 경우
    ser_a1 = pd.Series(['1','2','3','4'])
    print(ser_a1[0])
    print(ser_a1.at[2])
    print(ser_a1.iat[2]) # 기본값이 숫자로 01234인듯?

    return None

def testPd2():
    df_A = pd.DataFrame(
        [[1,2,3,4],[2,3,4,5]], # data
        #index=['1st','2nd'], # index(row)
        columns=['col1','col2','col3','col4'] # columns
    )
    print('df_A :\n',df_A)

    # implicit
    # print(df_A[1])
    print(df_A['col2']) # col 단위로 먼저 잘라야된다
    # Series를 가져오게 된다
    print(df_A['col2'][1]) #Series로 가져오면 인덱스로 접근 가능하지만

    # explicit
    #print(df_A.at['1st','col2'])
    print(df_A.loc[:,:'col2'].iat[1,1])
    # attribute임에 유의 - 결과가 값이다. doc 참고

    # index도 attribute - 결과가 값이다.
    print(df_A.index) # range index..

    return None

def main():
    testPd1()
    print('---------------')
    testPd2()
    return None

if __name__ == '__main__':
    main()