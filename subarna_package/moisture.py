import pandas as pd
def ingredients():
    df=pd.read_csv('soil.csv')
    c=input("Enter the type of the moisture 1 or 2")
    print("The ingredients and the quantities present in the soil are:\n")
    print(df.values[2])
    
