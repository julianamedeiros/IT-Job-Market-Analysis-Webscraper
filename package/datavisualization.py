import pandas as pd

def table(dictionary):
    df =pd.DataFrame.from_dict(dictionary)
    df.to_csv('data.csv', index=False)