import pandas as pd
from prediction_method import Prediction as pre

def final_df (actual,pred):
    df_2 = {}
    for i in actual.keys():
        dict1 = {}
        dict1['actual'] = actual[i].flatten()
        dict1['predicted'] = pred[i].flatten()
        df = pd.DataFrame(dict1)
        df_2[i] = df
    return df_2
gathered_data = final_df(pre.y_present,pre.present_pred)