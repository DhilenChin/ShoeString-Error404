import pandas as pd
import numpy as np

df = pd.read_csv('milling_machine.csv')
df['Points'] = 0

def giving_points (response, df, machine, trouble, analysis, solution):
    #input should only be 'yes' or 'no' , anything else shld be converted to these two
    # df is dataframe and everything else is a string
    if response == 'yes':
        for i in  range (len(df)):
            if df.iloc[i, 0] == machine and df.iloc[i, 1] == trouble and df.iloc[i, 2] == analysis and df.iloc[i, 3] == solution:
                df.iloc[i, 4] =+1 
                
        
    df = df.sort_values(['Trouble', 'Points'], ascending = [True, False])
    df.reset_index(drop = True, inplace = True)
    return df


machine = 'Milling Machine'
trouble = 'The workpiece milled is not flat'
analysis = 'Are the gibs of X, Y axis loose?'
solution = "Adjust the gibs' gap"



df = giving_points('yes', df, machine, trouble, analysis, solution)

print(df)