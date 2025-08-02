import pandas as pd

def dtype_func(df):
    dtypes = df.dtypes
    n_uniq = df.nunique()
    return pd.DataFrame({'Dtypes': dtypes, 'Num_unique' : n_uniq}).T

def null_sum(df):
    null = df.isnull().sum()
    ratio = (null/df.shape[0])*100 
    return pd.DataFrame({'Null_Sum': null, 'Ratio': ratio}).T