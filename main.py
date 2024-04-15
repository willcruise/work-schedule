import calendar
import datetime
from collections import defaultdict
import itertools



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
        calen[i].append(["토야"])
    elif calen[i][1] == 6:
        calen[i].append(["일야"])

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
    
print(dayoffs)
    
"""modify dayoffs"""
        
weights = {}
weights["평야"] = 1
weights["금야"] = 1.8
weights["토야"] = 1.5
weights["일야"] = 0.7


dutytypes = ["평야", "금야", "토야", "일야"]

calen1 = [calen[i] for i in range(len(calen)//2)]  
calen2 = [calen[i] for i in range(len(calen)//2, len(calen))]

print(calen1)
print(calen2)
        
monthlyduties1 = []
monthlyduties2 = []

monthlyduties1 = [c[0] for c in [i[3] for i in calen1]]
monthlyduties2 = [c[0] for c in [i[3] for i in calen2]]

    
def dutysort(e):
    return weights[e]

monthlyduties1.sort(reverse = True, key = dutysort)
monthlyduties2.sort(reverse = True, key = dutysort)

"""get and sort montly services"""

def dutygroups(monthlyduties):
    dutygroups = {} 
    for i in range(len(workers)): dutygroups[i] = []


    def elementcnt(e):
        return len(dutygroups[e])


    for i in monthlyduties: 
        groupweights = {}
        sums = {}
        for w in dutygroups:
            d = []
            for c in dutygroups[w]:
                d.append(weights[c])
            groupweights[w] = d
    
  
        for a in groupweights:
            sums[a] = sum(groupweights[a])
        
        finkeys = list(dict(sorted(sums.items(), key = lambda a: a[1])))
    
        dutygroups[finkeys[0]].append(i)
    
    return dutygroups

dutygroups1 = dutygroups(monthlyduties1)
dutygroups2 = dutygroups(monthlyduties2)


def workerbyduties(dutygroups):
    workerbyduties = {}
    for i in dutytypes:
        workerbyduties[i] = []

    for i in dutygroups:
        for c in dutygroups[i]:
            for q in dutytypes:
                if c == q:
                    workerbyduties[c].append(i)
                    break
                else: pass
    return workerbyduties
    
workerbyduties1 = workerbyduties(dutygroups1)
workerbyduties2 = workerbyduties(dutygroups2)

print(workerbyduties1)
print(workerbyduties2)

def daybyduties(calen):    
    daybyduties = {}
    for i in dutytypes:
        daybyduties[i] = []

    for i in calen:
        for c in i[3]:
            for q in dutytypes:
                if c == q:
                    daybyduties[c].append(i[0])
                    break
                else: pass
    return daybyduties
    
daybyduties1 = daybyduties(calen1)
daybyduties2 = daybyduties(calen2)

print(daybyduties1)
print(daybyduties2)


def combinelists(a, b):
    result = []
    for i in b:
        result.append(list(a)+list(i))
    return result


def combinations(workerbyduties, daybyduties):
    result = {}

    for i in workerbyduties:
        
        workercnt = defaultdict(int)
        for c in workerbyduties[i]:
            workercnt[c] += 1 
        workercnt = dict(workercnt)
        pegs = []      
        for q in workercnt:
            subjects = []
            if q == 0:
                subjects = [daybyduties[i]]
                pegs = list(itertools.combinations(subjects[0], workercnt[0]))
            
            else:
                for u in pegs:
                    subjects.append([f for f in daybyduties[i] if f not in u])
        
                def elements2():
                    for p in range(len(subjects)):
                        combi = list(itertools.combinations(subjects[p],workercnt[q]))
                        for o in combinelists(pegs[p], combi): yield(o)
            
                pegs = list(elements2())
            
        result[i] = pegs  
    
    return result
    
combinations1 = combinations(workerbyduties1, daybyduties1)
combinations2 = combinations(workerbyduties2, daybyduties2)




def matchdays(combinations, workerbyduties):
    
    matchcombi1 = defaultdict(list)
    for t in dutytypes:
        for i in combinations[t]:
            matchcombi2 = {}
            for q in range(len(i)):
                matchcombi2[i[q]] = workerbyduties[t][q]
            matchcombi1[t].append(matchcombi2)        
        
    return dict(matchcombi1)
            

matchcombi1 = matchdays(combinations1, workerbyduties1)
matchcombi2 = matchdays(combinations2, workerbyduties2)


def finalmatch(matchcombi):
    finalcalen = {}
    
    def elementyield(list):
        for g in list:
            yield g
    
    for d in dutytypes:
        matchcombi[d]
    
        
    yield finalcalen        
                

finalcalen1 = 0
finalcalen2 = 0


"""calencombi2 = matchdays(calen2, combinations2, workerbyduties2)"""


    
       

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
    2 : set restrictions for each workers according to offdays 
        
    3. use switch"""
    
"""mandatory modification points
***do not pre decide 토주, 일주, yet decide it last which best fits***""" 
    
    
    
    
    
