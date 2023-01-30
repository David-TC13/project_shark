
def column_na(df): 
    df.drop (labels = ['Case Number', 'Type', 'Activity', 'Name', 'Sex ', 'Age', 'Injury', 'Fatal (Y/N)', 'Time', 'Species ', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'Unnamed: 22', 'Unnamed: 23', 'original order', 'Area', 'Location'], axis= 1, inplace= True)
    return df

def drop_duplicates(df):
    df.drop_duplicates( inplace = True) 
    df.dropna(how = 'all', inplace = True)
    return df

def year_1946(df): 
    df = df [df["Year"] >= 1946]
    df['Year'] = df['Year'].astype('str') 
    df['Year'] = df['Year'].map(lambda x: x.rstrip('.0'))
    df['Year'] = df['Year'].astype('int')
    return df

def clean_country(df):
    df.dropna(subset = ['Country'], inplace=True)
    df['Country'] = df['Country'].apply(lambda x: x.lower())
    df['Country'] = df['Country'].str.strip()
    return df

def replace_country_values(df):  
    df['Country'] = df['Country'].replace(["usa"], 'united states')
    df['Country'] = df['Country'].replace(["sudan?"], 'sudan')
    df['Country'] = df['Country'].replace(["united arab emirates (uae)"], 'united arab emirates')
    return df