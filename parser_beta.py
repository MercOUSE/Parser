from datetime import datetime
from datetime import date
import datetime
import re
import time as t

dictionary = {'час' : 3600, 'часа' : 3600, 'часов' : 3600, 'минут' : 60,
              'минуту' : 60, 'минуты' : 60, 'секунду' : 1, 'секунд' : 1,
              'полтора' : 1.5, 'день' : 86400, 'дней' : 86400, 'дня' : 86400,
              'сутки' : 86400, 'января' : 1, 'февраля' : 2, 'марта' : 3,
              'апреля' : 4, 'мая' : 5, 'июня' : 6, 'июля' : 7, 'августа' : 8,
              'сентября' : 9, 'октября' : 10, 'ноября' : 11, 'декабря' : 12}

reminder = 1

while reminder == 1:
    print("О чём и когда напомнить Вам?")

    text = str(input())
    if len(text) > 0:
        notif = text + ' ' 
        datex_t = re.findall('[0-9][0-9][-][0-9][0-9][-][0-9][0-9][0-9][0-9]',notif)
        datex_p = re.findall('[0-9][0-9][.][0-9][0-9][.][0-9][0-9][0-9][0-9]',notif)
        datex_monthname = re.findall('[0-9]+ января [0-9][0-9][0-9][0-9] года+|[0-9]+ февраля [0-9][0-9][0-9][0-9] года+|[0-9]+ марта [0-9][0-9][0-9][0-9] года+|[0-9]+ апреля [0-9][0-9][0-9][0-9] года+|[0-9]+ мая [0-9][0-9][0-9][0-9] года+|[0-9]+ июня [0-9][0-9][0-9][0-9] года+|[0-9]+ июля [0-9][0-9][0-9][0-9] года+|[0-9]+ августа [0-9][0-9][0-9][0-9] года+|[0-9]+ сентября [0-9][0-9][0-9][0-9] года+|[0-9]+ октября [0-9][0-9][0-9][0-9] года+|[0-9]+ ноября [0-9][0-9][0-9][0-9] года+|[0-9]+ декабря [0-9][0-9][0-9][0-9] года+|[0-9]+ января [0-9][0-9][0-9][0-9]+ |[0-9]+ февраля [0-9][0-9][0-9][0-9]+ |[0-9]+ марта [0-9][0-9][0-9][0-9]+ |[0-9]+ апреля [0-9][0-9][0-9][0-9]+ |[0-9]+ мая [0-9][0-9][0-9][0-9]+ |[0-9]+ июня [0-9][0-9][0-9][0-9]+ |[0-9]+ июля [0-9][0-9][0-9][0-9]+ |[0-9]+ августа [0-9][0-9][0-9][0-9]+ |[0-9]+ сентября [0-9][0-9][0-9][0-9]+ |[0-9]+ октября [0-9][0-9][0-9][0-9]+ |[0-9]+ ноября [0-9][0-9][0-9][0-9]+ |[0-9]+ декабря [0-9][0-9][0-9][0-9]',notif)
        timex = re.findall('[0-9]+[:][0-5][0-9]', notif)
        skipping_time = re.findall('Через [0-9]+ часа+|Через [0-9]+ минут+|Через [0-9]+ часов+|Через час+|Через [0-9]+ минуты+|через [0-9]+ часа+|через [0-9]+ минут+|через [0-9]+ часов+|через час+|через минуту+|через [0-9]+ час+ |Через [0-9]+ час+ |Через сутки+ |через сутки',notif)
        skipping_days = re.findall('через [0-9]+ дня+ |через [0-9]+ день+ |через [0-9]+ дней+ |Через [0-9]+ дня+ |Через [0-9]+ день+ |Через [0-9]+ дней+ |Через день+ |через день,', notif)

        if len(skipping_days) and len(timex) != 0:
            print("Может, неверно указали время?")
            error_name = 'Неверно указано время'
            MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
            print(MESSAGE)
        elif len(skipping_time) and len(timex) != 0:
            print("Может, неверно указали время?")
            error_name = 'Неверно указано время'
            MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
            print(MESSAGE)
        elif len(datex_t) or len(datex_p) or len(datex_monthname) or len(timex) or len(skipping_time) or len(skipping_days) > 0:
            if len(skipping_days) != 0:
                s=[]
                for x in skipping_days:
                    s.append(re.findall(x, notif))
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
                if time_sleep_interval > 0:
                    message = notif.replace(s2,'')
                    seconds = t.time() + time_sleep_interval
                    result = t.localtime(seconds)
                    year_remind = result.tm_year
                    month_remind = result.tm_mon
                    day_remind = result.tm_mday
                    hour_remind = result.tm_hour
                    minute_remind = result.tm_min
                else:
                    print("Ошибка! Неверно указано время")
                    error_name = 'Неверно указано время'
                    MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
                    print(MESSAGE)
                

            elif len(datex_monthname) != 0:
                string1 = datex_monthname[0]
                string2 = string1.split()
                month = string2[1]
                day_remind = int(string2[0])
                month_remind = dictionary[month]
                year_remind = int(string2[2])
                if len(timex) != 0: 
                    string_time1 = timex[0]
                    time2 = string_time1.split(":")
                    time = datetime.time(hour=int(time2[0]), minute=int(time2[1]),
                                    second=0, microsecond=0, tzinfo=None, fold=0)
                    
                now = str(date.today())
                now1 = now.split("-")
                now2 = now1

                current_date_time = datetime.datetime.now()
                current_time = str(current_date_time.time())
                time_now = current_time.split(":")
                time_now[2] = 0

                day_now = int(now2[2])
                month_now = int(now2[1])
                year_now = int(now2[0])

                time_now2 = datetime.time(hour=int(time_now[0]), minute=int(time_now[1]),
                                        second=0, microsecond=0, tzinfo=None, fold=0)

                if len(datex_monthname) and len(timex) != 0:
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

                localtime = difference_day 
                time_sleep_interval = difference_day.total_seconds()
                if time_sleep_interval > 0:
                    seconds = t.time() + time_sleep_interval
                    result = t.localtime(seconds)
                    year_remind = result.tm_year
                    month_remind = result.tm_mon
                    day_remind = result.tm_mday
                    hour_remind = result.tm_hour
                    minute_remind = result.tm_min
                else:
                    print("Ошибка! Неверно указано время")
                    error_name = 'Неверно указано время'
                    MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
                    print(MESSAGE)

                print(string1)
                print(string_time1)

                if len(datex_monthname) and len(timex) != 0:
                    fragement = string1 + ' ' + 'в' + ' ' + string_time1
                    message = text.replace(fragement, '')
                    print(fragement)
                    if len(message) == len(text):
                        fragement = 'в' + ' ' + string_time1 + ' ' + string1
                        message = text.replace(fragement, '')
                        print(fragement)
                    if len(message) == len(text):
                        fragement = 'В' + ' ' + string_time1 + ' ' + string1
                        message = text.replace(fragement, '')
                        print(fragement)
                        print(fragement)
                elif len(datex_monthname) != 0 and len(timex) == 0:
                    fragement = string1
                    message = notif.replace(fragement, '')
                    print(fragement)
            elif len(skipping_time) != 0:
                s = []
                for x in skipping_time:
                    s.append(re.findall(x, notif))
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
                if time_sleep_interval > 0:
                    message = notif.replace(s2,'')
                    seconds = t.time() + time_sleep_interval
                    result = t.localtime(seconds)
                    year_remind = result.tm_year
                    month_remind = result.tm_mon
                    day_remind = result.tm_mday
                    hour_remind = result.tm_hour
                    minute_remind = result.tm_min
                else:
                    print("Ошибка! Неверно указано время")
                    error_name = 'Неверно указано время'
                    MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
                    print(MESSAGE)
        
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
                    time = datetime.time(hour=int(time2[0]), minute=int(time2[1]),
                                    second=0, microsecond=0, tzinfo=None, fold=0)
                    
                now = str(date.today())
                now1 = now.split("-")
                now2 = now1

                current_date_time = datetime.datetime.now()
                current_time = str(current_date_time.time())
                time_now = current_time.split(":")
                time_now[2] = 0

                day_now = int(now2[2])
                month_now = int(now2[1])
                year_now = int(now2[0])

                time_now2 = datetime.time(hour=int(time_now[0]), minute=int(time_now[1]),
                                        second=0, microsecond=0, tzinfo=None, fold=0)


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

                localtime = difference_day 
                time_sleep_interval = difference_day.total_seconds()
                if time_sleep_interval > 0:
                    seconds = t.time() + time_sleep_interval
                    result = t.localtime(seconds)
                    year_remind = result.tm_year
                    month_remind = result.tm_mon
                    day_remind = result.tm_mday
                    hour_remind = result.tm_hour
                    minute_remind = result.tm_min
                else:
                    print("Ошибка! Неверно указано время")
                    error_name = 'Неверно указано время'
                    MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
                    print(MESSAGE)


                if len(datex_p) and len(timex) != 0:
                    fragement = string1 + ' ' + 'в' + ' ' + string_time1
                    message = text.replace(fragement, '')

                    if len(message) == len(text):
                        fragement = 'в' + ' ' + string_time1 + ' ' + string1
                        message = text.replace(fragement, '')

                    if len(message) == len(text):
                        fragement = 'В' + ' ' + string_time1 + ' ' + string1
                        message = text.replace(fragement, '')

                elif len(datex_t) and len(timex) != 0:
                    fragement = string1 + ' ' + 'в' + ' ' + string_time1
                    message = text.replace(fragement, '')
                    
                    if len(message) == len(text):
                        fragement = 'в' + ' ' + string_time1 + ' ' + string1
                        message = text.replace(fragement, '')
                        
                    if len(message) == len(text):
                        fragement = 'В' + ' ' + string_time1 + ' ' + string1
                        message = text.replace(fragement, '')

                elif len(datex_t) == 0 and len(datex_p) == 0 and len(timex) != 0:
                    fragement = 'в' + ' ' + string_time1
                    message = text.replace(fragement, '')
                    if len(message) == len(text):
                        fragement = 'В' + ' ' + string_time1
                        message = text.replace(fragement, '')

                elif (len(datex_p) or len(datex_t) != 0) and len(timex) == 0:
                    fragement = string1
                    message = text.replace(fragement, '')
            if time_sleep_interval > 0:
                MESSAGE={'STATUS': 'SUCCESS', 'DATE': {'year': year_remind, 'month': month_remind, 'day': day_remind, 'hour': hour_remind, 'minute': minute_remind}, 'TEXT': message}
                print(MESSAGE)      
        else: 
            print("Ошибка! Укажите время.")
            error_name = 'Неверно указано время'
            MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
            print(MESSAGE)
    else: 
        print("Ошибка! Ничего не введено.")
        error_name = 'Неверно указано время'
        MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
        print(MESSAGE)