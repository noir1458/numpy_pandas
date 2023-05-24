import numpy as np
import pandas as pd

def given_func(parameters):
# your code
    return None

    # @brief: Basic 첫번째 문제
    # @param df_hotel - 호텔 이름과 City 열을 가져오기
def _basic_problem_1(df_hotel):
    # your code
    # Seongnam에 위치한 모든 호텔의 이름 출력
    is_Seongnam = df_hotel['City'] == 'Seongnam'
    df_hotel_Seongnam = df_hotel[is_Seongnam]
    return df_hotel_Seongnam['hName']

    # @brief: Basic 두번째 문제
    # @param df_guest - 주소와 이름 정보를 가진 열을 불러오기
def _basic_problem_2(df_guest):
    # your code
    # 테네시주에 사는 모든 고객의 ID와 이름을 이름의 오름차순의 정렬하여 출력
    # 테네시주 = TN
    is_TN = df_guest['gAddress'].str.contains('TN')
    df_guest_TN = df_guest[is_TN]
    return df_guest_TN[['gId','gName']].sort_values(by='gName', ascending=True)

    # @brief: Basic 세번째 문제
    # @param df_boooking - from, to시간 정보를 가진 dataframe 불러오기
def _basic_problem_3(df_boooking):
    # your code
    # 7월달에 투숙 예정인 고객의 총 인원을 출력
    df_boooking['From_month'] = df_boooking['From'].str.split('-').str[1]
    df_boooking['To_month'] = df_boooking['To'].str.split('-').str[1]
    df_boooking = df_boooking.astype({'From_month':np.int32,'To_month':np.int32})
    # (from_month가 7보다 작거나 같은 경우) and (to_month가 7보다 크거나 같은)
    df_boooking['7m_check'] = (df_boooking['From_month'] <= 7) & (df_boooking['To_month'] >= 7)
    
    # True 개수를 count해서 return
    m7_true = df_boooking['7m_check'] == True
    # 각 열별로 데이터 개수를 count하게 되는데. 모두 똑같은 값이므로 하나만 뽑으면 된다.
    return df_boooking[m7_true].count()[0]

    # @brief: Basic 네번째 문제
    # @param df_boooking - 고객ID와 from, to시간 정보를 가진 dataframe 불러오기
def _basic_problem_4(df_boooking):
    # your code
    # Regular expression과 pandas.Series.str을 이용하여 7월달에 투숙 예정인 고객의 ID를 출력하시오
    # 월에 대한 정보는 -00- 형태로 대쉬 안에 있다.
    df_boooking['From_month_R'] = df_boooking.From.str.extract('(-\d\d-)')
    # -00- 에서 안에 있는 숫자만 추출한다
    df_boooking['From_month_R'] = df_boooking.From_month_R.str.extract('(\d\d)')
    df_boooking['To_month_R'] = df_boooking.To.str.extract('(-\d\d-)')
    df_boooking['To_month_R'] = df_boooking.To_month_R.str.extract('(\d\d)')
    
    df_boooking = df_boooking.astype({'From_month_R':np.int64,'To_month_R':np.int64})
    is_m7True = (df_boooking['From_month_R'] <= 7) & (df_boooking['To_month_R'] >= 7)
    m7_true = df_boooking[is_m7True]
    return m7_true['guestId']

    # @brief: Basic 다섯번째 문제
    # @param df_room - 객실가격 정보 가져오기
def _basic_problem_5(df_room):
    # your code
    # 객실 가격의 Median, Average을 구하시오
    price_median = np.median(df_room[['Price']])
    price_average = np.average(df_room[['Price']])
    return [price_median,price_average]

    # @brief: Basic 여섯번째 문제
    # @param df_hotel - 호텔ID 가져오기 
    # @param df_boooking - from,to 시간정보와 hotelId 가져오기
def _basic_problem_6(df_hotel,df_boooking):
    # your code
    # 호텔별 호텔의 ID와 투숙일수의 평균을 구하시오
    # 투숙일수 구하기
    df_boooking['From_date'] = pd.to_datetime(df_boooking['From'])
    df_boooking['To_date'] = pd.to_datetime(df_boooking['To'])
    df_boooking['days'] = df_boooking['To_date'] - df_boooking['From_date']
    #print(df_boooking)
    #df_boooking['From_date'] = df_boooking['From'].apply(lambda x:pd.to_datetime(str(x),format='%Y-%m-%d'))
    #df_boooking['To_date'] = df_boooking['To'].apply(lambda x:pd.to_datetime(str(x),format='%Y-%m-%d'))
    #print(df_boooking.dtypes)
    #print(df_hotel)
    df_hotel = df_hotel.astype({'hId':np.str_})
    #print(df_boooking)
    df_boooking = df_boooking.astype({'hotelId':np.str_})
    df_merge = pd.merge(df_hotel,df_boooking,left_on='hId',right_on='hotelId',how='inner')
    df_merge2 = df_merge[['hName','hId','days']]
    result = df_merge2.groupby(['hName','hId']).mean()
    return result

    # @brief: Basic 일곱번째 문제
    # @param df_hotel - 호텔 이름 가져오기 위한 dataframe
    # @param df_room - 객실 유형과 가격 가져오기 위한 dataframe
def _basic_problem_7(df_hotel,df_room):
    # your code
    # Double tree 호텔에서 서비스하는 모든 객실의 유형과 가격을 출력하시오
    df_room = df_room.astype({'hotelId':np.str_})
    df_room['hotelId_l'] = df_room['hotelId'].str.lstrip()
    df_hotel = df_hotel.astype({'hId':np.str_})
    df_merge = pd.merge(df_room,df_hotel,left_on='hotelId_l',right_on='hId',how='inner')
    is_DoubleTree = df_merge['hName'] == 'Double tree'
    result = df_merge[is_DoubleTree]
    return result[['Type','Price']]

    # @brief: Basic 첫번째 문제
    # @param df_hotel - 호텔 이름 가져오기 위한 dataframe
    # @param df_boooking - 11월달에 투숙했는지 판단, check-in날짜 가져오기 위한 dataframe
    # @param df_guest - 고객이름 가져오기 위한 dataframe
def _basic_problem_8(df_hotel,df_boooking,df_guest):
    # your code
    # 2023년 11월 달에 Conrad 호텔에 투숙하여는? 모든 고객의 이름과 Check-in 날짜를 출력하시오
    df_hotel = df_hotel.astype({'hId':np.str_})
    df_boooking = df_boooking.astype({'hotelId':np.str_})
    df_merge = pd.merge(df_hotel,df_boooking,left_on='hId',right_on='hotelId',how='inner')

    df_merge = df_merge.astype({'guestId':np.str_})
    df_guest = df_guest.astype({'gId':np.str_})
    df_merge2 = pd.merge(df_merge,df_guest,left_on='guestId',right_on='gId',how='inner')

    Q1 = (df_merge2['From'].str[6:8].apply(int) <= 11) & (df_merge2['To'].str[6:8].apply(int) >= 11) # 11월달에 투숙했는가?
    Q2 = df_merge2['hName'] == 'Conrad' # Conrad 호텔인가?
    #print(Q2)
    result = df_merge2[Q1 & Q2]
    return result[['gName','From']]

    # @brief: Basic 아홉번째 문제
    # @param df_hotel - 호텔 이름 가져오기 위한 dataframe
    # @param df_boooking - 7월 예약 판단하기 위한 dataframe
    # @param df_room - 요금 판단하기 위한 dataframe
def _basic_problem_9(df_hotel,df_room,df_boooking):
    # your code
    # 모든 호텔은 예약 시점에서 객실요금의 선결제가 이루어진다고 가정하자.
    # 이때 2023년 7월 예약으로 Marriott호텔에 지불되는 금액의 총액을 출력하시오

    # hotelId와 roomNo를 같이 맞추어야 하므로 새로운 열에 hotelid-roomNo 형태로 작성
    df_room = df_room.astype({'hotelId':np.str_,'rNo':np.str_})
    df_room['hotel-room'] = df_room['hotelId'] + '-' +df_room['rNo']
    #print(df_room)
    df_boooking = df_boooking.astype({'hotelId':np.str_,'roomNo':np.str_})
    df_boooking['hotel-room'] = df_boooking['hotelId'] + '-' + df_boooking['roomNo']
    #print(df_boooking)
    df_merge = pd.merge(df_room,df_boooking,on='hotel-room',how='inner')
    #print(df_merge.dtypes)

    df_hotel = df_hotel.astype({'hId':np.str_})
    df_merge2 = pd.merge(df_merge,df_hotel,left_on='hotelId_x',right_on='hId',how='inner')
    #print(df_merge2)

    # 7월 예약인것
    is_m7 = df_merge2['From'].str[6:8] == '07'
    # Marriott 호텔인것
    is_Marriott = df_merge2['hName'] == 'Marriott'
    #print(is_m7)
    #print(is_Marriott)
    result = df_merge2[is_m7 & is_Marriott]
    return sum(result['Price'])

    # @brief: Basic 열번째 문제
    # @param df_hotel - 호텔 이름 가져오기 위한 dataframe
    # @param df_room - 각 호텔의 객실 정보 가져오기 위한 dataframe
def _basic_problem_10(df_hotel,df_room):
    # your code
    # Knoxville에 있는 각 호텔의 객실의 수를 출력하시오
    df_room = df_room.astype({'hotelId':np.str_})
    df_room['hotelId_l'] = df_room['hotelId'].str.lstrip()
    df_hotel = df_hotel.astype({'hId':np.str_})
    df_merge = pd.merge(df_hotel,df_room,left_on='hId',right_on='hotelId_l',how='inner')

    is_Knoxville = df_merge['City'] == 'Knoxville'
    Knoville_true = df_merge[is_Knoxville][['hName','rNo']]
    # groupby로 묶어서 호텔 단위로 rNo개수를 센다.
    return Knoville_true.groupby(['hName']).count()

# @brief: adv 첫번째 문제
# @param df_hotel - normalize 시킬 data 가져오기
def _adv_problem_1(df_data):
    #Problem #1 with pandas.DataFrame.transform()
    return df_data['Price'].transform(normalize)

def normalize(x):
    return (x - x.mean()) / x.std()

def _adv_problem_2(df_room,df_boooking):
    #Problem#2 with pandas.DataFrame.apply()
    # 객실/월별 수입을 구한 dataframe인 df_marriott_top 구하기
    # top() 함수를 Dataframd.apply()와 결합하여 결과 출력

    df_room = df_room.astype({'hotelId':np.str_,'rNo':np.str_})
    df_room['hotel-room'] = df_room['hotelId'] + '-' +df_room['rNo']
    df_boooking = df_boooking.astype({'hotelId':np.str_,'roomNo':np.str_})
    df_boooking['hotel-room'] = df_boooking['hotelId'] + '-' + df_boooking['roomNo']
    df_merge = pd.merge(df_room,df_boooking,on='hotel-room',how='inner')
    df_merge['month'] = df_merge['From'].str[6:8]
    df_merge2 = df_merge[['hotelId_x','rNo','Price','month']]
    #print(df_merge2)

    df_marriott_top = df_merge2.groupby(['hotelId_x','rNo','month']).sum()
    #print(df_marriott_top)
    return df_marriott_top.apply(top)

# @brief selects the rows with the largest values in a particular column
# @param df a DataFrame
# @param n # of rows
# @param col the name of a specific column
def top(df, n=3, col=['hotelId_x']):
    # 주어진 dataframe에 groupby를 적용하여 특정 column에 있는 값들이 묶이고 
    # 그 중에서 최대값을 갖는 row들을 찾아서 처음 n개만 출력하는 함수 작성
    return df.groupby(col).max().head(n)


def main():
    dt_hotel = {
        'hId':np.int16, #3digit
        'hName':np.unicode_,
        'City':np.unicode_
    }
    df_hotel = pd.read_csv('./hotel.csv',sep=',',dtype=dt_hotel)
    # csv 파일 콤마 뒤에 공백이 있으므로, 앞에 공백이 붙어야 한다
    room_type = [' penthouse', ' deluxe', ' standard',' family',' king', ' double']
    dt_room = {
        'rNo':np.int16, #3digit
        'hotelId':np.int16, #3digit
        'Type':pd.CategoricalDtype(categories=room_type),
        'price':np.float16
    }
    df_room = pd.read_csv('./room.csv',sep=',',dtype=dt_room)
    dt_boooking = {
        'hotelId':np.int16, #3digit
        'guestId':np.int8,  #2digit
        'roomNo':np.int16,  #3digit
        'From':np.unicode_, #S10
        'To':np.unicode_ #S10
    }
    df_boooking = pd.read_csv('./boooking.csv',sep=',',dtype=dt_boooking)
    dt_guest = {
        'gId':np.int8, #2digit
        'gName':np.unicode_, #S30
        'gAddress':np.unicode_ #S50
    }
    df_guest = pd.read_csv('./guest.csv',sep=',',dtype=dt_guest)
    # call functions
    
    
    print('1. Seongnam에 위치한 모든 호텔의 이름을 출력하시오',_basic_problem_1(df_hotel),'',sep='\n')
    print('2. 테네시주에 사는 모든 고객의 ID와 이름을 이름의 오름차순의 정렬하여 출력하시오.',_basic_problem_2(df_guest),'',sep='\n')
    print('3. 7월 달에 투숙 예정인 고객의 총 인원을 출력하시오.',_basic_problem_3(df_boooking),'',sep='\n')
    print('4. Regular expression과 pandas.Series.str 를 이용하여 7월달에 투숙 예정인 고객의 ID를 출력',_basic_problem_4(df_boooking),'',sep='\n')
    print('5. 객실 가격의 Median, Average를 구하시오.',_basic_problem_5(df_room),'',sep='\n')
    print('6. 호텔별 호텔의 ID와 투숙일수의 평균을 구하시오.',_basic_problem_6(df_hotel,df_boooking),'',sep='\n')
    print('7. Double tree 호텔에서 서비스하는 모든 객실의 유형과 가격을 출력하시오.',_basic_problem_7(df_hotel,df_room),'',sep='\n')
    print('8. 2023년 11월 달에 Conrad 호텔에 투숙하여는 모든 고객의 이름과 Check-in 날짜를 출력하시오.',_basic_problem_8(df_hotel,df_boooking,df_guest),'',sep='\n')
    # (11월달 conrad에 투숙하는 고객 없음)
    print('9. 2023년 7월 예약으로 Marriott 호텔에 지불되는 금액의 총액을 출력하시오.',_basic_problem_9(df_hotel,df_room,df_boooking),'',sep='\n')
    print('10. Knoxville에 있는 각 호텔의 객실의 수를 출력',_basic_problem_10(df_hotel,df_room),'',sep='\n')
    
    print('adv1.',_adv_problem_1(_basic_problem_7(df_hotel,df_room)),'',sep='\n')
    print('adv2.',_adv_problem_2(df_room,df_boooking),'',sep='\n')

    return None

if ("__main__" == __name__):
    main()