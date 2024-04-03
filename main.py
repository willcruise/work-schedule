import calendar
import datetime

print("Enter year and month: 0000-00")
yearmonth = input()
"""get year and month of the making schedule"""


datelist = yearmonth.replace(" ", "").split("-")
datelist[1] = datelist[1].replace("0","")

datetime_date = datetime.date(int(datelist[0]), int(datelist[1]), 1)
firstdayofweek = datetime_date.weekday()
monthrange = calendar.monthrange(int(datelist[0]), int(datelist[1]))[1]
"""get monthrange and day of week of the first day of month""" 

print("Enter the offdays: 00, 00, ...")
offdays = input()
offdays = offdays.replace(" ","").replace("0","").split(",")

for i in range(len(offdays)): 
    offdays[i] = int(offdays[i])
    
"""offdays_date = []
for i in offdays:
    date = datetime.date(int(datelist[0]), int(datelist[1]), int(i))
    print(date)
    offdays_date.append(date)"""
"""get offdays"""



calen = []

for i in range(monthrange):
    calen.append([i+1, firstdayofweek])
    if firstdayofweek < 6:
        firstdayofweek += 1
    else : firstdayofweek = 0

first = True
for i in calen:
    m = 0
    match = False
    for c in offdays:
        if i[0] == c:
            if first == True: 
                calen[m][1] = 5
            else : calen[m][1] = 6
            match = True
    if match == True : first = False
    else : first = True
    m += 1    
print(calen)        
"""get the calender for the month of the schedule"""
   
   
schedule = {}

for i in range(monthrange):
    if  calen[i][2] <= 3:
        schedule[calen[i]] =["평야"]
    elif calen[i][2] == 4:
        schedule[calen[i]] = ["금야"]
    elif calen[i][2] == 5:
        schedule[calen[i]] = ["토주","토야"]
    elif calen[i][2] == 6:
        schedule[calen[i]] = ["일주","일야"]


    
    
    
    
    
    
    
    
