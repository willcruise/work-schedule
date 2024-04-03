import calendar
import datetime

print("Enter year and month: 0000-00")
yearmonth = input()
"""get year and month of the making schedule"""


datelist = yearmonth.split("-")
datelist[1] = datelist[1].replace("0","")

datetime_date = datetime.date(int(datelist[0]), int(datelist[1]), 1)
print(datetime_date)
firstdayofweek = datetime_date.weekday()
monthrange = calendar.monthrange(int(datelist[0]), int(datelist[1]))[1]
"""get monthrange and day of week of the first day of month""" 

print("Enter the offdays: 00, 00, ...")
offdays = input()
offdays = offdays.replace(" ","").replace("0","").split(",")
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

first = true 
for i in calen:    
    match = false
    for c in offdays
        if i[0] == c:
            match = true
            if first == true: 
                i[1] = 5
                first = false
            else : i[1] = 6 
    if match == true : first = false
    else : first = true, match = false
        
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


    
    
    
    
    
    
    
    
