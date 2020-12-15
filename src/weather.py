import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
#from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('D:\\www\\main\\testfirst\\resource\\maxmin1.csv',parse_dates=['date'])
dta_test = data['tmin']
data = data
dta = data['tmin']
dta_year = data['date']


begin_year = dta_year[0:1].dt.year
end_year = dta_year[-1:].dt.year
print(end_year)

dta = np.array(dta, dtype=np.float)
dta = pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range(str(begin_year.values[0]), str(end_year.values[0])))

#dta.plot(figsize=(10, 6))
#plt.show(block = False)

#fig = plt.figure(figsize=(12,8))
#ax1 = fig.add_subplot(111)
#diff1 = dta.diff(1)
#diff1.plot(ax=ax1)
#plt.show(block = False)

diff1 = dta.diff(1)
#fig = plt.figure(figsize=(12,8))
#ax1 = fig.add_subplot(211)
#fig = sm.graphics.tsa.plot_acf(dta,lags = 30,ax=ax1)
#ax2 = fig.add_subplot(212)
#fig = sm.graphics.tsa.plot_pacf(dta,lags = 30,ax=ax2)
#plt.show(block = False)

arma_mod = sm.tsa.ARMA(dta,(7,7)).fit()
print(arma_mod.aic, arma_mod.bic, arma_mod.hqic)

resid = arma_mod.resid
#fig = plt.figure(figsize = (12,8))
#ax1 = fig.add_subplot(211)
#fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=30,ax=ax1)
#ax2 = fig.add_subplot(212)
#fig = sm.graphics.tsa.plot_pacf(resid, lags=30,ax=ax2)
#plt.show(block = False)

#fig = plt.figure(figsize=(12,8))
#ax = fig.add_subplot(111)
#fig = qqplot(resid, line = 'q', ax=ax,fit = True)
#plt.show(block = False)

predict_year = 10
predict_start_year = end_year.values[0] - 9
predict_end_year = end_year.values[0]+predict_year
predict_dta = arma_mod.predict(str(predict_start_year),str(predict_end_year),dynamic = True)

#print(dta[-10:])
#print(predict_dta[0:10])

MSE = np.sum(np.power((dta[-10:] - predict_dta[0:10]),2))/len(dta[-10:])
R2 = 1 - MSE/np.var(dta[-10:])
print('MSE and R2 is:')
print(MSE)
print(R2)
#predict_dta.to_csv('D:\\www\\main\\testfirst\\resource\\result2.csv')
