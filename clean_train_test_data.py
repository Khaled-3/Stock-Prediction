import numpy as np
from fetching_data import Fetching as ft

class Clean_spliting_data:
    #cleaning data and converting the columns to lowercase  
    def clean_data(uncleaned_data):
        cleaned_data = {}
        for d in uncleaned_data.keys():
            data = uncleaned_data[d]
            data.drop(['Dividends','Stock Splits'],axis = 1,inplace=True)
            data = data.reset_index()
            data = data.rename(columns={'Date': 'date','Open':'open','High':'high','Low':'low','Close':'close',
                                'Volume':'volume'})
            data['date'] = data['date'].dt.tz_localize(None)
            cleaned_data[d] = data
        return cleaned_data
    
    final_data = clean_data(ft.main_data)


    #scalling the data 
    def train_test_split(s_data):
        all_data_train = {}
        all_data_test = {}
        all_val_data = {}
        for name in s_data.keys():
            dat = s_data[name]['close']
            dat = np.array(dat).reshape(-1,1)
            q_1 = int(len(dat) * .7)
            q_2 = int(len(dat) * .85)
            
            train_data,test_data=dat[0:q_1,:],dat[q_2:,:1]
            val_data = dat[q_1:q_2]
            all_data_train[name] =train_data
            all_data_test[name] = test_data
            all_val_data[name] = val_data
        return all_data_train,all_data_test,all_val_data

    
    train_data,test_data,val_data = train_test_split(final_data)
    

