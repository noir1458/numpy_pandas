import numpy as np
import pandas as pd

def given_func(parameters):
# your code
    return None

    # @brief: Basic 첫번째 문제
    # @param para1 what for
    # @param para2 what for
def _basic_problem_1(df_hotel):
    # your code
    # Seongnam에 위치한 모든 호텔의 이름 출력
    is_Seongnam = df_hotel['City'] == 'Seongnam'
    df_hotel_Seongnam = df_hotel[is_Seongnam]
    return df_hotel_Seongnam['hName']

def _basic_problem_2(df_guest):
    # your code
    # 테네시주에 사는 모든 고객의 ID와 이름을 이름의 오름차순의 정렬하여 출력
    # 테네시주 = TN
    is_TN = df_guest['gAddress'].str.contains('TN')
    df_guest_TN = df_guest[is_TN]
    return df_guest_TN[['gId','gName']].sort_values(by='gName', ascending=True)

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

def _basic_problem_4(df_boooking):
    # your code
    # Regular expression과 pandas.Series.str을 이용하여 7월달에 투숙 예정인 고객의 ID를 출력하시오
    
    return None

def _basic_problem_5(df_room):
    # your code
    # 객실 가격의 Median, Average을 구하시오
    price_median = np.median(df_room[['Price']])
    price_average = np.average(df_room[['Price']])
    return [price_median,price_average]

def _basic_problem_6(para1,param2):
    # your code
    # 호텔별 호텔의 ID와 투숙일수의 평균을 구하시오
    return None

def _basic_problem_7(para1,param2):
    # your code
    # Double tree 호텔에서 서비스하는 모든 객실의 유형과 가격을 출력하시오
    return None

def _basic_problem_8(para1,param2):
    # your code
    # 2023년 11월 달에 Conrad 호텔에 투숙하여는? 모든 고객의 이름과 Check-in 날짜를 출력하시오
    return None

def _basic_problem_9(para1,param2):
    # your code
    # 모든 호텔은 예약 시점에서 객실요금의 선결제가 이루어진다고 가정하자.
    # 이때 2023년 7월 예약으로 Marriott호텔에 지불되는 금액의 총액을 출력하시오
    return None

def _basic_problem_10(para1,param2):
    # your code
    # Knoxville에 있는 각 호텔의 객실의 수를 출력하시오
    return None

def _adv_problem_1():
    #Problem #1 with pandas.DataFrame.transform()
    return None

def _adv_problem_1():
    #Problem#2 with pandas.DataFrame.apply()
    return None

def main():
    dt_hotel = {
        'hId':np.int8,
        'hName':np.unicode_,
        'City':np.unicode_
    }
    df_hotel = pd.read_csv('./hotel.csv',sep=',',dtype=dt_hotel)
    dt_room = {
        'rNo':np.int8,
        'hotelId':np.int8,
        'Type':np.unicode_,
        'price':np.float16
    }
    df_room = pd.read_csv('./room.csv',sep=',',dtype=dt_room)
    dt_boooking = {
        'hotelId':np.int32,
        'guestId':np.int8,
        'roomNo':np.int16,
        'From':np.unicode_,
        'To':np.unicode_
    }
    df_booking = pd.read_csv('./boooking.csv',sep=',',dtype=dt_boooking)
    dt_guest = {
        'gId':np.int16,
        'gName':np.unicode_,
        'gAddress':np.unicode_
    }
    df_guest = pd.read_csv('./guest.csv',sep=',',dtype=dt_guest)
    # call functions
    print('1. Seongnam에 위치한 모든 호텔의 이름을 출력하시오',_basic_problem_1(df_hotel),'',sep='\n')
    print('2. 테네시주에 사는 모든 고객의 ID와 이름을 이름의 오름차순의 정렬하여 출력하시오.',_basic_problem_2(df_guest),'',sep='\n')
    print('3. 7월 달에 투숙 예정인 고객의 총 인원을 출력하시오.',_basic_problem_3(df_booking),'',sep='\n')
    print('4. Regular expression과 pandas.Series.str 를 이용하여 7월달에 투숙 예정인 고객의 ID를 출력',_basic_problem_4(df_booking),'',sep='\n')
    print('5. 객실 가격의 Median, Average를 구하시오.',_basic_problem_5(df_room),'',sep='\n')
    '''
    print('6. 호텔별 호텔의 ID와 투숙일수의 평균을 구하시오.',_basic_problem_5(df_booking),'',sep='\n')
    print('7. Double tree 호텔에서 서비스하는 모든 객실의 유형과 가격을 출력하시오.',_basic_problem_5(df_booking),'',sep='\n')
    print('8. 2023년 11월 달에 Conrad 호텔에 투숙하여는 모든 고객의 이름과 Check-in 날짜를 출력하시오.',_basic_problem_5(df_booking),'',sep='\n')
    print('9. 2023년 7월 예약으로 Marriott 호텔에 지불되는 금액의 총액을 출력하시오.',_basic_problem_5(df_booking),'',sep='\n')
    print('10. Knoxville에 있는 각 호텔의 객실의 수를 출력',_basic_problem_5(df_booking),'',sep='\n')
    '''


    return None

if ("__main__" == __name__):
    main()