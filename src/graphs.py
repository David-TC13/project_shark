import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def extract_data_north(df_north):
    df_north.groupby("season").agg("count")
    sns.countplot(x=df_north.season).set(title='Northern Hemisphere');
    return sns.countplot

def extract_data_sout(df_south):
    
    df_south.groupby("season").agg("count")
    sns.countplot(x=df_south.season).set(title='Southern Hemisphere');
    return sns.countplot

def extract_data_together(df_north, df_south):
       
    df_both_hemisp_= pd.concat([df_north, df_south], ignore_index=True, sort=False)
    df_both_hemisp_.groupby("season").agg("count")
    sns.countplot(x=df_both_hemisp_.season).set(title='Both Hemispheres Together');
    return sns.countplot