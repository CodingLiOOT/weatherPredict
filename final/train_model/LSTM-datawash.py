from pyspark import SparkContext

import pandas as pd
from datetime import datetime
from dateutil import parser
import numpy as np


def data_wash(place):
    data_raw = pd.read_csv('resource\\'+place+'.csv', encoding='utf-8')


    data_raw['date'] = data_raw['DATE'].apply(parser.parse)
    data_raw['tmax'] = data_raw['TMAX'].astype(float)
    data_raw['tmin'] = data_raw['TMIN'].astype(float)



    data = data_raw.loc[:, ['date', 'tmax', 'tmin']]
    data = data[(data['date'] >= datetime(1980, 6, 28)) & (data['date'] <= datetime(2020, 7, 30))]
    #data.query("date.dt.day == " + str(day) + "& date.dt.month == 7", inplace=True)

    data = data[(pd.Series.notnull(data['tmax'])) & (pd.Series.notnull(data['tmin']))]



    data.to_csv('resource\\weather-info\\' + place+'-cleaned.csv', index=None)

if __name__ == '__main__':
    PLACE = ['beijing','shanghai','guangzhou','shenzhen']

    for place in PLACE:
        data_wash(place)