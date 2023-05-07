import numpy as np
import pandas as pd

def testpd1():
    #crime_loc
    crime_loc = {
        'latitude':[38.65042047,
                    37.47350069,
                    38.65784584,
                    38.50677377],
        'longitude':[-121.3914158,
                     -121.4901858,
                     -121.4621009,
                     -121.4269508]
    }
    #df_crime_loc
    df_crime_loc = pd.DataFrame(crime_loc)
    #print(df_crime_loc)
    #print(df_crime_loc.head())
    print(df_crime_loc.describe())
    print('')

    '''
    sr_df_crime_loc_lat = df_crime_loc['latitude']
    # descriptive statistics
    # min max mean std mode median
    sr_min = sr_df_crime_loc_lat.min()
    print(sr_min)
    sr_mean = sr_df_crime_loc_lat.mean()
    print(sr_mean)
    sr_mode = sr_df_crime_loc_lat.mode()
    print(sr_mode)
    sr_median = sr_df_crime_loc_lat.median()
    print(sr_median)

    # 행을 가져오기
    tmp = df_crime_loc.iloc[1]
    print(tmp.mean())
    '''

    # list the ranking
    print(df_crime_loc[['latitude']].rank())
    # crime location.latitude > 38.3

    # df_crime_loc['check'] = df_crime_loc[['latitude']] > 38.6 # 열 하나를 추가한다.
    df_crime_loc_tag = df_crime_loc[['latitude']] > 38.6
    print(df_crime_loc_tag)
    print(df_crime_loc_tag.any())
    # result
    print(df_crime_loc[df_crime_loc_tag])
    return None

def main():
    testpd1()
    return None

if __name__ == '__main__':
    main()