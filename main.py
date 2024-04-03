import calendar
import datetime

print("Enter year and month: year-month ex)2024-3")
yearmonth = input()
"""get year and month of the making schedule"""


datelist = yearmonth.replace(" ", "").split("-")
datelist[1] = datelist[1]

datetime_date = datetime.date(int(datelist[0]), int(datelist[1]), 1)
firstdayofweek = datetime_date.weekday()
monthrange = calendar.monthrange(int(datelist[0]), int(datelist[1]))[1]
"""get monthrange and day of week of the first day of month""" 

print("Enter the offdays: day1, day2, ... ex)4,5,6,15,29")
offdays = input()
offdays = offdays.replace(" ","").split(",")

for i in range(len(offdays)): 
    offdays[i] = int(offdays[i])
"""get offdays for the month"""


calen = []

for i in range(monthrange):
    calen.append([i+1, firstdayofweek])
    if firstdayofweek < 6:
        firstdayofweek += 1
    else : firstdayofweek = 0

for i in offdays:
    for c in range(len(calen)):
        if i == calen[c][0]:
            calen[c][1] = 5

yesteroff = False
for i in range(len(calen)):
    if calen[i][1] == 5 or calen[i][1] == 6:
        if yesteroff == True: calen[i][1] = 6
        yesteroff = True
    else: yesteroff = False
"""get the calender for the month of the schedule"""
  

for i in range(len(calen)):
    if  calen[i][1] <= 3:
        calen[i].append(["평야"])
    elif calen[i][1] == 4:
        calen[i].append(["금야"])
    elif calen[i][1] == 5:
        calen[i].append(["토주","토야"])
    elif calen[i][1] == 6:
        calen[i].append(["일주","일야"])

print(calen)

    
    
"""get vacations, outdoordays for workers"""

"""allot duties for workers"""

"""regression process"""
    
    
"""final schedule"""
    
    
    
    
    
    
