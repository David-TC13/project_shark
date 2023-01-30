def list_country_hemisphere(l_country):
    l_country["hemisphere"]=l_country["latitude"].apply(lambda x : "north" if x>0 else "south")
    l_country['name'] = l_country['name'].apply(lambda x: x.lower())
    return (l_country)

def cleaning_ref(l_country):
    l_country.drop (labels= ['latitude','longitude'], axis= 1, inplace= True)
    l_country= l_country[l_country.hemisphere == "south"]
    l_country.reset_index(drop=True)
    south_list= l_country['name'].values.tolist()
    
    return south_list