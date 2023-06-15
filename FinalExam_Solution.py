# @author : 김희상
# @date : 23/06/15


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

## 1 
## 아마추어 선수들의 인원수를 구하는 함수를 구현하시오
def count_amateur_players(df_players):
    num = len(df_players[df_players['PType'] == "A"])  ## Filtering
    return num

## 2부리그 2-nd에 속하는 팀의 준프로 SP 인 주장선수의 이름 나이와 주소를 출력하는 함수를 구현
def search_sp_captain_2nd_league(df_teams, df_players):
    _2nd = df_teams[df_teams['Division'] == '2-nd']  ## Filtering 2부리그 
    _2nd_CNo = _2nd['CNo'].values
    cap = df_players[df_players['PNo'].isin(_2nd_CNo)]
    cap = cap[cap['PType'] == 'SP']  ## Filtering SP
    cap['BDate'] = pd.to_datetime(cap['BDate']) ## dtype 변경
    cap['age'] = pd.datetime.now().year - cap['BDate'].apply(lambda x : x.year)  ## 나이 계산
    res = cap[['PName','age','Address']].copy
    return res



## 3 
## 2016년 1월 1일 이후 5번 이상의 징계로 인하여 벌금을 낼 선수들 중에서 가장 많은 벌금을 낸 선수의 이름과 벌금의 총액을 계산
def search_dirtiest_player(df_players, df_penalties):
    df_penalties['PDate'] = pd.to_datetime(df_penalties['PDate']) ## dtype 변경
    after_penalties = df_penalties[df_penalties['PDate'] > pd.to_datetime("2016-01-01")]  ## 2016년 이후
    amount_penalties = after_penalties.groupby('PNo').sum()  ## 벌금 총계
    amount_penalties.reset_index(inplace = True)
    ct_penalties = after_penalties.groupby('PNo').count()  ## 5회 이상 징계 
    ct_penalties.reset_index(inplace = True)
    ct_penalties = ct_penalties[ct_penalties['PId'] >= 5]  
    dirt_players = ct_penalties['PNo']  ## 5회 이상 징계 선수 No 추출
    amount_penalties = amount_penalties[amount_penalties['PNo'].isin(dirt_players)]
    max_amount_row = amount_penalties[amount_penalties['PAmount'] == amount_penalties['PAmount'].max()] ## 벌금 최대 선수 추출
    dirtiest_player = max_amount_row['PNo']
    dirty_name = df_players[df_players['PNo'].isin(dirtiest_player)]
    dirty_amount = max_amount_row['PAmount']
    return dirty_name['PName'][0], dirty_amount[0] 

## 4
## 정규식을 이용하여 경리(Treasurer) 업무를 역임한 선수의 이름과 재직기간을 계산하는 함수를 구현하시오
# 이때 정규식을 이용하여 재직기간에서 임명된 일자와 해임된 일자를 추출해야하며 재직기간은 총재직 일수를 의미한다.
def search_treasurer_players(df_committees, df_players):
    df_tre = df_committees[df_committees['Position'] == 'Treasurer']
    date_pattern = r'(\d{4}-\d{2}-\d{2})' ## 정규표현식
    df_tre['From'] = df_tre['Duration'].str.findall(date_pattern).apply(lambda x: '-'.join(x[:1]) if len(x) > 0 else None)
    df_tre['To'] = df_tre['Duration'].str.findall(date_pattern).apply(lambda x: '-'.join(x[1:]) if len(x) > 1 else None)
    ## 해임일자가 없는 경우는 현재까지 재직중임을 고려함
    now = pd.datetime.now().date()
    df_tre['To'] = df_tre['To'].fillna(now)
    df_tre['From'] = pd.to_datetime(df_tre['From'])
    df_tre['To'] = pd.to_datetime(df_tre['To'])
    df_tre['days'] = df_tre['To'] - df_tre['From']
    
    tre = pd.merge(df_tre, df_players, how = 'inner', on='PNo') ## PNo가 동일한 행을 병합
    return tre[['PName','days']]

## 5
## 년도별 벌금의 총계를 Bar Chart로 plotting 하는 함수를 구현하시오
def plot_penalty_amount(df_penalties):
    df_penalties['PDate'] = pd.to_datetime(df_penalties['PDate']) ## dtype 변경
    df_penalties['year'] = df_penalties['PDate'].dt.year ## year를 기준으로 변경
    year_amount = df_penalties.groupby('year').sum()  ## 년도별 벌금 총계
    year_amount.reset_index(inplace=True)
    x = year_amount['year']
    y = year_amount['PAmount']

    colors = plt.cm.get_cmap('rainbow', len(x))
    color_list = list(mcolors.CSS4_COLORS)
    ncolors = x.size
    ## OO-style 
    fig, ax = plt.subplots(figsize=(5,2.7), layout='constrained')
    ax.bar(x, y, label=x, color = color_list[:ncolors]) ## 년도별 색상 변경
    ax.set_xlabel('Years') ## xlabel 
    ax.set_ylabel('Amount (Won)') ## ylabel
    ax.set_title("The Total Amount of Penalities per Year") ## title
    ax.legend(title='Years') ## legend
    plt.show()

    return None

def main():
    players_path = './players.csv'
    teams_path = './teams.csv'
    matches_path = './matches.csv'
    penalities_path = './penalties.csv'
    committees_path = './committees.csv'
    dt_players      = {"PNo": np.int16, "PName": np.str_, "BDate": np.str_, "JDate": np.str_, 
                       "Sex": np.str_, "Address": np.str_, "PCode": np.str_, "Mobile": np.str_, "PType": np.str_}
    dt_teams        = {"TNo": np.int16, 
                       "CNo": np.int16, 
                       "Division": np.str_}
    dt_matches      = {"MNo": np.int16, "TNo": np.int16, "PNo": np.int16, "Win": np.int32, "Loss": np.int32}
    dt_penalties    = {"PNo": np.int16, "PId": np.int16, "PDate": np.str_, "PAmount": np.float64}
    dt_committees   = {"PNo": np.int16, "SDate": np.str_, "EDate": np.str_, "Position": np.str_}
    df_players = pd.read_csv(players_path, dtype = dt_players)
    df_teams = pd.read_csv(teams_path, dtype = dt_teams)
    df_matches = pd.read_csv(matches_path, dtype = dt_matches)
    df_penalties = pd.read_csv(penalities_path, dtype = dt_penalties)
    df_committees = pd.read_csv(committees_path, dtype = dt_committees)
    
#     2.1 #1
    res = count_amateur_players(df_players)
    print("#1 Problem\n The number of amateur players: ", res)
#     2.1 #2
    res = search_sp_captain_2nd_league(df_teams, df_players)
    print("#2 Problem\n The Captain of 2nd league: \n", res)
#     2.1 #3
    res = search_dirtiest_player(df_players, df_penalties)
    print(f'#3 Problem\n dirty name: {res[0]} amount : {res[1]}')
#     2.1 #4
    res = search_treasurer_players(df_committees, df_players)
    print(f'#4 Problem\n {res}')
#     2.2 #5
    plot_penalty_amount(df_penalties)



    
if ("__main__" == __name__):
    main()

