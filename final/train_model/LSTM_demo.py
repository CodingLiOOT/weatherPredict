
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
seed(1)
from tensorflow import set_random_seed
set_random_seed(1)


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

# Make our plot a bit formal
font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 10}
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


# 给定城市（place）,目标类型（type),训练目标模型
def train_model(type,place):
    url = 'D:\\www\\main\\testfirst\\resource\\weather-info\\' + place+'-cleaned.csv'
    model_type = 2

    dataset = pd.read_csv(url)
    if type == 'tmax':
        dataset = dataset.drop(['tmin'], axis=1)
    else:
        dataset = dataset.drop(['tmax'], axis=1)
    if filter_on == 1:
        dataset[type] = medfilt(dataset[type], 3)
        dataset[type] = gaussian_filter1d(dataset[type], 1.2)

    #
    # Set number of training and testing data
    #
    train_days = int(len(dataset) * train_size)
    testing_days = int(len(dataset) * test_size)

    train_set = dataset[0:train_days].reset_index(drop=True)
    test_set = dataset[train_days: train_days + testing_days].reset_index(drop=True)
    training_set = train_set.iloc[:, 1:2].values
    testing_set = test_set.iloc[:, 1:2].values

    #
    # Normalize data first
    #
    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(training_set)
    testing_set_scaled = sc.fit_transform(testing_set)

    #
    # Split data into n_timestamp
    #
    def data_split(sequence, n_timestamp):
        X = []
        y = []
        for i in range(len(sequence)):
            end_ix = i + n_timestamp
            if end_ix > len(sequence) - 1:
                break
            # i to end_ix as input
            # end_ix as target output
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return array(X), array(y)

    X_train, y_train = data_split(training_set_scaled, n_timestamp)
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test, y_test = data_split(testing_set_scaled, n_timestamp)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    if model_type == 1:
        # Single cell LSTM
        model = Sequential()
        model.add(LSTM(units=50, activation='relu', input_shape=(X_train.shape[1], 1)))
        model.add(Dense(units=1))
    if model_type == 2:
        # Stacked LSTM
        model = Sequential()
        model.add(LSTM(50, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 1)))
        model.add(LSTM(50, activation='relu'))
        model.add(Dense(1))
    if model_type == 3:
        # Bidirectional LSTM
        model = Sequential()
        model.add(Bidirectional(LSTM(50, activation='relu'), input_shape=(X_train.shape[1], 1)))
        model.add(Dense(1))

    #
    # Start training
    #

    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    history = model.fit(X_train, y_train, epochs = n_epochs, batch_size = 32)
    loss = history.history['loss']
    epochs = range(len(loss))
    model.save('D:\\www\\main\\testfirst\\resource\\prediction\\LSTM\\LSTM-model-'+place+'-'+type+'.h5')

    #model = load_model('D:\\www\\main\\testfirst\\resource\\prediction\\LSTM\\LSTM-model-tmin.h5')

    #
    # Get predicted data
    #
    y_predicted = model.predict(X_test)

    #
    # 'De-normalize' the data
    #
    y_predicted_descaled = sc.inverse_transform(y_predicted)
    y_train_descaled = sc.inverse_transform(y_train)
    y_test_descaled = sc.inverse_transform(y_test)
    y_pred = y_predicted.ravel()
    y_pred = [round(yx, 2) for yx in y_pred]
    y_tested = y_test.ravel()

    plt.plot(y_test_descaled)
    plt.plot(y_predicted_descaled)
    plt.show()

    mse = mean_squared_error(y_test_descaled, y_predicted_descaled)
    r2 = r2_score(y_test_descaled, y_predicted_descaled)
    return mse,r2



'''
for place in PLACE:
    for type in TYPE:
        mse, r2 = train_model(type,place)
        MSE.append(mse)
        R2.append(R2)
'''

if __name__ == '__main__':
    PLACE = ['beijing','shanghai','guangzhou','shenzhen']
    TYPE = ['tmax','tmin']
    MSE = []
    R2 = []
    for place in PLACE:
        for type in TYPE:
            mse, r2 = train_model(type, place)
            MSE.append(mse)
            R2.append(R2)

    print(MSE, R2[0])
