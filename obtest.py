#!/usr/bin/python
# Filename: obtest.py

import time
timenow = time.time() #get present time

f = file('/tmp/ob.log', 'r') #open ob.log
f.seek(0,0) #locate the first char
timetest = f.readline(10) #read the first 10 characters
f.readline() #change to the next line
f.seek(7,1) #locate the seventh character from the present char
onlinestatus = f.readline(4)
f.readline()
f.seek(8,1)
offlinestatus = f.readline(4)
f.close() #close the file

timepass = int(timenow) - int(timetest)

#print timetest
#print time.time()
#print timepass
#print onlinestatus
#print offlinestatus

if timepass<350:
  if (onlinestatus=='Pass' and offlinestatus=='Pass'):
    print 1
  elif (onlinestatus=='Pass' and offlinestatus=='Fail'):
    print 2
  elif (onlinestatus=='Fail' and offlinestatus=='Pass'):
    print 3
  else:
    print 4
else:
   print 0
