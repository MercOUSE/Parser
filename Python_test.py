slovar = {'час' : 3600, 'часа' : 3600, 'часов' : 3600, 'минут' : 60, 'минуту' : 60, 'минуты' : 60, 'секунду' : 1, 'секунд' : 1, 'полтора' : 1.5}
import time
from datetime import datetime
from datetime import date
import datetime
import re
import string
print("О чём напомнить Вам?")
text = str(input())
notif = text + ' ' 
datex = re.findall('[0-9][0-9][.,-][0-9][0-9][.,-][0-9][0-9][0-9][0-9]',notif)
print(datex)
test1 = datex[0]
test2 = test1.split(".")
now = str(date.today())
now1 = now.split("-")
test3 = test2[::-1]
print(test3)
now2 = now1
print(now2)
day_now = int(now2[2])
month_now = int(now2[1])
year_now = int(now2[0])
day_remind = int(test3[2])
month_remind = int(test3[1])
year_remind = int(test3[0])

aa = datetime.date(year_remind, month_remind, day_remind)
bb = datetime.date(year_now, month_now, day_now)
difference_day = aa-bb
print(difference_day) 
    
day_var = difference_day * 86400