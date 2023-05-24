''' timestamp
'''
import numpy as np
import pandas as pd

def test_timestamp():
    # 1. read csv
    # 2. conver into a dataframe
    # 3. pick a timestamp column
    # 4. convert int64_timestamp to datetime_timestamp
    tags_path = './tags.csv'
    dt_tags = {
        'userId':np.int16,
        'movieId':np.int32,
        'tag':np.str_,
        'timestamp':np.int64
    }
    df_tags = pd.read_csv(tags_path,dtype=dt_tags,sep=',')
    print(df_tags.head(5))

    df_ts = pd.to_datetime(df_tags['timestamp'], unit="s")
    # unit = s,D, ns, us, ms, ...
    print(df_ts.head(5))

    return None

def main():
    test_timestamp()
    return None

if __name__ =='__main__':
    main()