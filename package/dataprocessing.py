import pandas as pd

def star_scheme(dictionary):
    # convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(dictionary)
    df.reset_index(inplace=True)
    df = df.rename(columns= {'index' : 'offer_id'})
    df = df.explode('technologies') 

    #export to CSV files
    df.to_csv('df.csv', index=False)  

   

