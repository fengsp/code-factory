#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
print datetime.MINYEAR
print datetime.MAXYEAR
from datetime import timedelta
d = timedelta(microseconds=-1)
print d.days, d.seconds, d.microseconds
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
print year.total_seconds()
print year == another_year
ten_years = 10 * year
print ten_years, ten_years.days
nine_years = ten_years - year
print nine_years, nine_years.days
three_years = nine_years // 3;
print type(three_years), three_years.days // 365
print abs(three_years - ten_years) == 2 * three_years + year
import time
from datetime import date, datetime
today = date.today()
print today
print today == date.fromtimestamp(time.time())
my_birthday = date(today.year, 6, 24)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print my_birthday
time_to_birthday = abs(my_birthday - today)
print type(time_to_birthday), time_to_birthday.days
d = date.fromordinal(730920)
print d
t = d.timetuple()
for i in t:
    print i
ic = d.isocalendar()
for i in ic:
    print i
print d.isoformat()
print d.strftime("%d/%m/%y")
print d.strftime("%A %d. %B %Y")
print 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
from datetime import time
d = date(2005, 7, 14)
t = time(12, 30)
print datetime.combine(d, t)
print datetime.now()
print datetime.utcnow()
dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print dt
tt = dt.timetuple()
for it in tt:
    print it
ic = dt.isocalendar()
for it in ic:
    print it
print dt.strftime("%A, %d. %B %Y %I:%M%p")
print 'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time")
print len('                                                                ')
# Tally occurrences of words in a list
from collections import Counter
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print cnt
import re
words = re.findall(r'\w+', open('Hamlet.txt').read().lower())
print Counter(words).most_common(10)
print Counter('gallahad')
print Counter({'red':4, 'blue':2})
print Counter(cats=4, dogs=8)
print Counter(['eggs', 'ham'])
print list(Counter(a=4, b=2, c=0, d=-2).elements())
from collections import deque
d = deque('ghi')
for elem in d:
    print elem.upper()
d.append('j')
d.appendleft('f')
print d
print d.pop()
print d.popleft()
print list(d)
print d[0]
print d[-1]
print list(reversed(d))
print 'h' in d
d.extend('jkl')
print d
d.clear()
d.extendleft('abc')
print d
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4),('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print d.items()
from collections import OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorteded = sorted(d.items(), key=lambda t:t[0])
print dict(sorteded)
ordered = OrderedDict(sorted(d.items(), key=lambda t:t[0]))
for k, v in ordered.items():
    print ordered[k]
