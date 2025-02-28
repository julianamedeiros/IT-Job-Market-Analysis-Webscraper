import pandas as pd

df = pd.read_csv('tech_jobs.csv')

# Exploratory Data Analysis
print(df.head(10))
print(df.info())

# Counting unique job_offers
print(f"Total of job offers: {df['offer_id'].nunique()}") 

# Counting the occurrences of each technology
print(df['technologies'].value_counts())

# Counting the occurrences for each job level
no_duplicate_df = df.drop('technologies', axis=1)
no_duplicate_df = no_duplicate_df.drop_duplicates()
print(no_duplicate_df['level'].value_counts())

# Checking null values
print(f"Missing values per column: {df.isnull().sum()}")

# Checking the mode
print("Most common job role:", df['job_title'].mode()[0])
print("Most common technology:", df['technologies'].mode()[0])
print("Most common job level:", df['level'].mode()[0])


