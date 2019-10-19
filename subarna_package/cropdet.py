import pandas as pd
def crop_detect():
    df=pd.read_csv('crops.csv')
    seasons=df['Unnamed: 0']
    seasons=list(seasons)
    n=[0,1,2]
    t=dict(list(zip(seasons,n)))
    soil_type=input("Enter the type of soil:\n")
    season=input("Enter the name of season:")
    print("The crops suitable for production are: ")
    print(df[soil_type][t[season]])
    