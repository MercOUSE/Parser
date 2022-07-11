import re
dictionary = {'час' : 3600, 'часа' : 3600, 'часов' : 3600, 'минут' : 60,
              'минуту' : 60, 'минуты' : 60, 'секунду' : 1, 'секунд' : 1,
              'полтора' : 1.5}

print(dictionary['минут'])
spisok = ['через','2','часа']
string = 'через 2 часа посрать'
s=[]
for x in spisok:
    s.append(re.findall(x, string))
    #if len(find) != 0:
        #break
print(s)
s1 = s[0]
s2 = s1[0]
print(s2)