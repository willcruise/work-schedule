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


"""get the calender for the month of the schedule"""

print("Enter the workers: name1, name2, ...")
workers = input()
workers = workers.replace(" ","").split(",")

"""get workers"""

print("Enter the dayoffs of workers; name1: day1 ~ day2, day3, name2: ...")
dayoffs = input()

def processdayoff(dayoffs):
    temp = dayoffs.replace(" ", '')
    
    workerindex = []
    for q in workers:
        if temp.find(q) == -1: continue
        else:
            workerindex.append(temp.find(q))
    
    resultdraft = []
    previous = len(temp) + 1
    for e in reversed(range(len(workerindex))):
        resultdraft.append(temp[workerindex[e]:previous])
        previous = workerindex[e]
    

    resultdraft2 = {}
    for r in resultdraft:
        resultdraft2[r.split(':')[0]] = r.split(':')[1]
        
    for t in resultdraft2:
        resultdraft2[t] = resultdraft2[t].replace('/', '').split(',')
        for y in resultdraft2[t]:
            if y == '': resultdraft2[t].remove('')
    
    resultdraft3 = {}
    
    for u in resultdraft2:
        resultdraft3[u] = []
        for i in range(len(resultdraft2[u])):
            if '~' in resultdraft2[u][i]:
                o = resultdraft2[u][i].split('~')
                for p in range(int(o[0]), int(o[1])+1):
                    resultdraft3[u].append(p)
            else: resultdraft3[u].append(int(resultdraft2[u][i]))
    
    for a in workers:
        if a not in resultdraft3.keys():
            resultdraft3[a] = [] 
    
    
    return resultdraft3

    
dayoffs = processdayoff(dayoffs)
print(dayoffs)

"""configure dayoffs"""
        
        
weights = {}
weights["평야"] = 1
weights["금야"] = 1.8
weights["토야"] = 1.5
weights["일야"] = 0.7


dutytypes = ["평야", "금야", "토야", "일야"]

calen1 = [calen[i] for i in range(len(calen)//3)]  
calen2 = [calen[i] for i in range(len(calen)//3, len(calen)*2//3)]
calen3 = [calen[i] for i in range(len(calen)*2//3, len(calen))]

 

monthlyduties1 = []
monthlyduties2 = []
monthlyduties3 = []

monthlyduties1 = [c[0] for c in [i[3] for i in calen1]]
monthlyduties2 = [c[0] for c in [i[3] for i in calen2]]
monthlyduties3 = [c[0] for c in [i[3] for i in calen3]]
    
def dutysort(e):
    return weights[e]

monthlyduties1.sort(reverse = True, key = dutysort)
monthlyduties2.sort(reverse = True, key = dutysort)
monthlyduties3.sort(reverse = True, key = dutysort)
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
dutygroups3 = dutygroups(monthlyduties3)

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
workerbyduties3 = workerbyduties(dutygroups3)


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
daybyduties3 = daybyduties(calen3)


def combinelists(a, b):
    result = []
    for i in b:
        result.append(list(a)+list(i))
    return result

def makecombinations(ll, r):
    result = []
    final = []
    indices =list(range(r))
    n = len(ll)
    yield [ll[i] for i in indices]
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield [ll[i] for i in indices]
        
    

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
            if pegs == []:
                subjects = [daybyduties[i]]
                pegs = list(makecombinations(subjects[0], workercnt[q]))
            else:
                for u in pegs:
                    subjects.append([f for f in daybyduties[i] if f not in u])
        
                def elements2():
                    for p in range(len(subjects)):
                        combi = list(makecombinations(subjects[p], workercnt[q]))
                        for o in combinelists(pegs[p], combi): yield(o)
            
                pegs = list(elements2())
            
        result[i] = pegs  
    
    return result
    
combinations1 = combinations(workerbyduties1, daybyduties1)
combinations2 = combinations(workerbyduties2, daybyduties2)
combinations3 = combinations(workerbyduties3, daybyduties3)

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
matchcombi3 = matchdays(combinations3, workerbyduties3)

'''from now, merge the divided calender'''

matchcombi = [matchcombi1, matchcombi2, matchcombi3]

groups = {}
cnt = 0
for q in matchcombi:
    for w in q:
        groups[cnt] = q[w]
        cnt += 1


def sortandtest(merged):
    sortedcal = dict(sorted(merged.items()))
    previous = -1
    for q in sortedcal:
        if sortedcal[q] == previous: return
        previous = sortedcal[q]
    else:
        return sortedcal
        

def combimerge(matchcombi):
    indices = {d: 0 for d in matchcombi}
    first = {}
    for d in matchcombi:
        first.update(matchcombi[d][0])
        
    if sortandtest(first) == None:
        yield from []
    else : yield sortandtest(first)
    
    while True:
  
        for d in indices:
            if indices[d] < len(matchcombi[d]) - 1 : break
        else: return
    
        for d in indices:
           
            if indices[d] < len(matchcombi[d]) - 1:
                indices[d] += 1
                break
            else: 
                indices[d] = 0
                                
        merged = {}
        for d in indices:
            merged.update(matchcombi[d][indices[d]])
            
        if sortandtest(merged) == None: yield from []
        else: yield sortandtest(merged)            


calendraft = list(combimerge(groups))

print(len(calendraft))

def insertelement(l, e):
    result = []
    for i in range(len(l) + 1):
        first = l[:i]
        second = l[i:]
        element = first + [e] + second
        result.append(element)
    return result
    
def permutations(l):
    
    if len(l) == 2:
        result = []
        result.append(l)
        a = []
        a.append(l[1])
        a.append(l[0])
        result.append(a)
        return result
        
    else:
        e = l[0]
        l.remove(e)
        per = permutations(l)
        
        def yieldins(per):
            for j in per:
                for q in insertelement(j, e):
                    yield q
                
        return list(yieldins(per))


def allotworkerandconcernoffdays(calendraft):
    workerper = permutations(workers)
    global cnt = 0
    for q in workerper:
        for w in calendraft:
            allotedcal = {e: q[w[e]] for e in w}
            print(allotedcal)
            for e in allotedcal:
                if e in dayoffs[allotedcal[e]]:
                    cnt +=1
                    yield from []
            else: yield allotedcal    
    
    
finalcases = list(allotworkerandconcernoffdays(calendraft))
print(cnt)
print(len(finalcases))
    

 
""" 
combimerge1 = list(combimerge(matchcombi1))
combimerge2 = list(combimerge(matchcombi2))
combimerge3 = list(combimerge(matchcombi3))

 from now, merge the divided calender 

mergedcalen = {"A":combimerge1, "B":combimerge2, "C":combimerge3}


finalcalentemp = list(combimerge(mergedcalen))
calendraft = []
for e in finalcalentemp:
   
    calendraft.append(dict(sorted(e.items())))
print(calendraft)    



"""
"""

def insertelement(l, e):
    result = []
    for i in range(len(l) + 1):
        first = l[:i]
        second = l[i:]
        element = first + [e] + second
        result.append(element)
    return result
    
def permutations(l):
    
    if len(l) == 2:
        result = []
        result.append(l)
        a = []
        a.append(l[1])
        a.append(l[0])
        result.append(a)
        return result
        
    else:
        e = l[0]
        l.remove(e)
        per = permutations(l)
        
        def yieldins(per):
            for j in per:
                for q in insertelement(j, e):
                    yield q
                
        return list(yieldins(per))


def finalcalen(combimerge):
  
    for w in permutations(workers):
        match = [w[n] for n in range(len(w))]
        for e in combimerge:
            element = {}
            for k in e:
                for a in range(len(match)):
                    if a == k: 
                        element[k] = match[a]
                        break
                    else: continue
            yield(element)    
       
        
finalcalen1 = list(finalcalen(combimerge1))
finalcalen2 = list(finalcalen(combimerge2))
finalcalen3 = list(finalcalen(combimerge3)) 
"""

"""



def excludeoff(finalmatch):pass
  


calencombi2 = matchdays(calen2, combinations2, workerbyduties2)"""


    
       

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
    

    
    
    
