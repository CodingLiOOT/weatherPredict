import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
#from sklearn.metrics import mean_squared_error, r2_score

def predict(file, temType):

    data = pd.read_csv('D:\\www\\main\\testfirst\\resource\\weather-info\\' + file + '.csv', parse_dates=['date'])
    dta_test = data[temType]
    dta = data[temType]
    dta_year = data['date']

    begin_year = dta_year[0:1].dt.year
    end_year = dta_year[-1:].dt.year
    print(end_year)

    dta = np.array(dta, dtype=np.float)
    dta = pd.Series(dta)
    dta.index = pd.Index(sm.tsa.datetools.dates_from_range(str(begin_year.values[0]), str(end_year.values[0])))

    # dta.plot(figsize=(10, 6))
    # plt.show(block = True)

    # fig = plt.figure(figsize=(12,8))
    # ax1 = fig.add_subplot(111)
    # diff1 = dta.diff(1)
    # diff1.plot(ax=ax1)
    # plt.show(block = True)

    diff1 = dta.diff(1)
    # fig = plt.figure(figsize=(12,8))
    # ax1 = fig.add_subplot(211)
    # fig = sm.graphics.tsa.plot_acf(dta,lags = 30,ax=ax1)
    # ax2 = fig.add_subplot(212)
    # fig = sm.graphics.tsa.plot_pacf(dta,lags = 30,ax=ax2)
    # plt.show(block = True)

    AIC = []
    ARIMA_model = []

    for q in range(0, 8):
        for p in range(0, 8):
            print((p, q))
            try:
                arma_mod = sm.tsa.ARMA(dta, (p, q)).fit()

                predict_year = 10
                predict_start_year = end_year.values[0] - predict_year + 1
                predict_end_year = end_year.values[0]
                predict_dta = arma_mod.predict(str(predict_start_year), str(predict_end_year), dynamic=True)
                MSE = np.sum(np.power((dta[-10:] - predict_dta[0:10]), 2)) / len(dta[-10:])

                AIC.append(MSE)
                ARIMA_model.append([(p, q)])
            except:
                continue

    print(ARIMA_model[AIC.index(min(AIC))][0])
    arma_mod = sm.tsa.ARMA(dta, ARIMA_model[AIC.index(min(AIC))][0]).fit()
    arma_mod.save(os.path.join("d:www//main//testfirst//resource//prediction", "ARIMA" + file +'-' + type + ".h5"))

    resid = arma_mod.resid
    # fig = plt.figure(figsize = (12,8))
    # ax1 = fig.add_subplot(211)
    # fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=30,ax=ax1)
    # ax2 = fig.add_subplot(212)
    # fig = sm.graphics.tsa.plot_pacf(resid, lags=30,ax=ax2)
    # plt.show(block = False)

    # fig = plt.figure(figsize=(12,8))
    # ax = fig.add_subplot(111)
    # fig = qqplot(resid, line = 'q', ax=ax,fit = True)
    # plt.show(block = False)

    predict_year = 10
    predict_start_year = end_year.values[0] - 9
    predict_end_year = end_year.values[0] + predict_year
    predict_dta = arma_mod.predict(str(predict_start_year), str(predict_end_year), dynamic=True)

    # print(dta[-10:])
    # print(predict_dta[0:10])

    MSE = np.sum(np.power((dta[-10:] - predict_dta[0:10]), 2)) / len(dta[-10:])
    R2 = 1 - MSE / np.var(dta[-10:])
    #print('MSE and R2 is:')
    #print(MSE)
    #print(R2)

    predict_dta.to_csv('D:\\www\\main\\testfirst\\resource\\prediction\\pre-' + temType + '-' + file + '.csv')

    return MSE

FILE = ['7-4','7-5','7-6','7-7','7-8','7-9','7-10','7-11','7-12','7-13','7-14','7-15','7-16','7-17','7-18','7-19','7-20']
TYPE = ['tmax','tmin']

MSE = []

for file in FILE:
    print(file + ':')
    for type in TYPE:
        print(type)
        try:
            MSE.append(predict(file,type))
        except:
            print(type + ' not complete!!!' )
            continue

print(MSE)


