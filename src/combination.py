def combine_ref_df(df, south_list):
    import pandas as pd
    ls_country_df= df['Country'].values.tolist()
    df.set_index(['Country'], inplace=True) 
    
    lst_n_s=[]
    for i in ls_country_df:
        if i in south_list:
            lst_n_s.append("south")
        else:
            lst_n_s.append("north")
    dict_={"hemisphere":lst_n_s, "Country": ls_country_df}
    df_hemisphere=pd.DataFrame(dict_)
    df_hemisphere.set_index(['Country'], inplace=True) 
    df_concat = pd.concat([df, df_hemisphere], axis=1)
    
    return df_concat