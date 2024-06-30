from sklearn.preprocessing import MinMaxScaler
from clean_train_test_data import Clean_spliting_data  as csd
import numpy as np
class Scaling_Spliting_data:
    def scaling_data(data):
        scalers = {}
        scaled_data_dict = {}

        # Fit and transform data using MinMaxScaler
        for key, data in data.items():
            scaler = MinMaxScaler(feature_range=(0, 1))
            scaled_data = scaler.fit_transform(data)
            scaled_data_dict[key] = scaled_data
            scalers[key] = scaler
        return scaled_data_dict,scalers

    scaled_train,scaler_train = scaling_data(csd.train_data)
    scaled_test,scaler_test = scaling_data(csd.test_data)
    scaled_val,scaler_val = scaling_data(csd.val_data)

    

    def create_dataset(dataset, time_step=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-time_step-1):
            a = dataset[i:(i+time_step), 0]   
            dataX.append(a)
            dataY.append(dataset[i + time_step, 0])
        return np.array(dataX), np.array(dataY)
    
    time_step = 15
    X_train, y_train = create_dataset(scaled_train['Apple Inc.'], time_step)
    X_test, y_test = create_dataset(scaled_test['Apple Inc.'], time_step)
    X_val, y_val = create_dataset(scaled_val['Apple Inc.'], time_step)

    #reshaping the data to assing it to 1 feature array 
    X_train =X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
    X_test = X_test.reshape(X_test.shape[0],X_test.shape[1] , 1)
    X_val = X_val.reshape(X_val.shape[0],X_val.shape[1] , 1)

