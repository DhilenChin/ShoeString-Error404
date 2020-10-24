import pandas as pd
import numpy as np

df = pd.read_csv('milling_machine.csv')
df['Points'] = 0


def sorting_best_solution (input, df, machine, trouble, analysis, solution):
    #input should only be 'yes' or 'no' , anything else shld be converted to these two
    # df is dataframe and everything else is a string
    if input == 'yes':
        for index, rows in df.iterrows():
            if df.iloc[index, 0] == machine and df.iloc[index, 1] == trouble and df.iloc[index, 2] == analysis and df.iloc[index, 3] == solution:
                df.iloc[index, 4] =+1 

    
machine = 'Milling Machine'
trouble = 'The workpiece milled is not flat'
analysis = 'The spindle bearing is loose'
solution = 'Adjust the spindle bearing gap'

sorting_best_solution ('yes', df, machine, trouble, analysis, solution)
print(df)

