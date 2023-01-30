def concat_month(df_concat):
    import re
    
    df_concat['month'] = df_concat['Date'].apply(lambda x: re.search(r'-(\w+)-', x).group(1) if re.search(r'-(\w+)-', x) else "month_not_found")
    df_concat.month.replace({'Ap':'Apr','July': 'Jul'}, inplace =True )
    df_concat= df_concat[df_concat.month !='month_not_found'] 
    df_concat= df_concat[df_concat.month !='30']
    return df_concat
def south_season(month):
    season_month_south = {
            'Dec':'Summer', 'Jan':'Summer', 'Feb':'Summer',
            'Mar':'Autumn', 'Apr':'Autumn', 'May':'Autumn',
            'Jun':'Winter', 'Jul':'Winter', 'Aug':'Winter',
            'Sep':'Spring', 'Oct':'Spring', 'Nov':'Spring'}
    for key, value in season_month_south.items():
        if month in key:
            return value
    
def north_season(month):
    season_month_north = {
            'Dec':'Winter', 'Jan':'Winter', 'Feb':'Winter',
            'Mar':'Spring', 'Apr':'Spring', 'May':'Spring',
            'Jun':'Summer', 'Jul':'Summer', 'Aug':'Summer',
            'Sep':'Autumn', 'Oct':'Autumn', 'Nov':'Autumn'}
    for key, value in season_month_north.items():
        if key in month:
            return value