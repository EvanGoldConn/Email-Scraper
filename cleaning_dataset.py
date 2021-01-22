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
i = 0
times = [7,8,9]
for curTime in data_909.Time:
    curDate = data_909.Date[i]
    curAddress = data_909.Address[i]
    if(len(str(curTime)) != 8): #!= 8 and len(str(curTime)) != 9):
        print(curDate, curTime)
        
    i+=1

print('------------------- TIME DONE --------------------------------------------------------------------------')
i = 0
for curTime in data_909.Time:
    curDate = data_909.Date[i]
    curAddress = data_909.Address[i]
    if(str(curAddress) == 'nan'):
        print(curDate,  curAddress, i)
    i+=1

print('------------------- ADDRESS DONE --------------------------------------------------------------------------')
missingCity = []
count = {}
i = 0
for curTime in data_909.Time:
    curDate = data_909.Date[i]
    curAddress = data_909.Address[i]
    curCity = data_909.City[i] 
    if(str(curCity) == 'nan'):

##        print(data_909.City[i])
        curAddress = str(curAddress)
        
        if("1210 N RT130 324" in curAddress or "2601 MOUNT HOLLY RD SUITE B" in curAddress or "2015 RANCOCAS RD A" in curAddress or "412 GARNET DR 4F" in curAddress or "611 GARNET DR 6L" in curAddress or "500 RICHARDS RUN A" in curAddress or "101 GARNET DR 1L" in curAddress or "1700 COLUMBUS RD 102" in curAddress or "1900 MOUNT HOLLY RD 6" in curAddress or "708 GARNET DR 708" in curAddress or "811 SUNSET RD SUITE A" in curAddress or "1816 MOUNT HOLLY RD SUITE 102" in curAddress or "800 WALNUT ST 2" in curAddress or "1004 HIGH ST" in curAddress or "1815 N RT 130" in curAddress or "1130 SUNSET RD" in curAddress or "1824 N RT130" in curAddress or "1105 SUNSET RD" in curAddress or "1824 N RT130 110" in curAddress or "BURLINGTON BY" in curAddress or "NORTHGATE VILLAGE" in curAddress or "1714 HANCOCK LA" in curAddress or "1508 MOUNT HOLLY" in curAddress or "NECK RD" in curAddress or "2703 MOUNT HOLLY" in curAddress or "111 SUNSET RD" in curAddress or "TERRI LA" in curAddress or "2000 BURLINGTON BP" in curAddress or "1701 SALEM RD" in curAddress or "902 JACKSONVILLE" in curAddress or "115 SUNSET RD" in curAddress or "2305 RANCOCAS" in curAddress or "5 TERRI LA" in curAddress or "115 RT634" in str(curAddress) or "RT29" in str(curAddress) or "NJTP" in str(curAddress) or "RT 295" in str(curAddress)):
            data_909.City[i] = 'Burlington Twp'
        elif("4287 S RT130 A" in curAddress or "133 DELACOVE HOMES ST 133" in curAddress or "BENTLEY AV" in curAddress or "WARREN ST" in curAddress or "COOPER ST" in curAddress or "1306 COOPER" in curAddress or "603 SPRUCE" in str(curAddress)):
            data_909.City[i] = 'Beverly City'
        elif("S RT130 @ MOUNT HOLLY RD" in curAddress or "WOODLAND RD" in curAddress or "4385 S RT130" in curAddress or "907 WOODLANE RD" in curAddress or "1020 WOODLANE RD" in curAddress or "120 ELM ST" in curAddress or "275 GREEN ST" in curAddress or "1475 MOUNT HOLLY RD" in curAddress):
            data_909.City[i] = "Edgerwater Park"
        elif("122 W FEDERAL ST A" in curAddress or "329 W UNION ST A" in curAddress or "229 STACY ST 1" in curAddress or "965 BORDENTOWN RD B" in curAddress or "870 S RT130 S12" in curAddress or "115 W UNION ST 1" in curAddress or "218 HIGH ST" in curAddress or "411 HIGH S" in curAddress or "452 HIGH ST" in curAddress or "JONES AV" in curAddress or "1210 N RT130 336" in curAddress or "319 HIGH ST" in curAddress or "233 HIGH ST" in curAddress or "MITCHELL AV" in curAddress or "WASHINGTON AV" in curAddress or "400 HIGH ST" in curAddress or "TAYLOR AV" in curAddress or "LINDEN AV" in curAddress or "691 HIGH ST" in curAddress or "WALL ST" in curAddress or "BROAD ST" in curAddress or "E UNION ST" in curAddress or "E BROAD ST" in curAddress or "133 WALL ST" in curAddress or "870 RT130" in curAddress or "693 HIGH ST" in curAddress or "870 E RT130" in curAddress or "PENN ST" in curAddress or "PEARL ST" in curAddress or "240 E PEARL ST" in curAddress or "320 CONROW ST" in curAddress or "870 N RT130" in curAddress):
            data_909.City[i] = "Burlington City"
        elif("200 CAMPBELL DR SUITE 102" in curAddress or "4318 N RT130" in curAddress or "HOSPITAL DR" in curAddress or "55 SUNSET RD" in curAddress):
            data_909.City[i] = "Willingboro Twp"
        elif("95 CEDAR LA 17B" in curAddress or "398 CHARLESTON RD UNIT 10" in curAddress or "200 CAMPBELL DR SUITE 107" in curAddress or "620 3RD ST 1F" in curAddress or "2134 RT130" in curAddress or "249 WILBUR HENRY DR" in curAddress or "43 MAIN ST" in curAddress or "2134 N RT130" in curAddress or "FLORENCE" in curAddress or "HORNBERGER" in curAddress):
            data_909.City[i] = "Florence Twp"
        elif("403 CLEVELAND AV" in curAddress or "225 W SECOND ST 108" in curAddress or "1 W SCOTT ST" in curAddress):
            data_909.City[i] = "Riverside Twp"
        else:
            print(curDate, curAddress)
            
       
        
        
            substring = curAddress[:10]
            substring_in_list = any(substring in string for string in missingCity)
            if(substring_in_list == False):
                missingCity.append(curAddress)
            
##        print(curDate, curCity)
##        break
    i+=1

for st in missingCity:
    print(st)
print('------------------- CITY DONE --------------------------------------------------------------------------')
i = 0
for curTime in data_909.Time:
    curDate = data_909.Date[i]
    curAddress = data_909.Address[i]
    curType = data_909.Type[i]
    if(str(curType) == 'nan'):
        print(curDate, curType)
    i+=1

print('------------------- TYPE DONE --------------------------------------------------------------------------')
##i = 0
##for curTime in data_909.Time:
##    curDate = data_909.Date[i]
##    curAddress = data_909.Address[i]
##    if(len(str(curTime)) != 8):
##        print(curDate, curTime, curAddress)
##    i+=1

    
##print(data_909.Time)


data_909.to_csv("/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/FIXED_909_DATASET.csv")
