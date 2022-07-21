from datetime import datetime
from datetime import date
from threading import Thread
import datetime
import re
import time as t


dictionary = {'час' : 3600, 'часа' : 3600, 'часов' : 3600, 'минут' : 60,
              'минуту' : 60, 'минуты' : 60, 'секунду' : 1, 'секунд' : 1,
              'полтора' : 1.5, 'день' : 86400, 'дней' : 86400, 'дня' : 86400,
              'сутки' : 86400, 'завтра' : 86400, 'января' : 1, 'февраля' : 2, 'марта' : 3,
              'апреля' : 4, 'мая' : 5, 'июня' : 6, 'июля' : 7, 'августа' : 8,
              'сентября' : 9, 'октября' : 10, 'ноября' : 11, 'декабря' : 12, 'неделю' : 604800, 'недели' : 604800,
              'понедельник' : 0, 'вторник' : 1, 'среду' : 2, 'четверг' : 3, 'пятницу' : 4, 'субботу' : 5, 'воскресенье' : 6}
i = -1
j = -1
reminder = 1

cache_messages = []
cache_time = []

while reminder == 1:
    
    print("О чём и когда напомнить Вам?")
    text = str(input())
    
    if len(text) > 0:
        notif = text.lower() 
        datex_t = re.findall('[0-9][0-9][-][0-9][0-9][-][0-9][0-9][0-9][0-9]',notif)
        datex_p = re.findall('[0-9][0-9][.][0-9][0-9][.][0-9][0-9][0-9][0-9]',notif)
        datex_monthname = re.findall('[0-9]+ января [0-9][0-9][0-9][0-9] года+|[0-9]+ февраля [0-9][0-9][0-9][0-9] года+|[0-9]+ марта [0-9][0-9][0-9][0-9] года+|[0-9]+ апреля [0-9][0-9][0-9][0-9] года+|[0-9]+ мая [0-9][0-9][0-9][0-9] года+|[0-9]+ июня [0-9][0-9][0-9][0-9] года+|[0-9]+ июля [0-9][0-9][0-9][0-9] года+|[0-9]+ августа [0-9][0-9][0-9][0-9] года+|[0-9]+ сентября [0-9][0-9][0-9][0-9] года+|[0-9]+ октября [0-9][0-9][0-9][0-9] года+|[0-9]+ ноября [0-9][0-9][0-9][0-9] года+|[0-9]+ декабря [0-9][0-9][0-9][0-9] года+|[0-9]+ января [0-9][0-9][0-9][0-9]+ |[0-9]+ февраля [0-9][0-9][0-9][0-9]+ |[0-9]+ марта [0-9][0-9][0-9][0-9]+ |[0-9]+ апреля [0-9][0-9][0-9][0-9]+ |[0-9]+ мая [0-9][0-9][0-9][0-9]+ |[0-9]+ июня [0-9][0-9][0-9][0-9]+ |[0-9]+ июля [0-9][0-9][0-9][0-9]+ |[0-9]+ августа [0-9][0-9][0-9][0-9]+ |[0-9]+ сентября [0-9][0-9][0-9][0-9]+ |[0-9]+ октября [0-9][0-9][0-9][0-9]+ |[0-9]+ ноября [0-9][0-9][0-9][0-9]+ |[0-9]+ декабря [0-9][0-9][0-9][0-9]',notif)
        timex = re.findall('[0-9]+[:][0-5][0-9]', notif)
        skipping_time = re.findall('через [0-9]+ часа+|через [0-9]+ минуты+|через [0-9]+ минуту+|через [0-9]+ часов+|через [0-9]+ минут+|через час+|через минуту+|через [0-9]+ час+|через сутки',notif)
        skipping_days = re.findall('через [0-9]+ дня+|через [0-9]+ день+|через [0-9]+ дней+|через день+|через неделю+|завтра', notif)
        how_are_you = re.findall('как дела[?]', notif)
        day_of_week = re.findall('понедельник+|вторник+|среду+|четверг+|пятницу+|субботу+|воскресенье',notif)
        what_time_is_now = re.findall('который час[?]|сколько сейчас времени[?]|время сейчас|время в настоящий момент', notif)
        
        if len(what_time_is_now) != 0:
            print(datetime.datetime.now())
        elif len(how_are_you) != 0:
            print("Отлично! Готов к работе.")
        elif len(how_are_you) == 0:
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
            elif len(datex_t) or len(datex_p) or len(datex_monthname) or len(timex) or len(skipping_time) or len(skipping_days) or len(day_of_week) > 0:
                
                if len(day_of_week) != 0:
                    day_of_week_string = day_of_week[0]
                    key = dictionary[day_of_week_string]
                    time_now = datetime.datetime.today()
                    day_now = time_now.weekday()
                    if key == day_now:
                        time_sleep_interval = 604800
                    elif key < day_now:
                        num_of_days = 7 - day_now + key
                        time_sleep_interval = num_of_days * 86400
                    else: 
                        num_of_days = key - day_now
                        time_sleep_interval = num_of_days * 86400
                    if time_sleep_interval > 0:
                        fragement = 'в' + ' ' + day_of_week_string
                        message = notif.replace(fragement, '')
                        if len(notif) == len(message):
                            fragement = 'во' + ' ' + day_of_week_string
                            message = notif.replace(fragement, '')
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
                    
                elif len(skipping_days) != 0:
                    s=[]
                    for x in skipping_days:
                        s.append(re.findall(x, notif))
                        
                    s_list = s[0]
                    s_string = s_list[0]
                    s_splitted = s_string.split()
                    
                    if len(s_splitted) == 1:
                        first_multiplier = 1
                        key = s_splitted[0]
                    elif len(s_splitted) < 3:
                        first_multiplier = 1
                        key = s_splitted[1]
                    else:
                        first_multiplier = int(s_splitted[1])
                        key = s_splitted[2]
                    second_multiplier = dictionary[key]
                    time_sleep_interval = first_multiplier * second_multiplier
                    if time_sleep_interval > 0:
                        message = notif.replace(s_string,'')
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
                    string_found = datex_monthname[0]
                    string_list = string_found.split()
                    month = string_list[1]
                    day_remind = int(string_list[0])
                    month_remind = dictionary[month]
                    year_remind = int(string_list[2])
                    if len(timex) != 0: 
                        string_time1 = timex[0]
                        time2 = string_time1.split(":")
                        time = datetime.time(hour=int(time2[0]), minute=int(time2[1]),
                                        second=0, microsecond=0, tzinfo=None, fold=0)
                        
                    now = str(date.today())
                    now_splitted = now.split("-")
                    now_list = now_splitted

                    current_date_time = datetime.datetime.now()
                    current_time = str(current_date_time.time())
                    time_now = current_time.split(":")
                    time_now[2] = 0

                    day_now = int(now_list[2])
                    month_now = int(now_list[1])
                    year_now = int(now_list[0])

                    time_now_list = datetime.time(hour=int(time_now[0]), minute=int(time_now[1]),
                                            second=0, microsecond=0, tzinfo=None, fold=0)

                    if len(datex_monthname) and len(timex) != 0:
                        first_factor = datetime.datetime(year_remind, month_remind, day_remind,
                                    int(time2[0]), int(time2[1]), 0, 0)
                        second_factor = datetime.datetime(year_now, month_now, day_now,
                                    int(time_now[0]), int(time_now[1]), 0, 0)
                    elif len(timex) != 0:
                        first_factor = datetime.datetime(year_now, month_now, day_now,
                                    int(time2[0]), int(time2[1]), 0, 0)
                        second_factor = datetime.datetime(year_now, month_now, day_now,
                                    int(time_now[0]), int(time_now[1]), 0, 0)
                    else: 
                        first_factor = datetime.datetime(year_remind, month_remind, day_remind,
                                            int(time_now[0]), int(time_now[1]), 0, 0)
                        second_factor = datetime.datetime(year_now, month_now, day_now, 
                                            int(time_now[0]), int(time_now[1]), 0, 0)
                        
                    difference_day = first_factor - second_factor

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

                    if len(datex_monthname) and len(timex) != 0:
                        fragement = string_found + 'в' + ' ' + string_time1
                        message = notif.replace(fragement, '')
                        if len(message) == len(text):
                            fragement = 'в' + ' ' + string_time1 + ' ' + string_found
                            message = notif.replace(fragement, '')
                            if len(message) == len(text):
                                fragement = string_found + ' ' + 'в' + ' ' + string_time1
                                message = notif.replace(fragement, '')
    
                    elif len(datex_monthname) != 0 and len(timex) == 0:
                        fragement = string_found
                        message = notif.replace(fragement, '')

                elif len(skipping_time) != 0:
                    s = []
                    for x in skipping_time:
                        s.append(re.findall(x, notif))
                        
                    s_list = s[0]
                    s_string = s_list[0]
                    s_splitted = s_string.split()
                    
                    if len(s_splitted) < 3:
                        first_multiplier = 1
                        key = s_splitted[1]
                    else:
                        first_multiplier = int(s_splitted[1])
                        key = s_splitted[2]
                    second_multiplier = dictionary[key]
                    time_sleep_interval = first_multiplier * second_multiplier
                    if time_sleep_interval > 0:
                        message = notif.replace(s_string,'')
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
                            string_found = datex_t[0]
                            string_list = string_found.split("-")
                            string_list_reversed = string_list[::-1]
                            day_remind = int(string_list_reversed[2])
                            month_remind = int(string_list_reversed[1])
                            year_remind = int(string_list_reversed[0])
                        else: 
                            string_found = datex_p[0]
                            string_list = string_found.split(".")
                            string_list_reversed = string_list[::-1]
                            day_remind = int(string_list_reversed[2])
                            month_remind = int(string_list_reversed[1])
                            year_remind = int(string_list_reversed[0])
                    if len(timex) != 0: 
                        string_time1 = timex[0]
                        time2 = string_time1.split(":")
                        time = datetime.time(hour=int(time2[0]), minute=int(time2[1]),
                                        second=0, microsecond=0, tzinfo=None, fold=0)
                        
                    now = str(date.today())
                    now_splitted = now.split("-")
                    now_list = now_splitted

                    current_date_time = datetime.datetime.now()
                    current_time = str(current_date_time.time())
                    time_now = current_time.split(":")
                    time_now[2] = 0

                    day_now = int(now_list[2])
                    month_now = int(now_list[1])
                    year_now = int(now_list[0])

                    time_now_list = datetime.time(hour=int(time_now[0]), minute=int(time_now[1]),
                                            second=0, microsecond=0, tzinfo=None, fold=0)


                    if (len(datex_p) or len(datex_t)) and len(timex) != 0:
                        first_factor = datetime.datetime(year_remind, month_remind, day_remind,
                                    int(time2[0]), int(time2[1]), 0, 0)
                        second_factor = datetime.datetime(year_now, month_now, day_now,
                                    int(time_now[0]), int(time_now[1]), 0, 0)
                    elif len(timex) != 0:
                        first_factor = datetime.datetime(year_now, month_now, day_now,
                                    int(time2[0]), int(time2[1]), 0, 0)
                        second_factor = datetime.datetime(year_now, month_now, day_now,
                                    int(time_now[0]), int(time_now[1]), 0, 0)
                    else: 
                        first_factor = datetime.datetime(year_remind, month_remind, day_remind,
                                            int(time_now[0]), int(time_now[1]), 0, 0)
                        second_factor = datetime.datetime(year_now, month_now, day_now, 
                                            int(time_now[0]), int(time_now[1]), 0, 0)
                        
                    difference_day = first_factor - second_factor

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
                        fragement = string_found + ' ' + 'в' + ' ' + string_time1
                        message = notif.replace(fragement, '')

                        if len(message) == len(text):
                            fragement = 'в' + ' ' + string_time1 + ' ' + string_found
                            message = notif.replace(fragement, '')

                    elif len(datex_t) and len(timex) != 0:
                        fragement = string_found + ' ' + 'в' + ' ' + string_time1
                        message = notif.replace(fragement, '')
                        
                        if len(message) == len(text):
                            fragement = 'в' + ' ' + string_time1 + ' ' + string_found
                            message = notif.replace(fragement, '')

                    elif len(datex_t) == 0 and len(datex_p) == 0 and len(timex) != 0:
                        fragement = 'в' + ' ' + string_time1
                        message = notif.replace(fragement, '')


                    elif (len(datex_p) or len(datex_t) != 0) and len(timex) == 0:
                        fragement = string_found
                        message = notif.replace(fragement, '')
                        
                if time_sleep_interval > 0:
                    MESSAGE={'STATUS': 'SUCCESS', 'DATE': {'year': year_remind, 'month': month_remind, 'day': day_remind, 'hour': hour_remind, 'minute': minute_remind}, 'TEXT': message}
                    print(MESSAGE)
                    cache_time.append(time_sleep_interval)
                    i += 1
                    cache_messages.append(message)
                    j += 1
                    def time_sleep(i, j):
                        try:
                            t.sleep(cache_time[i])
                            print("Напоминаю!", cache_messages[j])
                        except OverflowError:
                            print("Слишком долго!")
                            MESSAGE={'STATUS': 'ERROR', 'TEXT': OverflowError}
                            print(MESSAGE)
                    th = Thread(target=time_sleep, args=(i, j))
                    th.start()
                    
            else: 
                print("Ошибка! Укажите время.")
                error_name = 'Неверно указано время'
                MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
                print(MESSAGE)
    else: 
        print("Ошибка! Ничего не введено.")
        error_name = 'Ничего не введено'
        MESSAGE={'STATUS': 'ERROR', 'TEXT': error_name}
        print(MESSAGE)