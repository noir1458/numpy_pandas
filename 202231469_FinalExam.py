"""
Spring, 2023 Python for Finance: Final Exam
"""
import re                as regex
import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# @brief    the prototypes of your functions
# @param    please replace them with your variables
# @param    ...
def count_amateur_players(df_players):
    # your code
    #print(df_players)
    df_players['is_A'] = df_players["PType"].str.contains("A")
    is_A_true = df_players['is_A'] == True
    return print(df_players[is_A_true].count()[0])

def search_sp_captain_2nd_league(df_teams,df_players):
    # your code
    #df_players = 
    #print(df_players)
    #print(df_teams)
    df_players = df_players.astype({'PNo':np.str_})
    df_teams = df_teams.astype({'CNo':np.str_})
    df_merge = pd.merge(df_players,df_teams,left_on='PNo',right_on='CNo')
    #print(df_merge)

    #나이
    df_merge['BDate2'] = df_merge.BDate.str.extract('(\d\d\d\d-)') #년도 추출
    df_merge['BDate3'] = df_merge.BDate2.str.extract('(\d\d\d\d)') 
    df_merge = df_merge.astype({'BDate3':np.int32})
    df_merge['age'] = 2023 - df_merge['BDate3']

    #print(df_merge)
    is_sp_and_2nd = (df_merge['PType'] == 'SP') & (df_merge['Division'] == '2-nd')
    sp_and_2nd = df_merge[is_sp_and_2nd]
    #print(sp_and_2nd[['PName','BDate','Address']])
    
    return sp_and_2nd[['PName','age','Address']]

def search_dirtiest_player(df_penalties,df_players): ##
    # your code
    print(df_penalties)
    df_players = df_players.astype({'PNo':np.str_})
    df_penalties = df_penalties.astype({'PNo':np.str_})
    df_merge = pd.merge(df_players,df_penalties,left_on='PNo',right_on='PNo')
    print(df_merge)
    
    # 5번 이상 낸 선수 찾기
    up5 = df_merge.groupby(['PNo']).count()
    print(up5)

    # 5번 이상 낸 선수중 많은 벌금낸 선수
    amount_max = df_merge.groupby(['PAmount']).sum()
    print(amount_max)
    
    # 벌금의 총액은?

    pass 

def search_treasurer_players(df_players,df_committees):
    # your code
    #print(df_committees)
    #print(df_players)

    df_players = df_players.astype({'PNo':np.str_})
    df_committees = df_committees.astype({'PNo':np.str_})
    df_merge = pd.merge(df_players,df_committees,left_on='PNo',right_on='PNo')
    #print(df_merge)

    # 경리
    is_Treasurer = df_merge['Position'] == 'Treasurer'
    Treasurer_true = df_merge[is_Treasurer]
    print(Treasurer_true)
    
    # 기간 정규식으로
    Treasurer_true['a'] = df_merge.Duration.str.extract('(\d\d\d\d-\d\d-\d\d )') 
    Treasurer_true['b'] = df_merge.Duration.str.extract('( \d\d\d\d-\d\d-\d\d)') 
    Treasurer_true['a'] = df_merge.a.str.extract('(\d\d\d\d-\d\d-\d\d)') 
    Treasurer_true['b'] = df_merge.b.str.extract('(\d\d\d\d-\d\d-\d\d)') 
    print(Treasurer_true)

    Treasurer_true['1_d'] = pd.to_datetime(Treasurer_true['a'])
    Treasurer_true['2_d'] = pd.to_datetime(Treasurer_true['b'])
    Treasurer_true['d'] = Treasurer_true['2_d'] - Treasurer_true['1_d']

    print(Treasurer_true)
    
    
    return None

def plot_penalty_amount(df_penalties):
    # your code
    print(df_penalties)
    
    df_penalties['y'] = df_penalties.PDate.str.extract('(\d\d\d\d-)') 
    df_penalties['y'] = df_penalties.y.str.extract('(\d\d\d\d)') 
    print(df_penalties)
    #df_result = df_penalties.merge('')

    df_result = df_penalties.groupby(['y']).sum()
    df_result['y'] = df_result.index
    #print(df_result)
    #print(df_result.index)
    
    color_names = list(mcolors.CSS4_COLORS)
    fig ,axis = plt.subplots(figsize=(10,8))
    axis.set_title('The Total Amount of Penalties per Year')
    axis.set_xlabel('Years')
    axis.set_ylabel('Amount(Won)')
    xvalues = df_result['y']
    yvalues = df_result['PAmount']
    axis.bar(xvalues,yvalues,color = color_names)
    axis.legend(title = 'index')
    
    plt.show()
    

    pass 

# @brief    the main entry
def main():
    # data loading
    # 1.1 file paths
    players_path    = "./players.csv"
    teams_path      = "./teams.csv"
    matches_path    = "./matches.csv"
    penalities_path = "./penalties.csv"
    committees_path = "./committees.csv"
    # 1.2 user-defined data types
    dt_players      = {"PNo": np.int16, "PName": np.str_, "BDate": np.str_, "JDate": np.str_, 
                       "Sex": np.str_, "Address": np.str_, "PCode": np.str_, "Mobile": np.str_, "PType": np.str_}
    dt_teams        = {"TNo": np.int16, 
                       "CNo": np.int16, 
                       "Division": np.str_}
    dt_matches      = {"MNo": np.int16, "TNo": np.int16, "PNo": np.int16, "Win": np.int32, "Loss": np.int32}
    dt_penalties    = {"PNo": np.int16, "PId": np.int16, "PDate": np.str_, "PAmount": np.float64}
    dt_committees   = {"PNo": np.int16, "SDate": np.str_, "EDate": np.str_, "Position": np.str_}
    # 1.3 data frames for each CSV file
    df_players      = pd.read_csv(players_path, dtype=dt_players, delimiter=",")
    df_teams        = pd.read_csv(teams_path, dtype=dt_teams, delimiter=",")
    df_matches      = pd.read_csv(matches_path, dtype=dt_matches, delimiter=",")
    df_penalties    = pd.read_csv(penalities_path, dtype=dt_penalties, delimiter=",")
    df_committees   = pd.read_csv(committees_path, dtype=dt_committees, delimiter=",")

    # problems
    # 2.1 problem #1
    #count_amateur_players(args, ...)
    


    count_amateur_players(df_players)
    search_sp_captain_2nd_league(df_teams,df_players)
    search_dirtiest_player(df_penalties,df_players)
    search_treasurer_players(df_players,df_committees)
    plot_penalty_amount(df_penalties)


    # your code

    return None

if ("__main__" == __name__):
    main()
