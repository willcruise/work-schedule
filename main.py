from typing_extensions import ParamSpecArgs
from typing import Generator, List, Dict, Tuple
import calendar
import datetime
from collections import defaultdict, deque
import itertools
import numpy as np


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

dutytypes = ["평야", "금야", "토야", "일야"]
"""list of duty types"""

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
        calen[i].append(dutytypes[0])
    elif calen[i][1] == 4:
        calen[i].append(dutytypes[1])
    elif calen[i][1] == 5:
        calen[i].append(dutytypes[2])
    elif calen[i][1] == 6:
        calen[i].append(dutytypes[3])
"""until now, got the calender for the month of the schedule"""

print("Enter the workers: name1, name2, ...")
workers = input()
workers = workers.replace(" ","").split(",")
"""get workers"""

print("Enter the dayoffs of workers; name1: day1 ~ day2, day3, name2: ...")
dayoffs = input()
'''get input of dayoffs'''

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
"""process the dayoffs input string"""


weights = {}
weights["평야"] = 1
weights["금야"] = 1.8
weights["토야"] = 1.5
weights["일야"] = 0.7
"""allot weights for each dutytype"""

print("How many PIECES?")
PIECES = int(input())
"""how many pieces are you going to divide the calendar"""

calens = []
for i in range(PIECES):
  if i == 0:
    calens.append([calen[i] for i in range(len(calen)//PIECES)])
  else: calens.append([calen[i] for i in range(len(calen)*i//PIECES, len(calen)*(i+1)//PIECES)])
"""divide the calendar"""

monthlyduties = []
for i in range(PIECES):
  monthlyduties.append([r[3] for r in calens[i]])
"""get all duties fo each divided calendar"""

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
"""alloting works for each anonymous workers regarging weights; by greedy allocation"""

def workerbyduty(dutygroups):
  workerbyduties = {}
  for i in dutytypes:
    workerbyduties[i] = []

  for i in dutygroups:
    for c in dutygroups[i]:
      workerbyduties[c].append(i)

  return workerbyduties

workerbyduties = [workerbyduty(d) for d in dutygroups]
print(workerbyduties)
"""group anonymous workers for each dutytype"""

def daybyduty(calen):
    daybyduties = {}
    for i in dutytypes:
        daybyduties[i] = []

    for i in calen:
      daybyduties[i[3]].append(i[0])

    return daybyduties

daybyduties = [daybyduty(c) for c in calens]
print(daybyduties)
"""group days for each dutytype"""

def combinelists(a, b):
    result = []
    for i in b:
        result.append(list(a)+list(i))
    return result

def combination(workerbyduties, daybyduties):
    result = {}

    for i in workerbyduties:
        workercnt = defaultdict(int)
        for c in workerbyduties[i]:
          workercnt[c] += 1
        workercnt = dict(workercnt)
        pegs = deque([])
        for q in workercnt:
            subjects = []
            if pegs:
                for u in pegs:
                    subjects.append([f for f in daybyduties[i] if f not in u])

                def elements2():
                    for p in range(len(subjects)):
                        combi = list(itertools.combinations(subjects[p], workercnt[q]))
                        for o in combinelists(pegs[p], combi): yield(o)

                pegs = list(elements2())
            else:
                subjects = [daybyduties[i]]
                pegs = list(itertools.combinations(subjects[0], workercnt[q]))

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
print(combinations)

'''from now, merge the divided calender'''

groups = {}
cnt = 0
for q in combinations:
    for w in q:
        groups[cnt] = q[w]
        cnt += 1

def combimerge(groups):
    indices = {d: 0 for d in groups}
    first = {}
    for d in groups:
        first.update(groups[d][0])

    yield first

    while True:
      for d in indices:
        if indices[d] < len(groups[d]) - 1 : break
      else: return

      for d in indices:
        if indices[d] < len(groups[d]) - 1:
          indices[d] += 1
          break
        else:
          indices[d] = 0

      merged = {}
      for d in indices:
            merged.update(groups[d][indices[d]])

      yield merged
'''combine elements of groups to make schedule cases'''

def sortandtestadjacent(merged):
  subject = dict(sorted(merged.items()))
  previous = -1
  for q in subject:
    temp = merged[q]
    if temp == previous: return False
    previous = temp
  else : return subject
'''filter1'''

def evaluatescore(calen):
  '''calen has to be sorted by date'''
  workingdays = defaultdict(list)
  for q in calen:
    workingdays[calen[q]].append(q)
  workingdays = dict(workingdays)
  gaps = []
  for e in workingdays:
    for r in range(len(workingdays[e])-1):
      gaps.append(workingdays[e][r+1] - workingdays[e][r])

  score = 0
  for t in gaps:
    score += np.log(t)

  return score
'''filter2'''

def allotworker(merged):
  if merged:
    workerper = list(itertools.permutations(workers))
    for q in workerper:
      allotedcal = {}
      for w in merged:
        allotedcal[w] = q[int(merged[w])]
      yield allotedcal
  else: yield False
'''filter3'''

def concerndayoffs(allotedcal):
  if allotedcal:
    for q in dayoffs:
      for w in dayoffs[q]:
        if allotedcal[w] == q:
          return False
  return allotedcal
'''filter4'''

def schedulelog(case):
  result : Dict[str,dict] = {}
  resulttemp : Dict[str,list] = {}
  for a in workers:
    resulttemp[a] = []
  for q in case:
    resulttemp[case[q]].append(calen[q-1][3])
  for w in resulttemp:
    dictt = {}
    for e in dutytypes:
      dictt[e] = 0
    for r in resulttemp[w]:
      dictt[r] += 1
    result[w] = dictt

  for l in result:
    print(l, ':', result[l])


def makefinalcase(combimerge):
  score = 0
  result = []

  for merged in combimerge:
    filtered1 = sortandtestadjacent(merged)
    filtered2 = allotworker(filtered1)
    filtered3 = [concerndayoffs(v) for v in filtered2 if concerndayoffs(v)]
    for g in filtered3 :
      scoreg = evaluatescore(g)
      if score > scoreg: continue
      elif score < scoreg:
        result.clear()
        result.append(g)
        score = scoreg
        print(g)
        print(score)
        schedulelog(g)
        result.append(g)
      else:
        result.append(g)

  return result

finalcases = makefinalcase(combimerge(groups))

print(finalcases)



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


mandatory modification points
use deque
make starting point different
***do not pre decide 토주, 일주, yet decide it last which best fits***"""
