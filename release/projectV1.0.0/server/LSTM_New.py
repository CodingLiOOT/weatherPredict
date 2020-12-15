#
#
# LSTM weather prediction demo
# Written by: Dan R 2020
#
#


#
# Core Keras libraries
#
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Bidirectional
from keras.models import Sequential, load_model

#
# For data conditioning
#
from scipy.ndimage import gaussian_filter1d
from scipy.signal import medfilt

#
# Make results reproducible
#
from numpy.random import seed

#seed(1)
#from tensorflow import set_random_seed

#set_random_seed(1)

#
# Other essential libraries
#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from numpy import array
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Make our plot a bit formal
font = {'family': 'Arial',
        'weight': 'normal',
        'size': 10}
plt.rc('font', **font)

#
# Set input number of timestamps and training days
#
n_timestamp = 10
train_size = 10/12  # number of days to train from
test_size = 1/12
n_epochs = 25
filter_on = 1

#
# Select model type
# 1: Single cell
# 2: Stacked
# 3: Bidirectional
#
model_type = 2

def prediction(type,date,place):
    url = 'data\\6-'+place +'.csv'
    dataset = pd.read_csv(url)
    if type == 'tmin':
        dataset = dataset.drop(['tmax'], axis=1)
    else:
        dataset = dataset.drop(['tmin'], axis=1)

    if filter_on == 1:
        dataset[type] = medfilt(dataset[type], 3)
        dataset[type] = gaussian_filter1d(dataset[type], 1.2)

    y = dataset[-n_timestamp:].reset_index(drop=True)
    y = y.iloc[:, 1:2].values

    sc = MinMaxScaler(feature_range=(0, 1))
    y = sc.fit_transform(y)
    model = load_model('data\\LSTM-model-'+place+'-'+type+'.h5')

    for i in range(0, date):
        x_input = array(y[-n_timestamp:])
        x_input = x_input.reshape((1, n_timestamp, filter_on))
        result = model.predict(x_input, verbose=0)
        # print(x_input,result)
        # result = np.insert(result,0,values = y['date'][len(y)]+1,axis = 1)
        y = np.insert(y, 0, values=result, axis=0)

    y = sc.inverse_transform(y)

    for i in range(0,date):
        y[n_timestamp+i] = (y[n_timestamp+i] -32) /1.8


    y = pd.DataFrame(np.rint(y[n_timestamp:]))

    return y





def predict_csv(place,date):


    TYPE = ['tmax','tmin']

    y = pd.DataFrame({'Date': pd.date_range(start=time.strftime("%Y/%m/%d", time.localtime()),periods=date,freq='D')})
    for type in TYPE:
        y[type] = prediction(type, date, place)

    y.to_csv('prediction\\predict_data-' + place + '.csv', header = None,index=None)

if __name__ == '__main__':
    PLACE = ['beijing','shanghai','guangzhou','shenzhen']
    TYPE = ['tmax', 'tmin']

    y = pd.DataFrame({'Date': pd.date_range(start=time.strftime("%Y/%m/%d", time.localtime()), periods=7, freq='D')})
    for place in PLACE:
        for type in TYPE:
            y[type] = prediction(type, 7, place)

        y.to_csv('prediction\\predict_data-' + place + '.csv', header=None, index=None)