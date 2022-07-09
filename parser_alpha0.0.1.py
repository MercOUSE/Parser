dictionary = {'час' : 3600, 'часа' : 3600, 'часов' : 3600, 'минут' : 60,
              'минуту' : 60, 'минуты' : 60, 'секунду' : 1, 'секунд' : 1,
              'полтора' : 1.5}

from datetime import datetime
from datetime import date
import datetime
import re
import time as t


print("О чём напомнить Вам?")
text = str(input())
notif = text + ' ' 
datex_t = re.findall('[0-9][0-9][-][0-9][0-9][-][0-9][0-9][0-9][0-9]',notif)
datex_p = re.findall('[0-9][0-9][.][0-9][0-9][.][0-9][0-9][0-9][0-9]',notif)
timex = re.findall('[0-2][0-3][:][0-5][0-9]', notif)
print(datex_t)
print(datex_p)
print(timex)

if len(timex) != 0:
    string_time1 = timex[0]
    time2 = string_time1.split(":")
print(time2)

if len(datex_p) == 0:
    string1 = datex_t[0]
    string2 = string1.split("-")
else: 
    string1 = datex_p[0]
    string2 = string1.split(".")
    
now = str(date.today())
now1 = now.split("-")
string3 = string2[::-1]
print(string3)
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
day_remind = int(string3[2])
month_remind = int(string3[1])
year_remind = int(string3[0])

time = datetime.time(hour=int(time2[0]), minute=int(time2[1]),
                     second=0, microsecond=0, tzinfo=None, fold=0)
time_now2 = datetime.time(hour=int(time_now[0]), minute=int(time_now[1]),
                          second=0, microsecond=0, tzinfo=None, fold=0)
print(time)
print(time_now2)
aa = datetime.datetime(year_remind, month_remind, day_remind,
                   int(time2[0]), int(time2[1]), 0, 0)
bb = datetime.datetime(year_now, month_now, day_now,
                   int(time_now[0]), int(time_now[1]), 0, 0)
difference_day = aa-bb
print(difference_day)
localtime = difference_day 
time_d_float = difference_day.total_seconds()
print(time_d_float) 
t.sleep(time_d_float)

words = text.split()
fragement = string1
new_words = []
for word in words:
    if fragement not in word:
        new_words.append(word)
out = ' '.join(new_words)

print(out)