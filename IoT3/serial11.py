# Reads serial data from Arduino & logs it to a CSV file
# Use it with pirRadar20.ino
# use the delimiters '[' and ']' on the two ends of the line.
# discard partially received lines.
# NOTE: the last 2 characters are \r and \n. So the right square
# bracket is at 3rd from the end.

import serial
import time
import datetime
ser = serial.Serial('COM5', 9600, timeout=0)
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)

f = open('radar1.csv', 'wt')
f.write('timeStamp,muradarON,muradarOFF,pir1ON,pir1OFF\n')
 
print "Press ^C to quit..."
 
while 1:
  try:
      x = ser.readline()
      n = len(x)
      if (n > 2):
          print x, n #, x[0], x[1], x[-3]
          if (x[0]=='['  and x[-3]==']'):
              x = x[1:-3]  # remove the delimiters
              if(x[0]=='D'):
                   x = x[1:]  # remove 'D'
                   t = datetime.datetime.now()
                   print 'data:', x	
                   f.write (t.strftime('%H:%M:%S,') +x +'\n')           
  except serial.SerialTimeoutException as e:
      print('* Cannot read serial port: ', e)
  except KeyboardInterrupt:
      #f.flush()
	  f.close()
	  print '\n', 'Done!'	
	  time.sleep(1)
	  exit()