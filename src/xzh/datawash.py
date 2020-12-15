from pyspark import SparkContext

import pandas as pd
from datetime import datetime
from dateutil import parser
import numpy as np

def dataProcessing(one_all_list, num=7):
    '''
    对于时间序列数据中的 0 进行处理，采用滑动平均的方法来填充(默认时间为一周)
    '''
    nozero_list=[one for one in one_all_list if one!=0]
    before_avg,last_avg=sum(nozero_list[:num])/num,sum(nozero_list[-1*num:])/num
    res_list=[]
    for i in range(len(one_all_list)):
        if one_all_list[i]!=0:
            res_list.append(one_all_list[i])
        else:
            tmp=int(num/2)+1
            if i<=tmp:
                res_list.append(int(before_avg))
            elif i>=len(one_all_list)-tmp:
                res_list.append(int(last_avg))
            else:
                slice_list=one_all_list[i-tmp:i+tmp+1]
                res_list.append(int(sum(slice_list)/(num-1)))
    return res_list


def data_wash(file):
    data_raw = pd.read_csv('D:\\www\\main\\testfirst\\resource\\2198198.csv', encoding='utf-8')


    data_raw['date'] = data_raw['DATE'].apply(parser.parse)
    data_raw['tmax'] = data_raw['TMAX'].astype(float)
    data_raw['tmin'] = data_raw['TMIN'].astype(float)



    data = data_raw.loc[:, ['date', 'tmax', 'tmin']]
    data = data[(data['date'] >= datetime(1980, 6, 28)) & (data['date'] <= datetime(2012, 7, 30))]
    data.query("date.dt.day == 28 & date.dt.month == 6", inplace=True)


    data_mean_tmax = np.mean(data[data['tmax']!=0])
    #data = dataProcessing(data['tmax'],num = 7)
    #data = dataProcessing(data['tmin'],num = 7)

    data = data[(pd.Series.notnull(data['tmax'])) & (pd.Series.notnull(data['tmin']))]



    data.to_csv('D:\\www\\main\\testfirst\\resource\\weather-info\\'+ file +'.csv', index=None)

FILE = ['7-4','7-5','7-6','7-7','7-8','7-9','7-10','7-11','7-12','7-13','7-14','7-15','7-16','7-17','7-18','7-19','7-20']

for file in FILE:
    data_wash(file)