import pandas as pd
def combine_ref_df(df, south_list):
    
    ls_country_df= df['Country'].values.tolist()
    df.set_index(['Country'], inplace=True)     
    lst_n_s=['south'if i in south_list else 'north' for i in ls_country_df]
    dict_={"hemisphere":lst_n_s, "Country": ls_country_df}
    df_hemisphere=pd.DataFrame(dict_)
    df_hemisphere.set_index(['Country'], inplace=True) 
    df_concat = pd.concat([df, df_hemisphere], axis=1)
    
    return df_concat