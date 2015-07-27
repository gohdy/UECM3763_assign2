# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:45:37 2015

@author: user
"""
from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p
import numpy as np

#Download daily data for Sime Darby Berhad from 1 July 2012 until 30 June 2015
start = dt(2012, 7, 1);
end = dt(2015, 6, 30);

#Calculate moving average for Sime Darby Berhad from 1 July 2012 until 30 June 2015
sime = DR("4197.KL", 'yahoo', start, end);['Close'];
Five_Day_Moving_Average = pd.rolling_mean(sime,5);       

#Plot the 5-day moving average plot for Sime Darby Berhad from 1 July 2012 until 30 June 2015
p.plot(Five_Day_Moving_Average);
plt.xlabel('Years')
plt.ylabel('5-day MA')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=4, mode="expand", borderaxespad=0.)
plt.subplot(2,1,2)
plt.plot(dw.index,dw['5D_MA'],'b',label='KLSE 5-day MA')
plt.xlabel('Years')
plt.ylabel('5-day MA')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=4, mode="expand", borderaxespad=0.)        
plt.show()

df = df.reset_index()
dw = dw.reset_index()
mm = pd.merge(df, dw, on='Date', suffixes=['_pbb', '_KLSE'])   # merge dataframe
a = np.corrcoef(mm['Close_pbb'],mm['Close_KLSE'])              # calculate correlation coefficient
print ('Correlation coefficient=', a)

