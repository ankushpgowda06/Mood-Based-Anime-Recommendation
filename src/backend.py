import pandas as pd

def age_filter(age):
    df = pd.read_csv("dataset/mood_clustered_anime.csv")
    if age < 7:
        return df[df['Rating'] == 'G - All Ages']
    elif 7 <= age < 13:
        return df[df['Rating'].isin(['G - All Ages', 'PG - Children'])]
    elif 13 <= age < 17:
        return df[df['Rating'].isin(['G - All Ages', 'PG - Children', 'PG-13 - Teens 13 or older'])]
    else: 
        return df