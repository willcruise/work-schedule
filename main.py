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
    if firstdayofweek == 0:
        calen.append([i+1, firstdayofweek, "월"])
    elif firstdayofweek == 1:
        calen.append([i+1, firstdayofweek, "화"])
    elif firstdayofweek == 2:
        calen.append([i+1, firstdayofweek, "수"])
    elif firstdayofweek == 3:
        calen.append([i+1, firstdayofweek, "목"])
    elif firstdayofweek == 4:
        calen.append([i+1, firstdayofweek, "금"])
    elif firstdayofweek == 5:
        calen.append([i+1, firstdayofweek, "토"])
    else:
        calen.append([i+1, firstdayofweek, "일"])
    
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

print("Enter the dayoffs of workers; name1: day1 ~ day2, day3, name2: ...")
dayoffss = input()
dayoffss = dayoffss.replace(" ", "")
dayoffs = {}
if dayoffss != '':
    index = []
    for i in workers:
        index.append(dayoffss.find(i))
    
    rem = []
    for i in index:
        if -1 < i : pass
        else: rem.append(index.index(i))
    for i in rem: index.pop(i)

    
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
    v = []
    for c in dayoffs[i]:
        if '~' in c:
            a = c.split('~')
            for y in range(int(a[0]),int(a[1])+1):
                v.append(y)
        else: v.append(int(c))
    dayoffs[i] = v
    
"""modify dayoffs"""
        
weights = {}
weights["평야"] = 1
weights["금야"] = 1.8
weights["토야"] = 1.5
weights["일야"] = 0.7
weights["토주"] = 0
weights["일주"] = 0

dutytypes = ["평야", "금야", "토야", "일야", "토주", "일주"]

        
monthlyduties = []
for i in calen:
    for c in i[3]:
        monthlyduties.append(c)

def dutysort(e):
    return weights[e]

monthlyduties.sort(reverse = True, key = dutysort)

"""get and sort montly services"""
print (monthlyduties)

dutygroups = {} 
for i in range(len(workers)): dutygroups[i] = []


def elementcnt(e):
    return len(dutygroups[e])


    
for i in monthlyduties: 
    takinggroup = []
    sum = 0
    d = dutygroups
    for w in d:
        csum = 0
        for c in d[w]:
            csum += weights[c]
        if csum < sum : 
            sum = csum
            takinggroup.remove()
            takinggroup.append(w)
        elif csum == sum:
            takinggroup.append(w)
            
        takinggroup.sort(key = elementcnt)
    print(takinggroup)
    finalgroup = takinggroup[0]
    
    dutygroups[finalgroup].append(i)
    
print(dutygroups)
    
    

    
        
        

    


"""group monthly duties for the weight sums of each group to be similar. Using greedy allocation"""        
        
        

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
    
    
""" optional modification point 1: set dutytypes
    point 2 : set restrictions for each workers according to offdays """
        
    
    
    
    
    
