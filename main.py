import calendar
import datetime

print("Enter year and month: 0000-00")
yearmonth = input()

datelist = yearmonth.split("-")
datelist[1] = datelist[1].replace("0","")

datetime_date = datetime.date(int(datelist[0]), int(datelist[1]), 1)
firstdayofweek = datetime_date.weekday()

print(firstdayofweek)
