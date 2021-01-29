filepath = '/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/FINAL_909_NO_OUTLIER.csv'
import pandas as pd
import csv

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

data = pd.read_csv(filepath, delimiter=',')
print(data)

##propCities = ["Burlington Township", "Burlington City", "Edgewater Park", "Beverly City","Florence Township", "Willingboro Township", "Springfield Township"]
##tot = []
##for i in range(len(data.City)):
##    curType = data.Type[i]
##    if(curType not in tot): tot.append(curType)
####    if(curType == 'FIRE F Fire Call' or curType == 'ASSIST: FIRE ' or curType == 'STRUCTURE: NON-FIRE ' or curType == 'ALARM: FIRE ' or curType == 'FIRE ' or curType == 'STRUCTURE: COMMERCIAL/MFD '):
##
####    if(curType == '115 E Electroc'):
####        print(data.Date[i], data.Address[i], data.Time[i], curType)
##
##new = []
##old = []
##for curTot in tot:
##    if(hasNumbers(curTot) == True):
##        old.append(curTot)
##    elif(hasNumbers(curTot) == False):
##        new.append(curTot)
##    else:
##        print('WTF?', curTot)
##
##        
##for i in range(len(data.City)):
##    curType = data.Type[i]
##
##    if(curType == '106 E Breathin' or curType == 'RESCUE: TECH '):
##        data.Type[i] = 'RESPIRATORY/ BREATHING '
##    elif(curType == '117 E Falls'):
##        data.Type[i] = 'FALL/ FRACTURE '
##    elif(curType == '125 E Psychiat'):
##        data.Type[i] = 'PSYCHIATRIC '
##    elif(curType == '132 E UnkMedEmrg' or curType == 'UNK MED EMER ' or curType == 'EMS ' or curType == 'EMS E EMS Call'):
##        data.Type[i] = 'MEDICAL EMER '
##    elif(curType == '131 E Uncon'):
##        data.Type[i] = 'UNCONSCIOUS '
##    elif(curType == '119 E Heart'):
##        data.Type[i] = 'HEART '
##    elif(curType == '17 F Fumes'):
##        data.Type[i] = 'FUMES: INTERIOR '
##    elif(curType == '101 E AbdmPain'):
##        data.Type[i] = 'ABDOMINAL PAIN '
##    elif(curType == '112 E Convulsn'):
##        data.Type[i] ='SEIZURES '
##    elif(curType == '110 E ChestPain'):
##        data.Type[i] = 'CHEST PAIN '
##    elif(curType == '113 E Diabetic'):
##        data.Type[i] = 'DIABETIC '
##    elif(curType == '128 E Stroke'):
##        data.Type[i] = 'STROKE '
##    elif(curType == '134 E SpclAssn'):
##        data.Type[i] = 'SPECIAL ASSIGNMENT '
##    elif(curType == '129F E Mva/Fire'):
##        data.Type[i] = 'MVC/FIRE '
##    elif(curType == '130 E Trauma' or curType == 'TRAUMA'):
##        data.Type[i] = 'TRAUMA '
##    elif(curType == '124 E Pregnant'):
##        data.Type[i] = 'PREGNANT '
##    elif(curType == '104 E AsltRape'):
##        data.Type[i] = 'ASSAULT '
##    elif(curType == '105 E BackPain'):
##        data.Type[i] = 'BACK PAIN '
##    elif(curType == '15 F Rubbish' or curType == 'RUBBISH/ TRASH/ DUMPSTER '):
##        data.Type[i] = 'RUBBISH/ TRASH/ DUMPSTER/ MULCH '
##    elif(curType == '126 E SickPers'): 
##        data.Type[i] = 'SICK PERSON '
##    elif(curType == '123 E Overdose' or curType == 'OVERDOSE '):
##        data.Type[i] = 'OVERDOSE/POISONING '
##    elif(curType == '109 E Arrest'):
##        data.Type[i] = 'ARREST: RESP/CARD '
##    elif(curType == '111 E Choking'):
##        data.Type[i] = 'CHOKING '
##    elif(curType == '121 E Hemrhage'):
##        data.Type[i] = 'HEMORRHAGE '
##    elif(curType == '1284 P DisputLand'):
##        data.Type[i] = 'DISPUTE '
##    elif(curType == '102 E AlergcReac'): 
##        data.Type[i] = 'ALLERGIC REACTION '
##    elif(curType == '136 E NonEmerg'):
##        data.Type[i] = 'TRANSPORT: NON EMERG '
##    elif(curType == '118 E Headache'):
##        data.Type[i] = 'HEADACHE '
##    elif(curType == '127 E Pentrwnd'):
##        data.Type[i] = 'PENTR WOUND/ STABBING/ GSW '
##    elif(curType == '133 E TrfcEntp' or curType == '30 F Rescue'):
##        data.Type[i] = 'MVC ENTRAPMENT/ RESCUE ASSGNMNT '
##    elif(curType == '116 E EyeProb'):
##        data.Type[i] = 'EYE PROBLEM '
##    elif(curType == '103 E AnmlBite'):
##        data.Type[i] = 'ANIMAL BITE '
##    elif(curType == '107 E Burns'):
##        data.Type[i] = 'BURN VICTIM '
##    elif(curType == '120 E Exposure'):
##        data.Type[i] = 'EXPOSURE '
##    elif(curType == '114 E Water Res'):
##        data.Type[i] = 'WATER RESCUE '
##    elif(curType == '13 F Vehicle'):
##        data.Type[i] = 'VEHICLE: FIRE '
##    elif(curType == '11 F StrctrFire' or curType == 'STRUCTURE: COMMERCIAL/MFD '):
##        data.Type[i] = 'STRUCTURE: BUILDING '
##    elif(curType == '129 E AccInjry' or curType == '32 F Assist EMS' or curType == '1660 P MVA No Inj' or curType == 'MVC W/INJRY ' or curType == 'MVC/ADD FD ' or curType == '1667 P MVA:Rept' or curType == '1660 P MVA No Inj'):
##        data.Type[i] = 'MVC w/ INJ '
##    elif(curType == '55 F Asst Polic'):
##        data.Type[i] = 'ASSIST: POLICE '
##    elif(curType == 'ASSIST: FIRE ' or curType == 'FIRE ' or curType == '16 F Alarms' or curType == '14 F Brush' or curType == 'STRUCTURE: NON-FIRE ' or curType == '44 F Wires' or curType == '18 F RdwyHazard' or curType == 'ALARM: FIRE ' or curType == 'FIRE F Fire Call' or curType == '12 F StrNonFire'):
##        data.Type[i] = 'FIRE-CALL'
##    elif(curType == '122 E Industrl'):
##        data.Type[i] = 'INDUSTRIAL/ MACHINERY ACCIDENT '
##    
##
##data.to_csv("/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/909_FIXED_DATASET.csv")
##
##    
##print(len(new), new, '\n\n')
##print(len(old), old)
##for curTot in tot: print(curTot)
##
##data.City = data.City.str.replace("Twp", "Township")
##
##details = { 
##    'Name' : ['Ankit', 'Aishwarya', 'Shaurya',  
##              'Shivangi', 'Priya', 'Swapnil'], 
##    'Age' : [23, 21, 22, 21, 24, 25], 
##    'University' : ['BHU', 'JNU', 'DU', 'BHU', 
##                    'Geu', 'Geu'], 
##} 
##  
### creating a Dataframe object  
##df = pd.DataFrame(details, columns = ['Name', 'Age', 
##                                      'University'], 
##                  index = ['a', 'b', 'c', 'd', 'e', 'f']) 
##print(df, '\n\n')
### get names of indexes for which column Age has value >= 21 
### and <= 23 
##index_names = df[ (df['Age'] >= 21) & (df['Age'] <= 23)].index 
##  
### drop these given row 
### indexes from dataFrame 
##df.drop(index_names, inplace = True) 
##  
##print(df)
##
##
####print(data)
##Cities = []
##for i in range(len(data.City)):
##
##    curCity = data.City[i].strip()
##
####    if(curCity not in Cities):
####        Cities.append(curCity)
####for curCity in Cities: print(curCity)
##    if(curCity == "Burl Township"):
##        data.City[i] = "Burlington Township"
##    elif(curCity == "Burl City"):
##         data.City[i] = "Burlington City"
##    elif(curCity == "Edgewater"):
##         data.City[i] = "Edgewater Park"
##    elif(curCity == "Beverly"):
##         data.City[i] = "Beverly City"
##    elif(curCity == "Florence"):
##        data.City[i] = "Florence Township"
##    elif(curCity == "Willingbor" or curCity == "Wilingboro Township"):
##        data.City[i] = "Willingboro Township"
##    elif(curCity == "Springfield" or curCity == "Springfld"):
##        data.City[i] = "Springfield Township"
##
##propCities = ["Burlington Township", "Burlington City", "Edgewater Park", "Beverly City","Florence Township", "Willingboro Township", "Springfield Township"]
##newIndex = data[ (data['City'] != 'Burlington Township') & (data['City'] != 'Burlington City') & (data['City'] != 'Edgewater Park') & (data['City'] != 'Beverly City') & (data['City'] != 'Florence Township') & (data['City'] != 'Willingboro Township') & (data['City'] != 'Springfield Township')].index
##data.drop(newIndex, inplace = True)
##data.to_csv("/Users/evangoldsmith/Documents/GitHub/Email-Scraper/saved_directory/FINAL_909_NO_OUTLIER.csv")
####print(newdf)
####for i in range(len(data.City)):
####    curCity = data.City[i]
####    if(curCity not in propCities):
####        print(data.Date[i], data.Address[i]. data.City[i])
####print(data)
