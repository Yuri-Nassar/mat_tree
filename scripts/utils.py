import pandas as pd

def get_dataset(df_name="fsny_10"):
    path= "./dataset/"

    if df_name.split('_')[0] == 'fsny':
        dtype = {'tid': 'int32', 'time': 'category', 'day': 'category', 'poi': 'category',
                 'type': 'category', 'root_type': 'category', 'rating': 'category',
                 'weather': 'category', 'label': 'category'}
        return pd.read_csv(path+df_name+"/foursquare.csv", sep=';', dtype=dtype, encoding="ISO-8859-1")
    
    elif df_name.split('_')[0] == 'basometro':
        return pd.read_csv(path+df_name+"/basometro.csv")
    
    else:
        print(f"'{df_name}' dataset does not exist! Check the available options.")

