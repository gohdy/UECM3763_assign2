# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:45:37 2015

@author: user
"""
from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p

#Download daily data for Sime Darby Berhad from 1 July 2012 until 30 June 2015
start = dt(2012, 7, 1);
end = dt(2015, 6, 30);
sime = DR("4197.KL", 'yahoo', start, end);

#Calculate moving average for Sime Darby Berhad from 1 July 2012 until 30 June 2015
sime_close = DR("4197.KL", 'yahoo', start, end)['Close'];
Five_Day_Moving_Average = pd.rolling_mean(sime_close,5);       

#Plot the 5-day moving average plot for Sime Darby Berhad from 1 July 2012 until 30 June 2015
p.plot(Five_Day_Moving_Average);
p.xlabel('Days');
p.ylabel('5-day moving average ($RM$)');
p.title('5-day moving average plot for Sime Darby Berhad from 1 July 2012 until 30 June 2015');
p.show();

#Download daily data for FTSEKLCI from 1 July 2012 until 30 June 2015
klci = DR("^KLSE",'yahoo',start,end);

#Compute the correlation of Sime Darby Berhad with FTSEKLCI
data = ["4197.KL","^KLSE"];
data_close = DR(data,'yahoo',start,end)['Close'];
correlation = data_close.corr();
print('Correlation of Sime Darby Berhad with FTSEKLCI =\n',correlation);