import pandas as pd, numpy as np

def resampleColumn(df, col_name):
    
    df[col_name].replace(0.0, np.nan, inplace=True)
    
    dist = df[col_name].value_counts(normalize=True)
    
    missing = df[col_name].isnull()
    
    np.random.seed(42)
    df.loc[missing, col_name] = np.random.choice(dist.index, size=len(df[missing]),p=dist.values)
    
    return df