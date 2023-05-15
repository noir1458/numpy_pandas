import numpy as np
import pandas as pd

def testpd1():
    crime_csv_path = "./SacramentocrimeJanuary2006.csv"
    df_csv = pd.read_csv(crime_csv_path,sep=",")
    # pick a column named 'beat' = SELECT * FROM CRIMES WHERE BEAT = "3C"
    #print(df_csv.head())
    beat_3c = df_csv[['beat']] == '3C        '
    # filter 
    df_beat_3c = df_csv[beat_3c]
    print(df_beat_3c)

    df_csv['3C_beat'] = beat_3c
    print(df_csv)

    print(df_csv.index)
    idx = df_csv.index
    print(idx.max())

    df1 = df_csv.drop(columns=['3C_beat'])
    print(df1.head())

    '''
    del_rows = [0,2]
    df2 = df_csv.drop(index=del_rows)
    '''

    return None

def testpd2():
    '''
    student_csv_file = "./student.csv"
    df_student = pd.read_csv(student_csv_file,sep=",")
    #print(df_student)

    df_gb_years = df_student.groupby('years')
    print(df_gb_years)          # <= groupby
                                # SELECT * FROM STUDENT GROUP BY YEARS
    print(df_gb_years.mean())   # <= aggregate by mean() <= general function
    print(df_gb_years.count())
    '''
    student_csv_file1 = "./student_sql.csv"
    dt_st1 = {
        #col_name:type
        'SID':np.int32,
        'SName':np.unicode_,
        'DepId':np.unicode_
    }

    df_st1 = pd.read_csv(student_csv_file1,sep=",",dtype=dt_st1)
    df_st2 = pd.read_csv(student_csv_file1,sep=",",dtype=dt_st1)
    print(df_st1)

    # concat = st1 || st2 with option axis = 0, axis = 1
    df_st = pd.concat([df_st1,df_st2])
    print('Concatenate : st1 || st2(row)\n',df_st) # axis = 0 (row 기준으로, hstack과 유사)
    df_st = pd.concat([df_st1,df_st2],axis=1)
    print('Concatenate : st1 || st2(column)\n',df_st) # axis = 1 (col 기준으로, vstack과 유사)

    student_csv_file2 = "./depart_sql.csv"
    dt_dep = {
        'DId':np.unicode_,
        'DName':np.unicode_
    }
    df_st2 = pd.read_csv(student_csv_file2,sep=",",dtype=dt_dep)
    df_school = pd.concat([df_st1,df_st2],axis=0) # axis = 0 (row의 기준)
    print('Concatenate : st1 || dep (row)',df_school)
    df_school = pd.concat([df_st1,df_st2],axis=1,join='inner') # axis = 1, join옵션 주면 NaN줄만 없어진다
    print('Concatenate : st1 || dep (col)',df_school)

    return None

def testpd3():
    # read student & depart
    # make df
    student_csv_file1 = "./student_sql.csv"
    dt_st1 = {
        #col_name:type
        'SID':np.int32,
        'SName':np.string_,
        'DepId':np.string_
    }
    df_st1 = pd.read_csv(student_csv_file1,sep=",",dtype=dt_st1)

    student_csv_file2 = "./depart_sql.csv"
    dt_dep = {
        'DId':np.string_,
        'DName':np.string_
    }
    df_dep = pd.read_csv(student_csv_file2,sep=",",dtype=dt_dep)
    print(df_st1)
    print(df_dep)
    
    # merge
    df_merge = pd.merge(df_st1, df_dep,left_on='DepId', right_on='DId',how='inner')
    df_school = pd.merge(df_st1,df_dep, left_on="depid", right_on="did")
    print(df_merge)

    return None

def main():
    #testpd1()
    #testpd2()
    testpd3()
    return None

if __name__ == '__main__':
    main()