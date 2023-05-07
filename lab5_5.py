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
    student_csv_file = "./student.csv"
    df_student = pd.read_csv(student_csv_file,sep=",")
    #print(df_student)

    df_gb_years = df_student.groupby('years')
    print(df_gb_years)          # <= groupby
                                # SELECT * FROM STUDENT GROUP BY YEARS
    print(df_gb_years.mean())   # <= aggregate by mean() <= general function
    print(df_gb_years.count())
    return None

def main():
    #testpd1()
    testpd2()
    return None

if __name__ == '__main__':
    main()