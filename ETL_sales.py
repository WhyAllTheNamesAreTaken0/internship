import pandas as pd
import datetime as dt
import os

def length(data):
        
    data_len = data.shape[0]
        
    print(f"The amount of rows in data set: {data_len}")
    print('The amount of null values in train:',data.isna().sum().sum())
        
def delete_neg_in_price_and_sales(data):
        
    data = data[data['item_price']>0]
    data = data[data['item_cnt_day']>0]
        
    return data
    
def delete_duplicates(data):
        
    return data.drop_duplicates()

    
def date_format(data, col):
        
    data[col] = pd.to_datetime(data[col], format='%d.%m.%Y')
        
    data['year'] = data[col].dt.year
    data['month'] = data[col].dt.month
    data['day'] = data[col].dt.day
        
    return data
        
def to_file(data):
    
    data.to_csv(f'C:/datasets/sales/{data}_sls.csv')  
    