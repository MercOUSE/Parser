from datetime import datetime
from datetime import date
import datetime
import re
import time as t

dictionary = {'час' : 3600, 'часа' : 3600, 'часов' : 3600, 'минут' : 60,
              'минуту' : 60, 'минуты' : 60, 'секунду' : 1, 'секунд' : 1,
              'полтора' : 1.5}

print("О чём напомнить Вам?")

text = str(input())

notif = text + ' ' 
datex_t = re.findall('[0-9][0-9][-][0-9][0-9][-][0-9][0-9][0-9][0-9]',notif)
datex_p = re.findall('[0-9][0-9][.][0-9][0-9][.][0-9][0-9][0-9][0-9]',notif)
timex = re.findall('[0-9]+[:][0-5][0-9]', notif)
skipping_time = re.findall('Через [0-9]+ часа+|Через [0-9]+ минут+|Через [0-9]+ часов+|Через час+|Через [0-9]+ минуты+|через [0-9]+ часа+|через [0-9]+ минут+|через [0-9]+ часов+|через час+|через минуту',notif)

print(skipping_time)
print(datex_t)
print(datex_p)
print(timex)

if len(skipping_time) != 0:
    s = []
    for x in skipping_time:
        s.append(re.findall(x, notif))
    print(s)
    s1 = s[0]
    s2 = s1[0]
    s3 = s2.split()
    if len(s3) < 3:
        first_multiplier = 1
        key = s3[1]
    else:
        first_multiplier = int(s3[1])
        key = s3[2]
    second_multiplier = dictionary[key]
    time_sleep_interval = first_multiplier * second_multiplier
    print(time_sleep_interval)
    message = text.replace(s2,'')
    #t.sleep(time_sleep_interval)
    print("Напоминаю!", message)
    
else:
    if len(datex_p) or len(datex_t) != 0:
        if len(datex_p) == 0:
            string1 = datex_t[0]
            string2 = string1.split("-")
            string3 = string2[::-1]
            day_remind = int(string3[2])
            month_remind = int(string3[1])
            year_remind = int(string3[0])
        else: 
            string1 = datex_p[0]
            string2 = string1.split(".")
            string3 = string2[::-1]
            day_remind = int(string3[2])
            month_remind = int(string3[1])
            year_remind = int(string3[0])
    if len(timex) != 0: 
        string_time1 = timex[0]
        time2 = string_time1.split(":")
        print(time2)
        time = datetime.time(hour=int(time2[0]), minute=int(time2[1]),
                        second=0, microsecond=0, tzinfo=None, fold=0)
        
    now = str(date.today())
    now1 = now.split("-")
    now2 = now1

    print(now2)

    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())
    time_now = current_time.split(":")
    time_now[2] = 0

    print(time_now)

    day_now = int(now2[2])
    month_now = int(now2[1])
    year_now = int(now2[0])

    time_now2 = datetime.time(hour=int(time_now[0]), minute=int(time_now[1]),
                            second=0, microsecond=0, tzinfo=None, fold=0)

    print(time_now2)

    if (len(datex_p) or len(datex_t)) and len(timex) != 0:
        aa = datetime.datetime(year_remind, month_remind, day_remind,
                    int(time2[0]), int(time2[1]), 0, 0)
        bb = datetime.datetime(year_now, month_now, day_now,
                    int(time_now[0]), int(time_now[1]), 0, 0)
    elif len(timex) != 0:
        aa = datetime.datetime(year_now, month_now, day_now,
                    int(time2[0]), int(time2[1]), 0, 0)
        bb = datetime.datetime(year_now, month_now, day_now,
                    int(time_now[0]), int(time_now[1]), 0, 0)
    else: 
        aa = datetime.datetime(year_remind, month_remind, day_remind,
                            int(time_now[0]), int(time_now[1]), 0, 0)
        bb = datetime.datetime(year_now, month_now, day_now, 
                            int(time_now[0]), int(time_now[1]), 0, 0)
        
    difference_day = aa-bb

    print(difference_day)

    localtime = difference_day 
    time_d_float = difference_day.total_seconds()

    print(time_d_float) 
    #t.sleep(time_d_float)

    if len(datex_p) and len(timex) != 0:
        fragement = string1 + ' ' + 'в' + ' ' + string_time1
        print(fragement)
        message = text.replace(fragement, '')

        if len(message) == len(text):
            fragement = 'в' + ' ' + string_time1 + ' ' + string1
            message = text.replace(fragement, '')
            print(fragement)

        if len(message) == len(text):
            fragement = 'В' + ' ' + string_time1 + ' ' + string1
            message = text.replace(fragement, '')
            print(fragement)

    elif len(datex_t) and len(timex) != 0:
        fragement = string1 + ' ' + 'в' + ' ' + string_time1
        print(fragement)
        message = text.replace(fragement, '')
        
        if len(message) == len(text):
            fragement = 'в' + ' ' + string_time1 + ' ' + string1
            message = text.replace(fragement, '')
            print(fragement)
            
        if len(message) == len(text):
            fragement = 'В' + ' ' + string_time1 + ' ' + string1
            message = text.replace(fragement, '')
            print(fragement)

    elif len(datex_t) == 0 and len(datex_p) == 0 and len(timex) != 0:
        fragement = 'в' + ' ' + string_time1
        print(fragement)
        message = text.replace(fragement, '')
        if len(message) == len(text):
            fragement = 'В' + ' ' + string_time1
            message = text.replace(fragement, '')
            print(fragement)

    elif (len(datex_p) or len(datex_t) != 0) and len(timex) == 0:
        fragement = string1
        print(fragement)
        message = text.replace(fragement, '')

    print("Напоминаю!", message)