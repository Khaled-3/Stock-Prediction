import numpy as np
from keras._tf_keras.keras.models import load_model
from scaling_xy_spliting import Scaling_Spliting_data as sd
model_path=r"Model.h5"
model=load_model(model_path)
class Prediction:
    #predict method 1 for future data 
    def predict_stock(data_set,scalers,days_to_predict=0):
        
        pred_data = {}
        time_step=15
        scal = scalers
        for n in data_set.keys():
            test_data = data_set[n]
            x_input=test_data[-time_step:].reshape(1,-1)
            temp_input=list(x_input)
            temp_input=temp_input[0].tolist()

            lst_output=[]
            n_steps=time_step
            i=0
            pred_days = days_to_predict
            while(i<pred_days):

                if(len(temp_input)>time_step):

                    x_input=np.array(temp_input[1:])
                    x_input = x_input.reshape(1,-1)
                    x_input = x_input.reshape((1, n_steps, 1))

                    yhat = model.predict(x_input, verbose=0)
                    temp_input.extend(yhat[0].tolist())
                    temp_input=temp_input[1:]
                

                    lst_output.extend(yhat.tolist())
                    i=i+1

                else:

                    x_input = x_input.reshape((1, n_steps,1))
                    yhat = model.predict(x_input, verbose=0)
                    temp_input.extend(yhat[0].tolist())

                    lst_output.extend(yhat.tolist())
                    i=i+1
            lst_output = scal[n].inverse_transform(np.array(lst_output).reshape(-1,1)).reshape(1,-1).tolist()
            pred_data[n] = lst_output
        return pred_data
    final_pred=predict_stock(sd.scaled_test,sd.scaler_test,1)


    #predict method 2 for all data from past to present
    def predicted_unscale(data,scalers):
        prediction_data = {}
        y_data = {}
        for n in data.keys():
            test_data = data[n]
            x_test,y_test = sd.create_dataset(test_data,15)
            x_test = x_test.reshape(x_test.shape[0],x_test.shape[1] , 1)
            predicted = model.predict(x_test,verbose =0)
            prediction_data[n] = scalers[n].inverse_transform(predicted)
            y_data[n] = scalers[n].inverse_transform(y_test.reshape(-1,1))
        return prediction_data,y_data
    present_pred,y_present = predicted_unscale(sd.scaled_test,sd.scaler_test)