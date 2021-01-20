'''

evan goldsmith
1/15/2021
cleaning up the 909 entire dataset. 


'''

import pandas as pd
import csv

#new cad emails working times start: Sun, Oct 20, 2019, 2:49 PM (start 10/21
#new cad emails NO TIMES WORKING, start: Tue, Oct 1, 2019, 5:20 AM


#old cad emails end: Tue, Oct 1, 2019, 2:00 AM
#grab the FINAL REPORTS ONLY: '** ** ** ** ** ** ** ** ** ** ** ** FINAL REPORT ** ** ** ** ** ** ** ** ** ** ** **' (old) | 'FINAL REPRT: Final' (new)
#address for these is 'Incident Location: 14 Address Rd'
#city for these is 'Venue: Edgewater'
#times for these are 'Dispatch - HH:MM:SS




#endeavor picked up edgewater in 2014; Endeavor will begin serving Edgewater Park on Nov. 1 at 6 a.m.
#endeavor picked up beverly 07/26/2017


file_909 = '/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/csv1/full_909_dataset.csv'

data_909 = pd.read_csv(file_909, delimiter=',')

print(data_909)


    
data_909['Time'] = data_909['Time'].str.replace("<", "")
data_909['Time'] = data_909['Time'].str.replace("/", "")
print('------------------- FIXED--------------------------------------------------------------------------')
##i = 0
##times = [7,8,9]
##for curTime in data_909.Time:
##    curDate = data_909.Date[i]
##    curAddress = data_909.Address[i]
##    if(len(str(curTime)) != 8): #!= 8 and len(str(curTime)) != 9):
##        print(curDate, curTime)
##        
##    i+=1
##
##print('------------------- TIME DONE --------------------------------------------------------------------------')
##i = 0
##for curTime in data_909.Time:
##    curDate = data_909.Date[i]
##    curAddress = data_909.Address[i]
##    if(str(curAddress) == 'nan'):
##        print(curDate,  curAddress, i)
##    i+=1
##
##print('------------------- ADDRESS DONE --------------------------------------------------------------------------')
i = 0
for curTime in data_909.Time:
    curDate = data_909.Date[i]
    curAddress = data_909.Address[i]
    curCity = data_909.City[i]
    if(str(curCity) == 'nan'):
        print(curDate, curCity)
        break
    i+=1

print('------------------- CITY DONE --------------------------------------------------------------------------')
##i = 0
##for curTime in data_909.Time:
##    curDate = data_909.Date[i]
##    curAddress = data_909.Address[i]
##    curType = data_909.Type[i]
##    if(str(curType) == 'nan'):
##        print(curDate, curType)
##    i+=1
##
##print('------------------- TYPE DONE --------------------------------------------------------------------------')
##i = 0
##for curTime in data_909.Time:
##    curDate = data_909.Date[i]
##    curAddress = data_909.Address[i]
##    if(len(str(curTime)) != 8):
##        print(curDate, curTime, curAddress)
##    i+=1

    
##print(data_909.Time)
