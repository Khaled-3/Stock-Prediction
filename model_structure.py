from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import math
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '1'

import tensorflow as tf
from keras._tf_keras.keras.layers import Dense, Dropout ,GRU
from keras._tf_keras.keras.models import Sequential

from scaling_xy_spliting import Scaling_Spliting_data as sd 


class Model:
    #bulding the model structure
    
    model=Sequential([GRU(32,return_sequences=True,input_shape=(sd.time_step,1)),
        GRU(32),
        Dropout(0.20),
        Dense(1)])
    model.compile(loss='mean_squared_error',optimizer='adam')
    model.summary()

    #running the model to fit the data
    history = model.fit(sd.X_train,sd.y_train,validation_data=(sd.X_val,sd.y_val),
                        epochs=100,batch_size=32,verbose=1)

    model.evaluate(sd.X_test,sd.y_test)
    train_predict=model.predict(sd.X_train)
    test_predict=model.predict(sd.X_test)
    print(train_predict.shape, test_predict.shape)

    train_predict = sd.scaler_train['Apple Inc.'].inverse_transform(train_predict)
    test_predict = sd.scaler_test['Apple Inc.'].inverse_transform(test_predict)
    original_ytrain =sd.scaler_train['Apple Inc.'].inverse_transform(sd.y_train.reshape(-1,1))
    original_ytest = sd.scaler_test['Apple Inc.'].inverse_transform(sd.y_test.reshape(-1,1))
    print("Train data RMSE: ",math.sqrt(mean_squared_error(original_ytrain,train_predict)))
    print("Train data MSE: ", mean_squared_error(original_ytrain,train_predict))
    print("Train data MAE: ", mean_absolute_error(original_ytrain,train_predict))
    print("-------------------------------------------------------------------------------------")
    print("Test data RMSE: ",math.sqrt(mean_squared_error(original_ytest,test_predict)))
    print("Test data MSE: ", mean_squared_error(original_ytest,test_predict))
    print("Test data MAE: ", mean_absolute_error(original_ytest,test_predict))
    print("-------------------------------------------------------------------------------------")
    print("Train data R2 score:", r2_score(original_ytrain, train_predict))
    print("Test data R2 score:", r2_score(original_ytest, test_predict))


    model.save('Model.h5')


