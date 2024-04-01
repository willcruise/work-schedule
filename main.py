import calendar
import datetime

print("Enter year and month: 0000-00")
yearmonth = input()

datelist = yearmonth.split("-")
datelist[1] = datelist[1].replace("0","")

datetime_date = datetime.date(int(datelist[0]), int(datelist[1]), 1)
firstdayofweek = datetime_date.weekday()
monthrange = calendar.monthrange(int(datelist[0]), int(datelist[1]))[1]

calen = []

for i in range(monthrange):
    calen.append([i+1, firstdayofweek])
    if firstdayofweek < 6:
        firstdayofweek += 1
    else : firstdayofweek = 0
   
schedule = {}

for i in range(monthrange):
    if calen[i] <= 3
    schedule[calen[i]] =[] 
