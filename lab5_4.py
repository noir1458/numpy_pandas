import numpy as np
import pandas as pd

# read a CSV file => inject the CSV file into a Dataframe
def testpd1():
    crime_csv_path = "./SacramentocrimeJanuary2006.csv"
    df_csv = pd.read_csv(crime_csv_path,sep=",")
    #print(df_crime)
    #print(df_csv.head())
    
    # trim a Series named 'address'
    sr_x = df_csv[['address']]
    print(sr_x)
    #trim a DataFrame named 'address, crimedescr, grid'
    
    y = df_csv[['address','crimedescr','grid']]
    print(y)
    return None

def main():
    testpd1()
    return None

if __name__ == '__main__':
    main()