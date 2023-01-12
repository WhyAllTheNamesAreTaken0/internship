import pandas as pd


class ETL:
    
    def __init__(this, data):
        
        this.data = data
    
    def length(this):
        
        data_len = this.data.shape[0]
        
        print(f"The amount of rows in data set: {data_len}")
        print('The amount of null values in train:',this.data.isna().sum().sum())
        
    def delete_neg_in_price_and_sales(this):
        
        this.data = this.data[this.data['item_price']>0]
        this.data = this.data[this.data['item_cnt_day']>0]
        
        return this.data
    
    def delete_duplicates(this):
        
        return this.data.drop_duplicates()
    
    def remove_outliers(this, col): ##

        Q1 = this.data[col].quantile(0.10)
        Q3 = this.data[col].quantile(0.90)
        IQR = Q3 - Q1
        this.data = this.data[~((this.data[col] < (Q1 - 1.5 * IQR)) | (this.data[col] > (Q3 + 1.5 * IQR)))]

        
        #Q1 = data['item_cnt_day'].quantile(0.10)
        #Q3 = data['item_cnt_day'].quantile(0.90)
        #IQR = Q3 - Q1
        #data = data[~((data['item_cnt_day'] < (Q1 - 1.5 * IQR)) | (data['item_cnt_day'] > (Q3 + 1.5 * IQR)))]
        
        return this.data
    
    def date_format(this, col):
        
        this.data[col] = pd.to_datetime(this.data[col], format='%d.%m.%Y')
        
        this.data['year'] = this.data[col].dt.year
        this.data['month'] = this.data[col].dt.month
        this.data['day'] = this.data[col].dt.day
        
        return this.data
    
    ###Only after date converting
    ## через get_dummies слишком большие размерности выходят, какой-то другой метод брать или оставлять пока?
    def cat_to_num(this, col):
        cat = [col for col in this.data.columns if this.data[col].dtype=='O']
        this.data
        return pd.get_dummies(this.data, columns = col)