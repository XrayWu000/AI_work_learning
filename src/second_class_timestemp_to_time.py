timestemp = 1764805953
#timestemp = 1764000000
#20251204 08:47:16
#start 1970

def is_leap_yesr(years):
    a = False
    if(years % 400 == 0):
        a = True
    elif(years % 100 == 0):
        a = False
    elif(years % 4 == 0):
        a = True
    else:
        a = False
    return a

def month_day(month, year):
    if(month == 2):
        if(is_leap_yesr(year)):
            return 29
        else:
            return 28
    elif(month < 8) and (month % 2 == 1):
        return 31
    elif(month < 8) and (month % 2 == 0):
        return 30
    elif(month > 7) and (month % 2 == 1):
        return 30
    elif(month > 7) and (month % 2 == 0):
        return 31

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR
year = 1970

while True:
    if(timestemp >= 365 * SECONDS_PER_DAY):
        if(is_leap_yesr(year)):
            timestemp = timestemp - 366 * SECONDS_PER_DAY
        else:
            timestemp = timestemp - 365 * SECONDS_PER_DAY
        year = year + 1
    else:
        break
month = 1
while True:
    if(timestemp > month_day(month, year) * SECONDS_PER_DAY):
        timestemp = timestemp - month_day(month, year) * SECONDS_PER_DAY
        month = month + 1
    else:
        month = str(month)
        break
day = 1
while True:
    if(timestemp > SECONDS_PER_DAY):
        timestemp = timestemp - SECONDS_PER_DAY
        day = day + 1
    else:
        day = str(day)
        break

hour = 0
while True:
    if(timestemp >= SECONDS_PER_HOUR):
        timestemp = timestemp - SECONDS_PER_HOUR
        hour = hour + 1
    else:
        hour = str(hour)
        break

min = 0
while True:
    if(timestemp >= SECONDS_PER_MINUTE):
        timestemp = timestemp - SECONDS_PER_MINUTE
        min = min + 1
    else:
        min = str(min)
        break

print(str(year)+"/"+month+"/"+day+" "+hour+":"+min+":"+str(timestemp))