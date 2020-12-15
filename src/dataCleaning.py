import pandas as pd
from datetime import datetime
from dateutil import parser

data_raw = pd.read_csv('C:/Users/Think/Desktop/2198198.csv', encoding='utf-8')
data_raw['date'] = data_raw['DATE'].apply(parser.parse)
data_raw['tmax'] = data_raw['TMAX'].astype(float)
data_raw['tmin'] = data_raw['TMIN'].astype(float)

data = data_raw.loc[:, ['date', 'tmax', 'tmin']]
data = data[(pd.Series.notnull(data['tmax'])) & (pd.Series.notnull(data['tmin']))]
data = data[(data['date'] >= datetime(1980, 6, 26)) & (data['date'] <= datetime(2020, 6, 28))]
data.query('date.dt.day==28 & date.dt.month==6', inplace=True)
data.to_csv('C:/Users/Think/Desktop/maxmin.csv', index=None)
