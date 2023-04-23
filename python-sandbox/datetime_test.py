# datetime_test.py
from datetime import datetime
import time
from time import mktime

date_string1 = "2020-10-29 03:59:45.303656578"
print(date_string1)

date_string1 = date_string1[:date_string1.find('.')]
print(date_string1)

date_object1 = time.strptime(date_string1, "%Y-%m-%d %H:%M:%S")
print(date_object1)

#####################################

date_string2 = "2020-11-19 03:59:45.303656578"
print(date_string2)

date_string2 = date_string2[:date_string2.find('.')]
print(date_string2)

date_object2 = time.strptime(date_string2, "%Y-%m-%d %H:%M:%S")
print(date_object2)

######################################

dt1 = datetime.fromtimestamp(mktime(date_object1))
dt2 = datetime.fromtimestamp(mktime(date_object2))

dur = dt2 - dt1
seconds_diff = dur.total_seconds()

print(dur)
print(seconds_diff)