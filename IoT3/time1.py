import time
import datetime

t = datetime.datetime.now()

print t, type(t)

s = str(t)
print s, type(s)

print t.strftime('today is %d, %b %Y')

print "today is {:%d, %b %Y}".format(t)

print t.strftime('now the time is %H:%M:%S')