import numpy as np
import pandas as pd

# read a CSV file => inject the CSV file into a Dataframe
def testpd1():
    # new data type in form of dictionary
    dt_crimes = {
        # 'column_name' : data_type
        'cdatetime': np.str_,
        'address': np.str_,
        'district':np.int8,
        'beat':np.object_,
        'grid':np.str_,
        'crimedescr':np.str_,
        'ucr_ncic_code':"S4",
        'latitude':np.float32,
        'longitude':np.float32
    }

    crime_csv_path = "./SacramentocrimeJanuary2006.csv"
    df_csv = pd.read_csv(crime_csv_path,dtype=dt_crimes,sep=",")
    print('head :\n',df_csv.head())
    # 유닉스 명령어 head tail default 5줄

    print(df_csv.dtypes)
    #print('Dataframd Size = ',df_csv.memory_usage())
    #print(df_csv.size)

    print('length =',df_csv.iloc[0,:].nbytes) # Series 의 attribute

    return None
    
def testpd2():
    csv_path = './ratings.csv'
    dt_ratings = {
    #    userId,movieId,rating,timestamp
        'userId':'S8',
        'movieId':'S8',
        'rating':np.float16,
        'timestamp':np.int64
    }
    df_ratings = pd.read_csv(csv_path,dtype=dt_ratings)
    #print(df_ratings.tail())
    #print(df_ratings.dtypes)
    
    print(df_ratings.index)
    print(df_ratings.columns)
    
    row_1 = df_ratings.iloc[1]
    print('row_1 :\n',row_1)
    print('row_1[1] :\n',row_1[1]) # 한줄이라서 Series로 변해서 가능. 그러나 쓰지말것. iat iloc 쓰기
    print('rating' in row_1)
    print(row_1['rating'])
    return None

def testpd3():
    crime_xls_file   = "./SacramentocrimeJanuary2006.xls"
    df_csv = pd.read_excel(crime_xls_file)
    print('head :\n',df_csv.head())
    return None

def main():
    testpd1()
    print('--------------')
    testpd2()
    print('--------------')
    testpd3()
    return None

if __name__ == '__main__':
    main()