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

print("Enter the holidays: day1, day2, ... ex)4,5,6,15,29")
holidays = input()
holidays = holidays.replace(" ","").split(",")
if holidays[0] != '':
    for i in range(len(holidays)): 
        holidays[i] = int(holidays[i])
"""get holidays for the month"""


calen = []

for i in range(monthrange):
    calen.append([i+1, firstdayofweek])
    if firstdayofweek < 6:
        firstdayofweek += 1
    else : firstdayofweek = 0

for i in holidays:
    for c in range(len(calen)):
        if i == calen[c][0]:
            calen[c][1] = 5

yesteroff = False
for i in range(len(calen)):
    if calen[i][1] == 5 or calen[i][1] == 6:
        if yesteroff == True: calen[i][1] = 6
        yesteroff = True
    else: yesteroff = False
    

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
"""get the calender for the month of the schedule"""

print("Enter the workers: name1, name2, ...")
workers = input()
workers = workers.replace(" ","").split(",")
"""get workers"""

print("Enter the dayoffs of workers; name1: day1 ~ day2, day3, name2: ... ex)홍길동: 10 ~ 19, 25, 홍길여: 14")
dayoffss = input()
dayoffss = dayoffss.replace(" ", "")
dayoffs = {}
if dayoffss != '':
    index = []
    for i in workers:
        index.append(dayoffss.find(i))
    
    for i in index:
        if not 0 <= i < len(dayoffss):
            index.remove(i)
    
    dayoffs_ = []
    for i in range(len(index)-1):
        dayoffs_.append(dayoffss[index[i]:index[i+1]])
    dayoffs_.append(dayoffss[index[len(index)-1]:])
    
    for i in dayoffs_:
        a = i.split(":")
        dayoffs[a[0]] = a[1]
       
for i in dayoffs:
    dayoffs[i] = dayoffs[i].split(",")
    if '' in dayoffs[i]: 
        dayoffs[i].remove('')

for i in dayoffs:
    for c in i:
        if '~' in c:
            a = c.split("~")
            

"""get vacations, dayoffs for workers"""

"""allot duties for workers"""

"""regression process"""

"""1. make calendars regarding to weights.
     allot specific weights to each duty types, 
     and group duties for each workers concerning the vacations, and dayoffs
    2. test the calenders built from the previous step by work counts, and distance between days of work
       alloted to each workers.
    3. evaluate the final schedule
    """
    
"""final schedule"""
    
    
    
    
    
    
