import pandas as pd

def combine_sat_lat_long(df):
    df['cordinates'] = df['satlat'].astype(str) + ',' + df['satlng'].astype(str)
    return df
