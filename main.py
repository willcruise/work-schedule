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
'''modify the type of the holiays'''    

for i in range(len(calen)):
    if  calen[i][1] <= 3:
        calen[i].append(["평야"])
    elif calen[i][1] == 4:
        calen[i].append(["금야"])
    elif calen[i][1] == 5:
        calen[i].append(["토야"])
    elif calen[i][1] == 6:
        calen[i].append(["일야"])

"""until now, got the calender for the month of the schedule"""

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

"""process the dayoffs input()"""
        
        
weights = {}
weights["평야"] = 1
weights["금야"] = 1.8
weights["토야"] = 1.5
weights["일야"] = 0.7


dutytypes = ["평야", "금야", "토야", "일야"]


print("How many PIECES?")
PIECES = int(input())


calens = []
for i in range(PIECES):
  if i == 0:
    calens.append([calen[i] for i in range(len(calen)//PIECES)])
  else: calens.append([calen[i] for i in range(len(calen)*i//PIECES, len(calen)*(i+1)//PIECES)])

monthlyduties = []
for i in range(PIECES):
  monthlyduties.append([c[0] for c in [i[3] for i in calens[i]]])

    
def dutysort(e):
    return weights[e]

for i in range(PIECES):
  monthlyduties[i].sort(reverse = True, key = dutysort)

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

dutygroups = [dutygroups(m) for m in monthlyduties]

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

workerbyduties = [workerbyduties(d) for d in dutygroups]    

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
    
daybyduties = [daybyduties(c) for c in calens]    

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
        
    

def combination(workerbyduties, daybyduties):
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
    
    result3 = {}
    for q in dutytypes:
        index = range(len(workerbyduties[q]))
        result3[q] = []
       
        for r in result[q]:
            result2 = {}
            for e in index:
                result2[r[e]] = workerbyduties[q][e]
        
            result3[q].append(result2)
    
    return result3

combinations = [combination(workerbyduties[i], daybyduties[i]) for i in range(PIECES)]    


'''from now, merge the divided calender'''


groups = {}
cnt = 0
for q in combinations:
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
        

def combimerge(combinations):
    indices = {d: 0 for d in combinations}
    first = {}
    for d in combinations:
        first.update(combinations[d][0])
        
    if sortandtest(first) == None:
        yield from []
    else : yield sortandtest(first)
    
    while True:
  
        for d in indices:
            if indices[d] < len(combinations[d]) - 1 : break
        else: return
    
        for d in indices:
           
            if indices[d] < len(combinations[d]) - 1:
                indices[d] += 1
                break
            else: 
                indices[d] = 0
                                
        merged = {}
        for d in indices:
            merged.update(combinations[d][indices[d]])
            
        if sortandtest(merged) == None:
            yield from []
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
    global cnt
    cnt = 0
    for q in workerper:
        for w in calendraft:
            allotedcal = {e: q[w[e]] for e in w}
            
            for e in allotedcal:
                if e in dayoffs[allotedcal[e]]:
                    cnt +=1
                    yield from []
            else: yield allotedcal    
    
    
finalcases = list(allotworkerandconcernoffdays(calendraft))
print(cnt)
print(len(finalcases))
'''
def evaluatecases(finalcases):
    
    workdays = {}
    for w in workers:
        workdays[w] = []
        
    for q in finalcases:
        for e in q:
            workdays[q[e]].append(e)
            
    print(workdays)
    
    
evaluatecases(finalcases)
 '''       

   


    
       

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
    

    
    
    
