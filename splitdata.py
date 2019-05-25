# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
from datetime import datetime

# Any results you write to the current directory are saved as output.

# split data according to companys
def DateParser(date):
    date = date.split('/')
    return f'{date[2]}-{date[1]}-{date[0]}'

data = pd.read_csv('rawData.csv', parse_dates=['Date'], date_parser=DateParser)

googleData = data[data['Stock'] == 'Google']
amazData = data[data['Stock'] == 'Amazon'][-len(googleData):]
fbData = data[data['Stock'] == 'Facebook']


# process the datasets to calculate price
googleData['Price'] = googleData.loc[:, 'Close'].copy()
amazData['Price'] = amazData.loc[:, 'Close'].copy()
fbData['Price'] = fbData.loc[:, 'Close'].copy()

# googleData = googleData.drop('Close', axis = 1)
# googleData = googleData.drop('Open', axis = 1)

# amazData = amazData.drop('Close', axis = 1)
# amazData = amazData.drop('Open', axis = 1)

# fbData = fbData.drop('Close', axis = 1)
# fbData = fbData.drop('Open', axis = 1)

googleData = googleData.drop('Stock', axis=1)
amazData = amazData.drop('Stock', axis=1)
fbData = fbData.drop('Stock', axis=1)

googleData = googleData[googleData['Date'] < pd.to_datetime('2018-1-1')]
amazData = amazData[amazData['Date'] < pd.to_datetime('2018-1-1')]
fbData = fbData[fbData['Date'] < pd.to_datetime('2018-1-1')]

googleData.to_csv('./google.csv')
amazData.to_csv('./amazon.csv')
fbData.to_csv('./facebook.csv')
print (googleData['Date'])

# test = pd.read_csv('./Stocker/price.csv', index_col='date', parse_dates=['date'])
# print (test.index)