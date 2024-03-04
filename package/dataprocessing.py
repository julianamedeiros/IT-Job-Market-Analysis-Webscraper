import pandas as pd

def star_scheme(dictionary):
    # convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(dictionary)
    df.reset_index(inplace=True)
    df = df.rename(columns= {'index' : 'offer_id'})
    
    #create the dimentional tables
    djob = df.drop(columns = ['technologies'])

    dtech = df.explode('technologies')
    dtech = dtech.drop(columns=['job_title', 'level', 'offer_id'])
    dtech.drop_duplicates(inplace=True)
    dtech.reset_index(drop=True, inplace=True)  
    dtech.reset_index(inplace=True)  
    dtech.rename(columns={'index': 'tech_id'}, inplace=True)  

    #create the fact table with merge
    fact = df.explode('technologies')
    fact = pd.merge(fact, dtech, on='technologies', how='left')
    fact = fact.drop(columns= ['level', 'job_title', 'technologies'])   

    #export to CSV files
    dtech.to_csv('dtech.csv', index=False)  
    djob.to_csv('djob.csv', index=False)
    fact.to_csv('fact.csv', index=False)


   

