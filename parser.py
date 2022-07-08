import time
import datetime
import re
print("О чём напомнить Вам?")
text = str(input())
notif = text +' ' 
find = re.findall('ерез [0-9]+|В [0-9:-]+|в [0-9:-]+|ерез час',notif)
day = re.findall('завтра|понедельник|вторник|среду|четверг|пятницу|субботу|воскресенье',notif)
datex = re.findall('[0-9][0-9][.,-][0-9][0-9][.,-][0-9][0-9][0-9][0-9]',notif)
print(find)
print(day)
print(datex)
now = datetime.datetime.now()
#local_time = local_time * 60
time.sleep(local_time)
print(text)
