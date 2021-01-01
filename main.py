'''

email scraper script
required param:
- email (username)
- password
mailbox type (i.e. imap.gmail.com)

public functions:

'''



counter = 0
testString = '634314 is your miHoYo verification code'



import email, getpass, imaplib, os, re

saved_directory = '/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory'

from imap_tools import MailBox, A
from imap_tools import A, AND, OR, NOT
import datetime
import csv


def writeToFile1(curDate, curTime, curAddress, curCity, curType, fileWriter):
    fileWriter.writerow(['', curDate, curTime, curAddress, curCity, curType])

def writeToFile2(curDate, curTime, curCity, curType, fileWriter):
    fileWriter.writerow(['', curDate, curTime, curCity, curType])



def numToCity(number):
    towns = {'12': 'Beverly City', '60':'Bordentown City', '32':'Bordentown Twp', '90':'Burlington City', '30':'Burlington Twp', '11':'Delanco Twp', '23':'Delran Twp', '14':'Edgewater Park', '40':'Florence Twp', '33':'Mansfield Twp', '50':'Mount Holly Twp', '36':'Mount Laurel Twp', '18':'Pemberton Twp', '21':'Springfield Twp', '27':'Westampton Twp', '16':'Willingboro Twp'}
    for townNum in towns:
        if(str(number) == townNum):
            return towns[townNum]

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta
        
def scraper(username, pwd, mailboxType, serverType, subjectScraper, fileWriter1, fileWriter2):
    burlCountyWarning1 = 'The information in this e-mail and any attachment therein is confidential and for use by the addressee only. If you are not the intended recipient, please return the email to the sender and delete it from your computer. Although Burlington County attempts to sweep e-mail attachments for viruses, it does not guarantee that they are virus-free and accepts no liability for any damage sustained as a result of viruses.'
    burlCountyWarning2 = 'The information in this e-mail and any attachment therein is confidential and for use by the addressee only. If you are not the intended recipient, please return the email to the sender and delete it from your computer. Although Burlington County attempts to sweep e-mail attachments for viruses, it does not guarantee that they are virus-free and accepts no liability for any damage sustained as a result of viruses.'
    newCadFinal = "FINAL REPRT: Final"
    
    oldCadFinal = "** ** ** ** ** ** ** ** ** FINAL REPORT ** ** ** ** ** ** ** ** **"

            
    counter = 0
    dates = []
    
    from datetime import date, datetime, timedelta
    for result in perdelta(date(2020, 12, 30), date(2020, 12, 31), timedelta(days=1)):
##    for result in perdelta(date(2019, 12, 1), date(2020, 12, 30), timedelta(days=1)):
        dates.append(result)

           
    curStorage = []
    with MailBox(serverType).login(username, pwd, mailboxType) as mailbox:
##        for msg in mailbox.fetch(A(AND(OR(text=[burlCountyWarning1, burlCountyWarning2]), date_gte=datetime.date(2019, 11, 29)), OR(body=[newCadFinal, oldCadFinal]))):
##        for msg in mailbox.fetch(A(A(AND(OR(text=[burlCountyWarning1, burlCountyWarning2]), date_gte=datetime.date(2019, 10, 21)), OR(body=[newCadFinal, oldCadFinal])), NOT(body='<div>FINAL REPRT: </div>'))):
##        for msg in mailbox.fetch(A(date_gte=datetime.date(2019, 11, 29))):
        for curDate in dates:
            for msg in mailbox.fetch(A(date=curDate)):
                #condition is containing 1. burlCountyWarning, 2. since the proper date 3. newCadFinalReport OR oldCadFinalReport
                
                sender = msg.from_
                body = msg.text or msg.html
                subject = msg.subject

                            
            

                    

        ##            print(msg.date)
                    
        ##            if("<div>FINAL REPRT: </div>" in body):
        ##                print("hi")
        ####                None
        ##            elif("<div>FINAL REPRT: </div>" not in body):
                   
            
                if("<div>FINAL REPRT: Final </div>" in body or "FINAL REPRT: Final" in body):
    ##            if("<div>FINAL REPRT: </div>" not in body):

                        
                   
    ##            break
            
                                    
                        
                        
            ##            print(subject)
            ##            print(sender)
            ##            print(body.find("DISPATCHED"))
                    
##                        '''
##                        date
##                        dispatch time
##                        location (address)
##                        type
##                        city (venue)
##
##
##
##                        '''
##                        
                        

            ##            print(subject, body)
                            
            ##            if(newCadFinal in body): #it's the new CAD report!
            ##                print('new!')

                        
                            
                    curDate = str(msg.date)[:str(msg.date).find(' ')] #date
                    
                    initAddress = body[body.find('ADDRESS')+8:body.find('LOCAL INFO')].strip() #initial address
                    
                    
                    secondAddress = initAddress[:initAddress.find('</div>')].strip() #address
                    curAddress = secondAddress[:secondAddress.find(',')].strip()
                    
                    
                    numCity = initAddress[initAddress.find(',')+1:initAddress.find('</div>')].strip() #city
                    curCity = numToCity(numCity)
                    
                    
                    
                    initTime = body[body.find('STA909'):body.find('ALERTS')]#initial time, starts when sta909 gets added

        ##            print(initTime)

                    
                    initCounter = initTime.replace('DISPATCHED', 'XXX', 1).find('DISPATCHED') #remove the first dispatch time (supervisor vehicle usually), no error if there is only one occurence
                    curTime = None
                    if(initCounter != -1):
                        curTime = initTime[initCounter+30:initCounter+38].strip() #get exact time
                        
                        
                        if('<' in curTime):
                            curTime = initTime[initCounter+28:initCounter+38].strip()
                            
                        
                    else:
                        curTime = initTime[initTime.index('DISPATCHED')+len('DISPATCHED')+13:initTime.index('DISPATCHED')+len('DISPATCHED')+21]
                        

                        if('<' in curTime):
                            curTime = initTime[initTime.index('DISPATCHED')+len('DISPATCHED')+11:initTime.index('DISPATCHED')+len('DISPATCHED')+21].strip()
                            
                    


                    initType = body[body.find('TYPE')+6:].strip() #call type
                    curType = initType[:initType.find("</div>")]
                    

                    
                    
        ##            if(counter%2500 == 0):
        ##                print(curDate, curTime, curAddress, curCity, curType)
                    
        ##            if(curAddress == '1617 BRIDGEBORO RD'):
        ##                print(body)
    ##                if([curDate, curTime, curAddress, curCity, curType, fileWriter1] not in curStorage):
    ##    ##                print(curStorage)
    ##                    curStorage.append([curDate, curTime, curAddress, curCity, curType, fileWriter1])
                    writeToFile1(curDate, curTime, curAddress, curCity, curType, fileWriter1)
                    writeToFile2(curDate, curTime, curCity, curType, fileWriter2)
                    if(counter%1000 == 0):
                        print(counter+1, '----------------------------------------------------------- ')
                        print(curDate, curTime, curAddress, curCity, curType)
                            
        ######            elif(oldCadFinal in body): #it's the old CAD report!
        ######
        ######                curDate = str(msg.date)
        ######                curDate = curDate[:str(curDate).find(' ')].strip() #date
        ######                
        ######
        ######                initTime = body[body.find("Unit: E909"):body.find("Unit: E909")+100]
        ######                curTime = initTime[initTime.find("DSP:")+13:initTime.find("ENR:")-4].strip() #dispatch time
        ######
        ######                print(curTime)
        ######
        ######                curAddress = body[body.find("Incident Location:")+18:body.find("Venue:")].strip()
        ######
        ######                curCity = body[body.find("Venue:")+6:body.find("Venue:")+17].strip()
        ######
        ######                curType = body[body.find("Incident Type  . :")+18:body.find("Priority:")-5].strip()
        ######                
        ######
        ######               
        ######
        ######    ##            print(curDate, curTime, curAddress, curCity, curType)
        ######                writeToFile1(curDate, curTime, curAddress, curCity, curType, fileWriter1)
        ######                writeToFile2(curDate, curTime, curCity, curType, fileWriter2)
        ######                    
        ######    ##                print(curDate)
        ######
        ######    ##                if(counter%7000 == 0):
        ######    ##                    print(curDate, curTime, curAddress, curCity, curType)
                            
                
                    counter += 1
        ##            if(counter%1000 == 0):
        ##            print(counter, '----------------------------------------------------------- ')
        ##            print(curDate, curTime, curAddress, curCity, curType)

                    
                        



def RNRScraper():
##    username = 'endeavorems@gmail.com'
##    pwd = 'EndeaVor909'
    mailboxType = 'INBOX'
    serverType = 'imap.gmail.com'
    subjectScraper = 'Automatic R&R Notification'

    with open('/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/csv1/909_stats.csv', mode='w') as file1: #creating the file we are writing to 
        fileWriter1 = csv.writer(file1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open('/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/csv2/909_stats2.csv', mode='w') as file2: #creating the file we are writing to 
            fileWriter2 = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            fileWriter1.writerow(['', 'Date', 'Time', 'Address', 'City', 'Type'])
            fileWriter2.writerow(['', 'Date', 'Time', 'City', 'Type'])
            scraper(username, pwd, mailboxType, serverType, subjectScraper, fileWriter1, fileWriter2)




RNRScraper()



#new cad emails working times start: Sun, Oct 20, 2019, 2:49 PM (start 10/21
#new cad emails NO TIMES WORKING, start: Tue, Oct 1, 2019, 5:20 AM


#old cad emails end: Tue, Oct 1, 2019, 2:00 AM
#grab the FINAL REPORTS ONLY: '** ** ** ** ** ** ** ** ** ** ** ** FINAL REPORT ** ** ** ** ** ** ** ** ** ** ** **' (old) | 'FINAL REPRT: Final' (new)
#address for these is 'Incident Location: 14 Address Rd'
#city for these is 'Venue: Edgewater'
#times for these are 'Dispatch - HH:MM:SS




#endeavor picked up edgewater in 2014; Endeavor will begin serving Edgewater Park on Nov. 1 at 6 a.m.
#endeavor picked up beverly 07/26/2017








def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


find_nth("foofoofoofoo", "foofoo", 2)

    
