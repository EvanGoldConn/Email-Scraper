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

def numToCity(number):
    towns = {'12': 'Beverly City', '60':'Bordentown City', '32':'Bordentown Twp', '90':'Burlington City', '30':'Burlington Twp', '11':'Delanco Twp', '23':'Delran Twp', '14':'Edgewater Park', '40':'Florence Twp', '33':'Mansfield Twp', '50':'Mount Holly Twp', '36':'Mount Laurel Twp', '18':'Pemberton Twp', '21':'Springfield Twp', '27':'Westampton Twp', '16':'Willingboro Twp'}
    for townNum in towns:
        if(str(number) == townNum):
            return towns[townNum]
        
def scraper(username, pwd, mailboxType, serverType, subjectScraper):
    burlCountyWarning = 'The information in this e-mail and any attachment therein is confidential and for use by the addressee only. If you are not the intended recipient, please return the email to the sender and delete it from your computer. Although Burlington County attempts to sweep e-mail attachments for viruses, it does not guarantee that they are virus-free and accepts no liability for any damage sustained as a result of viruses.'
    newCadFinal = 'FINAL REPRT: Final'
    oldCadFinal = '** ** ** ** ** ** ** ** ** ** ** ** FINAL REPORT ** ** ** ** ** ** ** ** ** ** ** **'
    with MailBox(serverType).login(username, pwd, mailboxType) as mailbox:
        for msg in mailbox.fetch(A(AND(text=burlCountyWarning, date_gte=datetime.date(2020, 12, 26)), OR(body=[newCadFinal, oldCadFinal]))):
            #condition is containing 1. burlCountyWarning, 2. since the proper date 3. newCadFinalReport OR oldCadFinalReport

            sender = msg.from_
            body = msg.text or msg.html
            subject = msg.subject
            
##            print(subject)
##            print(sender)
            '''
            date
            dispatch time
            location (address)
            type
            city (venue)



            '''
            if(newCadFinal in body): #it's the new CAD report!

                
                curDate = str(msg.date)[:str(msg.date).find(' ')] #date
                initAddress = body[body.find('ADDRESS')+8:body.find('"LOCAL INFO')].strip() #initial address

                curAddress = initAddress[:initAddress.find(',')].strip() #address
                numCity = initAddress[initAddress.find(',')+1:].strip() #city
                curCity = numToCity(numCity)
                
                
                initTime = body[body.find('STA909'):body.find('ALERTS')]#initial time, starts when sta909 gets added
                initCounter = initTime.replace('DISPATCHED', 'XXX', 1).find('DISPATCHED') #remove the first dispatch time (supervisor vehicle usually), no error if there is only one occurence
                if(initCounter != -1): curTime = initTime[initCounter+30:initCounter+38].strip() #get exact time
                else: curTime = initTime[initTime.index('DISPATCHED')+len('DISPATCHED')+13:].strip() #IF ONLY ONE UNIT

                curType = body[body.find('TYPE')+6:body.find('()')].strip() #call type

                print(curDate, curTime, curAddress, curCity, curType)
                
                
            
            elif(oldCadFinal in body): #it's the old CAD report!

                curDate = str(msg.date)
                curDate = curDate[:str(curDate).find(' ')].strip() #date

                '''---------------------------PLACHOLDER---------------------------

                    Scrape
                    dispatch time
                    location (address)
                    type
                    city (venue)
                '''



                
            print('-----------------------------------------------------------')




def RNRScraper():
    username = 'mcev10ev@gmail.com'
    pwd = 'mcev10ev-Pass-10'
    mailboxType = 'INBOX'
    serverType = 'imap.gmail.com'
    subjectScraper = 'Automatic R&R Notification'
    scraper(username, pwd, mailboxType, serverType, subjectScraper)




RNRScraper()




#new cad emails working times start: Sun, Oct 20, 2019, 2:49 PM
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

    
