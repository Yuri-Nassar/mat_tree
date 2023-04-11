import pandas as pd

def get_dataset(df_name="fsny_10"):
    path= "./dataset/"

    if df_name.split('_')[0] == 'fsny':
        return pd.read_csv(path+df_name+"/foursquare.csv", sep=',')
    elif df_name.split('_')[0] == 'basometro':
        return pd.read_csv(path+df_name+"/basometro.csv")
    else:
        print('Dataset does not exist! Check the options.')

