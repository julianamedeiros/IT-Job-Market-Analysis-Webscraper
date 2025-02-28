import pandas as pd

def cleaning(dictionary):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(dictionary)
    df.reset_index(inplace=True)
    df = df.rename(columns= {'index' : 'offer_id'})
    df = df.explode('technologies') 

    #print(df.head(10))

    # Data cleaning (casting types for columns, dealing with null values)
    df['job_title'] = df['job_title'].astype('string')
    df['level'] = df['level'].astype('string')
    df['technologies'] = df['technologies'].astype('string')
    #print(df.dtypes)

    # Renaming level {pratykant/intern, junior, mid, senior}

    df['level'] = df['level'].replace(to_replace=r'(?i).*Senior.*', value='Senior', regex=True)
    df['level'] = df['level'].replace(to_replace=r'(?i).*expert.*', value='Senior', regex=True)
    df['level'] = df['level'].replace(to_replace=r'(?i).*ekspert.*', value='Senior', regex=True)
    df['level'] = df['level'].replace(to_replace=r'(?i).*Mid.*', value='Mid', regex=True)
    df['level'] = df['level'].replace(to_replace=r'(?i).*Junior.*', value='Junior', regex=True)
    df['level'] = df['level'].replace(to_replace=r'(?i).*praktykant.*', value='Internship', regex=True)

    # Renaming technologies {get rid of 'Microsoft', 'Apache'. Changing Snowflake : Snowflake, Power BI : Power BI}
    df['technologies'] = df['technologies'].str.replace(r'(?i)Microsoft', '', regex=True).str.strip()
    df['technologies'] = df['technologies'].str.replace(r'(?i)Apache', '', regex=True).str.strip()
    df['technologies'] = df['technologies'].str.replace(r'(?i)Power\s*BI.*', 'Power BI', regex=True)
    df['technologies'] = df['technologies'].str.replace(r'(?i)S\s*flake', 'Snowflake', regex=True)
    #print(df)
   
    # Export to CSV files
    df.to_csv('tech_jobs.csv', index=False)  
    print('file ready!')

   

